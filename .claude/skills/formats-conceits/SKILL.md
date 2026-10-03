---
name: formats-conceits
description: Formats & Conceits — take a winning ad, pull out its MESSAGE, and re-tell that message in a new FORMAT (how the argument moves through time: timeline, listicle, story, comparison…) or a new CONCEIT (what media the ad pretends to be: podcast, UGC, street interview, doctor consult, villain…), message frozen. Use whenever the user says "formats and conceits", "re-stage this ad", "same message, new format", "turn this into a podcast / timeline / listicle", "what formats are proven", "which format should I try next", or pastes a winning ad and asks for versions. Runs with nothing installed: the ad, the two lists in references/, any AI.
---

# Formats & Conceits

Every winning ad is one cell in a grid. The message sits on top. Under it, two axes you can swap without touching the message:

- **Format** is how the argument moves through time. It fixes the beat order. Timeline, listicle, story, comparison, confession, testimonial.
- **Conceit** is what media the ad pretends to be. It fixes who speaks, where, and the genre's conventions. Podcast clip, UGC confession, street interview, doctor consult, the villain speaking.

(Style, the look of the pixels, is workflow 2. It carries no meaning, so it's the cheapest swap of all.)

A winner occupies one cell. Every neighbour is one swap away from proven. That's the whole workflow: **take a winner, pull out the message, re-tell it in a neighbouring cell, one axis at a time.**

## 1. Take any winning ad

Don't wait for the mega-winner. A competitor ad that's run 90 days, an ad with unusual comments, a post that outran its siblings all count. Paste the transcript, script, or post copy, verbatim.

## 2. Pull out the message

The message is everything that must survive when the staging changes. Write it out (the paste-in prompt is `references/isolate-the-message.md`):

1. **Who it's for** and what they already believe when the first line lands.
2. **The claim**: the hidden cause behind their symptom, and how the product reaches it. Quote it as the ad says it.
3. **Why they care now**: who's telling them, where it came from, why now, what's at stake.
4. **The beats**, in order, each with the question it answers (my problem is really caused by Y · what I tried never touched Y · Z fixes Y · this applies to me · I can't lose · now, not later).
5. **The hook**, verbatim, and the flip it performs.
6. **The loaded words**: coined names, crime verbs, lines lifted from the market. These travel unchanged. A softened line is a broken line.

Everything else (who's on camera, where, how it looks, how long it runs) is what you're allowed to change.

## 3. Pick a neighbouring cell

Pick from `references/formats.md` and `references/conceits.md`. Three rules:

- **Move one axis at a time.** Same message, same conceit, new format. Or same message, same format, new conceit. Two moves at once and a miss teaches you nothing.
- **Native pairs first, then the empty cells.** A timeline lives naturally inside UGC; a comparison inside a podcast with a founder guest; a re-diagnosis inside a doctor consult. Run those, then the ones nobody's tried (a timeline as a street interview, a listicle sung).
- **Match the messenger to the awareness.** Unaware and problem-aware want a peer or a story; solution-aware wants a founder or an expert; product-aware wants proof and a deal.

## 4. Write it

Paste the message, the format, and the conceit into `references/write-brief.md`. The format fixes the beat order; the conceit fixes who speaks, how it opens, and who says the CTA. The loaded words survive verbatim. Invent nothing the original didn't carry.

## 5. Check it, launch it, log it

Read the new ad against the message: every loaded word present? every beat the format needs, in order? does the pretense hold from the first line to the CTA? any line softer than the original? any invented number? Launch. One row per launch: winner · format · conceit · result. After ten rows you can see which axis you're under-exploring. The empty cells are the next tests.

**The loop:** winner in → message out → one axis swapped → check → launch → the cell that wins is the next winner in.
