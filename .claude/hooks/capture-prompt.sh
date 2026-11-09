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
exit 0
