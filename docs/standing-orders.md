# Standing Orders

The short list every Buddy OS installation runs by. (The longer conventions
live in `AGENTS.md`.)

1. **Dark mode on every page.** Every buddy website ships working dark mode
   (`prefers-color-scheme` or an equivalent toggle). Not polish — a
   requirement.
2. **Action options on every task.** Every task / needs-attention item, on
   every homepage and in the dashboard, carries its actions on the item
   itself: ✓ Done / Need more info / Later / Drop it, with Undo, plus
   ✎ Add a note… — persisted as registry stamps through the token-gated
   path. Statement-only task cards are a defect.
3. **A Files section on every homepage**, listing the documents the buddy
   manages. Contents are baked in at generation time — unless the buddy is
   flagged `private_files`, in which case names only.
4. **Every named thing gets its link.** If a message mentions a document,
   page, or repo the owner can open, the link is in the message.
5. **Verify on the served copy.** A change is done when the live page shows
   it — not when the local build says so.
6. **No credentials in chat or files.** Tokens are entered through secure
   prompts and stored on the device, never written into the repo.
7. **A new buddy's first task is its own homepage.**
