# Concepts

**A buddy** is a named specialist with a job: a persona, a brief, a registry
entry, and a homepage. Buddies are staff, not apps — you talk to them, they
keep knowledge, they own outcomes. *Less app, more buddy.*

**The registry** (`buddies.json`) is the source of truth: every buddy, its
parent, its status, its open attention items. If it isn't in the registry,
it isn't on the staff. See `registry-format.md`.

**The Coordinator** is the buddy at the root of the tree — your chief of
staff. It holds the macro view (every buddy's status and next actions),
tracks open items across the staff, and routes work to the buddy who owns it.

**System vs instance.** The *system* is the machinery in this starter:
dashboard, generators, formats, conventions. The *instance* is yours: your
buddies, your data, your pages. The starter ships system only — everything
personal gets created in your copy, by your Muse, during setup.

**Homepages** are a buddy's face: what it is, what it's working on, what
needs your attention — with action buttons on every task, so deciding never
requires a detour. The standard is `homepage-audition.md`.

**Ingest** is how things reach a buddy: notes, brain dumps, and task
dispositions are written (through a token-gated path) to the buddy's own
`docs/ingest.md`, and the buddy works from there.

**Privacy.** Buddies are private by default. A buddy's homepage is public
only if you choose it — GitHub Pages on a private repo keeps your copy
unlisted to the world only if the repo stays private; treat anything you
publish as published.
