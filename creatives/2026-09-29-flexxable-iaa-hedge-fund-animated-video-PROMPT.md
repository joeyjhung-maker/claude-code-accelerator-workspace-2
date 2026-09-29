---
date: 2026-09-29
client: Flexxable / Dan
offer: The Instant A.I. Agency book ($14.40)
type: video build prompt — code-rendered hand-drawn motion graphics
source_copy: copy/2026-09-28-flexxable-iaa-hedge-fund-FINAL-joey.md (Hook 1 + Body)
adapted_from: "Website → 30-second conversion film" prompt (@digitalstrategyai, Threads)
status: DRAFT prompt — not yet run
---

# Prompt — Hedge Fund Winner → Animated Build-Log Video

Related: [[2026-09-28-flexxable-iaa-hedge-fund-FINAL-joey]] [[2026-09-28-hedge-fund-winner]] [[2026-09-29-kittyspout-sung-animated-ad]]

---

```
You're turning a proven Facebook ad into a vertical animated video. The ad already wins.
Your job is to ILLUSTRATE it, not rewrite it. Think art director + motion designer, not copywriter.

## THE SCRIPT (locked — use verbatim, one line per beat, in this order)

[paste Hook 1 + Body from copy/2026-09-28-flexxable-iaa-hedge-fund-FINAL-joey.md]

Rules for the words:
- Every on-screen line is the ad's own line, verbatim. Do not add, merge, reorder or "punch up" any line.
- You may drop filler lines only if I approve it at the storyboard stage.
- No new claims, numbers, stats, testimonials or "trusted by" logos. The only numbers that exist are
  7-figure, $341,042, $14.40 and 30-day. Nothing else gets a number.
- "PROFIT" stays in caps. "$341,042" never rounds. Rob is first name only.
- Never explain what hedge fund managers do. The unanswered question is the engine of the ad.

## WHY THIS AD WORKS (protect these — they're what the animation must serve)
- It's a first-person build-log: Dan reporting one completed action per line, like a diary.
  Every claim lands as something that HAPPENED, not a promise. Never switch to "you" on screen.
- The hook opens on curiosity (hedge fund managers + a 7-figure business), NOT on pain.
  Do not add a pain-first opener.
- One spine: one deal / one client out-earning a whole salary. Everything serves that.
- It never breaks frame to sell. The offer, guarantee and sign-off are just more diary entries.

## VISUAL CONCEPT — "the diary that built a business"
- Look: clean hand-drawn line-art motion graphics on a warm off-white paper texture
  (ink-black strokes, one accent colour for money/wins, one muted red for the old way).
  Strokes draw themselves on. Kinetic typography in a bold, friendly sans for the line itself,
  a handwritten font only for small margin notes. Premium, calm, confident. Not SaaS-template.
- Device: each line is written into Dan's notebook and ticked off, then the page zooms into a
  doodle that literally illustrates that line. Literal beats clever. If the line says
  "Went through my phone…", we see a hand scrolling a contact list.
- Engineer these specific moments:
  - HOOK (0–3s): a sketched hedge-fund trader / trading screen, with a stock line that bends into
    the words "7-figure business". The text must be readable in under 2 seconds.
  - "All I did was copy how they got PAID…": the word PAID is stamped, then photocopied.
    It's the only hook-section line that gets a stamp.
  - "Made more money from one deal than my entire engineering salary.": the Von Restorff beat.
    A single deal card on a see-saw that outweighs a whole year of payslips. Hold for 1.5s.
  - "…and then made $341,042 in PROFIT…": the PEAK. The counter rolls up to $341,042, "PROFIT" slams
    in, then everything else on screen fades away. Hold for 2s. This is the most visually dominant frame in the film.
  - Offer lines ($14.40, video training, 30-day guarantee, keep everything): quick, satisfying
    ticks down the notebook page. A price tag for $14.40, and a stamp for the guarantee.
  - END (peak–end rule): "Signed off for the day…" shows the laptop closing. Then "And then picked up my kids
    from school." is a warm, slower wide shot: school gate, low sun, the only moment with colour wash.
    Then the CTA card: "Click the button below to see how it all works." with a pointing hand, held 2s.
- One idea per cut. Lots of whitespace. Big text: nothing smaller than 48px at 1080w.

## SOUND
- No voiceover (it's Dan's voice or nothing, and we don't fake Dan).
- Build a simple original soundtrack in code: a light, warm lo-fi groove (~90 BPM) synthesized
  from scratch, plus subtle SFX synced to the animation: pencil scratch on write-on, soft tick on
  each notebook tick, a cash-register "ding" on $341,042, a paper stamp on PAID and the guarantee.
- It must work with the sound OFF. The text carries 100% of the message.

## SPECS
- 1080×1920 (9:16), 30fps, H.264 + AAC, MP4, under 10MB.
- Meta Reels safe zones: keep all text out of the top 14% and the bottom 20%, and away from the right-edge icons.
- Length: whatever the script needs at a readable pace. Roughly 1.8–2.5s per line, fast on the
  short lines and held on the peaks. Expect about 60–75s. Then make a second 30s cutdown that
  keeps the hook, the one-deal beat, Rob's $341,042, $14.40 + guarantee, the kids and the CTA.

## PROCESS (gates are real — stop where it says STOP)
1. STORYBOARD FIRST: a table with columns shot # · timing · exact on-screen line (verbatim) · what we see ·
   motion · SFX · why the beat works. Flag any line you'd suggest dropping, and why. STOP. Wait for my approval.
2. BUILD: animate deterministically in code (HTML/SVG/Canvas with a frame-accurate timeline),
   render frame-by-frame and encode with ffmpeg. No stock footage, no AI video, no external assets.
3. SELF-QA before showing me: export a contact sheet (1 frame per shot) plus the 3 peak frames at
   full size. LOOK at them. Fix any text that's clipped, overlapping, outside the safe zone, misspelt or not
   verbatim. Check that the $341,042 frame is the most dominant frame in the film. Only then show me.
4. DELIVER: both MP4s, the contact sheet, and a one-line note on anything you couldn't do.
```
