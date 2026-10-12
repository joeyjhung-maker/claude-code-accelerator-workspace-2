#!/bin/bash
cd /Users/joey/Documents/claude-code-accelerator-workspace
H=swipes/primal-viking/ads-2026-10-08/hooks
for n in 54 66 70 74; do node .claude/skills/genesis-bots/scripts/genesis-stream.mjs ad-hook-bot-1 $H/prompt-$n.txt $H/bot-$n.md 0.9; sleep 2; done
echo done > $H/hooks.done
