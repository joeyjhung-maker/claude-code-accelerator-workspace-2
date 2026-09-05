# Workflow: rewrite a JV partner's affiliate swipe into Dan's voice

*Banked 2026-09-05 after the second run — first on Rich Schefren's manifesto VIP-waitlist
sequence, then on Matt Leitz/BotBuilders' "Crush It with Claude" / AI CMO sequence. Same
process both times, worth locking as a play.*

Related: [[always-use-mariobot-to-write]] [[run-judge-before-showing-copy]] [[judge-provenance-rule]] [[jv-additive-framing]]

## When to use this

A JV partner hands over their OWN affiliate swipe copy (a Google Doc, usually) for the "sell
THEIR offer to OUR audience" leg of a partnership — the reverse of us hosting them on a
webinar to their list. The content/offer/claims are theirs; the job is only to re-voice it as
Dan writing to his own list, not translate it into a different offer (that's the T3-swipe
workflow instead — see [[2026-08-26-t3-swipe-for-sales-letters]]).

## The steps

1. **Read the whole source doc first**, don't skim. Google Docs won't give up its text to
   `get_page_text` or the accessibility tree (canvas-rendered) — scroll + screenshot through
   it in a real browser tab. Capture every email's subject lines, preheader, and full body
   before writing anything. Missing a paragraph mid-email is easy to do with large scroll
   jumps — use small scroll increments (6-10 ticks) and check each screenshot connects
   cleanly to the last one's cutoff point.
2. **Per email, write an `instruction-emailN-slug.md` brief** in
   `jv/partners/{partner}/copy/sell-their-offer/_working/`, following the Rich Schefren
   emails' template shape:
   - What this is (sequence position, what's already landed vs. new in this email)
   - Word count target (count the source body yourself, word for word, sign-off to greeting —
     don't guess)
   - Every fact/number/name as a bullet, marked "keep exact, don't invent or embellish"
   - Any structural quirk unique to this email (no greeting line, doesn't mention price yet,
     etc.) — note it explicitly or mariobot will "fix" it back to a generic template
   - The full source email pasted verbatim at the bottom
3. **Run it through mariobot**, never freehand:
   `python3 scripts/run_mario.py --primer jv/shared/dan-voice-primer-excerpt.md --instruction
   <instruction file> --out <draft file>`
4. **Lint, then grade.** `scripts/copy_lint.py` first — rewrite every real FAIL. Known false
   positive: it treats "Inc." (and likely other abbreviations) as a sentence end, throwing a
   "two+ sentences on one line" FAIL on a line that's genuinely one sentence — verify by eye
   before treating it as real (see `skills/observations.md` Observation 4). Then grade against
   `rubrics/copy-rubric.md` + `rubrics/mariobot-style-contract.md` as an explicit tick-list —
   watch especially for: canned signposts mariobot adds ("here's what X does"), banned words
   slipping in even when the source's claim seems to justify them (e.g. "leverage" describing
   a real team benefit still fails — swap for a non-banned word, don't carve out exceptions),
   and the "never open on a question" rule when the source itself opens on one.
5. **Word count will run ~10% over the source on the first mariobot pass** — that's normal,
   not a failure. Note it, don't force a rewrite for it alone unless Joey asks.
6. **Show the scorecard + draft, save to `_working/`.** Joey may hand back his own edit
   pass — per [[judge-provenance-rule]], grade the NEXT draft's lint mechanically but don't
   "fix" his prose; flag anything that reads like a slip (grammar, a missing link) and let him
   decide.

## What NOT to do

- Don't assume a partner's "this is the new offer, nothing else" means an EARLIER leg of the
  same partnership is dead. JV deals run two independent directions at once (see
  `jv/JV-map.md` — "the play") — "nothing else" scopes the leg being discussed, not the whole
  relationship. Read the partner's `partner.md` for what's already locked before assuming it's
  stale.
- Don't skip capturing the full source doc before writing instruction files — a gap in the
  source (missed via a big scroll jump) becomes a gap in the brief mariobot never gets a
  chance to fill.

## Worked examples
- `jv/partners/rich-schefren-strategicprofits/copy/sell-their-offer/_working/` — emails 1-3
- `jv/partners/matt-leitz-botbuilders/copy/sell-their-offer/_working/` — emails 1, 2, 4
