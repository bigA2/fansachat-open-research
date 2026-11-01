# Research brief, 1 Nov 2026 (public data only, write results into `results/`)

Read first: `results/TEAMS.md`, `results/SOLO.md`, `results/teams.json`, `results/AUTOMATION.md`,
`results/PERSONA_REQUESTS.md`, `results/autofix/`, `results/zapier/`, and the crawled pages in `results/sources/<topic>/`
(`results/sources/index.json` says which loaded). If a page failed, use web search / fetch if you have it; otherwise say
"source not reached". Cite a URL for every claim about another product. Never invent numbers. Plain, short English.

Product context: FansaChat is a chat-first workflow automation app (one plain sentence -> a working workflow) on the
Activepieces engine, 744 apps. Plans: Starter $15 (2,000 runs, 100 AI builds), Pro $45 (10,000 / 400), Team $149
(30,000 / 1,500, 2-10 people), Scale $299 (100,000 / 5,000). All say "Unlimited workflows and users" today. Our step
JSON is `{id, type: trigger|action|router|ai|wait, app, label, after, branch}`, no field data yet.

Write these files:

1. `results/ONET_RECENCY.md`: which O*NET release we used (`teams.json` -> `onet_version`), the newest one listed on
   onetcenter.org (sources/onet), and whether the data is current for Oct 2026. If newer data exists that the scripts
   could not download, say so.
2. `results/BUYERS.md`: for Starter, Pro, Team, Scale: who buys (job titles from SOLO.md / TEAMS.md), why, and per
   person a table of their tasks marked **major** (FansaChat can do most of it now with our apps), **minor** (helps a
   part), **no fit** (judgement / physical / not app work). Use the Laya scores in `automation.json` as a signal, not
   as truth. As long a list as the data gives. End with the 30 most common automations across all people.
3. `results/TIER_AUDIT.md`: compare our four plans with Zapier, Make, n8n, Activepieces, Lindy, Relay (sources/pricing,
   sources/teams): price, runs/tasks, users, workflow limits, team / department features. Recommend (founder decides)
   whether Starter and Pro should limit active workflows and steps or apps per workflow, with numbers and reasons;
   what Team needs (departments, shared vs personal connections, roles, failed-run alerts); whether Scale should have
   separate department workspaces. Name what is missing on each tier.
4. `results/MAPPING_AND_NODES.md`: what Zapier field mapping is and how it works, what an n8n node / node panel /
   data-mapping UI is (ideas only: n8n is under the Sustainable Use License, copy no code), how Activepieces passes data
   (`{{step.field}}`), what FansaChat lacks, and the smallest design that adds it, plus how much it helps.
5. `results/NOTIFICATIONS.md`: does Zapier (and Make, n8n) show run notifications and status on hover; what they do;
   what we should do (toast in seconds, status on hovering an app dot).
6. `results/VERTEX.md`: "vertex" read as Google Vertex AI Agent Builder / Agent Engine and Google Application
   Integration: what it is, who it is for, what we could safely learn from it.
7. `results/INJECTION.md` + `results/injection_cases.json`: prompt injection and abuse classes from OWASP LLM Top 10
   2025 and the other sources (direct, indirect via app data / file names / app names, role-play, system prompt
   leak, JSON or schema break, unicode / homoglyph / zero-width, very long input, excessive agency, denial of wallet,
   improper output handling). At least 120 test inputs, each `{id, class, input, expect: "refuse"|"build"|"ask"}`,
   written for a workflow builder; include harmless look-alikes that must still build (no over-refusal).
8. `results/SUPERPOWERS.md`: licence of `obra/superpowers` and of `multica-ai/andrej-karpathy-skills` (two different
   projects; quote the licence line), what each teaches, whether its method (think first, ask when unclear, plan,
   verify) could be used in our builder prompt, and how to prove it helps (A/B on our eval set). No claims without a test.
9. `results/RESEARCH_SUMMARY_2026-11-01.md`: one page, the top findings and the recommendations, linking the files above.

Commit and push to `main` with clear messages. Do not add secrets or anything private. Do not touch `scripts/` or
`.github/`.
