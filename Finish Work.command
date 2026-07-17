#!/bin/bash
# ┌─────────────────────────────────────────────────────────────┐
# │  Double-click when you GET UP from this machine.           │
# │  Saves your Claude brain + pushes everything to GitHub.     │
# └─────────────────────────────────────────────────────────────┘
cd "$(dirname "$0")"

echo "════════════════════════════════════════════"
echo "  FINISH WORK — saving everything to GitHub"
echo "════════════════════════════════════════════"
echo ""

close() { echo ""; echo "Press any key to close this window."; read -n 1 -s; exit "${1:-0}"; }

# 1. Snapshot memory + skills + settings into the repo
echo "→ Snapshotting memory + skills…"
bash .claude-sync/sync.sh >/dev/null
echo "  ✓ snapshot done"

# 2. Commit your work locally FIRST, so it's saved no matter what happens next
if [ -n "$(git status --porcelain)" ]; then
  git add -A
  git commit -m "Work session — $(date '+%Y-%m-%d %H:%M')" --quiet
  echo "→ Committed your work."
else
  echo "→ Nothing new to commit."
fi

# 3. See where GitHub stands
echo "→ Checking GitHub…"
if ! git fetch origin --quiet; then
  echo "⚠️  Couldn't reach GitHub. Your work is committed safely on THIS machine."
  echo "    Try 'Finish Work' again once you're back online, before switching machines."
  close 1
fi
LOCAL="$(git rev-parse @)"
REMOTE="$(git rev-parse origin/main)"
BASE="$(git merge-base @ origin/main)"

if [ "$LOCAL" = "$REMOTE" ]; then
  echo ""
  echo "✅ DONE — already in sync. Safe to switch machines."
  close 0
elif [ "$BASE" = "$REMOTE" ]; then
  : # normal case: we're ahead, push below
elif [ "$BASE" = "$LOCAL" ]; then
  echo "→ GitHub had newer work — pulling it in first…"
  if ! git pull --ff-only origin main; then
    echo "⚠️  Couldn't merge cleanly. Your work is committed on THIS machine."
    echo "    Open Claude Code and ask for help before switching."
    close 1
  fi
else
  echo "⚠️  Both machines changed since the last sync (diverged)."
  echo "    Your work is committed safely on THIS machine — nothing lost."
  echo "    Open Claude Code and say: \"my repo diverged, help me merge and push\"."
  close 1
fi

# 4. Push — caffeinate keeps the Mac awake so the slow push actually finishes
echo "→ Pushing to GitHub (can take a minute on a slow connection — please wait)…"
if caffeinate -i git push origin main; then
  echo ""
  echo "✅ DONE — safe to switch machines."
else
  echo ""
  echo "⚠️  Push didn't finish. Your work IS committed on this machine (not lost)."
  echo "    Stay here, wait a moment, and run 'Finish Work' again."
  echo "    Do NOT start the other machine until this says DONE."
  close 1
fi
close 0
