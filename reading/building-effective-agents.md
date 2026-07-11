---
type: reading
title: Building Effective Agents — Workflow & Agent Patterns
description: "Notes on Anthropic's Building Effective AI Agents — workflow and agent composition patterns."
tags: [ai-engineering, agentic-workflows, reading]
topic: reading
status: notes
level: intermediate
related:
  - engineering/ai-native/harness-engineering.md
  - reading/agentic-sdlc-survey.md
  - engineering/ai-native/eval-driven-ai-development.md
  - engineering/ai-native/loop-driven-development.md
  - engineering/ai-native/agentic-sdlc.md
  - engineering/ai-native/ai-native-engineering-overview.md
  - reading/multi-agent-coding-coordination.md
  - reading/how-i-use-llms-2026.md
  - reading/agentic-ai-architecture-emag.md
  - case-studies/cloudflare-ai-code-review.md
source: "https://resources.anthropic.com/hubfs/Building%20Effective%20AI%20Agents-%20Architecture%20Patterns%20and%20Implementation%20Frameworks.pdf"
updated: 2026-06-27
---

# Building Effective Agents — Workflow & Agent Patterns

Notes on Anthropic's *Building Effective AI Agents: Architecture Patterns and
Implementation Frameworks*. It is the **composition-pattern** reference the rest
of the AI-native cluster leans on: where
[Harness Engineering](../engineering/ai-native/harness-engineering.md) describes
the internal anatomy of *one* agent and the
[agentic SDLC survey](agentic-sdlc-survey.md) gives the academic six-layer
architecture, this catalogues how to *compose* agentic systems from a few
repeatable patterns — and, just as importantly, when not to.

Anthropic's through-line is **simplicity first**: most production value comes from
composable patterns, not from maximally autonomous agents.

## Workflows vs. agents

The central distinction:

- **Workflows** follow predetermined paths — code orchestrates the LLM through a
  scripted sequence of steps with explicit branching. Deterministic, transparent,
  easy to debug.
- **Agents** direct their own process — the LLM decides the next step from context,
  using tools in a loop, with autonomy inside defined boundaries.

The differentiator: *agents make the control-flow decisions; workflows execute
predetermined logic*. Neither is superior — the guidance is to use the **least
autonomous option that solves the problem**.

## The augmented LLM

The foundational building block beneath every pattern: an LLM core extended with
**tool use, memory/retrieval, and a reasoning loop**. The model analyses a
situation, decides which tool to invoke, interprets the result, and iterates. Tool
design quality (clear inputs/outputs, good documentation) is treated as critical —
the same point the survey makes about the
[agent–computer interface](agentic-sdlc-survey.md).

## The pattern catalogue

The first five are **workflows** (orchestrated by code); the last is the **agent**
case.

| Pattern | What it is | When to use |
|---|---|---|
| **Prompt chaining** | Decompose a task into a fixed sequence; each step's output feeds the next | Tasks that cleanly split into ordered subtasks; high transparency / easy debugging |
| **Routing** | Classify the input, then dispatch to a specialised handler/prompt | Diverse request types; triage; matching problem class to the right specialist |
| **Parallelization** | Run independent subtasks concurrently, then aggregate (sectioning or voting) | Independent components; latency-sensitive work; broad information gathering |
| **Orchestrator–workers** | A coordinator decomposes work, delegates to worker agents, synthesises results | Complex problems where the subtasks aren't known in advance and need diverse expertise |
| **Evaluator–optimizer** | One LLM generates, another evaluates against criteria; loop until the bar is met | Quality-critical generation (code, content) with clear evaluation signals |
| **Autonomous agents** | The model plans and acts over a long horizon within guardrails, with tools and memory | Open-ended problems where steps can't be predetermined; needs monitoring + safety |

The patterns are **composable** — routing can feed an orchestrator, whose workers
each run an evaluator–optimizer loop.

## Principles

1. **Simplicity first** — start with a single LLM call or a deterministic workflow;
   add autonomy only when simpler options demonstrably fall short.
2. **Transparency** — keep the agent's planning and decisions visible; prefer
   explainable structure over hidden cleverness.
3. **Good tool / ACI design** — well-specified, documented tools reduce
   hallucination and unreliable calls.
4. **Composability** — stack patterns rather than building one monolithic agent.
5. **Pragmatism** — match system complexity to the problem; avoid over-engineering.

## When not to use agents

Agentic autonomy is overhead that is not always repaid. Prefer workflows or direct
calls when:

- the task is **simple, linear, and deterministic** — chaining or a direct call
  suffices;
- the domain is **highly regulated / needs step-by-step explainability**;
- the application is **latency-sensitive** and can't absorb reasoning loops;
- the operation is **low-stakes** and flexibility doesn't justify the cost.

This is the practical counterpart to the survey's caution that **benchmark gains
are not field throughput** — autonomy adds cost that only some problems repay.

## Relationship to other notes

- [Harness Engineering](../engineering/ai-native/harness-engineering.md) — the
  *anatomy* of the program an agent runs inside; this note is the *topology* of how
  to wire one or many such agents together.
- [Agentic AI in the SDLC — A Research Survey](agentic-sdlc-survey.md) — its L4
  orchestration layer (single-agent loop vs multi-agent) is the academic framing of
  the orchestrator–workers and autonomous-agent patterns here.
- [Eval-Driven Development](../engineering/ai-native/eval-driven-ai-development.md)
  — the evaluator–optimizer pattern is eval-driven development applied *inside* the
  agent loop.
- [Loop-Driven Development](../engineering/ai-native/loop-driven-development.md) —
  the generate→evaluate→repair loop these patterns run within.
- [The Agentic SDLC](../engineering/ai-native/agentic-sdlc.md) — where these
  patterns sit in the wider delivery lifecycle.
