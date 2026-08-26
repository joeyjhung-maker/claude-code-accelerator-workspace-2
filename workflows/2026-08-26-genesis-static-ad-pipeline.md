# Workflow: Genesis static-ad pipeline (locked ad copy → rendered image)

Related: [[Promotion]] [[2026-06-24-mariobot-genesis-body-copy]] [[creative-strategy-system]]

## When to use this
You have locked ad copy and need static image concepts, but don't know which format(s) fit, or
need the concept turned into a render-ready prompt. Ran this full chain three times in one session
(Founder's Note, Person Holding Sign, Reptile Triggers/visceral mechanism) — it's a repeatable play,
not a one-off.

## The chain
1. **Static Ad Info Extractor Bot** (`static-ad-info-extractor-bot`) — turns locked ad copy into an
   8-field brief (product, audience, problem, promise, price, CTA, visuals, tone). Primer = the
   locked ad. This brief becomes the shared input for every step after.
2. **Universal Static Ad Idea Bot** (`universal-static-bot`) — feed it the 8-field brief, it
   recommends the 3-5 best-fit formats out of 21 and names which generator bot to run for each.
   Better than guessing formats by feel — it reasons from the actual offer/audience, not habit.
3. **The format-specific generator bot** — there are ~30 in the roster (Note From Founder, Bold
   Typography, Person Holding Sign, Reptile Triggers, Comparison, Native News, Lo-Fi, Testimonial,
   etc. — `GET $GENESIS_BASE_URL/models` for the live list). Each takes the 8-field brief and
   returns 5 (sometimes more) full concept briefs: visual description, copy, layout, color notes.
   Some (e.g. Person Holding Sign) ask a clarifying quantity question first — answer it as a second
   `--turn`.
4. **1:1 Image Gen Bot** (`1.1-image-gen`) — takes ONE chosen concept and finalizes it into a
   locked, render-ready image-gen prompt (aspect, technical specs, exact copy, layout hierarchy,
   color palette). Don't skip this — it catches formatting a raw concept brief would leave loose.
5. **Render via KIE** — `scripts/run_image.py`, model `nano-banana-2` for anything text-heavy,
   `--aspect 1:1` to match. Translate the Genesis finalizer's structured prompt into one flowing
   description for the image API (it doesn't take markdown headers).
6. **Judge before shipping** — check every word of on-image text against the brief exactly (nano-
   banana-2 duplicates/drops words on long text blocks — re-render with "no duplicated words,
   double-check every word matches exactly" if it happens). Also see the book-cover gotcha below.

## Gotcha: fake book covers
If a concept includes a real product (e.g. "The Instant AI Agency" book) and you don't have the
real cover art wired into the render, nano-banana-2 will invent a plausible-looking FAKE cover —
including a literal "AUTHOR NAME" placeholder string baked into the image once. Fix: explicitly
prompt "a plain, generic hardcover book with a COMPLETELY BLANK cover — no title, no author name,
no text at all" and composite/retrofit the real cover in afterward (Joey's call was to do that
retrofit in ChatGPT separately, not re-render here).

## What good looks like
`creatives/flexxable/2026-08-26-learner-brain-static/note-from-founder-v1.png` — ~180 words of body
copy rendered with zero garbling on the first pass via this chain.
`creatives/flexxable/2026-08-26-visceral-mechanism/concept10-concrete.png` — full Reptile Triggers
Bot chain, clean render, blank-book gotcha caught and fixed before shipping.
