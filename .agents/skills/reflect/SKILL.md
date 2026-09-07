---
name: reflect
description: End-of-session ritual. Reviews what happened this session, finds what is worth promoting into memory per the data dictionary, proposes where each lesson goes (winners, losers, brand, workflows, the client file), files what you approve, and updates today's daily note. Run at the end of any working session so the workspace compounds. This is the executor for the workspace's promote step.
---

# Reflect (end-of-session promote ritual)

The executor for the workspace's compounding step. Without it, lessons stay in your head and the workspace never gets smarter. Takes about two minutes.

## When to run
At the end of any session where you made or judged work. If the operator says "wrap up," "reflect," "what should we save," or is closing out, run this.

## Process
1. Review the session: what did we make, what worked, what flopped, what rule did we learn or correct.
2. Apply the data dictionary (read the-data-dictionary.md if unsure). For each candidate, decide: is this worth promoting, or is it noise. Use the rule of the second time.
3. Propose promotions, one line each, with a destination:
   - a winning hook or ad, with WHY -> winners/
   - a dead angle, with WHY -> losers/
   - a voice rule, especially a corrected one -> brand/voice.md
   - a play run three or more times -> workflows/
   - a client-specific rule that bit -> clients/{name}.md
4. The operator approves or edits the list. Promote only what they approve.
5. File each approved item as YYYY-MM-DD-slug.md (or append to the right existing file). For new durable notes, include a short `Related:` line near the top:
   - winners/ and losers/ usually link to `[[Promotion]]` and `[[Workbench vs Memory]]`
   - brand/voice.md usually links to `[[Memory Loop]]`
   - workflows/ usually links to `[[Promotion]]`
   - client notes usually link to the relevant workflow, swipe, winner, or loser if one exists
6. Update today's daily note (daily/YYYY-MM-DD.md) with a one-line session summary and links to any notes that got promoted. If task-observer logged anything new this session, note the count with a link to skills/observations.md — don't duplicate its content here.
7. **Commit AND push to git.** Every close-out ends with a commit *and* a push (the vault backs up to GitHub, and this is a two-machine setup — a commit that never gets pushed is invisible on the other machine). First do a quick secrets scan (no real keys/tokens in the diff; `.env` and token files must stay gitignored), then `git add -A`, commit to `main` with a short summary of the session, then `git push`. This is a standing instruction — do it every day at close-out, no need to ask. If `git pull` shows divergent branches (both local and remote have new commits — can happen with the laptop), use `git pull --no-rebase` to merge before pushing, not `--force` anything. **If a push hangs past ~60 seconds with no progress past "Writing objects"/"Total X (delta Y)", it's stuck, not slow** — this repo's large binary creatives have triggered a silent HTTP/2 stall before (30+ min hang, no error, no server response). Kill it and retry with `git -c http.version=HTTP/1.1 push` rather than waiting longer.
8. Confirm what was promoted and where, and that the commit **and push** landed — check `git status` shows the branch even with `origin/main`, not just that a commit exists locally.

## Rules
- This step PROMOTES the lesson into memory. The work itself already lives in copy/ or creatives/. Do not re-save the work here.
- Never promote an unproven "admired" example into winners/. Admired goes to swipes/. winners/ is only for things that won.
- Skip anything remember-this already filed this session, so the same rule does not land twice.
- Keep each promoted note short and in the operator's own words. Never invent a result.
- Do not clutter memory-map.md with every new note. It is an entry point, not a running log.
