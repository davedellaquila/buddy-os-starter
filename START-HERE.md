# Start here 👋

*This guide is for you, the person. The other guide — [SETUP.md](SETUP.md) —
is written for your Muse, who will do the building. You don't need to
read that one; this one tells you what will happen and what to expect.*

## What is this?

**Buddy OS is a staff, not an app.** You get a small team of "buddies" —
little specialist helpers, each with one job (reading, fitness, budget,
home, travel, learning, whatever you invent) — who keep a homepage each,
track what's open, and report to one coordinator.

And above the staff sits **your Muse — your chief of staff.** That's who
you actually talk to. Your Muse runs the setup, directs the buddies, and
brings you the results. One distinction worth knowing: the **Coordinator**
buddy is *not* your chief of staff — it's a project-tracking buddy inside
the staff, keeping an eye on projects and open items. Your chief of staff
is the Muse you're chatting with; the Coordinator works for them.

### Want the thinking behind this?

[Buddies All the Way
Down](https://davedellaquila.substack.com/p/objects-all-the-way-down) is
the architecture story, in the author's words — where the staff of
buddies comes from. And when you reach the pick-list below, [How to
Choose Your
Buddies](https://davedellaquila.substack.com/p/how-to-choose-your-buddies)
is a short guide to choosing well.

Everything lives in a GitHub repository **you own**. The buddies' pages and
dashboard are just files in that repo, shown as web pages. Your data is
yours, in plain text, forever readable.

## What you need

### Must have before starting

- **A Muse account on a paid plan.** Your own Muse runs the whole
  system — it reads the setup guide, builds your buddies, and staffs your
  days. Honestly stated: **this is the one real cost.** Everything else
  below rides free tiers.
- **A GitHub account** (free is fine). Your copy of the starter, your
  buddies' pages, and your dashboard all live there.
- **A Google account** (a Gmail address). The system keeps its documents
  in Google Docs and its registers and trackers in Google Sheets — that's
  where your buddies' paperwork lives.

### Created during setup — nothing to prepare

Your Muse makes these with you, when they're needed:

- **Your own copy of this starter repo** — guided to be *private*, so
  your buddies and your life in them stay yours.
- **Your instance config** — a small file with your name and addresses
  that makes the generic machinery yours.
- **A fine-grained GitHub token** for the write-back buttons — created
  in the token step below, with the safety framing spelled out there.

### Not needed — deliberately

This list is here on purpose, because these are the things people assume
they'd need and don't:

- **No server.** GitHub hosts everything.
- **No custom domain.** The free `github.io` address works fine.
- **No coding knowledge.** Your Muse writes the code; you make the
  decisions.
- **No credit card beyond the Muse plan.** Free tiers carry the rest.

## What will happen

Your Muse follows SETUP.md. In plain terms:

1. **A short interview.** Your Muse asks what you'd like help with, what
   to call you, and a few preferences. Two minutes, conversational.
2. **You make a private copy.** This template is public, but *your* copy —
   with your buddies and your life in it — should be **private**. Your
   Muse will steer you to create it that way.
3. **You meet your first buddy.** Together you shape the Coordinator, the
   project tracker at the center of the staff.
4. **You pick your starting staff.** Six more buddies are offered as a
   menu — Reading, Fitness, Budget, Home, Travel, Learning. Pick the ones
   you want now. Stuck choosing? [How to Choose Your
   Buddies](https://davedellaquila.substack.com/p/how-to-choose-your-buddies)
   is a short guide to exactly that. The rest aren't deleted; their cards stay in your copy so
   you can install any of them later, and you can invent entirely new
   buddies whenever you like. The menu is a starting set, not a ceiling.
5. **Pages appear.** Your Muse generates your dashboard and each buddy's
   homepage, and walks you through turning on GitHub Pages so you can see
   them in a browser.
6. **One careful step: the token** (next section). Then you're running.

## The token step, in plain language

Some buttons on your dashboard and homepages *do* things — marking a task
done, adding a note. For a web page to save a change into your GitHub repo,
GitHub asks: *who is allowed to write here?* A **token** is your answer —
a key that says "this is me, and this page may write to my repo."

Your Muse will walk you through creating one, with this framing, and
you should hold it to every word:

- It's created in **your GitHub account**, for **one permission only**
  (read/write contents of your repos — nothing else).
- You'll paste it into a settings field **on your own device**, where it
  stays.
- **Never paste a token into a chat** — not with your Muse, not anywhere.
  If anything ever asks you to, stop and ask why.
- You can revoke it in GitHub settings at any time, instantly. Nothing is
  locked in.

Until you add the token, everything still works for *viewing*; buttons
simply save on that device only, and the page will tell you so honestly.

## Check the results with your own eyes

When setup finishes, your Muse will give you two links. Open them:

- **Your dashboard** — your whole staff on one page: every buddy, what's
  waiting on you, what changed. This is the page you'll live in.
- **Your Coordinator's homepage** — one buddy's page: its brief, its open
  items, its files. Every buddy's page looks like this.

Click a task on the Coordinator's page and mark it done. That's the whole
system in one gesture: a page that's also a tool.

## Day two

- Ask your Muse to install another buddy from the cards, or invent one
  of your own ("I want a buddy who tracks my garden").
- Anything you'd otherwise lose — a link, a half-thought, a receipt — can
  be *dumped* into a buddy's inbox from its homepage; your Muse files it.
- Once a week, ask your chief of staff: *"What's open, what's stuck, what
  needs me?"* That question is what the whole staff exists to answer.

Welcome aboard. 🧭

---

*Evaluating Buddy OS for someone else, or want the machinery explained?
The [tester guide](TESTING.md) is the deeper path.*
