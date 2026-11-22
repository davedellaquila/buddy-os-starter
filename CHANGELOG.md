# Changelog — Buddy OS Starter

## 1.1.0 — 2026-11-21

- The one-ask update path: `instance.json` gains a `starter_version`
  stamp, and UPDATE.md (written for the user's Muse) defines the
  update flow — check the latest release, read UPGRADING, checkpoint,
  apply system files around user data, regenerate, verify, report.
- START-HERE's day-two list gains the one ask: "check for Buddy OS
  updates."

## 1.0.0 — 2026-11-21

- First release: the dashboard (`build.py`), homepage generators (basic +
  Dossier/About), the registry format, and the view fragments — in generic,
  parameterized form (every installation configured by `instance.json`).
- Seven starter buddies as brief cards; the Coordinator is the fully-worked
  example the setup guide builds with the user.
- SETUP.md: the first-run guide written for the user's Muse, including
  the token step with its full safety framing.
- Setup flow: the seven starters are a pick-list (Coordinator pre-selected
  as the anchor; unpicked cards stay for later install; registry seeding
  follows the picks). Framing made explicit everywhere: the user's Muse
  is their chief of staff; the Coordinator is a project-tracking buddy
  inside the system, one level down.
- START-HERE.md: the human companion guide — plain terms, the full
  prerequisites in three groups (must-have incl. the paid Muse plan as
  the one real cost; created during setup; a deliberate "not needed"
  list), the token step in plain language, and day two.
- TESTING.md: the advanced tester guide — machinery, a suggested test
  route, feedback asks, and v1's known rough edges.
- The two human guides are published as a website on the repo's GitHub
  Pages (`build_guides.py` renders start-here.html + testing.html from
  the markdown sources); both link the author's Substack essays as
  further reading.
- Conventions and docs: AGENTS.md, concepts, registry format, standing
  orders, the homepage rubric, the tip-jar snippet.
- Release machinery: VERSION, this changelog, UPGRADING.md.
