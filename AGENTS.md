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

Decks come from two sources:

- **Downloaded decks** — imported from course providers as `.apkg`
  (e.g. the CKAD / CKS / KCSA / KCNA cert decks). Their bundled note
  types are opaque clones (`Basic++++`, `Basic+`, …); treat the
  imported notes as third-party content.
- **Authored decks** — ones we create ourselves.

### Target layout: one deck per Golden Kubestronaut cert

The goal is **one deck per certification** on the Golden Kubestronaut
track (all CNCF certs + LFCS). Naming: `<ACRONYM> - <full title>`,
flat top-level names matching the downloaded-deck style, e.g.
`PCA - Prometheus Certified Associate`.

Current set — full deck name → `cards/` folder (acronym slug).
**(dl)** = deck exists as a downloaded `.apkg` deck that doubles as the
cert deck; authored cards for those certs go INTO the downloaded deck,
never into a parallel authored one:

| Deck name in Anki | `cards/` folder | Source |
|---|---|---|
| `CKA - Certified Kubernetes Administrator` | `cards/cka/` | authored |
| `CKAD - Certified Kubernetes Application Developer` | `cards/ckad/` | **(dl)** |
| `CKS - Certified Kubernetes Security Specialist` | `cards/cks/` | **(dl)** |
| `KCNA - Kubernetes and Cloud Native Associate` | `cards/kcna/` | **(dl)** |
| `KCSA - Kubernetes and Cloud Native Security Associate` | `cards/kcsa/` | **(dl)** |
| `PCA - Prometheus Certified Associate` | `cards/pca/` | authored |
| `ICA - Istio Certified Associate` | `cards/ica/` | authored |
| `CCA - Cilium Certified Associate` | `cards/cca/` | authored |
| `CAPA - Certified Argo Project Associate` | `cards/capa/` | authored |
| `CGOA - Certified GitOps Associate` | `cards/cgoa/` | authored |
| `CBA - Certified Backstage Associate` | `cards/cba/` | authored |
| `OTCA - OpenTelemetry Certified Associate` | `cards/otca/` | authored |
| `KCA - Kyverno Certified Associate` | `cards/kca/` | authored |
| `CNPA - Certified Cloud Native Platform Engineering Associate` | `cards/cnpa/` | authored |
| `CNPE - Certified Cloud Native Platform Engineer` | `cards/cnpe/` | authored |
| `LFCS - Linux Foundation Certified System Administrator` | `cards/lfcs/` | authored |

General/foundations material goes to `Kubernetes for Beginners`
(`cards/kubernetes-for-beginners/`). CNCF adds certs over time —
re-check the official list before creating a new cert deck + folder.
- Cert attribution also lives in `k8s::<cert>` tags so content stays
  searchable across decks.

Deck names and note counts change over time — **always run `list_decks`
before adding notes** and resolve the live name; never guess or rely on
a remembered list.

- Notes that came from a downloaded deck are **read-only**: never edit,
  move, suspend, or delete them unless the user explicitly asks.
- Adding NEW cards to a downloaded deck is welcome whenever the user
  asks — e.g. extra material for a cert course. Those decks already
  carry hundreds of cards, so before adding, check for overlap:
  `find_notes` with `deck:<name>` + topic terms, and report similar
  existing cards rather than stacking near-duplicates (see "Adding
  cards — required workflow").
- For brand-new NON-cert decks we author, use `Kubernetes::<Name>`
  (create_deck supports max 2 levels of nesting) unless the user says
  otherwise. Cert decks always follow the `<ACRONYM> - <title>` naming
  above.
- When adding cards to a downloaded deck, use **stock note types**
  (`Basic`, `Cloze`, `Basic (and reversed card)`) — do NOT reuse the
  deck's bundled clones (`Basic++++`, `Basic+`, …). Those are opaque
  imports; standard types keep new cards predictable. One exception:
  `Many` is allowed anywhere for genuine multiple-choice cards (see
  "Note types").

## Note types

- Discover available types with `model_names`, and required fields with
  `model_field_names` before first use. Do not assume field names.
- **Mix card types when authoring a batch** — don't produce wall-to-wall
  `Basic`. Pick per card:
  - `Basic` — question/answer cards (the default workhorse).
  - `Basic (and reversed card)` — prefer this over plain `Basic` whenever
    reverse recall makes sense: definitions↔terms ("which object does X" /
    "what is X called"), flag→purpose, port↔protocol, acronym expansions.
    Skip it when the reverse question is meaningless (commands, long
    explanations, anything where the back can't function as a question).
  - `Cloze` — for `kubectl` commands, YAML keys, and flag values.
  - `Many` (the interactive MCQ model from the KCSA deck) — for
    multiple-choice cards with real distractors: "which of these…",
    "select all that apply", pick-the-right-command. Fields: `Domain`
    (exam domain/section), `Question`, `Options` (`A. …<br>B. …`),
    `Answer` (`C (3) – text`; multi-select: `A, C – text` — the template
    parses the leading letter run and requires the exact set),
    `Explanation`, `Sources`. Exception to the
    stock-types-only rule — this model is sanctioned for MCQ content.
    Fallback if `Many` is unavailable: `Basic` with options in `Front`
    and the answer letter in `Back`.
- **Match the card mix to the target deck's exam format** (formats are
  listed in `CERTS.md`, verified against official CNCF pages):
  - Pure-MCQ cert decks — KCNA, KCSA, PCA, CCA, CAPA, CGOA, CBA, OTCA,
    KCA, CNPA: **`Many` should be the majority (~50-70%)** since the
    real exam is multiple choice and MCQ cards rehearse the format.
    `Basic`/`Cloze` fill in where MCQ doesn't fit (commands, YAML).
  - Hands-on decks — CKA, CKAD, CKS, ICA, CNPE, LFCS: keep the default
    mix below — recall of commands/flags/YAML matters more than
    recognition.
  - Default mix (foundations/`Kubernetes for Beginners`): aim for
    ~60-70% `Basic` (using `Basic (and reversed card)` wherever it
    applies — it counts toward the `Basic` share and produces two
    cards per note), the rest split between `Cloze` and `Many`
    depending on the material.

## Card authoring rules

- One fact per card. If a card needs "and also", split it.
- Backs must be self-contained — the answer should teach the fact even
  with zero surrounding context: name the tool/command, define any term
  used, and include the "why" in one sentence. The user studies cards
  standalone; an answer that only makes sense next to the question or
  the video it came from is a bad card.
- Front is a real question ("Which command lists all pods in all
  namespaces?"), not a bare topic ("kubectl get pods").
- Wrap commands, flags, and YAML in `<code>` blocks so they render
  monospace. Keep code snippets under ~6 lines.
- Prefer practical, exam-relevant cards: imperative `kubectl` commands,
  YAML field names, troubleshooting steps, and concept distinctions
  (e.g. Deployment vs StatefulSet) over trivia.
- Cards must be accurate for current Kubernetes. Use the `fetch` MCP
  server liberally when authoring: verify concrete details (flags, API
  versions, deprecated features) AND pull general background info
  (concepts, terminology, how pieces relate) from authoritative sources
  like the kubernetes.io concepts/tasks/reference pages. Prefer fetched
  docs over memory so card backs carry correct, well-sourced "why"
  explanations.
- **Always check kubernetes.io docs for extra material.** Beyond
  verifying what was asked, read the fetched pages actively for better
  details and NEW question angles the request didn't cover — e.g.
  defaults, edge cases, related objects, common misconceptions. When a
  doc detail fits the concept and isn't a near-duplicate of an existing
  card, turn it into a card (or surface it to the user as a suggested
  follow-up if it's a stretch beyond the requested scope). The docs
  often know better what's worth drilling than the course notes do.
- **MCQ design (`Many`):** the template supports multi-select — when a
  question's material has more than one genuinely correct option, write
  it as a select-all/multi-answer question ("Which of the following are
  true? (Select all that apply)") and list EVERY correct letter in
  `Answer` (`A, C, D – text`). Never mark a single letter when the
  explanation validates several — the card evaluates the exact set.
  Keep single-letter answers only for genuinely single-best-answer
  questions, and make sure distractors are actually wrong.

## Tagging

Tag every note we create so content stays attributable and searchable
(don't retag downloaded notes — their own schemes are fine):

- `k8s::<cert>` — e.g. `k8s::cka`
- `topic::<area>` — e.g. `topic::rbac`, `topic::networking`, `topic::etcd`
- `src::<origin>` — e.g. `src::course-udemy`, `src::docs`, `src::session`

**Minimum 2 content tags per note.** Beyond the bookkeeping tags
(`k8s::`, `src::`), every note needs at least two `topic::` tags: one
for the broader topic area and one for the specific technology/term it
teaches (e.g. `topic::replicasets` + `topic::ha`, `topic::yaml` +
`topic::api`). The collection already has many tags — reuse existing
ones (check with `find_notes`/`tag` tools or the `cards/` mirror)
rather than inventing near-duplicate spellings like `topic::pod` vs
`topic::pods`.

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
  <cert>/<topic>.md    SPLIT IS PREFERRED — one folder per cert acronym
  kcsa/<domain>.md     (cka/, ckad/, pca/, lfcs/, …), one file per topic:
  cks/<domain>.md      ckad::* tag -> file per topic; KCSA 'Domain' field;
  kcna/<domain>.md     CKS -> CKS exam domain files (tools/resplit.py);
                       KCNA -> KCNA exam domain files (tools/resplit.py);
                       cert decks for other certs = topic files like
                       kubernetes-for-beginners/.
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
- **Session deck → folder mapping:** the user names the target deck at
  the start of a session. Mirror new notes into
  `cards/<deck-folder>/<topic>.md` where `<deck-folder>` is the
  slugified deck name — lowercase acronym for cert decks
  (`CKA - Certified Kubernetes Administrator` → `cards/cka/`,
  `Kubernetes for Beginners` → `cards/kubernetes-for-beginners/`), same
  `slugify()` logic as `tools/export_anki.py`. Create the folder (with
  `.gitkeep`) for decks that have no cards yet.
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
