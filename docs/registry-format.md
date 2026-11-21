# The Registry Format

`buddies.json` is `{ "buddies": [ <entry>, ... ] }`. Every field the
dashboard and generators understand:

| Field | Meaning |
|---|---|
| `id` | Kebab-case unique id (`reading-buddy`). Never changes once created. |
| `name` | Display name (`Reading Buddy`). Person buddies are possessive: `Sam's Buddy`. |
| `icon` | One emoji. |
| `kind` | Loose family grouping (`system`, `personal`, `work`, …) — drives tree colors. |
| `type` | `project`, `buddy`, or `people-group`. Projects get the project view. |
| `parent` | Another buddy's id, or `null` for a root. The Coordinator is the default root. |
| `brief` | One or two sentences: what this buddy is for. |
| `homepage` | Path of its homepage inside this repo (`reading-buddy/`). |
| `repo` | Its own GitHub repo name (bare name or full URL; the write paths normalize both). |
| `status` | Free-form short status (`active`, `brief`, `building`, …). |
| `attention` | Open items needing the owner: `[{id, text, date}]`. Dispositions are stamps on the entry — see below. |
| `links` | `[{label, url}]` — the buddy's important links. |
| `files` | `[{title, url? , path?, note?}]` — documents the buddy manages; shown in its Files section. |
| `private_files` | `true` = list repo file names on the homepage without publishing their contents. |
| `voice` / `persona` | Optional TTS voice id (from `voice-catalog.json`) and persona name (from `persona-roster.md`). |

## Attention dispositions (registry stamps)

A disposition is a stamp object on the attention entry, written through the
token-gated path by the dashboard and homepages:

- `cleared: {date, by}` — done.
- `later: {date, by}` — snoozed.
- `dropped: {date, by}` — deliberately dropped.

The three are mutually exclusive; Undo removes all three. A stamped item
leaves the open counts everywhere but stays visible in place with its stamp.
`date` is the owner's local date (`YYYY-MM-DD`); `by` is the owner name from
`instance.json`.

## Plans

`plans.json` is `{ "plans": [ {id, name, icon, buddies, desc, docs, status, statusClass} ] }` —
the dashboard's project plans. `docs` is `[{label, url}]`.
