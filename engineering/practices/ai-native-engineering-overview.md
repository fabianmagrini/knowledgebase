---
title: AI-Native Engineering — Overview
tags: [meta, ai-engineering]
topic: engineering/practices
status: complete
related:
  - engineering/practices/ai-native-engineering-stack.md
  - engineering/practices/agentic-sdlc.md
  - engineering/practices/agentic-sdlc-maturity-model.md
  - engineering/practices/agentic-ai-strategy-frameworks.md
  - engineering/practices/ci-cd-ai-engineering.md
  - engineering/practices/eval-driven-ai-development.md
  - engineering/practices/ai-augmented-engineering-team.md
  - engineering/practices/change-absorption-capacity.md
  - engineering/practices/ai-dlc-methodology.md
  - engineering/practices/harness-engineering.md
  - engineering/practices/quality-first-ai-coding.md
  - engineering/practices/agent-backpressure-loops.md
  - engineering/practices/agile-in-the-age-of-ai.md
  - engineering/practices/modern-engineering-values.md
  - engineering/practices/loop-driven-development.md
  - leadership/learning-organisation.md
  - engineering/architecture/design-systems-ai-control-plane.md
updated: 2026-06-13
---

# AI-Native Engineering — Overview

A map of the notes on building software with AI agents. They answer different questions —
*strategy, process, platform, team, control, quality* — and reinforce each other.

## Strategy & maturity — where are we going?

- [Agentic AI Strategy Frameworks](agentic-ai-strategy-frameworks.md) — how to think about
  adopting agentic AI at the organisation level.
- [Agentic SDLC Maturity Model](agentic-sdlc-maturity-model.md) — staged progression from
  assisted coding to controlled autonomy.

## Process — how does work flow?

- [The Agentic SDLC](agentic-sdlc.md) — the AI-assisted software delivery lifecycle.
- [CI/CD as the Control Plane for AI-Assisted Engineering](ci-cd-ai-engineering.md) — the
  pipeline as the guardrail that makes agent-speed delivery safe.
- [AI-DLC and the Reimagined SDLC](ai-dlc-methodology.md) — a concrete, ceremony-level
  methodology (AI-DLC, V-Bounce, Bolts/Units/Intents) instantiating the agentic loop.
- [Agile in the Age of AI](agile-in-the-age-of-ai.md) — the counterpoint: Agile principles
  persist; sustainable pace and human cognitive load bind how many agents you can direct.

## Platform & team — who and what enables it?

- [The AI-Native Engineering Stack](ai-native-engineering-stack.md) — the tooling/platform
  layer (the internal developer platform, golden paths).
- [The AI-Augmented Engineering Team](ai-augmented-engineering-team.md) — the operating
  model: team composition, Intent Specs, the delivery loop, transition roadmap. The capstone
  that ties the rest together.
- [Modern Engineering Values](modern-engineering-values.md) — a solo/small-team practitioner's
  values: ownership, taste, guardrails, context-in-the-repo, own your stack, option value.

## Control & quality — how do we keep it correct?

- [Design Systems as the AI Control Plane](../architecture/design-systems-ai-control-plane.md)
  — codified constraints as the control plane for AI-generated UI.
- [Eval-Driven Development for AI Capabilities](eval-driven-ai-development.md) — testing the
  prompts/skills/agents themselves, not just the code they emit.
- [Harness Engineering](harness-engineering.md) — the component-level anatomy of an agent
  harness (the program agents run inside): core loop, tools, memory, patterns, trade-offs.
- [Quality-First AI Coding](quality-first-ai-coding.md) — the practitioner workflow: multi-model
  bug review and quality-over-velocity use of AI to write better code more slowly.
- [Backpressure Loops for Coding Agents](agent-backpressure-loops.md) — move mechanical
  correctness feedback into agent-actionable loops (sensors) so agents self-correct and humans
  stop babysitting.
- [Loop-Driven Development](loop-driven-development.md) — the connective map: TDD scaled to agent
  loops (trigger/goal/harness/verifier/state) and the autocomplete→prompt→context→harness→loop
  leverage stack.
- [Change Absorption Capacity (CATS)](change-absorption-capacity.md) — raising a system's
  capacity to safely absorb agent-speed change: contracts, automated verification, telemetry,
  simplification.

## The through-line

When code generation is cheap, leverage moves to **intent, constraints, and judgement**.
Strategy sets direction; the SDLC and CI/CD move work; the stack and team supply capability;
design systems and evals keep output correct. See also the
[engineering leadership overview](../../leadership/engineering-leadership-overview.md) for the human/decision
side, much of which these notes depend on — and
[The Learning Organisation and AI Adoption](../../leadership/learning-organisation.md) for the
cultural prerequisite (psychological safety, slack, intelligent failure) that lets a team adopt
any of this faster than the tooling changes.
