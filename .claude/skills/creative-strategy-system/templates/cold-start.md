# Cold Start — when you have no winning ads yet

Primers and Loopback need *your own* winners. If you don't have any yet, that's normal — here's how to
get a real first ad and seed your primers, two ways.

## Route 0 — Have literally nothing? (works fully inside this folder)
Two ways to get a first ad with zero outside material:
- **Use the bundled example swipes** — `knowledge/swipe-bank/example-swipes.md` ships 3 generic example
  ads. Pick one and run the swipe-rewrite below against it. (They're practice structure, not real
  winners — swap in real competitor ads when you can.)
- **Or just describe your product** — tell the assistant your product, who it's for, the main problem it
  solves, and the mechanism. It will draft a first ad from scratch using the Copy Blocks + hook
  frameworks, which becomes your starting primer. (Prompt: *"I have no ads yet. Here's my product: […].
  Draft me one strong long-form ad using the Copy Blocks and vicious-hook frameworks, then save it as my
  first primer."*)

## Route 1 — Swipe-rewrite (do this on plain Claude Code, today)
Take a competitor ad you genuinely admire (find via Meta Ad Library, scrapecreators.com, Hookd, Get
Hooked — pick ones running a long time = proven; or use a bundled example to practice), and rewrite it
for your brand, Mad-Libs style.

**The prompt:**
> *"Here is a winning ad. Rewrite it using my brand info. **Keep it structured exactly the same** and
> treat it like Mad Libs — only swap out the specific words (product, mechanism, proof, names, details).
> Don't make it too derivative; keep the bones, change the specifics."*

Then:
1. **Paste the winning ad** + **your brand info** (product, mechanism, key benefits).
2. **Add your Copy Blocks** — your pain points, promises, proof, and the details you want in
   (`frameworks/copy-blocks.md`).
3. **Manually edit** to taste (`frameworks/editing-rules.md`), make the hook vicious
   (`frameworks/hook-quality.md`).
4. **Save the result into your primers** — now you have your first primer entry. As real winners come
   in, swap them in and the primer tightens.

## Route 2 — The 75-spot template bots (Genesis / Exodus)
If you have **Genesis or Exodus**, you get the **75-ads / 75-hook template spots** — drop in your brand
info and they generate ad/hook concepts from 75 proven templates in one pass. The fastest cold-start.
(No Genesis/Exodus? Route 1 gets you there manually.)

## Then
Once you have a few ads running, **Analysis** brackets them → winners flow into your **primers** →
**Loopback** comes online for statics. The cold start is temporary; the flywheel takes over.
