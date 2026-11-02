#!/usr/bin/env python3
"""Export Anki decks to markdown files under cards/.

Reads a consistent snapshot of collection.anki2 (via SQLite backup API,
safe on a running Anki) and writes one markdown file per topic group:

    cards/<deck-slug>/<group>.md

Grouping rules per deck (first match wins):
  1. If most notes carry a shared `prefix::<topic>` tag -> file per topic.
  2. If the note model has a `Domain` field          -> file per domain.
  3. Otherwise                                        -> sequential chunks
     of --chunk notes in creation (note id) order, preserving course order.

Card format inside a file is field-faithful (HTML kept verbatim) so cards
can be pushed back to Anki later:

    <!-- note:1781279834155 model:Basic++++ -->
    **Front:** question
    **Back:** answer
    **Tags:** tag1, tag2
    ---

Usage:
    tools/export_anki.py                      # export all non-empty decks
    tools/export_anki.py --deck "CKAD*"       # fnmatch filter on deck name
    tools/export_anki.py --db /path/collection.anki2 --out cards/
"""

import argparse
import fnmatch
import re
import sqlite3
import sys
import tempfile
from collections import Counter
from pathlib import Path

DEFAULT_DB = "/mnt/c/Users/crock/AppData/Roaming/Anki2/User 1/collection.anki2"

# Field order per note type (the `fields` table is not reliably readable;
# names verified via the anki MCP `model_field_names` tool).
MODEL_FIELDS = {
    "Basic": ["Front", "Back"],
    "Basic+": ["Front", "Back"],
    "Basic++": ["Front", "Back"],
    "Basic+++": ["Front", "Back"],
    "Basic++++": ["Front", "Back"],
    "Basic (and reversed card)": ["Front", "Back"],
    "Cloze": ["Text", "Extra"],
    "Many": ["Domain", "Question", "Options", "Answer", "Explanation", "Sources"],
}

SKIP_DECKS = {"Default"}


def slugify(text: str) -> str:
    text = text.split(" - ")[0] if " - " in text else text
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug or "misc"


def snapshot(db_path: str, tmp: str) -> sqlite3.Connection:
    src = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    dst = sqlite3.connect(tmp)
    src.backup(dst)
    src.close()
    return dst


def load(con: sqlite3.Connection):
    cur = con.cursor()
    decks = dict(cur.execute("select id, name from decks"))
    models = dict(cur.execute("select id, name from notetypes"))
    note_deck = {}
    for nid, _cid, did in sorted(cur.execute("select nid, id, did from cards")):
        note_deck.setdefault(nid, did)
    notes = {}
    for nid, mid, tags, flds in cur.execute("select id, mid, tags, flds from notes"):
        notes[nid] = {
            "model": models.get(mid, str(mid)),
            "tags": [t for t in tags.split() if t],
            "fields": flds.split("\x1f"),
        }
    return decks, note_deck, notes


def tag_family(nids, notes, min_share=0.6):
    """Return the tag prefix (e.g. 'ckad::') shared by >= min_share of notes."""
    fam = Counter()
    for n in nids:
        for t in notes[n]["tags"]:
            if "::" in t:
                fam[t.split("::", 1)[0] + "::"] += 1
                break
    if fam and fam.most_common(1)[0][1] >= min_share * len(nids):
        return fam.most_common(1)[0][0]
    return None


def group_notes(nids, notes, chunk):
    """Yield (group_title, filename_slug, [note ids])."""
    fam = tag_family(nids, notes)
    if fam:
        groups = {}
        for n in nids:
            topic = next((t.split("::", 1)[1] for t in notes[n]["tags"]
                          if t.startswith(fam)), "misc")
            groups.setdefault(topic, []).append(n)
        for topic in sorted(groups):
            yield topic.replace("::", "-"), slugify(topic), sorted(groups[topic])
        return

    models = {notes[n]["model"] for n in nids}
    if any("Domain" in MODEL_FIELDS.get(m, []) for m in models):
        groups = {}
        for n in nids:
            fields = notes[n]["fields"]
            groups.setdefault(fields[0] if fields else "misc", []).append(n)
        for domain in sorted(groups):
            yield domain, slugify(domain), sorted(groups[domain])
        return

    nids = sorted(nids)
    nchunks = max(1, -(-len(nids) // chunk))
    for i in range(nchunks):
        part = nids[i * chunk:(i + 1) * chunk]
        yield f"part {i + 1}", f"part-{i + 1:02d}", part


def render_file(deck_name, group_title, nids, notes):
    fields_of = lambda n: dict(
        zip(MODEL_FIELDS.get(notes[n]["model"], []) or
            [f"Field {i + 1}" for i in range(len(notes[n]["fields"]))],
            notes[n]["fields"]))
    models = sorted({notes[n]["model"] for n in nids})
    out = [
        f"# {deck_name} — {group_title}",
        "",
        f"> Deck: `{deck_name}` · Group: `{group_title}` · "
        f"Notes: {len(nids)} · Models: {', '.join(models)}",
        "",
    ]
    for n in nids:
        meta = f'note:{n} model:{notes[n]["model"]}'
        out.append(f"<!-- {meta} -->")
        for name, value in fields_of(n).items():
            out.append(f"**{name}:** {value}")
        if notes[n]["tags"]:
            # space-joined: Anki tags never contain spaces, but may contain
            # commas — joining with ', ' would be ambiguous on re-parse.
            out.append(f"**Tags:** {' '.join(notes[n]['tags'])}")
        out += ["", "---", ""]
    return "\n".join(out).rstrip() + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--db", default=DEFAULT_DB, help="path to collection.anki2")
    ap.add_argument("--out", default="cards", help="output directory")
    ap.add_argument("--deck", default="*", help="fnmatch filter on deck names")
    ap.add_argument("--chunk", type=int, default=100,
                    help="notes per file for ungrouped decks")
    args = ap.parse_args()

    if not Path(args.db).exists():
        sys.exit(f"collection not found: {args.db}")

    with tempfile.NamedTemporaryFile(suffix=".anki2") as tmp:
        con = snapshot(args.db, tmp.name)
        decks, note_deck, notes = load(con)
        con.close()

    total = 0
    for did, dname in sorted(decks.items(), key=lambda kv: kv[1]):
        if dname in SKIP_DECKS or not fnmatch.fnmatch(dname, args.deck):
            continue
        nids = [n for n, d in note_deck.items() if d == did]
        if not nids:
            print(f"skip  {dname} (empty)")
            continue
        deck_dir = Path(args.out) / slugify(dname)
        deck_dir.mkdir(parents=True, exist_ok=True)
        for title, slug, group in group_notes(nids, notes, args.chunk):
            path = deck_dir / f"{slug}.md"
            path.write_text(render_file(dname, title, group, notes))
        print(f"write {deck_dir}/  {len(nids)} notes from \"{dname}\"")
        total += len(nids)
    print(f"done: {total} notes exported")


if __name__ == "__main__":
    main()
