---
date: 2026-10-10
brand: RYZE Superfoods (mushroom coffee)
source: https://app.tryatria.com/ad/m3655995141229724
format: 2:20 3D-animated SONG ad, 9:16, US. Running since 14 Jul 2026 (89 days on 10 Oct), peak top 1% by impressions (#11 of 14.5K)
filed-for: pacing benchmark for animated ads. Why ours felt sluggish next to it.
---

# RYZE "mummy" song ad: the pacing numbers

Related: [[2026-10-04-ryze-weed-timeline-animated-ad]] [[2026-10-03-video-ad-rules]]

No lyrics are stored here (their copy). This is the structure and the measurements only. The video
file is in `_assets/2026-10-10-ryze-mummy-song-ad/`.

## What it is
A sung version of their "guy who smokes weed" timeline. The character is a mummy who gets
visibly fitter as the ad goes on. The vocal is the music: one track, one tempo, start to finish.

## Measured (ffmpeg scene detection, onset autocorrelation, Whisper word timings)

| | RYZE mummy | Primal Viking cut v1 (2026-10-10) |
|---|---|---|
| Runtime | 2:20 | 3:43 |
| Shots | 57 | 38 |
| Average shot | 2.5 s | 5.9 s |
| Median shot | 2.1 s | 5.8 s |
| Longest shot | 5.9 s | 10.7 s |
| Shots under 2 s | 44% | 3% |
| Words | about 330 | about 650 |
| Words per minute | about 142 | about 180 |
| Pauses over 0.4 s | 5 | 39 (about 34 s of dead air in total) |
| Tempo | about 129 BPM, constant | voice has none; music bed about 144 BPM, unrelated to the voice |
| Cuts on a beat or half-beat | about 75% | not aligned |
| Words per sung line | about 7 | sentences up to 30 words |

Scene detection can miss cuts between two similar shots of the same character, so their true
cut rate is probably a little faster than this.

## What makes it tight
1. **Lyric, beat and cut are one thing.** Words land on beats and three in four cuts land on a
   beat or half-beat. Nothing can drift.
2. **No shot outstays 6 seconds.** Nearly half are under 2.
3. **Almost no dead air.** Five real pauses in 140 seconds.
4. **Short lines.** About seven words each. A picture change every line or half-line.
5. **It says less.** Half our word count. Fewer words, but slower and on the beat.
6. **Captions are 2 to 4 words**, with single-word hits filling the frame.

## The lesson for our animated ads
Speaking faster doesn't fix "sluggish". We were already at 180 words a minute against their 142.
The drag came from long shots, pauses between lines, and three layers (read, music bed, picture)
that weren't locked to each other.

Targets when cutting a narrated animated ad:
- Average shot 2 to 2.5 s. Nothing over 6 s.
- Close every pause over about 0.3 s unless it's a deliberate comic beat.
- Pick the music first, find its tempo, and place cuts on beats.
- Caption pages of 2 to 3 words, with one-word punches.
- If the script can't be cut to short lines, consider making it a song.
