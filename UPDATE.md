# UPDATE.md — Checking for Buddy OS updates

**This guide is written for the user's Muse.** The user-facing flow is
one ask: when your user says **"check for Buddy OS updates"** (or asks
whether they're current, or what's new), you do the rest — check, apply,
verify, report. Never make them run a command or read a diff unless a
decision genuinely needs them.

## 1. Find the copy's current version

Read `starter_version` in `instance.json` (beside `build.py`). If the
field is missing, this copy predates version stamping: treat it as
**1.0.0**, and add the field during this update.

## 2. Check the latest release

The upstream is the Buddy OS Starter repo this copy was made from —
the template at
[github.com/davedellaquila/buddy-os-starter](https://github.com/davedellaquila/buddy-os-starter/releases)
(if this copy came from a fork, use that fork's releases). Compare
versions as semver. If the copy is current, say so in one line —
*"You're current (vX.Y.Z)"* — and stop.

## 3. Read what changed, before touching anything

Fetch `UPGRADING.md` at the new release's tag and read every section
between the copy's version and the latest, in order. Those sections are
the contract: what changed, the kind of change (Machinery / Conventions /
Schema), and how to adopt it. Summarize them for the user in plain
terms; for a **Schema** change, get their go-ahead before applying.

## 4. Checkpoint first

The copy is a git repository. Before applying anything, make sure the
working tree is committed (commit pending work as a checkpoint, or
confirm it's clean). This is the rollback point — tell the user it
exists. An update that can't be undone doesn't ship.

## 5. Fetch and apply the system files

Fetch the changed files from the release tag and apply them by class:

- **System-owned — replace with the release's versions** (after a quick
  diff check for local edits): `build.py`, `gen_basic_homepages.py`,
  `gen_default_homepages.py`, `buddy-tree.html`, `build_guides.py`,
  `voice-catalog.json`, `persona-roster.md`, `SETUP.md`, `UPDATE.md`,
  `START-HERE.md`, `TESTING.md`, and `docs/`.
- **User-owned — never overwrite:** `buddies.json`, `plans.json`, every
  value in `instance.json`, the contents of `samples/`, `docs/inbox/`,
  generated pages, and anything the user or their buddies wrote. For
  `instance.json`, merge only *new fields* a release adds, preserving
  every existing value.
- **Conventions — merge, don't replace:** `AGENTS.md` and the standing
  orders are a working model the user may have edited. Diff them, adopt
  what fits, and surface conflicts rather than overwriting.
- **Locally modified system files:** if a system file carries the user's
  own edits, show them the diff and ask. Never silently clobber.

When everything is applied, set `starter_version` in `instance.json` to
the new release's version.

## 6. Regenerate and verify

Rebuild the surfaces from the user's own data:

```bash
python3 gen_basic_homepages.py
python3 gen_default_homepages.py --about <every buddy id in buddies.json>
python3 build.py
python3 build_guides.py
```

Verify before reporting: the registry still parses, the dashboard
builds, and one homepage renders cleanly. If the release's UPGRADING
section carries Schema migration steps, follow them exactly and run
their checks. Updates never touch the user's GitHub token, their Pages
settings, or any buddy's own repository.

## 7. Report

Tell the user, in plain terms:

- the version change (old → new),
- what changed, from the UPGRADING sections,
- anything skipped, conflicted, or held for their decision — and why,
- and commit the whole update as one commit naming the version
  (e.g. `Update Buddy OS Starter to v1.1.0`).

If any step failed, say which, leave the checkpoint intact, and roll
back rather than leaving the copy in a half-updated state.
