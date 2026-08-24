# Producing a Flexxable video ad — checklist

Banked 2026-08-24 after the first video brief run through the Diversity Decoder gap-fill
batch (V3, "The 9PM Message"). Three real catches this session, bundled into one
checklist for the next video brief so they don't have to be rediscovered.
Related: [[Promotion]] [[dan-on-camera-coaching]] [[hook-rubric]]

## 1. Check runtime against the speaker's real WPM before finalizing

The brief said "3-6 min." The raw script came in at 1,114 spoken words — at Dan's actual
pace (~100 wpm), that's ~11 minutes. Nobody caught it until Joey asked directly.

**Do this every time:** count spoken words only (strip every `[VISUAL]`/`[BEAT]`/
`[PAUSE]` stage direction first), divide by the speaker's real wpm, and compare against
the brief's target BEFORE the script is presented as finished. For Dan specifically,
target 300-600 words for a 3-6 min ad at ~100 wpm. If it's over, trim redundant
elaboration first (repeated examples, restated caveats) — the structural beats (hook,
turn, mechanism, CTA) should survive intact.

## 2. `in-feed-vsl-bot` has no Flexxable voice priming — route accordingly

Raw output from `in-feed-vsl-bot` scored 4 FAIL / 34 FLAG against the copy rubric on
first pass — mostly AI-written em-dashes throughout (both stage directions and spoken
lines), plus canned signposts ("and here's the part...") and a banned word
("deliverable"). `mariobot`, which gets the Flexxable primers + style contract
prepended automatically, needed only 5 small taste fixes on a comparable pass.

The bot's STRATEGIC output was good (structure, tense discipline, the Vendor/Partner
binary all landed correctly, unprompted) — the gap is purely sentence-level craft from
having no voice priming.

**Do this every time:** either (a) prime `in-feed-vsl-bot` with the Flexxable primers
before instructing it, the same way `run_mario.py` does automatically, or (b) treat its
raw output as a structure/beat reference only and have `mariobot` write the actual
production script from that beat sheet. Don't ship a raw `in-feed-vsl-bot` draft as
final without a full rubric pass first — budget for heavier cleanup than a mariobot
draft needs.

## 3. Trim `[BEAT]`/`[PAUSE]` markers to real structural pivots only

The raw draft had 15 pacing markers, nearly one per paragraph. Most were pacing filler
between continuing thoughts, not real turns. Trimmed to 9 — kept only the ones marking
an actual pivot (a confession landing, a reframe, the mechanism reveal, the CTA
transition).

**Do this every time:** after the script is finalized, walk every `[BEAT]`/`[PAUSE]` and
ask "is this a real turn, or does the thought just continue across it?" Cut the ones
that are just paragraph breaks. The survivors double as safe places for the talent to
stop and restart filming — see [[dan-on-camera-coaching]].

## 4. Point first-time on-camera talent at the coaching primer

Dan has no screen/presenting experience. [[dan-on-camera-coaching]]
(`clients/flexxable/primers/dan-on-camera-coaching.md`) has the filming approach: don't
attempt one continuous take, read from a teleprompter rather than memorizing, and don't
chase polish — the account's whole native-feeling style depends on it NOT looking
produced. Reusable across every video brief in this batch, not just the first one.
