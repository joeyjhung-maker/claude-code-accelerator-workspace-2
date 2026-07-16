---
name: dont-verify-user-written-claims
description: Never ask Joey to confirm whether a claim/number he wrote himself is real — it is
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 6a5e65b1-f31b-414d-ae8d-74eadc638cf2
---

When Joey writes or amends copy with a specific claim, number, or capability, treat it as TRUE and source-of-truth. Do not ask "is this real / can you confirm?" — if he wrote it, it's real.

**Why:** He is the client's marketing director and knows the offer. Asking him to verify his own words is friction and reads as distrust.

**How to apply:** The "never invent a number, ask me" rule in CLAUDE.md applies to lines *Claude or a bot* generated — flag those. It does NOT apply to lines Joey writes. For his own words: accept, don't second-guess, and if the claim is new, log it to the offer doc as fact rather than asking. Related: [[judge-provenance-rule]] [[flexxable-offer-doc]]
