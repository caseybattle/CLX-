# NOW — working memory (survives compaction, /clear and new sessions)

> The agent rewrites this file at every checkpoint. Keep it short (< 60 lines).
> It is automatically re-injected after every compact / clear / resume.

## Current task
Fix context loss: agents forget Casey's messages and in-progress work after compaction / /clear.

## What Casey asked for (key facts, numbers, names, links — verbatim where it matters)
- Messages get compacted right after Enter, so the agent asks questions Casey already answered.
- Mid-task compaction makes the agent forget what it was doing.

## Decisions made (don't re-ask)
-

## Done so far
- Built memory system: memory/INBOX.md (auto-capture hook), memory/NOW.md (re-injected on startup/resume/clear/compact), protocol in CLAUDE.md.

## Next step
- Casey: open `/hooks` once or start a new session so the hooks load, then re-send the task from the other chat.

## Open questions for Casey (only things NOT answered above or in INBOX.md)
-

_Last updated: 2026-11-09_
