---
name: run-judge-before-showing-copy
description: Always run the copy-rubric judge pass before showing Joey any copy
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2fc0526e-8c59-4bf6-be56-5cc3f5bf1ca7
---

Before showing Joey ANY copy I wrote, run the judge pass against the copy-rubric first. Draft (the floor), then grade each line PASS/FAIL against [[copy-rubric]], rewrite the AI-written fails, and only show the clean version. Call out anything I'm flagging-not-fixing.

**Why:** The two-brain trick only works if the editor grades before Joey reads. I was skipping it and showing raw drafts — Joey ended up doing the editor's job (e.g. catching a stacked triplet I should never have shown). Default chosen 2026-06-30: option 1, judge every time.

**How to apply:** Applies to all copy I generate, Hulk campaign and beyond. Honor the [[judge-provenance-rule]] / [[dont-verify-user-written-claims]] — grade the machine's lines hard, only FLAG Joey's own. Fast-and-loose throwaways are the only exception, and only when Joey says so.

The draft this judges should come from mariobot, not from me writing directly — see [[always-use-mariobot-to-write]]. Full pipeline: mariobot writes → this rubric judges → Joey reviews.
