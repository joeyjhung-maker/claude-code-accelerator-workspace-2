---
name: daily-git-commit-on-closeout
description: Always commit AND push to git at close-out, and pull at session start (two-machine setup: desktop + laptop)
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 522d4dc6-404c-4b2e-b748-bbe2ced6b6cc
  modified: 2026-08-28T18:51:40.041Z
---

At every close-out / wrap-up, **commit AND push to git** — do it every day, without being asked. At the **start** of every session, **pull first**, before doing anything else. The vault backs up to GitHub, and this is a two-machine setup (desktop + laptop), so a commit that's never pushed is invisible on the other machine.

**Why:** Daily commits are the backup. Joey said "you need to do this everyday when we close out." Originally this rule only covered commit — on 2026-08-28, checking the repo found **6 commits sitting locally, never pushed**, meaning a laptop `git pull` at that point would have silently missed a week+ of work with no error. The rule was tightened the same day to close that gap, and a matching pull-at-session-start rule was added since committing alone doesn't help if the other machine never fetches it either.

**How to apply:** Part of the `reflect` close-out ritual (step 7, now explicitly commit + push) and the Script's "How I work" list (start-of-session pull, added 2026-08-28). Quick secrets scan first (no real keys/tokens in the diff; `.env` and token files stay gitignored), then `git add -A`, commit to `main` with a short session summary, then `git push`. Direct-to-main is correct for this vault — do not branch. Large binary creative files can make the push slow — run it in the background rather than letting a short timeout kill it mid-transfer, and confirm `git status` shows the branch even with `origin/main` before calling it done, not just that a local commit exists.

Related: [[flexxable-output-format]]
