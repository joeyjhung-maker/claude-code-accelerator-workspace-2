# Workflow: Use Segment/Mech Swapper Bot for segment-only ad swaps

Related: [[Promotion]] [[2026-06-24-mariobot-genesis-body-copy]] [[creative-strategy-system]]

## When to use this
You have a winning ad and want the SAME structure/rhythm/length, aimed at a different audience
segment (or a different problem/solution mechanism), with everything else locked. Not for a fresh
write, not for a hook-only swap — for a full-ad segment or mechanism swap.

## Why this bot over mariobot
Tried mariobot first on a Flexxable IAA ad (Burned-Out Agency Owner → 9-5 Escapee segment). Took
two corrective passes to get an exact line-for-line match — v1 drifted onto irrelevant research, v2
blew past the source's per-line length. Then tried the purpose-built Genesis bot for this exact job
and it nailed the 14-line structure on the first pass, matching length and rhythm closely enough
that only a light touch-up (cut 3 stray em-dashes, fixed one stacked triplet) was needed.

## The steps
1. **Bot:** `segmentmech-swapper-bot` ("Segment/Mech Swapper Bot" in the Genesis roster). Call via
   `scripts/run_genesis.py --bot segmentmech-swapper-bot --primer <source-ad.md> --turn <instruction.md>`.
2. **Primer = the winning ad itself**, verbatim, nothing else. This is what gets structurally
   cloned.
3. **Instruction = the new segment/mechanism facts**, not new copy. Give: who the new segment is,
   what's different about their situation, what they have NOT lived through yet (so the bot doesn't
   invent false experience for them), and which facts must stay exact (prices, real numbers, offer
   terms).
4. **Judge pass still applies** — run `copy_lint.py`, strip AI-written em-dashes, check for stacked
   triplets. The bot is fast and structurally faithful, not rubric-perfect.

## What good looks like
The Segment 2 swap of `2026-08-25-flexxable-iaa-nice-guy-trap-danhenry-swipe-STATIC-v01` (unfiled —
see session transcript 2026-08-26) — exact 14-line match, correct segment facts, only needed
mechanical cleanup.
