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

## v1.0.0 — the first release (2026-11-21)

**What it is:** the whole starter — dashboard, homepage generators,
registry format, seven starter buddies (Coordinator fully worked, six as
brief cards), the first-run guide (SETUP.md), conventions, and this file.

**Kind:** everything is new; there is nothing to migrate.

**Adopting:** you are here — follow SETUP.md. If you are reading this in a
copy you already run, you have v1.0.0's notes; later releases will append
their sections above this one.
