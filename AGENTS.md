# AGENTS.md — Operating Conventions

How this Buddy OS installation is run. This file ships with the starter as
*a* working model — adopt it, edit it, make it yours. When a convention
proves itself, write it down here so the next session starts knowing it.

## Working agreements

- **The registry is the source of truth.** Buddy status, parentage, and open
  items live in `buddies.json`. Pages and dashboards are views of it.
- **Verify on the served copy.** After any change to a page or the
  dashboard, check the live (or locally served) result before reporting it
  done. A local build is a promise; the served copy is the fact.
- **Every named thing gets its link.** Documents, pages, repos, sections —
  if the owner can click it, the message carries the link.
- **One topic per message.** When a reply covers several threads, send each
  as its own message so the owner can answer them individually.
- **Options inline.** When a question has logical answer choices, present
  them where the owner already is (tappable options), not somewhere else.
- **Git discipline.** In a shared checkout: fetch before you build, commit
  explicit paths (never a blanket add), keep the checkout clean, and do
  builds in a worktree when another session may be active.
- **Credentials never travel through chat or files.** Tokens are entered
  through secure prompts, stored on the device only, and scoped as narrowly
  as the service allows. Before any credential step, say which account,
  which single permission, what the owner will see, and what must never be
  pasted.
- **Critical items get two channels.** Anything outward-facing, money going
  out, or a same-day deadline blocked on the owner goes by chat *and* email,
  so it persists until handled.
- **Finished work doesn't linger.** Work that is done but unshipped or
  awaiting the owner gets resurfaced within a few days, not silently shelved.
- **Check for starter updates weekly.** Once a week, unprompted, the chief
  of staff runs the check in `UPDATE.md` against the starter's latest
  release. If a newer release exists, summarize what changed in plain
  terms and apply it on the owner's go (a Schema change always needs the
  go). Staying current is the staff's job, not the owner's memory.

## Buddy conventions

- A buddy for a person is named `<Name>'s Buddy`.
- A new buddy's first task is its own homepage (rubric:
  `docs/homepage-audition.md`).
- Persona and voice get sensible defaults at creation; the owner can change
  them any time. Never block creation on taste decisions.
- Buddies are private by default; public is an explicit per-buddy choice.
