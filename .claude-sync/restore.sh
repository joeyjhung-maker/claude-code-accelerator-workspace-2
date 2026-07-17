#!/usr/bin/env bash
# Restore Claude Code state FROM the repo onto this machine.
# Run this when you START working on the OTHER machine (after `git pull`).
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
CLAUDE_DIR="$HOME/.claude"
SLUG="$(printf '%s' "$REPO_ROOT" | sed 's/[/.]/-/g')"
MEM_DEST="$CLAUDE_DIR/projects/$SLUG/memory"

echo "→ Restoring Claude Code state from repo into ~/.claude…"

# 1. Memory — repo is the source of truth, UNLESS this machine has newer memory.
#    Guardrail: never clobber fresher local rules with a stale snapshot.
mkdir -p "$MEM_DEST"
SKIP_MEM=0
if [ -n "$(ls -A "$MEM_DEST" 2>/dev/null)" ]; then
  newest_live="$(find "$MEM_DEST"      -type f ! -name '.*' -exec stat -f '%m' {} + 2>/dev/null | sort -rn | head -1)"
  newest_snap="$(find "$SCRIPT_DIR/memory" -type f ! -name '.*' -exec stat -f '%m' {} + 2>/dev/null | sort -rn | head -1)"
  if [ -n "$newest_live" ] && [ -n "$newest_snap" ] && [ "$newest_live" -gt "$newest_snap" ]; then
    echo "  ⚠ SKIPPED memory — this machine has NEWER memory than the backup."
    echo "    Nothing was overwritten. Run 'Finish Work' here first to save it,"
    echo "    or open Claude Code and ask if you're unsure."
    SKIP_MEM=1
  fi
fi
if [ "$SKIP_MEM" = "0" ]; then
  rsync -a --delete "$SCRIPT_DIR/memory/" "$MEM_DEST/"
  echo "  ✓ memory → $MEM_DEST"
fi

# 2. Global skills — no --delete, so anything only on this machine is kept
mkdir -p "$CLAUDE_DIR/skills"
rsync -a --exclude 'node_modules' --exclude '.git' \
  "$SCRIPT_DIR/skills/" "$CLAUDE_DIR/skills/"
echo "  ✓ skills → $CLAUDE_DIR/skills"

# 3. Settings
cp -f "$SCRIPT_DIR/settings/settings.json"       "$CLAUDE_DIR/settings.json"       2>/dev/null || true
cp -f "$SCRIPT_DIR/settings/settings.local.json" "$CLAUDE_DIR/settings.local.json" 2>/dev/null || true
echo "  ✓ settings"

echo ""
echo "Done. Your other machine's brain is now on this one."
echo "Note: the 'last30days' skill needs its dependencies installed once before first use."
