# anki-kubernetes

A personal knowledge base for managing [Anki](https://apps.ankiweb.net/)
flashcards for the Golden Kubestronaut certification track — one deck
per CNCF certification plus LFCS (see `CERTS.md`).

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

The target is **one deck per Golden Kubestronaut certification** —
see `AGENTS.md` for the full deck-name → `cards/` folder mapping and
`CERTS.md` for exam formats (which exams are hands-on vs multiple
choice). Four decks are downloaded course decks (CKAD, CKS, KCNA,
KCSA); the rest are authored decks, plus `Kubernetes for Beginners`
for general/foundations material.

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
Anki collection. Writes always go through the `anki` MCP server — the
repo scripts never touch `collection.anki2` directly.

### Prerequisites

- Anki installed with a fresh/empty profile (or any collection you want
  to fill).
- The [ankimcp](https://ankiweb.net/shared/info/124672614) add-on
  installed and the `anki` MCP server configured in the client where the
  agent runs — same setup as the current machine.
- This repo checked out locally.

### How it works

The restore is agent-driven: the agent reads `cards/`, prepares the
collection, and feeds parser output to the MCP `add_notes` tool. Tell
the agent e.g. "restore the repo decks into this Anki" and it does the
steps below — they are listed explicitly so you can follow or reproduce
them:

1. **Generate the payloads** (local, no Anki contact):

   ```bash
   python3 tools/parse_cards.py cards/ > /tmp/payloads.jsonl
   ```

   Each line is one complete `add_notes` argument set
   (`{deck_name, model_name, notes: [...], tags}`), grouped by deck+model
   and capped at 50 notes (`--batch N` to change, `--keep-ids` to carry
   old note IDs for grepping).

   Restore a subset instead of everything:

   ```bash
   python3 tools/parse_cards.py cards/ckad/           # one deck
   python3 tools/parse_cards.py cards/kcsa/compliance.md   # one file
   ```

2. **Create the note types.** In an empty collection only stock types
   (`Basic`, `Cloze`, …) exist. The agent calls `create_model` for each
   definition in `models/models.json` — that rebuilds the bundled types
   the downloaded decks use (`Basic++++`, `Basic+`, `Basic++`,
   `Basic+++`) and the interactive MCQ type `Many`, including card
   templates and CSS.

3. **Create the decks.** `create_deck` for every deck appearing in the
   payloads (`deck_name` field of each JSONL line).

4. **Load the cards.** For each line of the JSONL the agent calls
   `add_notes`, then reports per-batch `created` / `skipped` / `failed`.
   Duplicates are skipped by Anki automatically, so re-running is
   idempotent.

5. **Re-anchor the mirror.** The new collection assigns fresh note IDs,
   so afterwards:

   ```bash
   python3 tools/export_anki.py --db /path/to/new/collection.anki2
   ```

   regenerates `cards/` with the new `<!-- note:... -->` anchors.
   `models/models.json` stays valid — note type names don't change.

### Things to know

- **Old note IDs are metadata only.** They are never sent to the new
  collection; Anki assigns its own.
- **Scheduling state is not in the markdown.** Review history, intervals
  and due dates live in Anki only — a restore gives you all cards as
  *new* cards. Keep AnkiWeb sync/backups for preserving progress.
- **`kubernetes-for-beginners/` cards are authored content** — they use
  stock models (`Basic`, `Cloze`, `Basic (and reversed card)`) plus
  `Many`, so they restore fine once `Many` exists (step 2).
- **Order matters but is simple:** models before notes, decks before
  notes. The agent handles it; `add_notes` fails with a clear error if a
  model or deck is missing.

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
