---
date: 2026-09-30
client: Flexxable / Dan
offer: The Instant A.I. Agency book ($14.40)
type: cinematic "heist" video ad: AI video + Dan's real footage + documentary titles, over Dan's master VO
format: 1080×1920, 30fps, 1:17.6
status: BUILT v1: creatives/2026-09-30-flexxable-iaa-whiskey-heist-v1.mp4
---

# Locked Whiskey Bottle: Cinematic Heist Version

Related: [[2026-09-30-flexxable-iaa-whiskey-16bit-game-BUILD]] [[2026-09-29-flexxable-iaa-whiskey-locked-bottle-animated-STORYBOARD]]

The third look for the same script and audio, picked from the five-looks test.

## Pipeline

All build files live in `creatives/_assets/2026-09-29-whiskey-locked-bottle/heist/`.

1. **Keyframes:** 17 frames made with KIE Nano Banana 2 (`key/`). The first frame, from the looks test, is the reference for every bottle shot. The CEO's first frame is the reference for his other shots, so the bottle, brass lock, wax seal and CEO stay consistent. Board: `creatives/2026-09-30-flexxable-iaa-whiskey-heist-keyframes.png`.
2. **Video:** 17 Veo 3.1 image-to-video clips, 6s at 1080p (`clips/`), made with `scripts/run_video.py` (new; prints the cost of each clip).
3. **Edit:** `build/edit.py` cuts the picture track to exactly 77.6s. The handshake is trimmed before a glitch at ~3.5s. The lock clip is reversed so it springs open. The aerial and book plate are slowed to fit.
4. **Dan's real footage:** 21.1–22.0 ("that's the whole pitch") and 71.4–75.55 (the refund line and "take care"). It comes from the 4K original and is cropped above the burned-in captions. It shares the audio's timeline, so the lip-sync is exact. It is graded teal and amber to match.
5. **Titles:** `heist.html` draws documentary titles over each frame of the base video.
   - Tracked Inter caps, Cormorant Garamond italics, gold numerals with glow.
   - A "Dan Wardrope · Author" chyron.
   - The real book cover with a light sweep.
   - Warm light-leaks on cuts, film grain and a vignette.
6. **Sound:** `build/heist_audio.py`.
   - **Foley:** clean Veo audio only for the dials, cash counter and ringing phone. The other clips had AI music or a stray voice, so their audio is dropped.
   - **Designed effects:** risers into impacts on $1.2M, $225K and the book reveal, plus the lock clack, paper, seal crack, dial, drawer and warm swell.
   - **Score:** a dark 96 bpm A-minor pulse with a ticking clock.
   - **Mix:** VO-first. Dan at -16 LUFS, the bus at -24 LUFS, master at -14 LUFS.

## Cost

About 1,240 KIE credits (≈ $12.40 at $20 per 2,000 credits):

- 17 keyframes × 8 credits
- 17 clips × 65 credits

The auto top-up is on.

## Text rule

Dan's own words only, plus the chyron (his real name and role). The only numbers on screen are $10 million, $1.2M, $225,000 and $14.40.
