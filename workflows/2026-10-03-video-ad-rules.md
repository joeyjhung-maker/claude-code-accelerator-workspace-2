# Video ad rules (any video we build or brief)

Banked 2026-10-03 from the whiskey locked-bottle series (doodle, 16-bit, heist, Pixar). Each rule here came from a correction Joey made on a real cut, so check every new video against all of them before he sees it.
Related: [[2026-08-24-produce-flexxable-video-ad]] [[Promotion]] [[hook-rubric]]

## 1. The first frame carries the hook

**The rule:** frame 0, the still that shows before anyone presses play, must already have the first line of the script on screen at full size, over the hero visual.

- No fade-in, pop-in, blank background or black frame at 0:00.
- Put the whole first line on it, not just the first word or two. Merge the opening caption pages if you have to.
- The words still highlight as they're spoken once it plays.

**Why:** in the feed the paused first frame is the thumbnail. RYZE's ads all open with their first line already on screen ("A dude who smokes…"). Ours opened on a vault with no text, because the caption animated in over the first 0.2s.

**The check:** export frame 0 from the *finished file* (`ffmpeg -i final.mp4 -frames:v 1 frame0.png`) and look at it. If the hook and the product aren't both readable, it isn't done.

## 2. Every spoken word is on screen

**The rule:** full captions, not highlight fragments. Fragments read as "words are missing".

- Get word-level timestamps from a local Whisper pass on the master audio.
- Hand-set the page breaks at natural phrase boundaries. Auto-breaking splits thoughts and leaves orphan words.
- Highlight the word being spoken.
- Make the build fail if the captions don't match the transcript word for word.
- Where transcripts disagree, check the captions burned into the original footage.

## 3. The product is the hero, and nothing covers it

**The rule:** the product has to be big and obvious within the first second. For the whiskey ads that was the bottle.

- Captions and graphics move per shot so they never sit on top of the product.
- If a prop swallows the product, re-shoot those moments with the product filling the frame. The vault hid the bottle, so we re-shot.

## 4. Something happens every second

**The rule:** pretty footage with slow moves and small titles is easy to scroll past. The heist cut died on this.

- A cut, a reaction or a graphic roughly every 1–2 seconds.
- Motion graphics across the whole frame, styled to match the footage: arrows, rings, bursts, reactions, swooshes.

## 5. Voice first in the mix

**The rule:** balance by loudness, not peaks.

- VO at about -16 LUFS.
- SFX and music 7–8 LU under it.
- Master at -14 LUFS.
- Always use the original master audio, never a platform rip.

## What good looks like

`creatives/2026-10-03-flexxable-iaa-whiskey-pixar-v5.mp4`, and its frame 0.
