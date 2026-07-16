---
name: daily-git-commit-on-closeout
description: Always commit to git at end-of-session close-out (the vault backs up to GitHub)
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 522d4dc6-404c-4b2e-b748-bbe2ced6b6cc
---

At every close-out / wrap-up, **commit to git** — do it every day, without being asked. The vault backs up to GitHub.

**Why:** Daily commits are the backup. Joey said "you need to do this everyday when we close out."

**How to apply:** Part of the `reflect` close-out ritual (now step 7). Quick secrets scan first (no real keys/tokens in the diff; `.env` and token files stay gitignored), then `git add -A` and commit to `main` with a short session summary. Direct-to-main is correct for this vault — do not branch.

Related: [[flexxable-output-format]]
