---
name: always-use-mariobot-to-write
description: Always draft copy with mariobot (Genesis) first, not Claude directly — the rubric judges mariobot's draft, not mine
metadata:
  type: feedback
  originSessionId: unknown
---

Mariobot is the writer, I am not. For any hooks/body/headlines/emails (Flexxable or JV), call mariobot via the Genesis 2-step protocol (prime with the relevant winning-ads/voice primer, then instruct) to produce the first draft. Only after mariobot has written it do I run the rubric judge pass — see [[run-judge-before-showing-copy]] — and show Joey the clean version.

**Why:** Joey caught me writing a JV email directly instead of using the two-brain trick. The established pipeline is mariobot (writer) → copy-rubric (judge) → Joey (final review). Skipping mariobot defeats the point of having a trained writer bot — the rubric was built to grade mariobot's floor, not my own draft.

**How to apply:** Before producing any piece of client-facing copy, check whether a Genesis writer bot fits (mariobot for body/email, ad-hook-bot-1 for hooks, swiping-master-bot for swipes, etc. — see the roster in `.claude/skills/creative-strategy-system/knowledge/genesis-exodus-keys.md`). Use it first.

**HARD RULE (Joey, 2026-07-06): mariobot writes or NO ONE writes.** If mariobot is unreachable — no key, blank key, endpoint down, whatever — STOP and come to Joey to fix the situation. Do NOT draft the copy myself as a fallback. The only exception is Joey explicitly asking for something fast-and-loose. (This overrides my earlier "draft directly if no Genesis key is present" note — Joey killed that fallback after I used it to write an IAA book ad myself when `clients/.env` had blank keys.)

**Known failure mode:** the mariobot route lives at `gas.copycoders.ai/api/v1`, keys in gitignored `clients/.env` (`GENESIS_API_KEY` + `ANTHROPIC_API_KEY` as X-Provider-Key). If those values are blank, mariobot can't be called — escalate to Joey for the keys, don't work around it.

Related: [[run-judge-before-showing-copy]]
