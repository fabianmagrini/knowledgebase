---
type: case-study
title: Ramp's Inspect Agent Platform
description: "An internal coding agent on remote cloud sandboxes, built because local harnesses cap parallel sessions — and which became a platform other teams build agents on. Notes cover the readable sections only; the architecture deep-dive is paywalled."
tags: [ai-engineering, agentic-workflows, architecture, reading]
topic: case-studies
status: notes
level: intermediate
related:
  - case-studies/stripe-kai-agent-platform.md
  - case-studies/openai-agent-first-harness.md
  - case-studies/rootly-pr-size-risk-labels.md
  - case-studies/anthropic-ai-native-teams.md
  - engineering/ai-native/harness-engineering.md
  - engineering/ai-native/team-topologies-agentic-platform.md
  - engineering/ai-native/long-running-agents.md
source: "https://newsletter.pragmaticengineer.com/p/why-ramp-built-inspect"
updated: 2026-08-30
---

# Ramp's Inspect Agent Platform

**Inspect** is Ramp's internal coding agent. It runs on remote cloud sandboxes rather than on
engineers' laptops, and Ramp reports it authored **75% of all merged PRs** at the company, past
**one million sessions** as of July 2026. It began as a Chrome extension letting designers make
UI tweaks and grew into a remote development environment with an agent attached.

> **Two limits on this note, both important.**
>
> **1. Paywalled.** Sections 1–3 (what Inspect is, why build one, how Ramp uses it) are
> readable; the paywall lands at the top of section 4, *Architecture and tech stack*. This note
> therefore carries the **what and the why but not the how** — the engineering is the part that
> was not available. Treat the stack list below as a name-drop from the introduction, not as an
> account of how any of it works.
>
> **2. Company-supplied.** Two of the three bylines are Ramp's own engineers. Every figure here
> is self-reported, with no external verification and no counterfactual.

## Why build rather than buy

The argument, which is the transferable part and is readable in full:

| Reason | The claim |
|---|---|
| **Parallelism ceiling** | Third-party harnesses run locally, so one machine caps how many agent sessions an engineer can have going at once. Cloud sandboxes remove the ceiling and centralise configuration |
| **Internal integration** | An in-house agent can reach telemetry, feature flags, production databases, Snowflake, Sentry and Datadog — access Ramp argues an external product structurally cannot have |
| **Closing the loop** | Inspect tests its code and visually confirms UI changes before the work is handed back, rather than stopping at "it compiles" |
| **Designers, not just engineers** | The origin story: the first users wanted to make frontend tweaks without a local dev environment |

The first is the sharpest and the most checkable: **it is an argument about where execution
lives, not about model or harness quality.** Ramp is not claiming a better agent than the
frontier labs ship — it is claiming that running agents somewhere with no machine limit and full
internal network access beats running a better agent on a laptop. That reframes buy-vs-build as
an infrastructure question, which is a more durable framing than "our prompts are better".

Reported sandbox contents: VS Code Server, Chromium, Postgres, Redis, RabbitMQ and Temporal,
spinning up in "five seconds or less". Named stack: React/Vite, Cloudflare Durable Objects,
SQLite, the Cloudflare Agents SDK, Modal sandboxes, and the **OpenCode** harness — notable in
itself, since Ramp built the environment and integrations rather than the agent loop.

## The platform effect

The part with no equivalent elsewhere in these notes. Inspect stopped being an agent and became
a substrate other teams build on. Ramp reports a **5.5-person team producing 200+ custom
agents** on it, including:

| Agent | Domain |
|---|---|
| ReviewBuddy | Code review |
| Oncall Assistant | Incident response |
| Testo | QA testing |
| Ramp Research | Data analysis |
| Voice of the Customer | Feedback aggregation |

This is the case that an internal agent platform's return is not the first agent but the tenth —
once sandboxing, integrations and configuration are solved centrally, the marginal agent is
cheap. It is the concrete instance of the platform-team argument in
[Team Topologies for the Agentic Platform](../engineering/ai-native/team-topologies-agentic-platform.md),
which reasons about the shape without an example this size.

## The numbers, and how much weight they hold

| Reported | Reading |
|---|---|
| **75%** of all merged PRs authored by Inspect | Counts authorship, not value or difficulty — see below |
| **1M+** total sessions (July 2026) | Volume, not outcome; a session is not a merged change |
| **150+** engineers contributed to the codebase | Adoption breadth, the more meaningful adoption figure |
| **~90%** of the Inspect repo's own PRs from Inspect sessions | Self-hosting |
| **80%+** of Inspect itself built with Inspect | The most flattering and least generalisable figure here |

**On the headline.** "75% of merged PRs" measures which entity opened the PR. It says nothing
about size, risk, or whether the work would otherwise have been done — and these notes already
hold two figures with exactly the same ambiguity:
[Rootly's 80%+](rootly-pr-size-risk-labels.md) and
[OpenAI's zero manually-written code](openai-agent-first-harness.md). All three are real and all
three are authorship counts. Read as a set, they establish that agent-authored majorities are
now unremarkable at some companies; none of them establishes what that majority is worth.

The self-hosting pair is worth separating out. A coding agent whose heaviest use is building
itself is working on the codebase its builders understand best, with the tightest feedback loop
and the most forgiving reviewer. It is genuine evidence of usability and weak evidence of
generality.

## Relationship to other notes

- [Stripe's Kai Agent Platform](stripe-kai-agent-platform.md) — the closest sibling and a useful
  contrast in *what* is being platformed. Kai is a conversational agent for all employees and
  the interesting problem is skills at scale; Inspect is a coding agent and the interesting
  problem is where execution runs. Both end up as substrates other teams build on.
- [OpenAI's Agent-First Harness](openai-agent-first-harness.md) — one team, one product, zero
  hand-written code, with the value in agent legibility and mechanically-enforced architecture.
  Inspect is the company-wide, many-teams version, and reports far less about how the codebase
  was shaped to suit agents.
- [Rootly Dropped Its Small-PR Rule](rootly-pr-size-risk-labels.md) — what changes downstream
  once agents author most PRs. Ramp reports reaching that state; Rootly describes adapting review
  policy to it.
- [Anthropic's AI-Native Team Structure](anthropic-ai-native-teams.md) — the other
  self-described account of AI-native working, and the one that locates leverage in project
  parallelism rather than authorship share. A useful corrective to reading 75% as a productivity
  figure.
- [Harness Engineering](../engineering/ai-native/harness-engineering.md) — the discipline this
  is an instance of. Ramp adopted an existing harness (OpenCode) and built the environment around
  it, which is a different division of labour from building the loop itself.
- [Long-Running Agents](../engineering/ai-native/long-running-agents.md) — remote sandboxes are
  the infrastructure premise that makes sessions outlive a laptop.
