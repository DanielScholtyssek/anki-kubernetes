# anki-kubernetes

A personal knowledge base for managing [Anki](https://apps.ankiweb.net/)
flashcards for Kubernetes certification courses (CKAD, CKS, KCSA, KCNA).

The repo serves two purposes:

1. **A restorable, greppable mirror of Anki decks.** Every note in the
   collection is exported to markdown under `cards/`, so decks survive a
   lost/corrupted collection and can be searched and diffed with normal
   text tools.
2. **A working directory for an AI agent that edits Anki.** Decks are
   created and updated through the `anki` MCP server connected to the
   local Anki app. `AGENTS.md` holds the conventions the agent follows
   (deck names, note types, tagging, card style, safety rules).

## Layout

```
AGENTS.md            conventions for the AI agent (read this first)
README.md            this file
tools/export_anki.py dumps the live Anki collection into cards/
tools/parse_cards.py turns cards/*.md into add_notes payloads (JSONL)
tools/resplit.py     re-splits tagless decks into exam-domain topic files
models/models.json   note type definitions for rebuilding into empty Anki
cards/               markdown mirror of every deck, one file per topic
  ckad/<topic>.md    one file per ckad::* tag
  cks/<domain>.md    one file per CKS exam domain (via resplit.py)
  kcna/<domain>.md   one file per KCNA exam domain (via resplit.py)
  kcsa/<domain>.md   one file per MCQ 'Domain' field value
downloads/           (gitignored) original .apkg files / import notes
```

Inside each `cards/**/*.md` file, a card looks like:

```markdown
<!-- note:1781279834155 model:Basic++++ -->
**Front:** Command: list Pods in all namespaces.
**Back:** kubectl get pods -A
**Tags:** ckad::pods command namespaces

---
```

The `note:` comment carries the Anki note ID so edits can be pushed back
to the exact note. Field names are the real Anki field names and HTML is
kept verbatim for lossless round-tripping.

## Decks currently tracked

| Deck | Notes | Note type |
|---|---|---|
| CKAD - Certified Kubernetes Application Developer | 530 | Basic++++ |
| CKS - Certified Kubernetes Security Specialist | 993 | Basic+ |
| KCSA - Kubernetes and Cloud Native Security Associate | 310 | Many (MCQ) |
| KCNA - Kubernetes and Cloud Native Associate | 166 | Basic++/Basic+++ |

## Refreshing the mirror

`tools/export_anki.py` takes a consistent snapshot of `collection.anki2`
(using SQLite's backup API — safe while Anki is running) and regenerates
`cards/`:

```bash
python3 tools/export_anki.py               # export all non-empty decks
python3 tools/export_anki.py --deck "CKS*" # export matching decks only
python3 tools/export_anki.py --db /path/to/collection.anki2
```

Run it after importing a new `.apkg` or after a batch of MCP edits to
re-sync the repo. Default DB path is the Windows-side collection
(`/mnt/c/Users/crock/AppData/Roaming/Anki2/User 1/collection.anki2`).

## Restoring into Anki

The markdown round-trips losslessly (fields, tags and note types all
verified against the collection), so `cards/` can rebuild an empty
Anki — or add authored cards — via the `anki` MCP server:

1. The agent creates missing decks (`create_deck`) and missing note
   types (`create_model` from `models/models.json`).
2. `python3 tools/parse_cards.py cards/` emits one `add_notes`
   argument set per JSONL line (batches of 50, `--batch N` to change).
3. Each line is passed to the MCP `add_notes` tool.
4. After a restore, note IDs change — re-run `export_anki.py` so the
   `<!-- note:... -->` comments re-anchor.

## Working with the agent

Typical asks:

- "Add 10 cards about NetworkPolicies to the CKAD deck" — agent checks
  the deck/model, looks for duplicates via `find_notes`, batches
  `add_notes`, and appends the new cards to `cards/ckad/networkpolicy.md`.
- "Create a new deck for <course>" — agent creates `Kubernetes::<Name>`
  and seeds it with properly tagged notes.
- "Export/sync the repo with Anki" — run the export script.

See `AGENTS.md` for the full rule set (required add-workflow, tagging
scheme `k8s::<cert>` / `topic::<area>` / `src::<origin>`, and which
operations always require confirmation first).
