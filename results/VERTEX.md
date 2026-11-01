# "Vertex": Google's agent platform and Application Integration

Read as: Google Vertex AI Agent Builder / Agent Engine, and Google Application Integration. Sources: crawled copies in
`results/sources/vertex/` (all four loaded).

## Naming note (important)

The pages we asked for under the old "Vertex AI" names now show new names:

- https://cloud.google.com/vertex-ai/generative-ai/docs/agent-builder/overview now opens "Agent Platform overview":
  "Gemini Enterprise Agent Platform is a unified platform to build, deploy, govern, and optimize enterprise-grade AI
  agents and model-based solutions. As an evolution of Vertex AI, it supports the complete AI lifecycle from accessing
  over 200 foundation models to deploying and managing your agents." (page "Last updated 2026-10-30 UTC").
- https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview now opens "Scale your agents", which
  describes a managed **Agent Runtime** (the role Agent Engine had).
- https://cloud.google.com/products/agent-builder now opens a product page titled "Gemini platform".

So "Vertex AI Agent Builder" is now marketed as **Gemini Enterprise Agent Platform**. Below I use the current names.

## 1. Gemini Enterprise Agent Platform (was Vertex AI Agent Builder)

**What it is** (https://cloud.google.com/vertex-ai/generative-ai/docs/agent-builder/overview):
- Four pillars: **Build, Scale, Govern, Optimize**.
- Low-code: **Agent Studio** ("Design agents and interact with models without code").
- Code: **Colab Enterprise notebooks** and the **Agent Development Kit (ADK)**, "a modular, model-agnostic framework".
- Security: "**Agent Identity** lets you grant granular permissions to agents. **Agent Gateway**, together with
  **Model Armor**, secures all agent interactions, enforces runtime policies, and helps protect against threats".
- Models: "200+ Google and third-party AI models", including Anthropic's Claude models and open Gemma models
  (https://cloud.google.com/products/agent-builder).

**Agent Runtime (was Agent Engine)** (https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview):
- "a fully managed Agent Runtime to deploy and scale agents ... with built-in observability".
- **Sessions** and a **Memory Bank** for conversation state and long-term memory.
- **Example Store** and **Evaluation Service** "to test, monitor, and trace agent behavior, creating a continuous
  feedback loop".
- Sandboxed **Code Execution** and **Computer Use**.
- Runs agents built with ADK, LangChain, LangGraph, LlamaIndex, AG2 and Agent2Agent; guides for tracing (Cloud Trace),
  logging and monitoring with alerts; per-agent IAM identity, service accounts, API keys and OAuth clients.

**Who it is for:** "technical teams", developers and data scientists: "Gemini platform enables technical teams to
build agents" and "For developers, Gemini platform remains our advanced platform"
(https://cloud.google.com/products/agent-builder). It needs a Google Cloud project. It is not aimed at the
non-technical small-business buyer FansaChat targets (`results/BUYERS.md`).

## 2. Google Application Integration

**What it is** (https://cloud.google.com/application-integration/docs/overview): "an Integration-Platform-as-a-Service
(iPaaS) solution in Google Cloud" to connect Google Cloud services and third-party SaaS. It is "serverless,
auto-scales, and is fully managed by Google."

Key features listed on that page:
- drag-and-drop **integration editor**;
- pre-built **connectors**;
- a **visual data mapping editor** with mapping functions;
- built-in **tasks** (actions) and **event-driven triggers**;
- **Cloud Monitoring** ("usage, performance, alerts, and the overall health") and **Cloud Logging**;
- identity federation;
- "**Gemini to build integrations**": "Gemini assists you to create and build integrations using your natural
  language statements (or prompts) as input."

**Who it is for:** Google Cloud customers connecting enterprise systems, for example Salesforce, MySQL and Cloud Pub/Sub
(same page). It also needs a Google Cloud project.

## 3. What FansaChat could safely learn (ideas, not code)

These are general product ideas from public docs. We copy no code, text or design.

1. **Prompt to workflow is now a big-vendor feature.** Application Integration has "Gemini to build integrations"
   from natural language. Our "one sentence -> working workflow" is not unique; our edge must be simplicity and the
   small-business buyer, not the idea itself.
2. **Data mapping is a named core feature** in Application Integration (visual data mapping editor). This backs the
   gap in `results/MAPPING_AND_NODES.md`.
3. **Give each workflow its own identity and limited permissions** (Agent Identity idea): a workflow should only use
   the connections it was built with, and an AI step should not call apps the user did not approve. This also helps
   against excessive agency (`results/INJECTION.md`).
4. **A gateway or filter in front of AI steps** (Agent Gateway + Model Armor idea): check inputs coming from app data
   for prompt injection, and check AI outputs before they are sent to another app.
5. **Evaluation as a loop** (Example Store + Evaluation Service idea): keep a fixed eval set of builder prompts and
   re-run it on every prompt or model change (`results/SUPERPOWERS.md` uses this for A/B tests).
6. **Monitoring with alerts per workflow** (Cloud Monitoring idea): health view of runs, failures and alerts, in plain
   language for non-technical users (`results/NOTIFICATIONS.md`).
7. **Memory per user** (Memory Bank idea): remember a user's usual apps and choices so the builder asks fewer questions.
   Only with clear consent and a delete button.

## 4. What not to take

- Google Cloud project setup, IAM, notebooks and SDKs: far too technical for our buyers.
- Pricing: I did not read Google's pricing pages for these products, so this file makes **no price comparison**.
