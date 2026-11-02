#!/usr/bin/env python3
"""Parse cards/**/*.md into add_notes-ready JSON payloads (JSONL on stdout).

The parser only reads repo files — it never touches Anki. Feed each output
line as the arguments to the anki MCP `add_notes` tool:

    python3 tools/parse_cards.py cards/ckad/pods.md
    python3 tools/parse_cards.py cards/            # everything
    python3 tools/parse_cards.py cards/ --batch 25 # smaller batches

Card format expected (produced by tools/export_anki.py):

    <!-- note:1781279834155 model:Basic++++ -->
    **Front:** question text
    **Back:** answer text
    **Tags:** tag1 tag2        (optional, space-separated)
    ---

Notes:
- Field values may wrap onto continuation lines; a line that does not start
  with `**Name:**`, `<!-- note:`, `---`, `#` or `>` is appended to the
  previous field's value.
- The deck name comes from the file header line `> Deck: "<name>"`.
- Old `note:` IDs are kept in a `_note` key inside each payload so output
  can be grepped back to source; strip it before calling add_notes if your
  MCP server rejects unknown args.
"""

import argparse
import json
import re
import sys
from pathlib import Path

CARD_RE = re.compile(r"^<!--\s*note:(\d+)\s+model:(\S+)\s*-->\s*$")
FIELD_RE = re.compile(r"^\*\*([^*]+):\*\*\s?(.*)$")
DECK_RE = re.compile(r"^>\s*Deck:\s*`([^`]+)`")
STOP_RE = re.compile(r"^(---|#|>|<!--)")


def parse_file(path: Path):
    """Yield (deck_name, model, note_id, fields, tags) per card in a file."""
    deck = None
    cards = []
    cur = None  # dict: model, note_id, fields(ordered dict), tags, last_field

    def flush():
        if cur and cur["fields"]:
            cards.append((deck, cur["model"], cur["note_id"],
                          cur["fields"], cur["tags"]))

    for line in path.read_text().splitlines():
        m = DECK_RE.match(line)
        if m:
            deck = m.group(1)
            continue
        m = CARD_RE.match(line)
        if m:
            flush()
            cur = {"note_id": int(m.group(1)), "model": m.group(2),
                   "fields": {}, "tags": [], "last": None, "blanks": 0}
            continue
        if cur is None:
            continue
        m = FIELD_RE.match(line)
        if m:
            name, value = m.group(1).strip(), m.group(2)
            if name.lower() == "tags":
                cur["tags"] = value.split()
                cur["last"] = None
            else:
                cur["fields"][name] = value
                cur["last"] = name
            cur["blanks"] = 0
            continue
        if line.strip() == "---":
            flush()
            cur = None
            continue
        if line.strip() == "":
            cur["blanks"] += 1  # maybe intra-field blank; decided later
            continue
        if cur["last"] and not STOP_RE.match(line):
            cur["fields"][cur["last"]] += "\n" * (cur["blanks"] + 1) + line
            cur["blanks"] = 0
    flush()
    return cards


def iter_markdown(paths):
    for p in paths:
        p = Path(p)
        if p.is_dir():
            yield from sorted(p.rglob("*.md"))
        elif p.is_file():
            yield p
        else:
            print(f"warn: no such path {p}", file=sys.stderr)


def main():
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="*", default=["cards"],
                    help="markdown files or directories (default: cards/)")
    ap.add_argument("--batch", type=int, default=50,
                    help="max notes per payload; 0 = one payload per "
                         "deck+model (default: 50)")
    ap.add_argument("--keep-ids", action="store_true",
                    help="include '_note' (old note id) in each note entry")
    args = ap.parse_args()

    groups = {}  # (deck, model) -> [note entries]
    skipped = []
    nfiles = 0
    for f in iter_markdown(args.paths or ["cards"]):
        nfiles += 1
        cards = parse_file(f)
        if not cards:
            skipped.append(str(f))
            continue
        for deck, model, nid, fields, tags in cards:
            if not deck:
                print(f"warn: {f}: card {nid} has no deck header; "
                      f"using dir name", file=sys.stderr)
                deck = f.parent.name
            entry = {"fields": fields}
            if tags:
                entry["tags"] = tags
            if args.keep_ids:
                entry["_note"] = nid
            groups.setdefault((deck, model), []).append(entry)

    total = 0
    nbatches = 0
    for (deck, model), entries in sorted(groups.items()):
        size = args.batch or len(entries)
        for i in range(0, len(entries), size):
            payload = {"deck_name": deck, "model_name": model,
                       "notes": entries[i:i + size]}
            print(json.dumps(payload, ensure_ascii=False))
            nbatches += 1
        total += len(entries)
        print(f"  {deck} [{model}]: {len(entries)} notes "
              f"({-(-len(entries) // size)} batch(es))", file=sys.stderr)

    for f in skipped:
        print(f"warn: no cards parsed from {f}", file=sys.stderr)
    print(f"done: {total} notes, {nbatches} payload(s), {nfiles} file(s)",
          file=sys.stderr)


if __name__ == "__main__":
    main()
