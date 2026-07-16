#!/usr/bin/env bash
# Snapshot this machine's Claude Code state INTO the repo, ready to commit + push.
# Run this when you FINISH working on a machine (fits your close-out git commit).
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
CLAUDE_DIR="$HOME/.claude"
# Claude Code stores per-project memory under a slug of the repo's absolute path
SLUG="$(printf '%s' "$REPO_ROOT" | sed 's/[/.]/-/g')"
MEM_SRC="$CLAUDE_DIR/projects/$SLUG/memory"

echo "→ Snapshotting Claude Code state into the repo…"

# 1. Memory (source of truth for your rules brain)
if [ -d "$MEM_SRC" ]; then
  rsync -a --delete "$MEM_SRC/" "$SCRIPT_DIR/memory/"
  echo "  ✓ memory"
else
  echo "  ! no memory folder at $MEM_SRC — skipping"
fi

# 2. Global skills — exclude installed deps, nested git, and bulky demo media
#    (heavy sample images/audio/video bundled in third-party skills; not needed)
rsync -a --delete \
  --exclude 'node_modules' --exclude '.git' \
  --exclude '*.jpeg' --exclude '*.jpg' --exclude '*.png' --exclude '*.gif' \
  --exclude '*.mp3' --exclude '*.mp4' --exclude '*.mov' --exclude '*.wav' \
  "$CLAUDE_DIR/skills/" "$SCRIPT_DIR/skills/"
echo "  ✓ skills"

# 3. Settings (plugin flags + permissions — no secrets)
cp -f "$CLAUDE_DIR/settings.json"       "$SCRIPT_DIR/settings/settings.json"       2>/dev/null || true
cp -f "$CLAUDE_DIR/settings.local.json" "$SCRIPT_DIR/settings/settings.local.json" 2>/dev/null || true
echo "  ✓ settings"

echo ""
echo "Done. Now push it up:"
echo "    cd \"$REPO_ROOT\" && git add -A && git commit -m 'sync claude state' && git push"
