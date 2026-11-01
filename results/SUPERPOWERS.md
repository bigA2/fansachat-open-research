# Superpowers and andrej-karpathy-skills: licences, methods, and how to test them in our builder

Two different projects. Crawled copies are in `results/sources/licences/`.

## 1. Licences

| project | licence line (quoted) | source |
|---|---|---|
| `obra/superpowers` | "MIT License Copyright (c) 2025 Jesse Vincent Permission is hereby granted, free of charge, ..." | https://github.com/obra/superpowers/blob/main/LICENSE (`00.md`); README: "MIT License - see LICENSE file for details" (https://github.com/obra/superpowers) |
| `multica-ai/andrej-karpathy-skills` | README section "License": "MIT" | https://github.com/multica-ai/andrej-karpathy-skills (`02.md`) |

**Caveat for the second project:** https://github.com/multica-ai/andrej-karpathy-skills/blob/main/LICENSE returns
"404 - page not found. The main branch of andrej-karpathy-skills does not contain the path LICENSE." (`03.md`). So
the only licence statement found is the one word "MIT" in the README, with no licence file and no copyright line.
The README's install commands also point to a different owner, `forrestchang/andrej-karpathy-skills`. Before copying
any text from it, check that path for a LICENSE file, or write our own wording. Using the **ideas** needs no licence.

MIT allows use, copying and changes, including commercial use, if the copyright and licence notice is kept with any
copied substantial part. If we copy text from Superpowers into our prompt, keep its MIT notice in our repo's
third-party notices. Paraphrasing the method (below) is safer and enough.

## 2. What each one teaches

### Superpowers (https://github.com/obra/superpowers)

"a complete software development methodology for your coding agents, built on top of a set of composable skills".
Its basic workflow: **brainstorming** (draws out what you want "through questions", "then plays its understanding back
for correction"), **writing-plans** (small tasks, each with "verification steps"), subagent or inline execution with
review, **test-driven-development** (RED-GREEN-REFACTOR), code review, and finishing the branch. Philosophy: "Test-Driven
Development", "Systematic over ad-hoc", "Complexity reduction", "Evidence over claims - Verify before declaring
success". It tests skill behaviour with an eval harness (superpowers-evals).

### andrej-karpathy-skills (https://github.com/multica-ai/andrej-karpathy-skills)

"A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations". Four principles:
1. **Think Before Coding**: "State assumptions explicitly - If uncertain, ask rather than guess"; "Stop when confused".
2. **Simplicity First**: "No features beyond what was asked".
3. **Surgical Changes**: "Touch only what you must".
4. **Goal-Driven Execution**: "Define success criteria. Loop until verified."
Its own "Tradeoff Note": the guidelines "bias toward caution over speed".

Both are written for **coding agents**, not for workflow builders. Neither page reports measured results; Superpowers
names an eval harness but the README gives no numbers. **So there is no evidence yet that they help our builder.**

## 3. Could the method go into our builder prompt?

Yes, as ideas rewritten for workflows. A possible mapping (to be tested, not assumed):

| method | builder version |
|---|---|
| think first / state assumptions | before the JSON, write a one-line plan: trigger, actions, apps, and assumptions |
| ask when unclear | if the trigger app, the target app, or a recipient is missing or ambiguous, ask one short question instead of guessing |
| simplicity | fewest steps that do the request; no extra steps the user did not ask for |
| plan + verify | after building, check: every app is in the catalog, every step has `after`, routers have branches, required inputs are filled (once `inputs` exist, see `results/MAPPING_AND_NODES.md`) |
| caution over speed | only for risky actions (delete, pay, send to many people); simple requests should build at once |

Risk: more questions mean more friction. "Ask when unclear" must not become "always ask". That is why it needs a test.

## 4. How to prove it helps: A/B test on our eval set

- **Arms:** A = current builder prompt. B = current prompt + the short method block above. Same model, same
  temperature, same app catalog.
- **Eval set:** the 60 one-sentence requests in `results/persona_requests.json`; the top 30 automations in
  `results/BUYERS.md` written as one sentence each; and a set of deliberately vague requests where asking is the right
  answer (to be written; each labelled "build" or "ask").
- **Measures** (all automatic, from the builder output):
  1. valid JSON that passes our schema check;
  2. every app is a real catalog app;
  3. the workflow matches the request (trigger app and action apps right; checked against a hand-written answer key);
  4. asked when it should have asked, built when it should have built (two error rates, reported separately);
  5. number of steps vs the answer key (extra steps = over-building);
  6. tokens and time per build (cost).
- **Run** each request at least 3 times per arm, because outputs vary. Report per-measure results for A and B with
  counts, not just a total.
- **Decide** B wins only if it improves measures 3 and 4 without making 1, 2 or 6 worse. If it is a tie, keep A
  (simpler).

No results exist yet. Nothing in this file claims the method helps until this test is run.
