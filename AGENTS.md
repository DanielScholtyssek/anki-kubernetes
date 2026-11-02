# anki-kubernetes

This repo manages Anki flashcards for Kubernetes certification courses.
Cards are created and maintained through the **anki MCP server** connected
to the user's local Anki collection. Treat this file as the source of truth
for conventions; treat Anki itself as the source of truth for what exists.

## Prerequisites

- Anki desktop must be running (the MCP server talks to the live app).
- The `anki` MCP server must be connected. If a call fails, tell the user
  to start Anki — do not retry in a loop.
- Offer to `sync` with AnkiWeb at the start and end of a session.

## Decks

Existing decks (downloaded from course providers, imported as `.apkg`):

| Deck name in Anki | Notes | Model(s) |
|---|---|---|
| `CKAD - Certified Kubernetes Application Developer` | 530 | Basic++++ |
| `CKS - Certified Kubernetes Security Specialist` | 993 | Basic+ |
| `KCSA - Kubernetes and Cloud Native Security Associate` | 310 | Many (MCQ) |
| `KCNA - Kubernetes and Cloud Native Associate` | 166 | Basic++/Basic+++ |
| `Kubernetes for Beginners` | 0 | — |

- Downloaded decks are **read-only by default**: never edit, move,
  suspend, or delete their notes unless the user explicitly asks.
- **Always run `list_decks` before adding notes** — never guess deck names.
- New content the user asks for goes into the deck they name. If they name
  a downloaded deck, add to it directly rather than creating a parallel one.
- For brand-new decks we author, use `Kubernetes::<Name>` (create_deck
  supports max 2 levels of nesting) unless the user says otherwise.
- When adding cards to a downloaded deck, always use **stock note types**
  (`Basic`, `Cloze`, `Basic (and reversed card)`) — do NOT reuse the
  deck's bundled custom models (`Basic++++`, `Basic+`, `Many`, …). Those
  are opaque imports; standard types keep new cards predictable. Only
  deviate if the user explicitly asks for the deck's format (e.g. the
  interactive MCQ `Many` for KCSA).

## Note types

- Discover available types with `model_names`, and required fields with
  `model_field_names` before first use. Do not assume field names.
- Defaults:
  - `Basic` — question/answer cards (most cards).
  - `Basic (and reversed card)` — only when reverse recall is genuinely
    useful (e.g. "which flag does X", not for commands).
  - `Cloze` — for `kubectl` commands, YAML keys, and flag values.

## Card authoring rules

- One fact per card. If a card needs "and also", split it.
- Front is a real question ("Which command lists all pods in all
  namespaces?"), not a bare topic ("kubectl get pods").
- Wrap commands, flags, and YAML in `<code>` blocks so they render
  monospace. Keep code snippets under ~6 lines.
- Prefer practical, exam-relevant cards: imperative `kubectl` commands,
  YAML field names, troubleshooting steps, and concept distinctions
  (e.g. Deployment vs StatefulSet) over trivia.
- Cards must be accurate for current Kubernetes. If unsure about a flag,
  API version, or deprecated feature, verify before creating the card.

## Tagging

Tag every note we create so content stays attributable and searchable
(don't retag downloaded notes — their own schemes are fine):

- `k8s::<cert>` — e.g. `k8s::cka`
- `topic::<area>` — e.g. `topic::rbac`, `topic::networking`, `topic::etcd`
- `src::<origin>` — e.g. `src::course-udemy`, `src::docs`, `src::session`

## Adding cards — required workflow

1. `list_decks` → resolve the exact target deck name.
2. `model_field_names` → confirm the fields for the note type.
3. `find_notes` with `deck:<name>` plus topic terms → check for existing
   cards covering the same fact. Report duplicates to the user instead of
   silently re-adding (only use `allow_duplicate: true` when asked).
4. Prefer one `add_notes` batch call over repeated `add_note` calls.
5. Report the summary back: created / skipped / failed, with deck name
   and tags used.

## Editing cards

- For bulk edits, run `update_notes` with `dry_run: true` first and show
  the user the planned changes before writing.
- To edit a card, `find_notes` → `notes_info` to read current fields,
  then `update_notes` with only the changed fields.
- Use `tag_add` / `tag_remove` / `tag_batch` for retagging rather than
  rewriting note fields.

## Destructive operations — always ask first

Never run the following without explicit user confirmation for that
specific action: `delete_notes`, `filtered_deck_delete`, `card_forget`,
`card_change_deck` (moves study progress), `model_field_rename`,
`update_model_templates`, `update_model_styling`, `optimize_fsrs_params`,
`set_fsrs_params`.

## Repo layout

```
AGENTS.md              this file — conventions for the agent
README.md              human-facing overview of the repo
tools/export_anki.py   dumps the live collection to cards/ (Anki -> repo)
tools/parse_cards.py   cards/*.md -> add_notes JSONL (repo -> Anki input)
tools/resplit.py       re-splits decks thematically (CKS/KCNA exam domains)
models/models.json     note type defs (fields/templates/css) for restore
cards/                 markdown mirror of every deck. THEMATIC/TOPIC
  ckad/<topic>.md      SPLIT IS PREFERRED — one file per topic:
  kcsa/<domain>.md     ckad::* tag -> file per topic; KCSA 'Domain' field;
  cks/<domain>.md      CKS -> CKS exam domain files (tools/resplit.py);
  kcna/<domain>.md     KCNA -> KCNA exam domain files (tools/resplit.py).
downloads/             (gitignored) original .apkg files / import notes
```

Card format inside `cards/**/*.md` (field names are real Anki field
names, HTML kept verbatim, `note:` comment anchors each card for sync,
tags space-separated like Anki stores them):

```markdown
<!-- note:1781279834155 model:Basic++++ -->
**Front:** Command: list Pods in all namespaces.
**Back:** kubectl get pods -A
**Tags:** ckad::pods command namespaces

---
```

## Mirroring Anki -> repo

`tools/export_anki.py` snapshots `collection.anki2` (via SQLite backup —
safe while Anki runs) and rewrites `cards/`:

```bash
python3 tools/export_anki.py                 # all non-empty decks
python3 tools/export_anki.py --deck "CKS*"   # one deck
```

The default DB path is the Windows-side collection at
`/mnt/c/Users/crock/AppData/Roaming/Anki2/User 1/collection.anki2`;
override with `--db` if it moves.

- **Grouping preference:** the user prefers thematic files —
  `cards/<deck>/<topic>.md`, one file per topic, filename = lowercase
  slug of the topic. When adding cards to Anki via MCP, append them to
  the matching topic file (create it if needed, same format) so the repo
  stays a restorable record — or re-run the export to re-sync
  everything. Never start a new `part-NN` file for authored content when
  a topic file fits.
- For decks that lack a topic signal, `tools/resplit.py` derives topics:
  CKS notes are scored per lecture segment into the six CKS exam domains
  (+ fundamentals/exam-prep), KCNA notes per card into the five KCNA
  domains. Re-run it after new notes land in those decks — and note its
  `*_KEYWORDS`/`*_OVERRIDES` maps are heuristics worth reviewing.
- Caveat: `export_anki.py` regenerates `cks/`/`kcna/` as sequential
  `part-NN` files (it only knows tags/Domain). After a full export,
  re-run `tools/resplit.py` to restore the thematic split.
- The `note:` comments carry Anki note IDs. Keep them when editing a
  file; they make `update_notes` lookups trivial.
- When the user pastes course material, turn it into cards per the
  workflow above — don't dump raw text into `cards/` files.

## Restoring repo -> Anki (import)

To push markdown cards into Anki — e.g. rebuilding an empty collection or
adding authored files — do NOT write to collection.anki2. Go through MCP:

1. `list_decks` → `create_deck` for every missing target deck.
2. `model_names` → for each `model:` used in the files, if missing
   recreate it with `create_model` using `models/models.json`
   (`in_order_fields`, `card_templates`, `css`, `is_cloze`).
3. Generate payloads: `python3 tools/parse_cards.py cards/<dir>`
   emits one `add_notes` argument set per JSONL line (batches of 50;
   `--batch N` to change, `--keep-ids` to carry old note ids).
4. Call `add_notes` per line; report created/skipped/failed totals.
5. After a full restore, note IDs change — re-run `tools/export_anki.py`
   so the `<!-- note:... -->` comments re-anchor to the new IDs.

The markdown↔fields mapping is verified lossless against the collection
(all fields, tags, models round-trip exactly), so trust the payloads.
