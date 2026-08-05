# Sales Bro / Demo-Not-Sell — static concepts (native)

Ads: "Sales Extinct" (headline: Sales bros going extinct) and "Not Salesperson"
(headline: I hate sales. Still closed 7-figs (copy this)).
Category: native SCRAWLS, cold/warm top-of-funnel text ads. Image = the
variable against the locked copy.

**Proof note:** "7-figure agency" has account precedent
([[flexxable-parsed-hooks-bodies-headlines]] line 222, [[flexxable-winning-ads]]
line 268) — safe to use as a general claim. The **20-30% / 60-80% close-rate
stats** and the **8/12/15-minute timing claims** in these two ad bodies aren't
in any client file I can find — flag before baking any of those specific
numbers into a static as bold on-image text. The mechanism-led concepts below
don't need them; the stat-callout concepts are marked and held for sign-off.

---

## Mechanism-reveal (proof-safe, no disputed numbers)

1. **The reactivation text exchange** ⭐ — iMessage-style screenshot: an AI
   (as the business) texts a lead marked "no response" 6+ months ago, the lead
   replies, a call gets booked. Reuses the proven format from
   `bizopp-static-c1-sms-reactivation-v1.png` (keeper, 2026-07-10) — new
   render swaps the caption to match THIS ad's language: "a dead lead, coming
   back to life." Native, no money claim, ties directly to "Not Salesperson"'s
   body ("leads he'd completely written off... suddenly responding").
2. **Screen-share moment** ⭐ — over-the-shoulder / screen-recording style
   frame: a Zoom call window, one tile is a business owner's reaction (leaning
   in, surprised), the shared screen shows a live SMS thread lighting up.
   Caption-native: "Not a pitch. Just a screen-share." Ties to both ads'
   "just showing, not convincing" mechanism.
3. **Old Plan vs New Plan split** — a literal two-column native graphic
   mirroring the ad's own → bullet structure: left column headed "OLD WAY"
   (a guy on a headset, sweating, stack of objection-handling scripts) vs
   right column "NEW WAY" (a phone screen showing dead leads replying). No
   close-rate numbers on the image itself — let the copy carry those, if
   approved.

## Curiosity / native text-post (no face, no disputed number)

4. **"Sales bros going extinct" native post** ⭐ — plain bold-typography text
   static (Notes-app or native FB text-post chrome): "the sales bro is going
   extinct. he doesn't even know it yet." Direct lift of the ad's own opening
   line — pure curiosity, matches [[hooks]] principle 6 (reads like news/
   confession, not an ad).
5. **"I'm not a salesperson" confession** — Notes-app screenshot style,
   handwritten-feel caption: "I'm not a salesperson. Never have been. I don't
   even like sales calls." Mirrors the "Not Salesperson" ad's own opening
   lines verbatim — voice-matched confession static, no invented claim.

## Stat-callout concepts — HELD, need sign-off on the underlying numbers first

6. **Close-rate comparison card** — bold split-stat graphic: "20-30%" (old
   way) vs "60-80%" (new way). **Do not render until the stats are
   confirmed** — baking an unverified percentage into a permanent image asset
   is a bigger risk than a copy line; it's the first thing a viewer's eye
   locks onto.
7. **"7-figures, zero sales skills" stat card** — bold text: "7-figures in
   AI deals. Zero sales skills." The 7-figure AGENCY claim has account
   precedent; "7-figures in AI deals" specifically as phrased in this ad body
   is close enough to reuse, but flag for a quick confirm since it's a
   slightly different framing (deals vs agency revenue).

---

## Picks to render first (⭐)
1. **#1 reactivation text exchange** — new caption variant, proof-safe.
2. **#2 screen-share moment** — proof-safe, ties both ads' core mechanism.
3. **#4 "sales bro extinct" text post** — pure curiosity, zero risk.

Render order: #1 → #4 → #2 (text-heavy screenshots → `nano-banana-2` per the
banked lesson in kie-render-reference.md; #2's screen-share/reaction frame is
more photo-style, may work on base `nano-banana` — test both if #2 comes back
weak on the base model).

---

## Render log (2026-07-21) — via scripts/run_image.py (nano-banana-2)
- **#1 v1** `salesbro-static-c1-reactivation-v1.png` — **KEEPER.** Clean iMessage
  screenshot, "Mike's Auto Detailing" texts a lapsed lead, she replies and
  books Thursday. Legible, on-brief, pairs directly with the "Not Salesperson"
  ad's "leads he'd completely written off... suddenly responding" line.
- **#4 v1** `salesbro-static-c4-extinct-textpost-v1.png` — **KEEPER.** Bold
  native text-post static, verbatim lift of the "Sales Extinct" ad's own
  opening line. Zero risk, zero invented claim.
- **#2 v1** `salesbro-static-c2-screenshare-v1.png` — **CUT.** Zoom sidebar
  contact list rendered as gibberish text ("Jurinh Allagliner," "Dioneale a
  swirand mq tract heve...") — the known nano-banana text-garbling failure,
  worsened by a busy UI with lots of small text elements. Also drifted off
  the brief (generic team chat, not a dead-lead reactivation thread).
- **#2 v2** `salesbro-static-c2-screenshare-v2.png` — **KEEPER.** Re-rendered
  with the fix: stripped the sidebar/contact-list clutter, full-screen SMS
  thread only, 3 large legible bubbles matching the reactivation narrative,
  surprised business-owner reaction in the webcam tile. Clean text, on-brief.
  **Lesson for next time:** when a text-heavy render includes a busy list UI
  (sidebars, multi-contact panels), simplify the prompt to ONE clean text
  surface — nano-banana-2 still garbles small repeated UI text even on the
  Pro model.

**First sales-bro static test set = #1 + #2v2 + #4**, all proof-safe, ready to
pair with the locked hooks/body.

- **#6 v1** `salesbro-static-c6-closerate-v1.png` — **KEEPER.** Signed off by
  Joey (2026-07-21). Clean split-stat graphic, "OLD WAY 20-30% close rate"
  vs "NEW WAY 60-80% close rate," legible, no garbling.
- **#7 v1** `salesbro-static-c7-7figures-v1.png` — **KEEPER.** Signed off by
  Joey (2026-07-21). "7-figures in AI deals. Zero sales skills." Clean bold
  text-post, matches the "Not Salesperson" ad's own claim.

- **#3 v1** `salesbro-static-c3-oldnewplan-v1.png` — **KEEPER.** Full 5-bullet
  Old Way/New Way comparison, verbatim from the "Sales Extinct" ad body
  (2026-07-21). Stacked-block layout (not side-by-side columns) mirroring
  #6's successful structure, given more vertically for 5 lines/side. Clean
  on the first render — no garbling despite being the most text-dense static
  in this batch.

**Full set = #1, #2v2, #3, #4, #6, #7 — 6 statics, all keepers.**

---

## Round 2 (2026-07-21) — proper bot pipeline, not hand-written prompts

Joey flagged the first batch as "super plain." Switched to the real Genesis
image pipeline instead of me freehand-writing render prompts:
`comparison-bot` (writes 5 comparison-ad concepts) → `1.1-image-gen` (locks
the chosen concept into a render-ready prompt) → `scripts/run_image.py` (KIE
render). This is the same "bot writes, don't self-draft" principle as
mariobot/hookbot, applied to statics.

`comparison-bot` returned 5 concepts for the Old Way/New Way comparison (full
output: `comparison-bot-output.md` in scratch). Picked the 2 strongest for
"premium, not flat typography":

- **#8 v1** `salesbro-static-c8-splitscene-v1.png` — **KEEPER.** 50/50 photo
  split (grainy red-graded "sales bro at whiteboard" vs clean "Zoom demo on
  laptop"), verbatim bullet lists below each photo, both close-rate numbers
  bold and correct. Background scene details (whiteboard scribbles, laptop
  chat bubbles) are illegible/garbled, but that's just texture — the actual
  claims (the 10 bullet lines + 2 close rates) are all crisp.
- **#9 v1** `salesbro-static-c9-papertable-v1.png` — **KEEPER.** Torn-paper
  comparison table on a matte dark background, editorial feel. Every row
  matches the copy verbatim (dropped the quote marks around "Overcome
  resistance" — cosmetic only, meaning unchanged). Close-rate row color-coded
  red vs green, correctly oversized. Book thumbnail is a generic placeholder,
  not the real cover.

Both are a clear step up from round 1's flat text-post style — genuine scene/
concept work instead of plain typography-on-background.

- **#8 v2** `salesbro-static-c8-splitscene-v2-ctabutton.png` — **KEEPER.**
  Reference-guided edit of #8 v1 (`--ref`, nano-banana-edit) — Joey wanted
  the understated footer text turned into an orange CTA button so it stands
  out. Everything else held identical (photos, bullets, close rates,
  layout); only the footer changed to a bold orange rounded-rectangle button
  reading "The Instant AI Agency — $14.40," spanning both halves.

Related: [[bizopp-static-concepts]] [[kie-render-reference]]
