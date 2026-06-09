#!/bin/bash

# Daily workspace backup to GitHub
# Runs at 5pm UK time via LaunchAgent

WORKSPACE="/Users/joey/Documents/claude-code-accelerator-workspace"
LOG="$WORKSPACE/scripts/daily-backup.log"
TOKEN_FILE="$WORKSPACE/scripts/.gh-token"

cd "$WORKSPACE" || exit 1

# Read token from file
if [ ! -f "$TOKEN_FILE" ]; then
  echo "$(date '+%Y-%m-%d %H:%M') — ERROR: token file not found at $TOKEN_FILE" >> "$LOG"
  exit 1
fi
TOKEN=$(cat "$TOKEN_FILE" | tr -d '[:space:]')
REMOTE="https://joeyjhung-maker:${TOKEN}@github.com/joeyjhung-maker/claude-code-accelerator-workspace-2.git"

# Check if there's anything to commit
if git diff --quiet && git diff --cached --quiet && [ -z "$(git ls-files --others --exclude-standard)" ]; then
  echo "$(date '+%Y-%m-%d %H:%M') — No changes to commit." >> "$LOG"
  exit 0
fi

# Stage everything
git add -A

# Commit with date stamp
git commit -m "Daily backup — $(date '+%Y-%m-%d %H:%M')"

# Push using token
git remote set-url origin "$REMOTE"
git push origin main
git remote set-url origin "https://github.com/joeyjhung-maker/claude-code-accelerator-workspace-2.git"

echo "$(date '+%Y-%m-%d %H:%M') — Backup complete." >> "$LOG"
