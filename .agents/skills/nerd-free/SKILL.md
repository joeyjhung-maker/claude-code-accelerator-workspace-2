---
name: nerd-free
description: Find a compelling ad IDEA before any hook gets written — Mario Castelli's "Nerd-Free" method (the Consequence Cascade) from Genesis. Use when Joey says "nerd-free", "nerd free this", "consequence cascade", "find me a better idea", "this idea is boring", "isolate the idea", "what's the idea in this ad", "is the idea weak or the writing", "diagnose this ad", or hands over a boring fact, a research finding, or a batch of flat hooks. Two modes — BUILD takes a boring but true fact and walks it to a vivid, defensible idea; DIAGNOSE strips an existing ad down to its idea and says whether the idea or the writing is the weak part. Output is idea cards, not hooks. Hooks are written afterwards by the hook bot through /produce.
---

# /nerd-free — get the idea right before anyone writes a word.

Most weak hooks are a weak idea in strong language. Lipstick on a pig. A hook
usually gets better because the **idea** got better, not the wording.

"Writing like a nerd" means staying literal: research → claim → wording. This
method puts the creative work in the middle:

**Fact → why → possibility → and then what → human consequence → scene →
what kind of mess is this → the irresponsible version → what's defensible →
hook.**

Read `reference.md` in this folder before the first run of a session.

## Mode A — BUILD (from a boring fact to an idea)

### 0. Load
Client, product, segment, awareness level. Read the client file and research.

### 1. Lock the boring fact
One flat, true statement **with its source** (client file, a study, research
notes). No copy yet. If the fact has no source, stop and ask Joey.
Don't cheat by starting with an interesting fact. The flat one is the start.

### 2. Ask why it would be true, and branch
Under what conditions would this fact hold? List five or more branches.
**Pick the branch with a human being at the end of it**: someone doing
everything right and still losing. Say why you picked it. This is a judgment
call, so show the branches you dropped.

### 3. "What does this make possible?"
If that's true, what else could be true? Chain it: therefore, therefore,
therefore. Several chains, not one.

### 4. "And then what?"
Keep going past the mechanism. **Stop only at a human consequence**: money,
pain, embarrassment, exhaustion, lost time, sex, status, a relationship,
feeling stupid, feeling betrayed. A mechanism is never the endpoint.

### 5. Turn it into a scene
A one-second movie the customer can see. A time, a place, an object.
If they can't see it happening, it's still nerd writing.

### 6. Name the kind of mess
What kind of situation is this? The solution causing the problem. Escalating
the wrong fix. The suspect dressed as the victim. Pick from the idea types in
`reference.md`. Metaphors come later, if at all.

### 7. Write the irresponsible version
The most shocking fair reading, written as if nobody could sue. **Do not
fact-check while writing it.** This finds the ceiling.
*This line is a working step. It never ships.*

### 8. Backsolve what's defensible
Now the lawyers come back. For each part of the line: what would need to be
true for this to be fair? Mark each part **supported** (with the source),
**plausible**, or **unsupported**. Back off only the unsupported part, and
only as far as needed. Keep the rest of the force.

### 9. The Nerd-Free Test
Four questions. All four must pass.
1. **Is there a new idea?** Strip the wording. Is the bare claim still
   surprising?
2. **Can I see it?**
3. **Does it hit my life?**
4. **Did the customer have to work anything out?** If they must complete the
   argument, it fails.

### 10. The idea card — show Joey, get the pick
One card per idea. Show several, numbered.

| Field | |
|---|---|
| The fact, and its source | |
| The branch taken | |
| The idea, stated flat | |
| The leap (X ↔ Y) | |
| Idea type | |
| The human consequence | |
| The scene | |
| The irresponsible version (not for use) | |
| What's supported / plausible / unsupported | |
| The defensible version | |
| Nerd-Free Test (4 × pass/fail) | |
| Idea grade, 1–10 | |

**Joey picks by number.** Then hand the chosen idea to `/brief` or straight to
`/produce` for hooks.

## Mode B — DIAGNOSE (an ad that exists)

1. **State the idea flat.** Strip every intensifier. Say it the way you would
   in a meeting.
2. **Write the leap as X ↔ Y.** Two things this market never had side by side.
   No leap means no idea, only decoration.
3. **Grade the idea 1–10** before looking at the writing.
4. **Grade the line separately** for vagueness (detectors in `reference.md`).
5. **Name the weak layer.**
   - Weak idea → run Mode A from the ad's underlying fact. Bigger wins here.
   - Strong idea, weak line → keep the idea and rewrite the line through the
     hook bot.
6. **Name the idea type**, and note which consequence it lands on.

Use this on competitor ads too. A proven idea type is a set of lines to colour
inside: ask what could be made true and defensible for *this* client within it.

## Unaware story hooks
For unaware traffic the opening shows **A and Z and hides B through Y**: the
strange event and the outcome the market cares about, with the explanation
held back. The product stays out of the opening. See `reference.md`.

## Rules that bite here
- **Every fact has a source.** Never invent a study, a number, a mechanism or
  an ingredient. An idea that needs one isn't an idea.
- **The irresponsible version never leaves the card.**
- **Step 8 is not optional**, and it's separate from step 7. Write hot, then
  check. Not both at once.
- **No hooks written here.** The hook bot writes them in `/produce`, graded by
  `rubrics/hook-rubric.md`.
- **Never make the customer complete the argument.**
- **Don't promote the lesson here.** That's /reflect.

## Sources
- Call: Copy Coders / Genesis, Mario Castelli, 31 Aug 2026.
  Transcript: `inbox/2026-08-31-copy-coders-nerd-free-hooks-transcript.md`
- Slides, workbook and swipe file: https://mcastelli99.github.io/trainings/nerd-free/
- Built 2026-10-04. Not yet run on a live brief.

Related: [[hooks]] [[hook-rubric]] [[concepts-and-angles]] [[Ad Genome]] [[produce]] [[brief]] [[multiply]]
