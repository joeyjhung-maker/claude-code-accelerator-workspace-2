#!/bin/bash
# ┌─────────────────────────────────────────────────────────────┐
# │  Double-click when you SIT DOWN at this machine.            │
# │  Pulls the other machine's work + restores your Claude brain.│
# └─────────────────────────────────────────────────────────────┘
cd "$(dirname "$0")"

echo "════════════════════════════════════════════"
echo "  START WORK — catching this machine up"
echo "════════════════════════════════════════════"
echo ""

close() { echo ""; echo "Press any key to close this window."; read -n 1 -s; exit "${1:-0}"; }

echo "→ Checking GitHub…"
if ! git fetch origin --quiet; then
  echo "⚠️  Couldn't reach GitHub. Check your internet, then try again."
  close 1
fi

LOCAL="$(git rev-parse @)"
REMOTE="$(git rev-parse origin/main)"
BASE="$(git merge-base @ origin/main)"
DIRTY="$(git status --porcelain)"

if [ "$LOCAL" = "$REMOTE" ]; then
  echo "→ Already up to date with GitHub."
elif [ "$BASE" = "$REMOTE" ]; then
  # This machine is AHEAD — it has commits never pushed (last Finish didn't run).
  echo "→ Note: this machine has work that was never pushed to GitHub."
  echo "  Nothing to pull. Remember to run 'Finish Work' when you're done."
elif [ "$BASE" = "$LOCAL" ]; then
  # This machine is BEHIND — GitHub has newer work.
  if [ -n "$DIRTY" ]; then
    echo "⚠️  STOP — this machine has unsaved changes AND GitHub has newer work."
    echo "    Pulling now could clash. Run 'Finish Work' here first to save,"
    echo "    or open Claude Code and say: \"help me sync, I have a conflict\"."
    close 1
  fi
  echo "→ Pulling the other machine's work…"
  if ! git pull --ff-only origin main; then
    echo "⚠️  Couldn't pull cleanly. Open Claude Code and ask for help before working."
    close 1
  fi
else
  # DIVERGED — both sides have unique commits.
  echo "⚠️  STOP — both machines have unsynced changes."
  echo "    This machine AND GitHub each have work the other doesn't have."
  echo "    Do NOT continue. Open Claude Code and say:"
  echo "    \"my repo has diverged, help me merge safely\""
  close 1
fi

echo ""
echo "→ Restoring memory + skills + settings…"
bash .claude-sync/restore.sh

echo ""
echo "✅ READY — this machine now matches GitHub. Go to work."
close 0
