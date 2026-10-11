---
name: compliance-check
description: Run a Meta + FTC/FDA compliance check on a health or supplement ad. Use when Joey says "compliance check", "run compliance", "is this compliant", "will Meta reject this", "check this ad against the rules", or "/compliance-check". Grades the ad line by line against rubrics/meta-health-compliance-rubric.md and returns a findings table with two columns (Meta rejection risk, legal exposure) and the smallest swap for each flag. On-demand only — never run it on a round-1 spec ad unless asked. It flags, it does not rewrite. Health and supplements only for now; not for coaching or income-claim ads.
---

# /compliance-check — will Meta reject it, and could the brand get in trouble

A screen, not a lawyer. A clean report means no known flags against the sources on file.

## When to run
Only when Joey asks. Round 1 spec ads are raw and unflagged on purpose. This is the round 2 pass.

## The run

### 1. Find the ad and the brand
Joey names a file or pastes the ad. Work out the brand. Look for
`rubrics/compliance/claims/{brand}.md`.

No claim sheet: tell Joey in one line, then carry on. Every factual claim will be CHECK FIRST at
minimum. Offer to build the sheet from the brand's ads and pages afterwards.

### 2. Check the sources are fresh
Read the "Last full refresh" date in `rubrics/compliance/sources.md`. Older than 45 days: say so
before anything else and offer to refresh. Meta's policy pages need a real browser; a plain
fetch returns only the page title.

### 3. Hand the ad to a fresh judge
The judge must not be the session that wrote the ad. Spawn one subagent and give it:
- the ad, exactly as written
- a description of any visuals, video or landing page Joey supplied
- these paths to read: `rubrics/meta-health-compliance-rubric.md`,
  `rubrics/compliance/sources.md`, `rubrics/compliance/rejection-log.md`,
  `rubrics/compliance/case-file.md`, and the claim sheet
- the instruction: follow "How to run it" in the rubric and return the report in the rubric's
  format, nothing else

Do not give it `rubrics/compliance/test-set-key.md`.

### 4. Check the judge's work before Joey sees it
- Every finding cites a rule ID that exists in the rubric.
- No finding rests on a rule that isn't in `sources.md`. If one does, mark it CHECK FIRST and
  say "not in sources".
- No swap invents proof, a number or a quote.
- The NOT CHECKED list is present.

### 5. Show the report, then stop
Show the report as it came back. Do not apply the swaps. Joey picks which flags to act on.
If he wants a compliant version written, that goes through mariobot and the copy rubric like any
other rewrite, with the accepted swaps as constraints.

### 6. Save it
Save the report next to the ad as `{ad-name}-COMPLIANCE.md`.

## After a real Meta decision
Any rejection, restriction or surprise approval gets logged in
`rubrics/compliance/rejection-log.md`. That log outranks the policy text.

## Rules
- Two columns, always. Never merge Meta risk and legal risk into one score.
- A disclaimer is never offered as the fix for a NEVER.
- Lines Joey wrote are flagged, never changed.
- Never say "compliant", "cleared" or "safe to run". Say "no known flags".
- After changing the rubric, re-run `rubrics/compliance/test-set.md` and log the result in the
  key file.
