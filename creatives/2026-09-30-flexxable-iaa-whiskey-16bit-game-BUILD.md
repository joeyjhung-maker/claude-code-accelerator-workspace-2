---
date: 2026-09-30
client: Flexxable / Dan
offer: The Instant A.I. Agency book ($14.40)
type: animated video ad, 16-bit SNES game look, over Dan's master VO
format: 1080×1920, 30fps, 1:17.6
status: BUILT v2 (big bottle, real cover): creatives/2026-09-30-flexxable-iaa-whiskey-16bit-game-v2.mp4
---

# Locked Whiskey Bottle: 16-bit Game Version

Related: [[2026-09-29-flexxable-iaa-whiskey-locked-bottle-animated-STORYBOARD]]

The second look for the same script and the same Dan master audio. Picked by Joey from the five-looks test (`creatives/_assets/2026-09-29-whiskey-locked-bottle/looks/2026-09-30-five-looks.png`).

## How it's built

**Source:** everything lives in `creatives/_assets/2026-09-29-whiskey-locked-bottle/game/`.

**Pixel-true rendering:** `game.html` draws the world on a 270×480 canvas and scales it up 4× with no smoothing. The text is Press Start 2P on the 1080×1920 layer. CRT scanlines and a vignette sit on top.

**Backgrounds:** street, office, boss lobby, overworld map and shop. They were generated with KIE Nano Banana 2, then pixelized to 270×480 with a 48-colour palette.

**Portraits and cover:** Dan's dialogue portrait was generated from his 4K frame and pixelized to 48×48. The book is the real cover, pixelized to 40×55.

**Sprites:** Dan (idle, walk, arms-up), the android, the business owner, the bottle, lock, letter, coin, lead card, chest, SMS, check and ∞. All hand-authored as pixel maps in code.

**Transitions:**

- iris into the tower door
- a battle-swirl into the boss fight
- SNES mosaic between menu screens
- iris into the shop
- white-out into the end card

**Sound:** `sfx8.py` synthesizes 50 chiptune sounds from square, triangle and noise voices, plus a 150 bpm music loop that switches to a minor key for the boss fight. There are 495 cues, all exported from the same timeline (`collectCues()`), including a text blip on every other typed character.

**Mix:** Dan is compressed and sits at -16 LUFS. The SFX and music bus sits at -24 LUFS, 8 LU under him, and ducks further under speech. The master is at -14 LUFS.

## Beat map (VO timing)

1. **0:00 WORLD 1-1, street:** Dan walks in. ITEM GET: the bottle rises over his head, the lock drops onto it (3.0s), then the letter arrives (4.25s). "$10M BUSINESS" lights up on the tower sign (5.0s). Dan walks to the door, a red "!" pops, and the iris closes.
2. **0:07.7 Office:** the phone rings. The menu shows ONE SINGLE OFFER.
3. **0:11.2 Dialogue:** Dan's portrait and the offer are typed out word for word, ending on "SALES?". The android joins as "AI + SMS". The rules window reads "If you don't get paid, we don't get paid." Then "THAT'S THE WHOLE PITCH."
4. **0:22 Boss battle:** the $10M BUSINESS boss appears. The FIGHT / OFFER / ITEM menu selects OFFER and an SMS volley goes out. A green **+$1.2M** heal fills the revenue bar. The thank-you chest drops and opens: **+$225,000**.
5. **0:31.6 Inventory:** 8 OLD LEADS cards, each stamped PAID, under "ALREADY PAID FOR". Coins flow from the cards into the pot.
6. **0:37 Office:** RIDICULOUSLY EASY TO SELL. The offer card flies to the business owner, and a red "!" pops on "immediately".
7. **0:43 Quest log:** 4 pain lines, each ticked on the beat.
8. **0:51 Overworld:** THE EASIEST AI OFFER ON THE PLANET. 22 businesses light up as coins, and the counter reads LEADS × ∞.
9. **0:59.5 Skill tree:** TECH GURU gets X'd. OLD LEADS → SMS → SALES lights up, then "VERY, VERY SIMPLE."
10. **1:04 Shop:** the legendary book in a light beam, "THE INSTANT AI AGENCY", "$14.40 ▶ BUY", "GRAB IT BELOW". Then the refund line.
11. **1:14.6 GAME CLEAR:** TAKE CARE. The lock digits spin to ✓ and it pops open, with fireworks, confetti and the level-clear fanfare.

**On-screen text rule:** only Dan's words or plain game labels (WORLD 1-1, INVENTORY, QUEST LOG, SKILL TREE, FIGHT/OFFER/ITEM, BUY, GAME CLEAR). The only numbers on screen are ones he says: $10M, $1.2M, $225,000, $14.40.

## Mix lesson (applies to every VO ad)

Peak-normalizing Dan's master left his speech body ~5 LU **under** the SFX bus. It was the real cause of "the bells are too loud".

**The fix:** balance by loudness, not by peaks. Compress the VO, set it to -16 LUFS, set the SFX/music bus to -23 or -24 LUFS, then normalize the master to -14.

The doodle version was re-mixed the same way as v5.
