# NOW — working memory (survives compaction, /clear and new sessions)

> The agent rewrites this file at every checkpoint. Keep it short (< 60 lines).
> It is automatically re-injected after every compact / clear / resume.

## Current task
Add a Stop hook that auto-commits + pushes memory/ every turn (so Casey's messages reach GitHub immediately and the 'uncommitted changes' nag stops).

## What Casey asked for (key facts, numbers, names, links — verbatim where it matters)
- Messages get compacted right after Enter, so the agent asks questions Casey already answered.
- Mid-task compaction makes the agent forget what it was doing.

## Decisions made (don't re-ask)
-

## Done so far
- Built memory system: INBOX.md auto-capture hook + NOW.md restore hook + CLAUDE.md protocol. Both hooks verified live (capture on 19:22 msg, restore on 20:13 resume).
- Fixed capture hook logging system notifications as Casey's messages.
- PR #3: GitGuardian green, no reviews, mergeable.

## Next step
- Write .claude/hooks/autosave-memory.sh, wire as Stop hook, test, push.
- Then: Casey merges PR #3; optionally trim unused connectors to reduce compaction.

## Open questions for Casey (only things NOT answered above or in INBOX.md)
-

_Last updated: 2026-11-09_
