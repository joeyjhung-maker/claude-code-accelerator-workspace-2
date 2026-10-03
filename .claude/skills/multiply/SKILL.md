---
name: multiply
description: Multiply a winning ad — the router over the five Genesis "Winning Ad Workflows". Use when Joey says "multiply this", "scale this winner", "what should I test next on this ad", "give me versions of this winner", "which swap", or hands over a winner without saying which workflow he wants. Tags the ad's genome, helps pick ONE part to swap (the people, the look, the staging, the words, or the opener), then hands off to the installed skill for that swap: horizontal-scaling, formats-conceits, comment-goldmine or organic-hooks, or the styles list. If Joey names one of those workflows directly, that skill runs, not this one. No copywriting happens here.
---

# /multiply — one cheap swap away from something proven.

Winning ads aren't invented. They're extracted. An ad is made of parts. Some
parts are proven and some are cheap to swap. **Every launch should be one swap
away from something that already works.**

Read `reference.md` in this folder before the first run of a session.

## The rule that decides everything
- **Validation** = someone already paid to prove it. A winner with spend.
- **Signal** = the market is talking. A comment, a viral reel. Free, and it
  proves nothing yet.

**Multiply what's validated. Test what has signal. Launch nothing that's
neither.**

## The run

### 0. Load
Client file, strategy map, and the source: a winning ad (transcript or copy,
verbatim), or a piece of signal (a block of comments, a reel).
Say which it is: validated or signal.

### 1. Tag the genome
Write the source ad's parts in a table. Most fundamental first. The six-layer
model and a worked dissection are in `concepts/Ad Genome.md`.

| Layer | This ad |
|---|---|
| Segment (outcome · demographic · facet) | |
| Awareness level | |
| Concept (the claim) and angle (why they care) | |
| Format (the beat order) | |
| Conceit (what it pretends to be) | |
| Actor, style, look | |
| Hook, verbatim | |
| Loaded words that must not change | |

If a layer can't be filled in, say so. Don't guess.

### 2. Pick ONE swap

| Swap | Mode | Use when |
|---|---|---|
| **The people** | Horizontal | The current segments are squeezed. **Not before.** If two segments are printing, stay vertical |
| **The look** | Styles | A winner needs reach. The cheapest swap: same script, new picture |
| **The staging** | Formats / conceits | The message is proven and the creative is worn out |
| **The words** | Comments | You want the market's own language, or ideas nobody is running |
| **The opener** | Organic hooks | A proven body needs a fresh top |

**One axis at a time.** Two moves at once and a miss teaches nothing.

### 3. Hand to the installed skill for that swap
The five Genesis workflows are installed as shipped. This skill picks the
swap. Those skills run it.

| Swap | Runs | Files |
|---|---|---|
| The people | `horizontal-scaling` | `.claude/skills/horizontal-scaling/` |
| The look | the styles list (no skill of its own) | `styles/winning-ad-styles.md` and `styles/style-references.md` in this folder |
| The staging | `formats-conceits` | `.claude/skills/formats-conceits/`, with `references/` |
| The words | `comment-goldmine` | `.claude/skills/comment-goldmine/`, with `one-line-prompts/` |
| The opener | `organic-hooks` | `.claude/skills/organic-hooks/` |

**Styles, since it has no skill:** freeze the script. Pick five styles from
`styles/winning-ad-styles.md` that the account has never run. One production
brief per style, saved to `creatives/`. Match the skin to the awareness. Note
where a style break belongs. Public examples per style are in
`styles/style-references.md`.

**House rules those skills don't know.** They were written for anyone. Apply
these on top, every time:
- Where a Genesis skill says "write it" or "paste this into any AI", **stop
  and hand to `/produce`.** Mariobot writes. The judge grades before Joey
  reads it.
- For segments, use `/segments` and the client's strategy map as the starting
  map. Don't rebuild what's already there.
- If the new format is a timeline, hand to `/timeline-ad`.
- New ideas from comments go to the client's seed bank, tagged with their
  source.
- Client facts come from the client file. Never from the skill's examples.

### 4. The gate — show the options, get the pick
One numbered table. Each row: the swap, the new value, what stays frozen, the
proof behind it (quoted, or marked HYPOTHESIS), and one line of hypothesis.
**Joey picks by number.** Nothing moves on until he does.

### 5. Hand off and log
- Transplants and organic welds → `/produce` (swipe or organic route).
- New formats and conceits → `/brief`, or `/timeline-ad`.
- New styles → production briefs in `creatives/`.
- New segments → `clients/{name}/strategy-map.md`.
- One row per launch in `clients/{name}/multiply-log.md`:
  date · source ad · axis · new value · result. After ten rows, the empty cells
  are the next tests.

## Rules that bite here
- **Loaded words travel unchanged.** A softened line is a broken line.
- **Never improve a hook that already earned its audience.** Change the subject
  word and nothing else.
- **Never invent** a stat, a study, a quote or a number. Never tidy a quote.
- **A new market is not a new segment.** If it needs new proof, it's a
  different account.
- **No copywriting here.** Mariobot writes, in `/produce`.
- **Don't promote the lesson here.** That's /reflect.

## Sources
- Deck: "5 Workflows That Make Winning Ads" (Genesis), 127 slides.
- Genesis's own free skill files for the five workflows, **installed
  2026-10-03 at Joey's request**, unchanged, from
  `~/Documents/Skills/Winning Ad Workflows Genesis/`. Online copy:
  https://drive.google.com/drive/folders/1XSuG6Wk_Ox7vEhJhnY3ni7RY5Rfgn9mx
  Don't edit those files. If Genesis ships a new version, replace them whole.
- Built 2026-10-03. Not yet run on a live ad.

Related: [[segments]] [[storm]] [[brief]] [[produce]] [[timeline-ad]] [[creative-coverage]]
