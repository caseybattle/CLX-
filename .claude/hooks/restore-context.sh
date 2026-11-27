#!/usr/bin/env bash
# SessionStart hook (startup | resume | clear | compact): print the saved working
# memory so it is injected back into the agent's context automatically.
set -u
ROOT="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "$0")/../.." && pwd)}"
NOW="$ROOT/memory/NOW.md"
INBOX="$ROOT/memory/INBOX.md"
src="$(cat 2>/dev/null | jq -r '.source // "startup"' 2>/dev/null)"
echo "=== RESTORED WORKING MEMORY (session event: ${src:-startup}) ==="
echo "Context may have been compacted or cleared. Do NOT ask Casey to repeat anything"
echo "that is written below — read it, then continue the task from 'Next step'."
echo
if [ -f "$NOW" ]; then echo "----- memory/NOW.md -----"; cat "$NOW"; echo; fi
if [ -f "$INBOX" ]; then
  echo "----- last 6 messages from Casey (memory/INBOX.md; open the file for older) -----"
  awk 'BEGIN{RS="\n---\n"} NR>1{a[NR]=$0} END{s=NR-5; if(s<2)s=2; for(i=s;i<=NR;i++) if(i in a) print "---\n" a[i]}' "$INBOX" | tail -c 12000
fi
echo "=== END RESTORED MEMORY ==="
exit 0
