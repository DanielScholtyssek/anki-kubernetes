# anki-kubernetes

Flashcard decks for the CNCF **Golden Kubestronaut** certification track,
stored as plain markdown — plus tooling to mirror a live
[Anki](https://apps.ankiweb.net/) collection into this repo and restore it
into a fresh one.

Every note is a markdown file under `cards/`, so the decks are greppable,
diffable, and survive a lost or corrupted Anki collection. Cards target
the exam formats in `CERTS.md` (pure-MCQ certs get interactive
multiple-choice cards; hands-on certs get command/YAML recall cards).

## What's inside

```
AGENTS.md            conventions for AI agents that edit Anki via MCP
CERTS.md             Golden Kubestronaut exam formats (verified vs official pages)
README.md            this file
models/models.json   custom note type definitions (incl. the interactive "Many" MCQ type)
tools/export_anki.py snapshot collection.anki2 -> regenerate cards/
tools/parse_cards.py cards/*.md -> add_notes JSONL payloads (repo -> Anki)
tools/resplit.py     re-group tagless decks into topic/domain files
cards/<deck>/<topic>.md   one markdown file per topic, per deck
```

Inside each file, one card looks like:

```markdown
<!-- note:1781279834155 model:Many -->
**Domain:** Kubernetes Fundamentals
**Question:** Which command lists all pods in all namespaces?
**Options:** A. kubectl get pods<br>B. kubectl get pods -A<br>C. kubectl pods -A
**Answer:** B (2) – kubectl get pods -A
**Explanation:** -A/--all-namespaces is required; kubectl only shows the current namespace by default.
**Tags:** k8s::kcna topic::kubectl src::session

---
```

The `note:` anchor carries the Anki note ID; field names are the real
Anki field names and HTML is kept verbatim, so the format round-trips
losslessly back into Anki.

## Deck status

One folder per certification (target layout in `AGENTS.md`). Populated
decks:

| Folder | Anki deck | Notes | Provenance |
|---|---|---|---|
| `cards/ckad/` | CKAD - Certified Kubernetes Application Developer | 530 | shared AnkiWeb deck |
| `cards/cks/` | CKS - Certified Kubernetes Security Specialist | 993 | shared AnkiWeb deck |
| `cards/kcna/` | KCNA - Kubernetes and Cloud Native Associate | ~490 | mixed: ~318 authored here + shared-deck cards |
| `cards/kcsa/` | KCSA - Kubernetes and Cloud Native Security Associate | 310 | shared AnkiWeb deck |
| `cards/kubernetes-for-beginners/` | Kubernetes for Beginners | 135 | authored |

Planned-but-empty folders (with `.gitkeep`): `cka`, `ica`, `cnpe`,
`lfcs`, `pca`, `cca`, `capa`, `cgoa`, `cba`, `otca`, `kca`, `cnpa`.

## Using the cards

**Read them as markdown.** `cards/<deck>/<topic>.md` is plain text —
browse, grep, or feed to whatever you like. `**Question:**`/`**Front:**`
fields are the prompt; everything after is the answer and explanation.

**Import into your own Anki.** The restore path is designed around the
[ankimcp](https://ankiweb.net/shared/info/124672614) add-on and an MCP
client (e.g. an AI agent — see "Working with the agent" below):

1. `python3 tools/parse_cards.py cards/<dir>` emits one `add_notes`
   argument set per JSONL line (batches of 50, `--batch N` to change).
2. Create missing decks and custom models first (`models/models.json`
   has the definitions — `Many` is the interactive MCQ type).
3. Feed each JSONL line to the MCP `add_notes` tool.
4. Re-run `tools/export_anki.py` afterwards to re-anchor note IDs.

Anki assigns its own note IDs and scheduling — a restore gives you all
cards as *new*; review history lives in Anki, not in this repo.

## Refreshing the mirror

`tools/export_anki.py` snapshots `collection.anki2` via SQLite's backup
API (safe while Anki runs) and regenerates `cards/`:

```bash
python3 tools/export_anki.py                 # all non-empty decks
python3 tools/export_anki.py --deck "CKS*"   # matching decks only
python3 tools/export_anki.py --db /path/to/collection.anki2
```

The collection path resolves via `--db`, the `$ANKI_COLLECTION` env var,
or auto-detection (`~/.local/share/Anki2`, `~/Library/Application
Support/Anki2`, WSL `/mnt/c/Users/*/AppData/Roaming/Anki2/`).

For decks without topic tags, `tools/resplit.py` re-groups notes into
thematic files (KCNA/CKS exam domains); run it after a full export of
those decks.

## Working with an AI agent

`AGENTS.md` documents the conventions an agent follows when creating or
editing cards through the `anki` MCP server: deck naming, note types
(stock types + the custom `Many` MCQ model), the `k8s::<cert>` /
`topic::<area>` / `src::<origin>` tagging scheme, required duplicate
checks, and operations that always need confirmation. If you point an
agent at this repo, that file is the contract.

## Content provenance

Several folders mirror decks **shared publicly on AnkiWeb** and imported
as `.apkg` files — they're other authors' work, distributed freely via
AnkiWeb's sharing mechanism:

| Folder | Source deck | AnkiWeb |
|---|---|---|
| `cards/cks/` | KodeKloud - Certified Kubernetes Security Specialist | [shared deck](https://ankiweb.net/shared/info/20691376) |
| `cards/kcna/` (`src::deck-import` cards) | KCNA - Kubernetes and Cloud Native Associate | [shared deck](https://ankiweb.net/shared/info/1507217991) |
| `cards/kcsa/` | KCSA - Kubernetes and Cloud Native Security Associate | [shared deck](https://ankiweb.net/shared/info/1889916994) |
| `cards/ckad/` | Kubernetes CKAD - Complete Exam Deck | [shared deck](https://ankiweb.net/shared/info/317264836) |

The remaining cards were authored for this repo. Credit where credit's
due — the shared-deck authors did the heavy lifting on those folders.

## License

See `LICENSE`. Code in `tools/` is MIT; card content provenance is
described above.
