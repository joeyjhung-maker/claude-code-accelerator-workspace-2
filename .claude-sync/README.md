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
Think of it like closing and opening a laptop lid. **Two double-clicks, no typing:**

- **Sit down at a machine →** double-click **`Start Work.command`** (in the repo root).
  Pulls the other machine's work and restores your memory + skills. Refuses to
  continue if both machines have unsynced changes (instead of breaking things).
- **Get up from a machine →** double-click **`Finish Work.command`**.
  Snapshots memory + skills, commits, and pushes to GitHub. Waits for the slow
  push to finish, then prints **"DONE — safe to switch machines."**

That's the whole routine. Always Finish where you stop, Start where you sit down.
Last machine to sync wins, so don't work both at once without finishing between.

### Under the hood (what the commands run — for reference)
- `Finish Work.command` → `.claude-sync/sync.sh` + commit + `git push`
- `Start Work.command`  → `git pull --ff-only` + `.claude-sync/restore.sh`

You can still run those by hand if you ever want to. `restore.sh` will **skip**
restoring memory if this machine's memory is newer than the backup, so it can
never overwrite fresher rules.

## First-time laptop setup
1. Install Claude Code + log in (see the workspace's setup notes).
2. `git clone` this repo to the **same path** you use on your main Mac.
3. `bash .claude-sync/restore.sh`
4. Open Claude Code in the folder — it's now identical to your main machine.
