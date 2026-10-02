---
date: 2026-09-30
client: Flexxable / Dan
offer: The Instant A.I. Agency book ($14.40)
type: hybrid video ad: hand-drawn explainer + Dan's real footage, over Dan's master VO
format: 1080×1920, 30fps, 1:17.6
status: BUILT v1: creatives/2026-09-30-flexxable-iaa-whiskey-hybrid-v1.mp4
---

# Locked Whiskey Bottle: Hybrid (Doodle + Dan)

Related: [[2026-09-29-flexxable-iaa-whiskey-locked-bottle-animated-STORYBOARD]] [[2026-09-30-flexxable-iaa-whiskey-heist-BUILD]]

Joey's brief: the hand-drawn slides, but switching over to Dan's real face seamlessly. It has to keep people watching and build rapport, so viewers feel they've met him.

## The idea

**Dan is the host. The sketchbook is his whiteboard.**

- He's on camera for the personal and trust beats: the stunt, the proof, the energy, the guarantee.
- The drawings take the mechanism beats: the offer card, AI + SMS, the checklist, the globe, the book.
- When the drawings take over, Dan doesn't leave. He shrinks into a live **Dan-cam bubble** (lip-synced, labelled "Dan") in the bottom-left, then grows back out to full screen for his next line.

Dan's face is on screen for roughly 75% of the ad (about 19s full screen, about 35s in the bubble). The only stretches without him are 3.4–7.5s (his original has the letter and building b-roll there) and the globe (51–59.7s, which was also b-roll).

## Beat map

| Time | Mode | Dan says | What happens |
|---|---|---|---|
| 0:00–3.0 | **Dan** | I sent this bottle of whiskey, with this little combination code… | Real bottle, real face in frame 1. At 2.45s a red ink circle scribbles round the **real** lock he's pointing at. |
| 3.0–3.4 | hole | …and a letter | The ink circle opens outward into the drawn world. The drawn lock clacks on right as it lands. |
| 3.4–7.5 | doodle | to a $10M business, to get their attention | The original doodle: letter, $10M tag, tower, 👀. |
| 7.55–8.0 | tear | | The paper rips upward and Dan is behind it. |
| 8.0–11.0 | **Dan** | when they dial a number… I put one single offer in front of them | A drawn index card, "one single offer", slides in beside him. |
| 10.95–11.45 | card | | That card grows to fill the screen and becomes the offer card. |
| 11.9–21.0 | doodle + bubble | Do you have any old leads… performance basis… if you don't get paid… | The Dan-cam pops in. |
| 21.0–27.0 | **Dan** | that's the whole pitch… we've just done this for a client… an extra $1.2m | The bubble grows to full screen. At 25.3s an "an extra / $1.2M" sticker slams onto his footage, with a cash burst, a flash and a shake. |
| 27.0–37.2 | doodle + bubble | …they've sent us over $225,000… old leads they already own | He shrinks back to the bubble. The money-rain from his original edit is still visible round his head. |
| 37.2–39.8 | **Dan** | this offer is ridiculously easy to sell | Yellow highlight on "ridiculously easy", with sparkles round his head. |
| 39.8–50.9 | doodle + bubble | every serious business owner… paid for, forgotten, no resource… | Owner and lightbulb, then the checklist. |
| 50.9–59.7 | doodle | easiest AI offer on the planet… never run out of old leads | The globe. The bubble whooshes away. |
| 59.7–62.2 | **Dan** | plus you don't have to be a tech guru | Tear reveal. A **TECH GURU wizard hat is face-tracked onto his head**, struck through in red, then flicked off-screen. |
| 62.2–64.2 | doodle + bubble | the AI behind it is very, very simple | The 3-box flowchart. |
| 64.2–65.9 | **Dan** | I'm so pumped about this offer | Ink energy dashes and amber lightning bolts round his head. |
| 65.55–71.5 | doodle (+ bubble from 69.1) | I wrote a book on it… grab it below, only $14.40 | A hole opens from his chest into the box-to-book reveal. |
| 71.5–74.4 | **Dan** | if you don't love it, you can keep it and I'll refund you your money | The guarantee is on his face. A "keep it ✓" sticker pops in. |
| 74.4–77.6 | end card | take care | Full-screen Dan shrinks straight into the end card beside the book, and the bottle unlocks. |

## Why these beats went to Dan

- **Frame 1 is a real person holding a real, strange object.** You don't get that pattern interrupt from a drawing. The first cut (his real lock turning into the drawn lock) tells the viewer straight away that this ad plays between the two worlds.
- **Proof and the guarantee are spoken to camera.** "$1.2M" and "I'll refund you your money" land harder from a face than from a graphic.
- **The mechanism stays drawn.** Lists, flows and the globe explain better as pictures, and the bubble keeps Dan in the room while they do.
- **The gags on his footage** (the ink circle, the $1.2M sticker, the wizard hat, the energy lines) show his personality. They make the two worlds feel like one piece.

## Captions

His original has burned-in captions. Paper-tape captions in the doodle style are laid over them: same font system, with key words in colour (whiskey amber, $1.2m green, tech guru red, yellow marker on "one single offer" and "ridiculously easy"). Muted viewers get captions in every Dan section. The words are verbatim, and "$225k" was written out as the doodle's "$225,000".

## Pipeline

Build files are in `creatives/_assets/2026-09-29-whiskey-locked-bottle/hybrid/`.

1. **Face tracking:** `build/faces.swift` runs Apple Vision over the original, frame by frame. `build/faces_smooth.py` smooths the track without crossing any cut in his original edit, so the bubble snaps with his cuts instead of drifting. Output: `build/faces.js`.
2. **Composite:** `hybrid.html` is the doodle's `anim.html` with the old static badge hidden. `build/hybrid.js` adds the layers.
   - A canvas with Dan's 4K footage (downscaled to 1080), clipped by the current beat's shape: full, bubble, bubble↔full morph, ink hole, paper tear, or card.
   - An SVG layer with ink rims, tape captions and the gags.
   - Everything is a pure function of t. The whole beat map is the `TL` table at the top of `hybrid.js`.
3. **Render:** headless Chrome (puppeteer-core), 2,329 frames. The render script lives in the session scratchpad. The same approach can be re-created from `hybrid.html?frames=<dir>` plus `window.renderAt(t)`.
4. **Sound:**
   - `window.collectCues()` keeps the doodle's cues only where the doodle is actually on screen.
   - It adds 47 hybrid cues: rips, whooshes on every morph, bubble pops, the lock scribble, a boing and whoosh on the hat, the $1.2M riser and impact, and a ding on "keep it".
   - All of it is synthesized by the existing `build/sfx.py`.
   - Mix is VO-first: Dan at -16 LUFS, SFX at -24 LUFS, master at -14 LUFS (measured -14.4, peak -0.4 dB).

## Text rule

Dan's words only, plus his first name on the bubble. The only numbers are $10M, $1.2M, $225,000 and $14.40.

## Next levers, if wanted

- A/B the opener: this Dan-first cut vs the doodle-first v5.
- Cut-down: a 30s version (hook → $1.2M on Dan → the checklist → book + guarantee).
- More bubble moments: Dan could react to the doodle (glance, point) if we pick bubble clips where he gestures.
