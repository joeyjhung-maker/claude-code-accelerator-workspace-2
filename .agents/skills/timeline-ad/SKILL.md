---
name: timeline-ad
description: Build a Timeline Ad ("this is what happens to X if they do Y for 30 days") from start to finish, using the Genesis timeline training. Use when Joey says "timeline ad", "write a timeline", "day 1 to day 30 ad", "what would happen if ad", "/timeline-ad", or picks a seed or brief whose structure is Timeline. Runs one fixed process — collect the avatar's real day, write the last rung first, build the claim ladder, get the ladder approved as a table, THEN mariobot writes and the judge grades with the five timeline checks. Covers every frame (hypothetical, testimony, diary, skeptic, yapper friend, false warning, body-part narrator, negative timeline). Not for other ad structures — use /brief and /produce for those.
---

# /timeline-ad — one process for timeline ads. Decisions first, ladder approved, then mariobot writes.

A timeline ad walks a viewer through ordered checkpoints and shows what changes
at each one. It works because the viewer **watches** it happen to someone. He is
never asked to judge a claim.

**The one law:** claim size can rise no faster than the viewer's willingness to
believe. Every rung he accepts on the way up is one you don't have to argue for
at the close.

Read `reference.md` in this folder before the first run of a session. It holds
the ladder, the clocks, the frames, the sales-block order and the numbers.

## The run

### 0. Load, and check this is the right tool
- Name the client and product. Read `clients/{name}/client.md`, the strategy
  map, and any primer or research that holds real customer language.
- Timeline fits when the benefit **arrives in stages over time**. If the offer's
  result is one event, say so and suggest /brief instead.
- **Not a supplement?** The training was built on consumables. For a coaching
  or info offer, use the translation table in `reference.md` and tell Joey it
  is an untested port.

### 1. Collect the raw material (ask, never invent)
Four lists. Pull from the client file first. Anything missing, **ask Joey**.
1. **The avatar, as one spoken noun phrase**, and the habit the product
   replaces or sits beside. If the phrase needs a comma, it's two avatars.
2. **8–12 real moments from this avatar's day.** Coping behaviours, objects
   that measure the problem without a feeling, and who is in the room. Taken
   from research or Joey. Never borrowed from another avatar's ad.
3. **The heroes.** Each ingredient or component, what it truly does, and how
   fast. Plus any spec that beats the cheap version.
4. **What can be defended.** Which results, on which timescale, the client can
   stand behind. Proof assets, offer, guarantee. No number that isn't in the
   client file.

### 2. Build the construction sheet (in this order)
1. **Last rung first.** The identity line in the avatar's own mouth, and the
   life scene as a picture. Decide whether a number appears. If it does, it
   goes last and hedged.
2. **Horizon and clock.** Horizon sized to the last rung. Clock chosen for the
   feeling. The clock can loosen as claims grow.
3. **The villain, in one sentence.** Physical, has agency, lets the avatar off
   the hook. Decide where it's named and where it's explained.
4. **One hero per rung**, fastest first. Choose the weight of each "because".
   Plant the spec inside a rung. The comparison waits for the sales block.
5. **Day 1.** Ease first, the smallest believable claim, his objection said for
   him, and one hedged line about what has started underneath.
6. **The climb.** One milestone per rung, 3 to 7 in total. Absences early, a
   behaviour rung, an object before a person, hedges, a momentum line at every
   checkpoint, gaps widening, nothing visible before about halfway.
7. **Spikes, one to three.** Event, then because, then unlike. At the first
   felt win, where the false solution stood, or where his biggest past failure
   lives.
8. **The seal.** Connect the problems, remove the sacrifice, shrink the ask.
9. **Sales block facts**, in the standard order, each one defensible.
10. **Frame last.** Who, habit swap, horizon, tease of the last rung.

### 3. The gate — show the ladder, get the yes
**Show the actual thing, not a description.** Render the ladder as a table:

| # | Marker | Rung type | The moment | The because | Hedge | Momentum line |
|---|---|---|---|---|---|---|

Under it: the villain sentence, the spikes, the seal, and **two or three frames
written out as real opening lines** so Joey can pick by reading them.

Run the **ceiling check** on the plan before showing it: would a stranger
believe this rung on this day? Fix any rung that reads as a promise.

Flag every claim that came from me and not from the client file.

**Nothing gets written until Joey approves the ladder.** This is the last cheap
decision.

### 4. Save the sheet as a brief
`clients/{name}/briefs/TIMELINE_{Avatar}_{Frame}_{Horizon}_{FORMAT}_v01.md`,
frontmatter `status: ready`, `structure: timeline`. Body is the approved sheet
plus one line of **hypothesis**: why this should work and what a miss teaches.

### 5. Write — mariobot, from the sheet
- Check `clients/.env` carries `GENESIS_API_KEY` and `ANTHROPIC_API_KEY`.
  Blank or missing: **STOP.** Do not self-draft. ([[always-use-mariobot-to-write]])
- `scripts/run_mario.py` with the sheet as the brief. Tell it: timeline is
  about three quarters of the script, sales block the last quarter, 320 words
  as a working length for video unless the sheet says otherwise.
- Ask for the **frame in several versions** across the two or three structures
  Joey liked. Present them all. **Never pick the opener for him.**
- Whoever told the days sells the product. A person narrator keeps the sales
  block short and in their voice.

### 6. Judge before showing
Nothing reaches Joey ungraded. Show a PASS / FAIL tick-list, never a summary.
1. `python3 scripts/copy_lint.py <draft>`, then `rubrics/copy-rubric.md`.
2. **The five timeline checks**, read aloud:
   - **Ceiling.** Every rung believable on its day.
   - **Witness.** Every line inside the days could be said by the person living
     it. If only the brand could say it, move it to the frame or the sales block.
   - **Momentum.** The last line of each checkpoint says the curve is rising.
   - **Proportion.** About 75% timeline, 25% sale. 3 to 7 milestones.
   - **Moments.** Count the specifics from step 1 that made it in. A rung that
     is a benefit with a date on it fails.
3. **Sheet match.** Did the draft keep the approved rungs, in order?
4. **Compliance, as a separate pass.** Every number traceable to the client
   file. No invented stock counts. No disease names. Hard claims hedged.

Grade and fix mariobot's lines. Flag Joey's own lines, never rewrite them.

### 7. Save, flip, hand off
- Save to `copy/` as `YYYY-MM-DD-{client}-timeline-{avatar}-{frame}-v01.md`.
- Flip the brief to `status: written` and add the `copy:` pointer.
- Show the copy, the tick-list, and the **versioning order** for when it wins.

## Versioning (only after the script wins)
One swap at a time, in this order: avatar noun (the moments swap with it) →
wrapper, same audio → frame → hook line only → horizon → port the angle to a new
product. The rungs stay frozen through all of it.

## Rules that bite here
- **He's a witness, never the judge.** No brand voice inside the days. Argument
  shows up as something he experiences or realises.
- **Event first, reason second.** A reason with nothing to explain is a lecture.
- **Never explain the product before he has felt a rung.** One hedged line about
  what has *started* is the only exception, on Day 1.
- **The biggest claim sits on top of everything else.** Identity and any number
  land around 80% of the way through.
- **Never invent.** Not a moment, not a result, not a timescale, not a count.
  If it isn't in the client file, ask.
- **Mariobot writes or no one writes.**
- **Don't promote the lesson here.** That's /reflect.

## Sources
- Master training doc: https://claude.ai/artifact/T9DyJLUhVsRLBNkmpTYHW4
- 14-step build guide: https://claude.ai/artifact/6RmY4UVgGazqRXA4a3qGEU
- Swipe library (306 verified timeline ads, RYZE / IM8 / Resilia), Google Doc:
  https://docs.google.com/document/d/1B58h0BmgvavSl8U10JJaaSGWS6xJ0vlt7BHzVwjiO-o/edit
- Built 2026-10-03 from the Genesis "Constructing Timeline Ads" training. Not
  yet run on a live brief.

Related: [[produce]] [[brief]] [[hooks]] [[The Lock]] [[show-dont-tell-decisions]]
