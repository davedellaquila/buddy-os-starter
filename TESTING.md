# Testing Buddy OS — the advanced guide

*For testers evaluating the system. If you're setting up your own Buddy OS
to use it, [START-HERE.md](START-HERE.md) is your guide — read that first;
this one goes under the hood.*

## Background reading

Two essays by the author, for the thinking behind the machinery:

- [Buddies All the Way
  Down](https://davedellaquila.substack.com/p/objects-all-the-way-down) —
  the architecture: why a staff of linked buddies, and what it descends
  from.
- [How to Choose Your
  Buddies](https://davedellaquila.substack.com/p/how-to-choose-your-buddies) —
  the choosing problem the pick-list in setup is designed around.

## How the machinery actually works

**The registry is the single source of truth.** `buddies.json` holds one
entry per buddy: identity (name, icon, persona), tree position (parent),
repo, status, its open **attention items**, and its files list. Attention
items carry disposition stamps — `cleared`, `later`, `dropped`, each
`{date, by}` — written by the action buttons. If a fact about a buddy
matters, it lives here or it doesn't live anywhere.

**The dashboard is a build, not an app.** `build.py` renders `index.html`
from the registry, `plans.json`, and the `buddy-tree.html` fragments.
`index.html` is a generated file — never hand-edit it; change the sources
and rebuild. The same rule applies to homepages: `gen_basic_homepages.py`
builds the standard pages, `gen_default_homepages.py` builds dossier-style
pages and every About page, baking registry data (attention tiles with the
full action set, Files sections) into static HTML.

**Writes are token-gated.** The action buttons (Done / Need more info /
Later / Drop it / ✎ Add a note…) write through the GitHub Contents API
using a fine-grained token stored on the device: dispositions stamp the
registry entry; info requests and notes append to the owning buddy's
`docs/ingest.md`. With no token on the device, actions still record
locally and the page says plainly that they didn't sync. Nothing ever
fails silently — that honesty is part of the design, so test it.

**Instances are parameterized.** `instance.json` (owner, GitHub account,
system repo, Pages URL, tip jar, root order, root name) is the only file
that says whose system this is. The machinery carries placeholders the
build substitutes; that's how the same code serves every user.

**Upgrades are documents, not magic.** `UPGRADING.md` carries one section
per release: what changed, what to adopt, what to leave alone. Adopting =
take the new machinery files, keep your data files (registry, instance
config, your buddies' content), regenerate.

## A suggested test route

1. **Create a private copy** from the template ("Use this template") and
   run [SETUP.md](SETUP.md) with your Muse, for real. Note every place
   you hesitate — hesitation is the feedback gold.
2. **Use the pick-list honestly.** Install two of the six optional
   buddies, skip the rest. Confirm the skipped buddies' brief cards are
   still in `samples/` afterwards (nothing was deleted), then install one
   of the skipped ones a day later.
3. **Exercise the action buttons.** On the Coordinator's homepage and in
   the dashboard panel: mark the sample item Done, another Later, add a
   note. With the token set up, check the registry stamp and the
   `docs/ingest.md` entry landed. Then revoke/remove the token on one
   device and confirm the buttons degrade honestly instead of erroring.
4. **Create a buddy of your own** — something the starter never imagined
   (a garden, a boat, a thesis). The system should bend; note where it
   creaks.
5. **Apply an upgrade.** Pull the current release's machinery files into
   your copy per UPGRADING.md, regenerate, and confirm your buddies, your
   dispositions, and your notes all survived untouched.
6. **Live in it for a few days.** The morning question — *"what's open,
   what's stuck, what needs me?"* — is the real test. Does the staff
   answer it?

## Feedback: what's wanted, and how to send it

Wanted, in order of value:

- **Where you got stuck** — the exact step, what you expected, what
  happened. A screenshot beats a paragraph.
- **What surprised you** — pleasantly or not.
- **Anything that felt unsafe** — a moment you weren't sure what a button
  would do, or what would become public.
- **What you'd never use** — dead weight is a finding too.

Send it as an **issue in this repository**, or hand it to the person who
invited you to test. Either route reaches the maintainer.

## Known rough edges in v1 (don't re-report these)

- **Muse only.** SETUP.md is written for the user's Muse specifically;
  other agents aren't supported yet (an any-agent variant is a standing
  future task).
- **GitHub only.** No GitLab/Bitbucket path in v1.
- **No visitor counter.** The starter dashboard deliberately ships
  without one (the original pointed at the author's own analytics
  endpoint; an instance-configurable version may come).
- **Generated files everywhere.** Editing a homepage or the dashboard
  directly is always overwritten by the next build — changes belong in
  the registry, the instance config, or the generators.
- **Voices are environment-dependent.** A sample persona roster and the
  voice catalog ship as data, but spoken audio depends on the user's own
  Muse setup; text is the guaranteed surface.
- **Upgrades are manual.** Read UPGRADING.md, adopt, regenerate. There
  is no auto-updater in v1 — by design, so nothing changes under you.
