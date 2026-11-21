# Buddy OS Starter

**Less app, more buddy.** Buddy OS is a personal staff of AI "buddies" — one
coordinator and a set of specialists — that live in a GitHub repo you own:
a registry (`buddies.json`), a dashboard, and a homepage for every buddy.

This starter is the system with nobody's life in it yet. You bring the life.

## The 10-minute tour

1. **Make your copy.** Click **Use this template** → create the repository
   under your own account, and **make it private** — it will hold your
   personal system. (The template is public; your copy should not be.)
2. **Open SETUP.md with your Muse.** The setup guide is written for your
   Muse, not for you: your Muse interviews you, creates your first buddy
   with you, wires the registry, and builds your first homepage.
3. **Meet the staff.** Seven starter buddies ship as brief cards in
   `samples/` — a Coordinator (fully worked example) plus Reading, Fitness,
   Budget, Home, Travel, and Learning buddies. Setup presents them as a
   pick-list: install the ones you want now, keep the other cards for
   later, and create entirely new buddies whenever you like.
4. **Run the dashboard.** `python3 build.py` builds `index.html` from the
   registry. Enable GitHub Pages on your repo and it's live.
5. **Grow it.** Every new buddy gets a registry entry, a repo of its own
   when it needs one, and a homepage. The conventions in `AGENTS.md` and
   `docs/` keep the system behaving as it grows.

## What's in the box

| Piece | What it is |
|---|---|
| `SETUP.md` | First-run guide, written for your Muse |
| `build.py` | Builds the dashboard (`index.html`) from the registry |
| `gen_basic_homepages.py` | Generates buddy homepages |
| `gen_default_homepages.py` | Generates Dossier + About pages |
| `buddies.json` | The registry — the source of truth for your staff |
| `instance.json` | Your installation's config (name, GitHub owner, URLs) |
| `samples/` | The seven starter buddies as brief cards |
| `docs/` | Concepts, the registry format, the homepage rubric, standing orders |
| `AGENTS.md` | Operating conventions — adopt, edit, make them yours |
| `UPGRADING.md` | How starter releases reach your copy |

## License

MIT — see `LICENSE`. Your copy, your data, your rules.
