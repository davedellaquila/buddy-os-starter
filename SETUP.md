# SETUP.md — First Run

> **A note for the person holding this file: you don't need to read
> it.** You can if you're curious — nothing here is secret — but it is
> written for your Muse, not for you, and it is long and technical by
> design. Your only job is to get this document over to your Muse:
> copy and paste its contents into a new chat, or attach the file.
> Once your Muse has it, it reads the file on its own and takes over
> from the first step. Your own guide is
> [START-HERE.md](START-HERE.md).

**This guide is written for the user's Muse.** If you are the Muse who
just received a fresh copy of this repository: this is your job now. Work
through it with your user, in order. Skip nothing silently — where a step
needs a choice, ask; where a default exists, take it and keep moving.

Your user's copy of this repo should be **private** (the template is public;
a working Buddy OS holds a life). If their copy is public, say so once and
offer to walk them through making it private before anything personal goes in.

The human has a companion guide, [START-HERE.md](START-HERE.md) — it tells
them what you'll do and what you'll ask, in plain language. Keep your
questions consistent with what it promises.

---

## Who's who (read this first)

- **You — the Muse running this setup — are the user's chief of staff.**
  You are the main interface they talk to. That role is never "installed";
  it is who is holding this guide.
- **The Coordinator is a buddy inside the system** — a project-tracking
  buddy (it tracks projects, open items, and the buddy tree), one level
  down from you. Setup creates it *with* the user in step 3. Never describe
  the Coordinator as the user's chief of staff or as their interface;
  it is staff, not the front door.

## 1. Interview (10 minutes, conversational)

Learn, in this order:

1. Their name, and what to call them.
2. Their timezone.
3. What they care about right now — the 3–5 things a staff should help with.
4. Who matters to them (people a future buddy may be named for).
5. Their GitHub username (the copy lives under it) — and confirm they
   have a Google account: the system keeps its documents in Google Docs
   and its registers and trackers in Google Sheets. If either account is
   missing, pause and help them create it before step 2.

Defaults rule: persona, voice, and icon choices never block setup. Pick
sensible defaults; they can change everything later.

## 2. Configure the instance

Create `instance.json` beside `build.py` (start from `instance.example.json`):

```json
{
  "owner_name": "<what to call them>",
  "github_owner": "<their GitHub username>",
  "system_repo": "<the name of THIS repo in their account>",
  "pages_url": "",
  "tipjar_url": "",
  "root_order": ["coordinator-buddy"],
  "root_name": "Coordinator",
  "starter_version": "<the starter release this copy came from>"
}
```

`starter_version` records which starter release this copy is running —
it is how a future update knows where this copy stands. Leave it exactly
as the template shipped it; [UPDATE.md](UPDATE.md) maintains it from
here.

`pages_url` may stay empty — the build derives
`https://<github_owner>.github.io/<system_repo>/`. Set `tipjar_url` only if
they have a tip destination (Ko-fi or similar); empty hides the dashboard's
tip jar.

## 3. Create the first buddy together: the Coordinator

The starter ships the Coordinator as a fully-worked example
(`samples/coordinator-buddy/` — brief, config, knowledge). Walk it with your
user and make it *theirs*:

1. Read the brief card aloud (summarized). Ask: does this job description
   match the job you want tracked — projects, open items, the tree itself?
   Edit `BRIEF.md` in their words.
2. Pick a persona from `persona-roster.md` (default: The Coordinator) and an
   icon (default 🧭). Record both in the registry entry and `CONFIG.md`.
3. Confirm the registry entry in `buddies.json` — it is already wired
   (`parent: null`, `homepage: "coordinator-buddy/"`). The registry format
   is documented in `docs/registry-format.md`.

## 4. The pick-list: choose the starting staff

Your Coordinator already exists (step 3) — it is the anchor: pre-selected,
recommended, their first buddy. Now present the other six starter buddies
as a **pick-list**, using each brief card as the pitch
(`samples/*/BRIEF.md`): Reading 📚, Fitness 🏃, Budget 🧾, Home 🏠,
Travel 🧳, Learning 🌱. One question per card: *install this one now?*

- **Picked:** spend two minutes making the brief theirs; the buddy is
  wired into the registry in step 5 and gets its homepage.
- **Not picked:** the buddy is simply not installed yet. **Do not delete
  anything** — its brief card stays in `samples/` in their copy, and they
  can install it any later day by asking you. Prune only its registry
  entry for now (registry seeding follows the picks; the card is how it
  comes back).
- Say this plainly, in so many words: **the pick-list is a starting set,
  not a ceiling.** They can install any of these later, and they can
  create entirely new buddies of their own at any time — the seven are
  a menu, not the whole kitchen.

## 5. Generate homepages and build the dashboard

```bash
python3 gen_basic_homepages.py            # every buddy's homepage
python3 gen_default_homepages.py --about coordinator-buddy reading-buddy fitness-buddy budget-buddy home-buddy travel-buddy learning-buddy
python3 build.py                          # the dashboard: index.html
```

(Adjust the `--about` list to the buddies they picked in step 4 — generation follows the registry, which now holds exactly their picks plus the Coordinator.) Then open the
dashboard locally and walk it together: the tree, the Coordinator's panel,
its attention item — which is real: *"Finish setup and turn one brief card
into your first real buddy."* Leave it open; it closes when they've done it.

## 6. Publish with GitHub Pages

In their repo: **Settings → Pages → Deploy from a branch → `main` / root.**
Their dashboard is then at the `pages_url` from step 2. **Verify on the
served copy** — open the live URL and confirm the dashboard and the
Coordinator's homepage render there. A local build is a promise; the served
copy is the fact.

## 7. The token step (token-gated writes)

The dashboard and homepages write back to GitHub (attention dispositions,
brain dumps, notes) using a token the user pastes **once, into the page's
token prompt, on their own device**. Before they create it, give them the
full framing — this exact shape, every time:

- **Which account:** their GitHub account, the one that owns this repo.
- **Which single permission:** a classic personal access token with the
  **`repo`** scope — nothing broader.
- **What they will see:** GitHub's token page, then the dashboard's token
  pill turning green. The token is stored only in their browser's local
  storage on that device.
- **What must never happen:** the token is never pasted into chat, never
  written into any file, never committed. If it ever is, it gets revoked
  and reissued — no exceptions.
- **Abort condition:** if anything about the page asking for the token looks
  different from this description, stop and check before pasting.

Walk them to **GitHub → Settings → Developer settings → Personal access
tokens → Tokens (classic) → Generate new token**, have them tick only
`repo`, generate, and paste it into the dashboard's token pill (top of the
page). Then prove it works: disposition the Coordinator's sample attention
item as **Later** from its homepage, and show them the stamp it wrote into
`buddies.json`. Undo it together.

## 8. Day two

- Rename a sample buddy into something truly theirs, or create a brand-new
  one: brief first (use the Coordinator's brief as the pattern), registry
  entry, homepage. First task is always the homepage.
- Read `AGENTS.md` together and edit one line so it's theirs.
- Set a standing rhythm: a morning glance at the dashboard's open items.
- When a starter release lands, `UPGRADING.md` explains what changed and
  how to adopt it — you (their Muse) apply it, keeping their data.

Welcome to the staff. Less app, more buddy.
