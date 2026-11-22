# Upgrading

Template copies do not receive upstream updates automatically — this file
is how they travel. Each starter release adds a section here: what changed,
which kind of change it is, and how your Muse should adopt it into your
copy **while keeping your data** (your registry, your buddies, your pages'
content).

Change kinds:

- **Machinery** — build/generator code. Usually safe to copy over; your
  Muse diffs first and keeps any local edits you made on purpose.
- **Conventions** — AGENTS.md / docs changes. Read and adopt what fits;
  these are a working model, not a creed.
- **Schema** — registry or config format changes. Follow the migration
  steps in the release section exactly; your Muse verifies the registry
  still parses and the dashboard still builds before calling it done.

---

## v1.1.0 — the one-ask update path (2026-11-21)

**What it is:** updates become a conversation. `instance.json` gains a
`starter_version` stamp recording which starter release a copy is
running, and a new UPDATE.md — written for the user's Muse, the way
SETUP.md is — defines the whole flow: the user says *"check for Buddy OS
updates"* and their Muse checks the latest release, reads these notes,
checkpoints the copy in git, applies the system files around the user's
data (user-owned files are never overwritten; conventions are merged,
not replaced), regenerates, verifies, and reports what changed and
anything that conflicted.

**Kind:** Machinery (the stamp + UPDATE.md) — no schema migration; the
stamp field is additive and 1.0.0 copies are treated as 1.0.0 until
their first update adds it.

**Adopting:** if your copy predates this release, your Muse can adopt
it by hand this once: add `"starter_version": "1.1.0"` to
`instance.json` and copy UPDATE.md in. Every later release then arrives
through UPDATE.md itself.

## v1.0.0 — the first release (2026-11-21)

**What it is:** the whole starter — dashboard, homepage generators,
registry format, seven starter buddies (Coordinator fully worked, six as
brief cards), and three guides: SETUP.md (the first-run guide for the
user's Muse), START-HERE.md (the short human companion), and TESTING.md
(the advanced tester guide). Setup presents the buddies as a pick-list —
the Coordinator pre-selected as the anchor, the rest opt-in, unpicked
cards kept for later. The framing is explicit throughout: the user's
Muse is their chief of staff; the Coordinator is a project-tracking
buddy inside the system. The companion guide carries the full
prerequisites (a paid Muse plan — the one real cost — a GitHub account,
a Google account; what setup creates; and a deliberate "not needed"
list). The two human guides are also published as a small website on the
repo's GitHub Pages (generated from the same markdown by
`build_guides.py`, so they can't drift), and they link the author's two
essays — "Buddies All the Way Down" and "How to Choose Your Buddies" —
as further reading. Plus conventions, and this file.

**Kind:** everything is new; there is nothing to migrate.

**Adopting:** you are here — follow SETUP.md. If you are reading this in a
copy you already run, you have v1.0.0's notes; later releases will append
their sections above this one.
