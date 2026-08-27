# Client Acquisition Calls — Content Mining Pipeline

## What this is
Dan Wardrope's team (Leandro and Nat, mostly) run live weekly Q&A calls for ROYA
students — the group coaching Zoom where students bring real client-acquisition
problems (pricing, niche picking, outreach channels, objections, compliance) and
get live answers. This folder pulls that gold out for Flexxable daily content.

**Correction from the original pilot note:** the "three years of backlog"
originally assumed to be sitting in Zoom does not exist — Zoom's actual
cloud retention only goes back to 2026-03-11 (see the retention-boundary
note below). The 25 calls mined here (5-call Aug pilot + 20 more pulled back
to that retention floor) are the full available history, not a sample.

**This is the "ROYA Onboarding call" backlog Joey flagged as parked in the
2026-08-26 daily note** — now started.

## Where the source recordings live
- Zoom → Recordings and Transcripts → search "ROYA Onboarding call"
- Meeting ID 864 5153 4898 — a shared personal-meeting-room ID used for many
  different call types (1:1 onboarding calls, short Notetaker-bot joins, and
  the real weekly group Q&A). **Filter by duration > 1hr** to skip the noise —
  short entries (<20 min) are bot joins or truncated 1:1s, not the real call.
- Real cadence: Mondays 5pm UK time, Wednesdays 9am UK time. Occasional
  schedule drift (see actual dates pulled below).
- Each recording has a small "Audio transcript - English(original)" file
  (~80-140KB .vtt) — download that, not the video. Click the row, then the
  small ↓ download icon that appears on hover next to "Change Language" (the
  icon only renders after a real hover event — click the row text first, then
  hover, then click the icon at the far right of the row).

## Full batch mined to date (25 calls, Mar–Aug 2026)
Zoom's actual cloud call recording/transcript retention only goes back to
**2026-03-11** — there is no earlier history to pull. The "3-year backlog"
Joey originally assumed was sitting in Zoom does not exist; 2026-03-11 is a
hard floor. What's below is therefore the full available Zoom history for
these calls, not a sample of a larger pile.

| Date | Duration | Hosts | Notable students |
|---|---|---|---|
| 2026-03-16 | not captured | Leandro, Nat | Noor Hibbert, Alex, Scott, Cal Costea |
| 2026-03-30 | not captured | Leandro, Nat | Dorene Wharton, Geir Nummestad, Harry Anstock, "GHD Agency", Dale Nichols, Brian |
| **2026-04-27** | **1:46:35** | **unretrievable — see note below** | — |
| 2026-05-04 | not captured | Leandro (solo — UK bank holiday) | Colin, Jason "JSpeck" Speckert, Charles Koonce, Ash, McMillan's, Murray Wilkinson |
| 2026-05-11 | not captured | Leandro, Nat | Franky, Deuce, JSpeck, Charles Koonce |
| 2026-05-18 | not captured | Leandro, **Dan Wardrope** | JSpeck, Wade Collins |
| **2026-05-20** | **1:08:15** | **unretrievable — see note below** | — |
| 2026-05-25 | not captured | Leandro | Cal Costea, Charles Koonce, Wade Collins, Howard Whiteson, Gabriel |
| 2026-05-27 | not captured | Nat | Alex, Howard Whiteson |
| 2026-06-01 | not captured | Leandro, **Dan Wardrope** | JSpeck, Alexander Hamilton |
| 2026-06-08 | not captured | Nat | Franky, Jenisse Lim, Ethan, "Octerly"/Phil, Mark ("yoben") |
| 2026-06-10 | not captured | Nat | Wes Stevens, Chris Pidgeon, Mark Avila, Marc |
| 2026-06-15 | not captured | Leandro, Nat | Eric Gousheh, Chris Pidgeon |
| 2026-06-22 | not captured | Nat | Nikki Oliveira, Chris Pidgeon, Eric Gousheh |
| 2026-06-24 | not captured | Nat | Philip Jepson, Mark ("yoben"), Rob |
| 2026-06-29 | not captured | Leandro, Nat | Kip Niswonger, Joe Garrity |
| 2026-07-01 | not captured | Nat | Laura, Philip Jepson, Joe Garrity, Mike Dudley |
| 2026-07-06 | not captured | Leandro, Nat | Dorene Wharton, Joe Garrity, Jeff Minderlein, Paul Brenkman, Nikki, Philip |
| 2026-07-08 | not captured | Nat | Paul Brenkman, Gareth ("People+") |
| **2026-07-13** | **~4:51:00 — notable outlier, see note below** | Leandro | David Easton, Michael Oliver, Cal Costea, Joe Garrity |
| 2026-07-15 | not captured | Nat | Philip Jepson (tech-support/product-feedback session, not a typical coffee-date coaching call) |
| 2026-07-20 | not captured | Leandro | Marc, Joe Garrity |
| 2026-08-03 | 1:02:52 | Leandro | Joe Garrity, Marc Krull |
| 2026-08-10 | 1:06:43→1:46:37* | Leandro, Nat | Abhi Amalsadia, Tallinn Cavanaugh, L&L, Jan |
| 2026-08-12 | 1:18:23 | Nat | Patrick Reidin, Greg McDonnell, gary |
| 2026-08-19 | 1:12:31 | Leandro, Nat | Andrew Hickinbotham, Phil3baker, Michael Oliver |
| 2026-08-24 | 1:43:08 | Leandro, Nat | Angie deBorja, Pierre Patrouillard, Brian, Murray Wilkinson |

Durations above "not captured" are genuinely unknown — the 20 newly-mined
transcripts were plain speaker-collapsed text with no duration metadata in
the file itself, and no guessing was done. Only the two unretrievable dates
and the 07-13 outlier have known/estimated durations, noted below.

**Two dates are permanently missing.** 2026-04-27 (1:46:35) and 2026-05-20
(1:08:15) hit a list-virtualization bug in the Zoom recordings UI during
download and could not be retrieved. Their durations are known from Joey's
own tracking, but the transcripts themselves are gone short of manually
retrying the Zoom UI again. This leaves a genuine two-call gap in the
corpus at those two dates — not an oversight, a hard limitation.

**2026-07-13 is a notable outlier** at roughly 4 hours 51 minutes — several
times the length of a typical call. It runs long mostly because of two
extended one-on-one conversations (David Easton's list-sequencing questions,
and Cal Costea's partnership-vetting question about bringing on a
website/SEO subcontractor), not because more students attended.

Raw `.vtt` files and speaker-collapsed `.clean.txt` versions are in
`/private/tmp/.../scratchpad/roya-transcripts/` for this session only — they
were NOT banked here since they're just intermediate transcripts, not the
mined output. Re-download if you need to re-read the source.

## What got produced from this batch
- [gold-nuggets.md](gold-nuggets.md) — banked stories, frameworks, analogies,
  and one-liners worth turning into daily posts. Tagged by theme, sourced by
  call date. Not written as posts yet — that's the next phase, pending
  Joey's direction (see "Next step" below).
- [common-questions.md](common-questions.md) — the questions ROYA students
  actually ask, ranked by how often they came up across the full 25-call
  corpus. This is the "what problems are people having" signal Joey wanted.

## Caution before publishing anything pulled from here
- These are named individuals in a real coaching community (Angie, Pierre,
  Abhi, Joe Garrity, Philip Jepson, and many more across the full 25-call
  corpus) talking about their own real prospects/clients. This caution now
  applies to a much larger set of named individuals than the original
  5-call pilot — genericize or drop names before anything goes out as a
  Flexxable post, and don't publish a ROYA student's business details
  without checking with Joey first.
- Case-study-style numbers mentioned in these calls (e.g. the £18K/month debt
  client, the $20-per-saved-cart e-com client, Gareth's £80K DBR recovery,
  the £18K/month heating-company retainer) are **ROYA's own results, not
  Flexxable's** — per [[dont-verify-user-written-claims]] / the workspace's
  never-invent-a-client-result rule, these need Joey's sign-off before being
  used as if-Flexxable-said-it proof.

## Next step (not done yet, needs Joey's call)
Mining is now done through the full available Zoom history — there is
nothing older to pull (see the retention-boundary note above), and the two
unretrievable dates are a permanent, known gap. The "scale past the pilot"
question from the original 5-call version of this note is answered: this
**is** the whole available corpus, short of Joey manually re-trying the
Zoom UI on the two missing dates.

What's banked in gold-nuggets.md and common-questions.md are drafted,
sourced raw material — not yet turned into actual daily posts. Turning this
into real Flexxable content is the next phase, and it's explicitly not
started here: it needs Joey's direction on which nuggets to prioritize, which
names/numbers are safe to genericize and use, and what the actual posting
cadence and format should look like.

Related: [[Flexxable]] [[the-data-dictionary]]
