# Project Registry (all chats)

Maintained by the `chief-of-staff` agent via `/chats-sync`. Built from Claude Code
session titles, statuses and their latest summaries. Full transcripts of chats
started from your computer (Remote Control) can only be read from a trusted device,
so details below come from each chat's latest summary only.

Last synced: 2026-11-11 07:30 ET (morning brief)

## Waiting on Casey (blocked)

| Project | Chat | Last updated | What it needs from you | Revenue link |
|---------|------|--------------|------------------------|--------------|
| Agent Indexed (Casey's own directory, agentindexed.com) | Chief revenue officer setup (CLX) | 2026-11-11 | **Decided 11-11: site stays on ChatGPT Sites (no extra hosting spend).** Next step: paste cro/prompts/agentindexed-chatgpt-email-capture.md into ChatGPT to add email capture to the live site. Stripe bank re-linked (Chase ••5628); webhook we_1UVC2g… enabled, points to agentindexed.com/api/stripe-webhook. 0 sales so far. $49 upgrade outreach to past submitters is ON HOLD until Casey says go. New free submission 11-11: SendHQ (Basic). Email-capture code merged in caseybattle/agentindexed (Vercel copy, not on the domain) | Direct: Featured/Sponsor tiers via Stripe |
| BattleLabs Prompts (prompt library site) | BattleLabs Prompts domain launch | 2026-10-11 | **Casey hasn't decided.** ~1h from taking money: add 8 env vars in Vercel (Production + Preview) with Stripe keys/prices + merge PR #2 in caseybattle/promptlibrary. Related: Vercel email 11-10 says promptbattle.site nameservers still point to another provider | **Direct**: paid product, Stripe checkout |
| Bash Kings app game | Bash kings app game | 2026-11-10 | Casey approved **push small-ramps to main**, but the relay to that desktop chat was blocked. Casey must type it in that chat himself (chat still shows it waiting). Still: forward Google's Japan payments invite when it arrives (deadline Dec 1) | Direct: in-app payments |
| Custom TV OS | Custom TV OS design | 2026-10-23 | Enable ADB + unknown sources on Fire TV, send its IP | None found |
| Trading strategy | Cloud chat history access (archived) | 2026-10-05 | Market, account size, platform, trading style | Unclear |
| Vercel account limits | (Gmail alert, not a chat) | 2026-10-31 | Free tier at 100% of 10 GB deployment storage; 2 domains misconfigured on 1 project | Supporting: sites could go down |
| YouTube channel ideas (Episode 1 in production) | Viral YouTube channel ideas (archived Nov 10) | 2026-11-09 | Chat was archived while paused on "Stopping here until your next message." Unarchive and send the next instruction, or drop it | Supporting: content/lead engine |
| KDP (new chat, Nov 2) | kdp | 2026-11-11 | Chat moved again 11-11 07:10 ET and is now "ready for review" (earlier failure was an expired login on Casey's computer). No summary; details only on trusted device. Open it and review | Direct: royalties |
| KDP word-search pilot | kdp (old chat, now archived) | 2026-11-02 | Spec saved to SPEC-WORDSEARCH.md, no pages built. Pick a new village setting for a 3-case pilot, or keep Hotel Larkspur. Scene book PDF (96 pages) was built earlier | Direct: royalties |
| Word Pop promo video | Video transcript to AI agent instructions | 2026-11-11 | Latest: "v11 rendered and sent; frames checked, not watched end to end or audio-checked." Watch v11 with sound and approve or send fixes | Supporting: Word Pop ads |
| AI micro drama series | I want to make a vertical AI micro drama series | 2026-11-11 | Latest: "Built v7 via build_v7.py with corrected start frames for both story fixes and the end line cut; two minor defects left for the tester." Review v7 | Unclear |
| CLX memory system | Chief revenue officer setup | 2026-11-09 | Draft PR #3 caseybattle/CLX- (hooks for memory/INBOX.md + NOW.md). Mark ready + merge PR #3 | Supporting: CRO infra |
| Overseer automation | Super agent monitoring setup (archived Nov 10) | 2026-11-08 | overseer-daily is **not** in the cloud scheduled-task list (likely a Cowork desktop task, not visible from here). Confirm it is still running | Supporting |
| Reel analysis | Email information | 2026-10-05 | Run the provided prompt in Gemini with the reel, paste result back | Content |

## In review / waiting on a platform

| Project | Chat | Status (from summary) | Revenue link |
|---------|------|-----------------------|--------------|
| Word Pop (Android game) | Android game for Google Play Store (archived) | Last chat summary: in Google Play review; AdMob linking + ad test after it's live. 11-11 a third-party email (ExtensionLaunch) congratulates Casey on "releasing Word Pop: Word Search Puzzle", so it may be live. Not confirmed in Play Console | Direct: ads |
| Ad videos (Instagram/Facebook) | Video transcript to AI agent instructions | D-snowy-brain-teaser.mp4 and E-emergency-rush.mp4 in "08 Ad Videos" (9:16, 13.5s). 4:5 Facebook versions not made | Supporting: ads (product unclear, likely Word Pop) |
| KDP book (earlier) | kdp | Earlier book in KDP review; edits locked until live | Direct: royalties |
| Word Pop social kit | Claude Mods guide (earlier) | 34-image social kit in Google Drive (Word Pop > promo > social) with captions + posting plan | Marketing for Word Pop |

## Done / ready to review

| Project | Chat | Result |
|---------|------|--------|
| Honkle: Bus Jam Word Puzzle (Google Play) | (Casey, 2026-11-10) | **Live in production on Google Play** (Casey confirmed) |
| Stripe setup guide | Stripe account setup instructions | PR #4 merged 2026-11-10 (stripe-setup-guide/ in CLX-); PDF ready to send |
| Stripe payouts bank | Chief revenue officer setup | Bank re-linked 2026-11-11 (Chase ••5628, replaced deactivated tokenized ••6198) |
| Cinematic promo videos, 3 games | Cinematic promo videos, 3 games (archived Nov 10) | Pushed ec1c257 to main; a compose.mjs BRAND change is left uncommitted |
| Live activity dashboard | Live activity dashboard (archived Nov 10) | Artifact v5 published; Games panel marks handles confirmed from Blotato |
| Blip sample video | Video transcript to AI agent instructions | blip-sample-v4.mp4 (15.8s) sent; beat 4 and ending unchecked |
| Roofer plan / Claude mods | Claude Mods guide | Latest turn explained the 7 installed mods. Roofer plan status unclear |
| Fire TV launcher | FireTV Launcher Package | Installed; 27 ad/tracking packages disabled. To do: back up the signing key, turn off ADB debugging |
| Prompt library push | BattleLabs Prompts GitHub push | Pushed to caseybattle/promptlibrary main |
| Prompt library site | Prompt library site launch | Ready for review |
| Business review ideas | Business review ideas | Ready for review (archived) |
| Workout app | Workout app project location | Ready for review |
| CRO setup | Chief revenue officer setup | This repo |

## Failed / stale (candidates to archive)

| Chat | Status | Note |
|------|--------|------|
| ChatGPT plugin brainstorm | Failed (archived) | Last turn errored on 2026-10-06 |
| Code review and execution | Failed | Last turn errored on 2026-08-25 |
| CLAUDE.md documentation (×3) | Pending / waiting on approval since Jun–Jul 2026 | Never finished |
| Tradingview/OANDA, Oanda Trading, Repository checkout | Blocked since Jul 2026 | Waiting on Casey; no activity since July |
| Agentindexed daily check (×20+) | Archived | Daily scheduled runs, Jul–Aug; stopped after 2026-08-29 |

## Not visible from here

Regular claude.ai chats (outside Claude Code), Cowork desktop scheduled tasks and chats
on other accounts don't show up in this list. Paste or summarize anything important from those into this file.
