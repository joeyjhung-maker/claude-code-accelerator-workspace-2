# Workflow: T3 swipe structure for Google Doc sales letters

*Banked 2026-08-26. Joey's call: "T3 is a good swipe structure for writing Google Doc sales
letters. So we will reuse in the future."*

Related: [[t3-phoneless-sales-machine-fb-msgr]] [[2026-06-24-mariobot-genesis-body-copy]] [[hopper-millions-synthesis]] [[copy-rubric]]

## When to use this

Any time you're writing a long-form sales letter as a Google Doc — not a Skool post, not a
Meta ad, not a short landing page. T3 (from Travis Sago's Hopper Millions framework — the tap
sequence is T1 = awareness post, T2 = qualifying conversation, T3 = the actual offer/pitch) is
built for exactly this format: a single document that has to do the whole sell in one read,
personalized to the reader, no back-and-forth.

The reference swipe is banked at
`mentors/travis-sago/hopper-millions/swipes/t3-phoneless-sales-machine-fb-msgr.md` — a real T3
(the "Phoneless Sales Machine" pitch), with its 8-beat skeleton broken down. First real-world
run of this move: the B2B Leads Lab DFY beta waitlist page
(`copy/2026-08-25-b2b-leads-lab-dfy-beta-waitlist-landing-page-FINAL.md`), which went through
this exact process before Joey built it out further.

## The steps

1. **Hand Claude the T3 swipe** (`t3-phoneless-sales-machine-fb-msgr.md`) as the structural
   reference, plus the new offer's real facts — avatar, mechanism, proof, price/terms, CTA
   destination. Say explicitly: "keep it as close as possible, change only what's needed to be
   relevant, keep the tone and way [the swipe's author] writes."
2. **Rewrite line-for-line onto the new offer**, preserving the skeleton exactly: personalization/
   identity-callout → overview (dates/format) → unique promise → proof statement → what's-
   stopping-them (general pattern, then the specific missing piece) → why-now (real constraint,
   not manufactured urgency) → risk-reversal/terms → CTA.
3. **The substitution rule, not a rewrite rule:** where the swipe's original detail is
   offer-specific (a named case study, a fixed date, a five-figure deposit-plus-backend pricing
   model), don't force it to fit — swap it for the new offer's REAL equivalent fact, or drop the
   beat's specific mechanic while keeping its JOB. Never invent a name, date, or number to fill a
   slot the swipe originally had — that's the one hard line. On the beta waitlist run, this meant
   swapping an invented "Elizabeth" case study for real proof numbers already on file, and
   swapping a $5k-deposit guarantee structure for the new offer's actual (much simpler) terms.
4. **Check step:** run `scripts/copy_lint.py`, then a full taste-rubric pass against
   `copy-rubric.md`. Specifically watch for the swipe's own voice patterns accidentally
   reintroducing banned constructions (e.g. a "not X, it's Y" antithesis flip) that the new
   brand's rubric doesn't allow even if the original author used something adjacent to it.

## What good looks like
`copy/2026-08-25-b2b-leads-lab-dfy-beta-waitlist-t3-structure.md`'s process (later superseded by
Joey's own further build-out, but the T3-adaptation pass itself is the reusable part) — clean
lint pass, one taste-rubric catch (a banned antithesis pattern) fixed before it reached Joey.
