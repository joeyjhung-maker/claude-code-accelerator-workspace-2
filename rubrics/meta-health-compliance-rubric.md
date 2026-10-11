# Meta Health Compliance Rubric — the compliance judge's scorecard

*A screen for health and supplement ads running on Meta in the US. It answers two questions and
keeps them apart: will Meta reject this, and could the brand get in legal trouble for it.*

**Status: v1, built 2026-10-09.** Tested once, on Primal Viking AD74. Not yet checked against a
real Meta rejection.

Related: [[copy-rubric]] [[sources]] [[case-file]] [[rejection-log]]

## What this is not
- **Not the copy judge.** It never grades selling power, voice or rhythm. `copy-rubric.md` does.
- **Not a rewrite.** It flags, and offers the smallest swap that keeps the hook. Joey decides.
- **Not legal advice.** A clean report means "no known flags against the sources on file". It
  never means "cleared".
- **Not automatic.** Round 1 spec ads are raw and unflagged. This runs when Joey calls it.

## Files the judge must load first
1. `rubrics/compliance/sources.md` — the rules. Check the "Last full refresh" date. Older than
   45 days: say so in the first line of the report.
2. `rubrics/compliance/claims/{brand}.md` — what proof is on file. No claim sheet: say so, and
   every factual claim is CHECK FIRST at minimum.
3. `rubrics/compliance/rejection-log.md` — what Meta has actually rejected.
4. `rubrics/compliance/case-file.md` — only when a finding needs an example.

Grade from these files. If a rule isn't in `sources.md`, say "not in sources" and mark the
finding CHECK FIRST. Never fill a gap from memory and present it as a rule.

## The two columns
Every finding gets both.

- **META** — will the ad be rejected or the account restricted. Graded against S-M rules.
- **LAW** — FTC and FDA exposure for the brand. Graded against S-F and S-D rules.

They disagree often. A fake testimonial sails through Meta and is the worst legal problem in the
ad. "Do you have X?" is a Meta rejection and legally harmless.

## The four levels
| Level | Meaning |
|---|---|
| **NEVER** | Banned by Meta's written policy or by law. No sign-off fixes it. |
| **RISKY** | Not banned in so many words, but likely to be rejected or to mislead. Off by default. |
| **CHECK FIRST** | Fine once the named proof is on file. Without it, treat as RISKY. |
| **OK** | No flag. |

## Grading conventions
*(Added 2026-10-09 after the first cold run. Each one answers a question the judge had to guess.)*

- **Grade every line in context.** A symptom question is legally harmless alone and an L1
  problem once the ad sells the fix. Grade the line as it sits in this ad. A single line with no
  ad around it (the test set) is graded alone.
- **The level in a row is the worst across the rules cited.**
- **Group repeated or adjacent lines** that break the same rules into one row.
- **CHECK FIRST stays CHECK FIRST** when the proof isn't on file. Print CHECK FIRST and name the
  document. Use RISKY only when the rule itself says RISKY.
- **Plain product description is OK even with no claim sheet.** Ingredients, dose, how to take
  it, price. "Every factual claim is CHECK FIRST" means claims about what the product does, how
  well, for whom, and where it's from.
- **A structure/function line is OK on META and CHECK FIRST on LAW.** The wording is right, the
  proof still has to exist.
- **Who wrote the line.** The judge can't know. It offers a swap on every flagged line and
  changes nothing. Joey applies the provenance rule himself.
- **Rejection log.** A logged rejection moves that pattern up one level for that brand:
  CHECK FIRST to RISKY, RISKY to NEVER.
- **META grades policy, not enforcement.** (Added 2026-10-09 after comparing against Primal
  Viking's live ads.) The META verdict says what Meta's written policy does with the ad. When
  the rejection log shows the same brand running ads that break the same rule, add one line
  under the verdict: "Observed: this account runs worse and it's live." Never lower a level
  because a competitor got away with it, and never apply it to the LAW column.
- **Judgment rules.** Some rules below go further than the source text, because the source is
  thin and the pattern is a known trigger. They are marked *(judgment)*. A finding that rests
  only on a judgment rule can never be higher than RISKY.

---

## META rules

**M1 — Don't tell the viewer about their own body or health.** (S-M2)
- NEVER: a question or statement that says or implies the viewer has a condition, symptom or
  body feature. "Do you…?" + symptom. "Your" + a body part, hormone or condition **described as
  being in a bad state** ("your weak thyroid", "your remaining testosterone"). A symptom
  checklist addressed to "you".
- OK: "your" + a neutral noun that asserts nothing ("your doctor", "your morning", "your plan").
- RISKY: a named body complaint with no "you" at all ("the man boobs", "that gut"). No attribute
  is asserted, but the reader is plainly meant to see himself.
- NEVER: "you" + age + a health or body state together.
- OK: "you / your" with no attribute. A passing age range or gender ("for men 30 to 55").
  Describing the product, the mechanism, or people in the third person ("most men over 40…").
- Test: is the sentence about the product or about the person reading it?

**M2 — No attacks on appearance in a weight or body ad.** (S-M1)
- Applies when the ad sells weight loss, fat loss or a body change.
- NEVER: negative words, descriptions or questions aimed at the viewer's appearance or a body
  part.
- RISKY: the same insulting body terms used about a third person or "men" in general. Meta's
  text is about attacking "an individual's" appearance, so third person is the weaker case, but
  the words themselves are what an automated review sees.

**M3 — The can't-cure list.** (S-M1)
- NEVER: claiming to cure, heal or eliminate Diabetes, Herpes, Thyroid, Psoriasis, Ebola,
  Cancer, Autism, Alzheimer's, Parkinson's, MND or HIV. Applies even when a doctor says it.
- RISKY *(judgment)*: any claim to fix, restore, reverse or repair one of those, short of
  "cure". The source lists only the word "Thyroid", so any claim to mend a weak, sluggish or
  failing thyroid counts.
- Managing symptoms of these is outside this rule (but check L1).
- M2 scope: an ad that promises less belly fat, chest fat or weight counts as a weight ad,
  whatever the product category.

**M4 — No clickbait, no naked timelines.** (S-M1)
- NEVER: a promise to the reader of a specific outcome in a set time frame with no qualifier
  ("lose 20 pounds in 3 weeks").
- RISKY: one person's specific result and time frame, with nothing saying what's typical
  ("Matthew lost 27 pounds in two months"). Meta's text doesn't define "qualifier". Treat it as
  a statement, in the same line, of who got the result and that results vary or what's typical.
- RISKY: sensational or extreme language around a health result.
- OK: reporting how long noticeable results took for a described group, with the qualifier
  ("men in the study saw changes after eight weeks of daily use"), at 18+. Still L2.

**M5 — Imagery.** (S-M1)
- NEVER: close-up of pinched fat.
- CHECK FIRST: before/after for a weight or body-change product. Meta's text allows it for
  general cosmetic products. Third-party reports on weight loss conflict.

**M6 — Targeting.** (S-M1) Supplements and weight products must target 18+. Note it for the
media buyer. Not a copy issue.

**M7 — Drug territory.** (S-M5)
- RISKY: positioning the supplement as a replacement for, or better than, a prescription drug
  or medical treatment.
- CHECK FIRST: unusual ingredients. Meta decides what is an "unsafe supplement" at its own
  discretion.

**M8 — Misinformation.** (S-M4)
- RISKY: factual claims about medicine, nutrition or history that a fact-checker could debunk,
  and claims that doctors or "the medical system" hide something.

**M9 — Commercial practices.** (S-M3)
- CHECK FIRST: price cuts, sale deadlines, guarantees, "risk-free", "free", subscriptions. Each
  must match what the landing page and checkout actually do.
- NEVER: fake urgency, fake stock counts, unauthorised endorsements.

**M10 — Sexual framing.** (S-M1)
- RISKY: selling on sexual performance, pleasure or enhancement. Keep libido lines about health.

**M11 — Everything is the ad.** Captions, on-screen text, thumbnail, voice-over, landing page
and quiz are all reviewed. A clean primary text doesn't clear a dirty video.

---

## LAW rules

**L1 — No disease claims on a supplement.** (S-D1)
- NEVER: saying or implying the product diagnoses, treats, cures, mitigates or prevents a
  disease or medical condition. That includes:
  - naming the condition as the thing the product fixes
  - describing the condition's signs or symptoms, in medical or everyday words, as what the
    product fixes
  - diagnosing the reader ("that's [condition]")
  - positioning the product as a substitute for a drug or therapy
- OK: structure/function wording about normal, healthy function ("supports healthy X levels
  already within the normal range"), with the FDA disclaimer on the label and site.
- The line is the claim, not the vocabulary. Swapping one word while the ad still promises to
  fix a condition changes nothing.

**L2 — Proof before the ad runs.** (S-F1)
- CHECK FIRST: every objective claim, express or implied. Proof must be on the claim sheet as
  SEEN.
- RISKY: ingredient-level or animal science presented as proof the product works.
- RISKY: a number with no source (percentages, "2x", "99% of supplements").
- NEVER: a claim the brand admits it can't support.

**L3 — Net impression.** (S-F1)
- After the line-by-line pass, state in one or two sentences what a reasonable reader would
  believe after the whole ad. That belief is the claim. Grade it under L1 and L2.

**L4 — Testimonials.** (S-F1, S-F2, S-F3)
- NEVER: an invented person, an invented experience, or a reworded quote presented as real.
- NEVER: a testimonial making a claim the brand couldn't make itself. A customer saying it
  doesn't launder it.
- CHECK FIRST: real testimonials with specific results. Needs the original, a release, and a
  clear statement of typical results next to the quote. "Results not typical" doesn't work.
- Numbers in a testimonial (pounds, lab values, days) are efficacy claims. Grade under L2 too.

**L5 — First-person and "my friend" stories.** (S-F3)
- NEVER: a made-up first-person or friend story a viewer would take as a real user's
  experience. An AI avatar telling it makes it worse, not better.
- CHECK FIRST: the same story told by the real person it happened to.
- **Default is NEVER.** A first-person or friend story in copy written by a bot or a copywriter
  is invented unless the claim sheet holds the real person. Print "NEVER unless real".

**L6 — Experts.** (S-F1) NEVER: an invented doctor or a doctor's reaction that didn't happen.
CHECK FIRST: a real, qualified expert who evaluated the product, with any payment disclosed.

**L7 — Establishment claims.** (S-F1) CHECK FIRST: "clinically proven", "lab tested",
"third-party tested", "doctor recommended", "backed by science". Each needs exactly that level
of proof, and "tested" must say for what.

**L8 — Origin.** (S-F4) CHECK FIRST: "Made in USA" and variants. Unqualified needs all or
virtually all of the product, ingredients included.

**L9 — Comparisons and superlatives.** (S-F1) CHECK FIRST: "the only", "best", "2x", "more
than any other", and claims about what competitors' products fail to do.

**L10 — History and tradition.** (S-F1)
- CHECK FIRST: historical facts need a source.
- RISKY: using tradition or history as evidence the product works.
- NEVER: tradition used to imply treating a medical condition.

**L11 — Price, guarantee, urgency.** (S-F4) CHECK FIRST, same items as M9.

**L12 — Steering people away from medical care.** (S-F1)
- RISKY: telling readers doctors are wrong or hiding something, or that they can skip a
  prescribed treatment.

**L13 — Disclaimers don't cure.** (S-F1) A disclaimer never downgrades a finding. Never offer
one as the fix for a NEVER.

---

## How to run it

1. **Load** the four files. Note the refresh date and whether a claim sheet exists.
2. **Number the ad.** One line per sentence, numbered, exactly as written.
3. **Line pass.** Grade every line against M1–M11 and L1–L13. One line can break several rules.
   List them all.
4. **Net impression pass (L3).** Write the belief the whole ad leaves. Grade it.
5. **Not-checked list.** Name what you couldn't see: visuals, video, landing page, quiz,
   targeting, the brand's proof.
6. **Report** in the format below.

## Don't over-flag
A judge that flags everything gets ignored. These are OK and must not be flagged:
- "you / your" with no health or body attribute attached
- an age range or gender as a passing reference
- plain product description: what's in it, how to take it, what it costs
- opinion and puffery that isn't measurable ("blew me away", "the good stuff")
- third-person description of how the body works, when it makes no claim about the product
- a CTA

When a line is OK, leave it out of the findings table. Don't list passes.

## Report format

```
COMPLIANCE CHECK — {ad name} — {date}
Sources refreshed: {date}   Claim sheet: {file or NONE}

META: {LIKELY REJECT | BORDERLINE | LIKELY PASS}   — {one sentence why}
LAW:  {HIGH | MEDIUM | LOW exposure}               — {one sentence why}

FINDINGS (worst first)
| # | Line | Rule | META | LAW | Why | Smallest swap |

NET IMPRESSION
{what the reader believes after the whole ad} → {rules} → {level}

PROOF THAT WOULD UNLOCK CLAIMS
- {claim}: {document needed}

NOT CHECKED
- {list}
```

Rules for the "smallest swap" column:
- Keep the hook's idea. Change the grammar before you change the idea: second person to third,
  diagnosis to description, "fixes" to "supports".
- Never invent proof, a study, a number or a quote to make a swap work.
- If no honest swap exists, write "No swap. Cut, or get the proof."
- A swap is a suggestion. Lines Joey wrote are flagged, never changed.
- Say when a swap only fixes one column. Moving "you" to "men" fixes META and leaves LAW where
  it was.

## Rules that outrun their sources
Be honest about these in a report. A finding under them is the rubric's judgment, not a quoted
rule.

| Rule | Gap |
|---|---|
| M3 RISKY tier, M7 "unusual ingredients", M8 beyond fact-checked content, M9 fake urgency, M10 where health ends and performance begins, M11 | Meta's page is silent or vague. Judgment. |
| L6 invented doctor reactions, L9, L12 | The FTC guidance was only part-read on 2026-10-09. Likely covered, not confirmed. |
| L8, L11 | S-F4 is from general knowledge, not re-read. |
| L1 on low testosterone and gynecomastia specifically | S-D2 was seen in search results, not read in full. The general disease-claim rule (S-D1) was read. |

Closing these gaps is the first job of the next source refresh.

## Living log
Bank every correction here, dated, the way `copy-rubric.md` does.

- *(2026-10-09)* v1 built from Meta's Health and Wellness page (change log 22 Jul 2026), the
  FTC Health Products Compliance Guidance, 16 CFR 465 Q&A, and 21 CFR 101.93.
- *(2026-10-09)* First cold run by a fresh judge. Test set: 0 hard misses, 1 soft miss (friend
  story graded CHECK FIRST, should default to NEVER), 0 false flags. The judge listed ten
  places it had to guess. Added "Grading conventions", narrowed M1's "your" pattern, defined
  M4's qualifier, made L5 default to NEVER, and added the "outrun their sources" table.
  The edited rubric has not been re-run.
