# .claude-sync — your Claude Code brain, backed up to GitHub

This folder makes two machines work as if they're the same setup. It snapshots the
parts of Claude Code that live *outside* this repo (in `~/.claude/`) into the repo,
so they ride along on GitHub with everything else.

## What's in here
- `memory/` — your rules brain (the auto-memory Claude reads every session)
- `skills/` — your global marketing skills (hook-miner, mechanism-finder, ads-analyst…)
- `settings/` — plugin flags + permissions

## What is NOT backed up (on purpose)
- Credentials / login — these live in your Mac's Keychain, never in a file. You just
  log in once per machine with `claude`.
- Past conversation transcripts, caches, session state — machine-specific and bulky.
- Plugins (diversity-decoder, playwright) — re-install these on the laptop.
- Installed skill dependencies (`node_modules`) — reinstalled on first use.

## The routine (the important bit)
Think of it like closing and opening a laptop lid.

**When you FINISH on a machine:**
```
bash .claude-sync/sync.sh
git add -A && git commit -m "sync claude state" && git push
```
(Your normal close-out commit already does the last line.)

**When you START on the other machine:**
```
git pull
bash .claude-sync/restore.sh
```

That's it. Always sync+push where you finish, pull+restore where you start.
Last machine to sync wins, so don't work on both at once without syncing between.

## First-time laptop setup
1. Install Claude Code + log in (see the workspace's setup notes).
2. `git clone` this repo to the **same path** you use on your main Mac.
3. `bash .claude-sync/restore.sh`
4. Open Claude Code in the folder — it's now identical to your main machine.
