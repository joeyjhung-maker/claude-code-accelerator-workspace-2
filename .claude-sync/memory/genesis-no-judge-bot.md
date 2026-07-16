---
name: genesis-no-judge-bot
description: The Genesis server has no judge/editor bot; the editor half is a local rubric
metadata: 
  node_type: memory
  type: reference
  originSessionId: 522d4dc6-404c-4b2e-b748-bbe2ced6b6cc
---

The Genesis server roster is writers + analysts only (`mariobot`, `ad-hook-bot-1`, `swiping-master-bot`, analysis bots) — there is **no judge / editor / grader / critic bot**. Mario's "MarioJudge" from the Standards Ladder doc is his own local grading skill, not a server product.

So the editor half of the two-brain trick is built locally: `rubrics/copy-rubric.md` (the judge's scorecard). Verify against the live roster (`GET $GENESIS_BASE_URL/models`) if a Genesis key is ever added. No `.env` / Genesis key present as of 2026-06-10 — local bots only.

Related: [[judge-provenance-rule]]
