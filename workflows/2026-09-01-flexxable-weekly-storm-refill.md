# Flexxable — weekly automated storm refill + proposed briefs

The first automation build in this workspace. Born from reviewing an NHB Pro
success-story post — the "Mr Media Buyer" story of waking up to creatives
already done — and Joey saying he's doing everything manually and it's
costing him the time to take on another client.

## What it does
A scheduled Routine fires weekly (Tuesdays, 11:00 UTC / ~7am ET) into a fresh
session:
1. Loads Flexxable's client file, analysis config, latest account-read, and
   strategy map.
2. Runs `/storm` in Open mode, ~15-20 seeds, pulling from all 8 sources
   (weighted toward Matrix — this week's gaps — and Internal vectors — the
   winners corpus). Saved normally to `clients/flexxable/seeds/`.
3. Picks the 3-5 strongest seeds against the most under-covered gaps and
   drafts (never locks) proposed briefs for them in `clients/flexxable/briefs/`,
   each headed `STATUS: PROPOSED — UNCONFIRMED, awaiting Joey's pick/edit`.
4. Logs a short summary to that day's `daily/` note.

Trigger ID: `trig_01DpvYK3QLiyFRJ9zhLQC2ey`.

## Why it stops short of full automation
`/brief`'s own skill file has a hard rule: "Never pick the seed, the hook, or
the angle FOR him. Propose, he decides." So this Routine proposes briefs but
never locks them, and never runs `/produce` — no copy gets written
unattended. This is a deliberate boundary, not a limitation to work around.
`/produce` also can't run headless anyway — copy has to come from mariobot,
and the hard rule there is "mariobot writes or no one writes," no
Claude-direct fallback.

## What Joey does each week
Open the proposed briefs, confirm or edit the DNA (same 2-minute motion as a
normal `/brief` pick), then run `/produce` on the ones he wants written.
Everything upstream of that is already done when he sits down.

## Adjusting it
- Cadence, scope (seeds-only vs. seeds+proposed-briefs) were chosen 2026-09-01.
  To change: edit or delete `trig_01DpvYK3QLiyFRJ9zhLQC2ey` via the trigger
  tools, or ask Claude.
- If this holds up over a few weeks, worth promoting the pattern — same
  shape could extend to other repetitive creative work once it's proven here.

Related: [[storm]] [[brief]] [[account-read]] [[Flexxable]]
