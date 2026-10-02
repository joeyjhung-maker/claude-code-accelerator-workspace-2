---
name: curiosity-headlines
description: Generate 10 genuinely different curiosity headlines (or email subject lines) for a finished post or email by looking at its core argument through an unexpected lens — culture, history, anthropology, status, enemies, odd comparisons, reversals, current events. Use when Joey says "curiosity headlines", "curiosity subject lines", "more out there", "wilder headlines", or asks for headline / subject line options on a Dan Skool post or email. Origin example: "What Japanese gift culture knows about landing WHALES".
---

# Curiosity Headlines

Turn a finished post or email into 10 headline (or subject line) options that make people curious, by finding a surprising lens on the post's real idea. "Out there" means a surprising angle on the same argument, never random weirdness.

Origin: built from the 2026-09-25 Codex run on the Japanese gift-giving post, which produced "What Japanese gift culture knows about landing WHALES" (`copy/2026-09-25-b2b-leads-lab-skool-post-japanese-gift-giving.md`).

## Inputs
- The full post or email (required). Headlines come from the finished piece, not from a brief.
- Where it's going: Skool post headline, or email subject line.

## Process (Mariobot writes, Joey's rule 2026-09-29)
Steps 1-2 are prep; the 10 options are WRITTEN BY MARIOBOT, then judged. Never write them directly.
1. Read the whole piece and name its single strongest argument in one line.
2. Find a wider lens that makes that argument more interesting:
   - anthropology or human behaviour
   - history or cultural customs
   - status and reputation
   - enemies or conflict
   - unexpected comparisons
   - bold reversals
   - zeitgeist and current events
3. Verify any unfamiliar cultural, historical or scientific claim with an authoritative source before using it.
4. Build an instruction file: the finished piece verbatim + the strongest argument + 3-5 candidate lenses (with any verified facts) + the rules below + "write exactly 10". Run `python3 scripts/run_mario.py --no-style-contract --primer <Dan Skool primer, e.g. clients/flexxable/primers/dan-skool-posts-body.md> --instruction <file>`. If Mariobot is unreachable, STOP and tell Joey (no fallback drafting).
5. Judge Mariobot's list: exactly 10 genuinely different options in this mix:
   - 3 bold but direct
   - 4 playful or provocative
   - 3 slightly wild but still defensible
6. Truth + fit check on every option: character count, invented facts, CAPS rule, and does it still point at the piece's actual idea. If a reader clicked, would the post deliver on it?

## Rules
- Never invent facts, numbers or results to make a headline stronger. Obvious playful exaggeration is fine.
- No stereotypes, and don't reduce another culture to a marketing trick.
- No ten minor variations of one sentence. Each option uses a different lens or shape.
- Dan Skool posts: aim for 45-65 characters, never more than about 80.
- Email subject lines: same process; keep each one short enough to read in full in a phone inbox.
- CAPS on one stress word only, never the whole line.
- Prefer concrete nouns, named cultures, enemies, characters and outcomes.
- Back-pocket inspiration if the first ideas are flat: `swipes/reference-banks/2009-made-you-look-527-email-subject-lines.md` (borrow the tension, never the claims).

## Output
The 10 numbered options only. Add a factual caveat underneath only when one is genuinely needed. Plain text, no Markdown bold, so it pastes cleanly into Google Docs.
