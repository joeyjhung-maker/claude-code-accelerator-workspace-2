#!/bin/bash
cd /Users/joey/Documents/claude-code-accelerator-workspace
G=swipes/primal-viking/ads-2026-10-08/genesis
while pgrep -f "75-ads-69-75.md" >/dev/null; do sleep 10; done
for n in 1 2 3 4 5 6; do
  node .claude/skills/genesis-bots/scripts/genesis-stream.mjs ad-tagging-bot- $G/tag-in-$n.txt $G/tags-$n.md
  sleep 2
done
echo ALLTAGSDONE > $G/tags.done
