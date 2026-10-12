# Workflow: Song hook splice (test a new hook on a song ad without redoing the song)

Banked 2026-10-12 after one run on the Primal Viking "52-year-old Viking" song ad (song cut v4). Run once so far: promoted early because Joey wants it for split testing video hooks.
Related: [[2026-10-03-video-ad-rules]] [[2026-10-12-line-options-loop]] [[hooks-are-80-percent-vicious-flinch]]

## When to use this
A song ad is finished and you want a different hook on it: a rewrite, or several hooks to split test.
The song after the hook stays exactly as it is.

## The steps
1. **Sing the new hook on its own.** Same music model, same style text and same tempo as the full song. Send only the hook lines, with an `[End]` tag after the last one. One generation gives two takes of about 30 seconds and costs about a twentieth of what the full song does. Save the task ID.
2. **Check the takes before Joey hears them.** Transcribe both and compare with the hook as written. Sung words transcribe loosely, so flag a mismatch as "listen for this", not as a fault.
3. **Give Joey the takes next to the original opening**, cut from the current song and set to the same loudness. He picks by ear.
4. **Measure the picked take against the song.** Tempo, key and loudness of the take, and of the song just after the hook. On the Viking ad: 119 against 123 beats per minute, G major against D major, 0.3 dB apart. That was close enough.
5. **Cut on the beat.** End the take one beat after its last sung sound. Start the original in the quiet gap just before the first word of the next line, so that word lands on the take's next beat. Short fade out, short fade in, no overlap.
6. **Splice the word timings the same way.** New take's words up to the cut, then the original's words shifted by the difference. The video build reads this file.
7. **Rebuild the video.** Point the build script at the spliced song and words, change the hook lines in its script list, and render a new version. Only the opening is re-timed: on the Viking ad everything after the hook moved by 0.07 seconds.
8. **Check frame 0 and the opening captions** on the finished file, then send the small copy with the time of the join called out.

## Limits
- The singer is a different voice after the join. It is one generation per hook, not one voice across the ad.
- It needs a clean line start in the original right after the hook. If the old hook runs into the next line with no gap, there is nowhere to cut.
- If tempo is more than a few percent out, or the keys clash, regenerate the whole song with the new opening instead.
- For a split test, every hook variant gets its own take and its own splice onto the same song body, so the only thing that differs between the videos is the first 30 seconds.

## What good looks like
`creatives/_assets/2026-10-10-primal-viking-57-year-old-viking/songcut/song-cut-v4-small.mp4`, join at 0:29.
Scripts: `song/hook_gen.py` (sings the hook) and `songcut/build.py` (the video build) in the same folder.
