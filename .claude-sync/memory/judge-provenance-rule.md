---
name: judge-provenance-rule
description: "When grading/editing copy, grade AI's lines hard but only flag the user's own lines"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 522d4dc6-404c-4b2e-b748-bbe2ced6b6cc
---

When reviewing or grading copy, behave by **provenance**: auto-fix AI-WRITTEN copy hard against the rubric, but anything the user wrote himself — do NOT "correct" it. At most FLAG it and let him decide.

**Why:** His lines are his call. The judge polices the machine's output, not his. He pushed back specifically on being told to remove his own dashes and his own "In short:".

**How to apply:** On a review, separate "this is AI's draft" (fix it) from "the user wrote this" (flag, offer, let him choose). Example: AI dashes get removed; his dashes stay untouched and unflagged.

Related: [[genesis-no-judge-bot]]
