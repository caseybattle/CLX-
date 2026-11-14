#!/usr/bin/env bash
# Stop hook: at the end of every turn, commit memory/ and push it, so Casey's
# messages and the agent's checkpoint survive even if this container is reclaimed.
# Only touches memory/. Never pushes to main/master (commits locally there).
set -u
ROOT="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "$0")/../.." && pwd)}"
cd "$ROOT" 2>/dev/null || exit 0
cat >/dev/null 2>&1   # drain hook stdin
git rev-parse --is-inside-work-tree >/dev/null 2>&1 || exit 0
[ -n "$(git status --porcelain -- memory/ 2>/dev/null)" ] || exit 0
git add -- memory/ >/dev/null 2>&1
git commit -q -m "memory: autosave $(date -u '+%Y-%m-%d %H:%M UTC')" -- memory/ >/dev/null 2>&1 || exit 0
branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null)"
case "$branch" in main|master|HEAD|"") exit 0 ;; esac
for delay in 0 2 4 8; do
  sleep "$delay"
  git push -q -u origin "$branch" >/dev/null 2>&1 && exit 0
done
echo "autosave-memory: push failed; memory/ is committed locally" >&2
exit 0
