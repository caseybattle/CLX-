# CLX — Casey's revenue HQ

This repo is the home base for Casey's Chief Revenue Officer (CRO) agent.

- CRO identity, mentality and routing: `.claude/agents/cro.md`
- Strategy and rules: `cro/OPERATING-SYSTEM.md`
- Live numbers and active projects: `cro/SCORECARD.md`
- Decision log: `cro/DECISIONS.md`
- Every project across all chats: `cro/PROJECTS.md` (kept current by the `chief-of-staff` agent)
- Commands: `/cro-daily`, `/cro-weekly`, `/chats-sync`

For any question about revenue, priorities, projects, pricing or "what should I work on",
take the `cro` role (or delegate to the `cro` agent) and follow its output format.
Never invent numbers. Draft outbound actions and wait for Casey's approval before sending.

## Memory protocol — survive compaction and /clear (MANDATORY, every agent)

Chats here compact or clear often. Anything only in chat history will be lost.
Two files in `memory/` are the durable brain, and hooks in `.claude/settings.json` wire them in:

- `memory/INBOX.md`: **auto-captured**. Every message Casey sends is appended by a
  `UserPromptSubmit` hook *before* you see it. Never ask Casey to repeat something that's in here.
- `memory/NOW.md`: **you maintain it.** Current task, key facts, decisions, done, next step.
  It is re-injected automatically by a `SessionStart` hook after every startup / resume / clear / compact.

Rules:
1. **Write first, work second.** On any substantive request, update `memory/NOW.md`
   (task + key facts verbatim) *before* doing the work.
2. **Checkpoint as you go.** After each meaningful step (file written, research found,
   decision made) update "Done so far" and "Next step". Rule of thumb: never go more than
   ~3 tool calls of real work without a checkpoint.
3. **After a compact/clear, resume.** Don't restart. Read the restored memory (and the
   full `memory/INBOX.md` if needed) and continue from "Next step". Only ask Casey about
   things that truly aren't written down.
4. **Put big outputs in files, not chat.** Drafts, research and plans go in a file
   and get linked from NOW.md, so a compaction can't erase them.
5. **Persist across sessions.** Cloud containers are temporary. A `Stop` hook
   (`.claude/hooks/autosave-memory.sh`) auto-commits and pushes `memory/` after every turn.
   You still commit and push other work files yourself at the end of a work block.
6. When a task finishes, move its summary to the relevant `cro/` file or `cro/DECISIONS.md`
   and reset NOW.md's "Current task".
