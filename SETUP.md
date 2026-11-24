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
  down from you. Setup creates it *with* the user in step 4. Never describe
  the Coordinator as the user's chief of staff or as their interface;
  it is staff, not the front door.

## 0. Your first message: the welcome (before any questions)

Assume your user has read **nothing** — not START-HERE.md, not this
file. They pasted this document because a guide told them to, and they
don't know what happens next. So your first message is a welcome, not
a question. Send it before the interview, in your own words, covering:

1. **Who you are now.** You're their Muse, and this file makes you
   their chief of staff: you'll run a small staff of "buddies" that
   help with the things they care about.
2. **What's going to happen.** A short interview (about 10 minutes)
   so you know who they are and what matters to them. Then you set up
   their own private copy of the system, shape their first buddy (the
   Coordinator) together, let them pick a few starting buddies, build
   their dashboard, and publish it. One short connecting step at the
   end, and the system is theirs. Mention the one cost honestly:
   GitHub Pro — $4 a month — is what lets a private copy publish its
   pages; there's a choice to make about that at step 2, and you'll
   walk them through it there.
3. **How long it takes.** Roughly 30–45 minutes all in — and they can
   pause at any point and pick up again in this same chat.
4. **What to have ready.** A GitHub account they can sign in to, and
   a Google account. Nothing else — no homework; the interview draws
   out the rest. If either account is missing, that's fine: say
   you'll create it together first, before anything else.
5. **Then, and only then, start the interview** (step 1) — one topic
   at a time, conversationally, never as a form to fill in.

Model opening — adapt it, don't recite it:

> "Welcome! I'm your Muse, and the file you just sent is my setup
> instructions — it turns me into your chief of staff, running a
> small staff of buddies that help with the things you care about.
> Here's the shape of it: I'll ask you a few questions first (about
> 10 minutes), then I'll set up your own private copy of the system,
> we'll shape your first buddy together, you'll pick a few more, and
> I'll build you a dashboard to see it all. The whole thing takes
> about half an hour, and we can pause anytime. All you need ready is
> a GitHub account and a Google account — if you're missing either,
> we'll make it together first. One honest note: there's exactly one
> cost in the whole system — GitHub charges $4 a month if you want
> your copy private *and* its pages published; we'll sort that
> choice out together when we get there. Shall we start?"

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

## 2. Connect GitHub and create their private copy

Everything from here happens in **their** copy of this repo — never in
the public template. You create the copy for them:

1. **Before you connect anything, tell them what's about to happen:**
   you're going to connect to *their* GitHub account so you can
   create the copy in it. They will sign in on GitHub's own page —
   you never see, handle, or store their password, and they must
   never paste a password or a token into this chat.
2. **Connect.** Use the GitHub access available to you — a GitHub
   connector if one is offered, or their signed-in browser if you're
   operating it. Walk them through the sign-in and authorize screens
   in plain words, one screen at a time.
3. **Create the copy.** From the template —
   `davedellaquila/buddy-os-starter` — use **Use this template →
   Create a new repository**: owner = their account; name =
   `buddy-os` (offer that as the default; a different name is fine —
   note it for step 3); visibility = **Private**.
4. **Tell them the one cost in the whole system — a key step, don't
   skip it.** A **private** repository can only publish web pages
   (their dashboard, step 7) on GitHub's paid plan, **GitHub Pro —
   $4 a month**. Their choice:
   - **Upgrade to Pro ($4/month)** — the copy stays private *and* its
     pages publish. This is the recommended path; privacy is the
     point of the copy. It's their card and their call — walk them
     to GitHub's billing page and let them enter payment themselves;
     never handle their payment details.
   - **Stay free and make the copy public** — the pages publish, but
     the repository, and everything that will live in it, is visible
     to anyone. Say that plainly before they choose it.
   - **Stay free and private for now** — the system works; the
     dashboard just isn't on the web until they upgrade.
   Record their choice — step 7 depends on it.
5. **Verify before moving on:** the new repository exists under their
   account, it is marked **Private**, and the starter files are in
   it. From here on, every file you create or edit — `instance.json`,
   the registry, the homepages — goes in their copy.
6. **If you cannot connect** (no connector and no browser access):
   say so plainly and steer instead — give them these same clicks one
   at a time (open the template → **Use this template** → name it
   `buddy-os` → **Private** → **Create repository**) and have them
   confirm each screen. The copy still ends up private and theirs;
   only the hands differ.

## 3. Configure the instance

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

### Mail and calendar access

Before you move on, check that the owner has enabled mail and calendar
access in the Muse app (in the app: Settings → Connectors — their email
and calendar accounts). If either is off, walk them through turning it
on, in plain language: this is how their staff sees the day ahead, puts
real events on the calendar instead of just talking about them, and
watches the inbox for what matters. It is the owner's choice — if they
decline one, note it and carry on; several buddies simply do less
without it. Do not let this block the rest of setup.

## 4. Create the first buddy together: the Coordinator

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

## 5. The pick-list: choose the starting staff

Your Coordinator already exists (step 4) — it is the anchor: pre-selected,
recommended, their first buddy. Now present the other six starter buddies
as a **pick-list**, using each brief card as the pitch
(`samples/*/BRIEF.md`): Reading 📚, Fitness 🏃, Budget 🧾, Home 🏠,
Travel 🧳, Learning 🌱. One question per card: *install this one now?*

- **Picked:** spend two minutes making the brief theirs; the buddy is
  wired into the registry in step 6 and gets its homepage.
- **Not picked:** the buddy is simply not installed yet. **Do not delete
  anything** — its brief card stays in `samples/` in their copy, and they
  can install it any later day by asking you. Prune only its registry
  entry for now (registry seeding follows the picks; the card is how it
  comes back).
- Say this plainly, in so many words: **the pick-list is a starting set,
  not a ceiling.** They can install any of these later, and they can
  create entirely new buddies of their own at any time — the seven are
  a menu, not the whole kitchen.

## 6. Generate homepages and build the dashboard

```bash
python3 gen_basic_homepages.py            # every buddy's homepage
python3 gen_default_homepages.py --about coordinator-buddy reading-buddy fitness-buddy budget-buddy home-buddy travel-buddy learning-buddy
python3 build.py                          # the dashboard: index.html
```

(Adjust the `--about` list to the buddies they picked in step 5 — generation follows the registry, which now holds exactly their picks plus the Coordinator.) Then open the
dashboard locally and walk it together: the tree, the Coordinator's panel,
its attention item — which is real: *"Finish setup and turn one brief card
into your first real buddy."* Leave it open; it closes when they've done it.

## 7. Publish with GitHub Pages

In their repo: **Settings → Pages → Deploy from a branch → `main` / root.**
If their copy is private, Pages needs GitHub Pro — the choice from
step 2. If they chose free-and-private, skip this step gracefully:
tell them the dashboard is built but not on the web yet, and leave it
as an open item, not an error.
Their dashboard is then at the `pages_url` from step 3. **Verify on the
served copy** — open the live URL and confirm the dashboard and the
Coordinator's homepage render there. A local build is a promise; the served
copy is the fact.

**Finish by putting the dashboard on their home screen.** Once the
served copy verifies, walk them through saving the dashboard as a
standalone app — this is how they'll open it every day:

- **iPhone or iPad:** open the dashboard URL in **Safari** → tap the
  **Share** button (the square with an arrow pointing up) → scroll
  down and tap **Add to Home Screen** → keep the suggested name (or
  use their system name) → **Add**. The dashboard now sits on their
  home screen and opens full-screen, like an app — no browser bars.
- **Mac:** open the dashboard URL in **Safari** → **File → Add to
  Dock…** → name it → **Add**. It opens from the Dock in its own
  window, like an app.

Have them open it from the new icon once, so the finished system's
first launch is from the app — not from a browser tab they'll lose.

## 8. The token step (token-gated writes)

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

## 9. Day two

- Rename a sample buddy into something truly theirs, or create a brand-new
  one: brief first (use the Coordinator's brief as the pattern), registry
  entry, homepage. First task is always the homepage.
- Read `AGENTS.md` together and edit one line so it's theirs.
- Set a standing rhythm: a morning glance at the dashboard's open items.
- Updates are the staff's job: once a week, unprompted, check for Buddy OS
  updates (the flow is `UPDATE.md`) and, when a release has landed,
  summarize what changed and adopt it on their go — `UPGRADING.md`
  explains each release, and you apply it keeping their data.

Welcome to the staff. Less app, more buddy.
