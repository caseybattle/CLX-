#!/usr/bin/env bash
# UserPromptSubmit hook: save every message Casey sends to memory/INBOX.md
# BEFORE the model sees it, so nothing is lost if the chat compacts or clears.
set -u
ROOT="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "$0")/../.." && pwd)}"
INBOX="$ROOT/memory/INBOX.md"
mkdir -p "$ROOT/memory"
[ -f "$INBOX" ] || printf '# Inbox — every message Casey sent (auto-captured, newest at bottom)\n' > "$INBOX"
payload="$(cat)"
prompt="$(printf '%s' "$payload" | jq -r '.prompt // empty' 2>/dev/null)"
sid="$(printf '%s' "$payload" | jq -r '.session_id // "?"' 2>/dev/null)"
# Skip empty prompts and bare slash commands like /clear
trimmed="$(printf '%s' "$prompt" | tr -d '[:space:]')"
if [ -z "$trimmed" ] || printf '%s' "$prompt" | grep -Eq '^/[A-Za-z:_-]+[[:space:]]*$'; then exit 0; fi
# Skip automated, non-Casey turns: system/task notifications, PR wake events, hook feedback
first="$(printf '%s' "$prompt" | sed -n '/[^[:space:]]/{p;q;}' | sed 's/^[[:space:]]*//')"
case "$first" in
  "<"*|"Stop hook feedback"*|"[SYSTEM NOTIFICATION"*) exit 0 ;;
esac
{
  printf '\n---\n### %s · session %s\n\n' "$(date -u '+%Y-%m-%d %H:%M UTC')" "${sid:0:8}"
  printf '%s\n' "$prompt"
} >> "$INBOX"
# Commit right away (so nothing is left uncommitted at turn end) and push in the
# background. Never pushes main/master. Failures are harmless: the Stop hook retries.
(
  cd "$ROOT" || exit 0
  git rev-parse --is-inside-work-tree >/dev/null 2>&1 || exit 0
  git add -- memory/INBOX.md && git commit -q -m "memory: capture message $(date -u '+%Y-%m-%d %H:%M UTC')" -- memory/INBOX.md || exit 0
  b="$(git rev-parse --abbrev-ref HEAD)"
  case "$b" in main|master|HEAD|"") exit 0 ;; esac
  git push -q -u origin "$b"
) >/dev/null 2>&1 &
exit 0
