---
type: note
title: The AI Factory
description: "Narrowed to software engineering, an AI Factory is a production system for AI coding agents."
tags: [ai-engineering, agentic-workflows, architecture]
topic: engineering/ai-native
status: notes
level: intermediate
related:
  - reading/factory-engineers.md
  - engineering/ai-native/ai-native-engineering-stack.md
  - engineering/ai-native/agentic-sdlc.md
  - engineering/ai-native/scaling-ai-adoption.md
  - engineering/ai-native/apex-framework.md
  - engineering/ai-native/harness-engineering.md
  - reading/new-sdlc-vibe-coding.md
updated: 2026-07-03
---

# The AI Factory

Narrowed to software engineering, an **AI Factory** is a *production system for AI
coding agents*. Instead of employing engineers to write every line, the factory
orchestrates specialised agents that design, implement, review, test, and operate
software under human supervision. The value of the framing is that it moves the
conversation from "AI-assisted coding" to **industrialised software production**.

This is distinct from the [Trust Factory](trust-factory.md) (Kent Beck's metaphor
for how development builds or erodes trust) — here "factory" means a literal
production line of agents.

## Factory vs. traditional software factory

A traditional software factory ran `Requirements → Developers → QA → Operations`.
An AI Factory collapses the human labour into intent-setting and oversight:

```text
Requirements → Product Engineer → AI Factory → Production Software
```

The factory contains dozens — eventually hundreds — of specialist agents working
together, each with defined inputs, outputs, quality gates, and ownership.

## The production line

Rather than one coding assistant, picture an assembly line under an orchestrator:

```text
Human Product Engineer  (defines intent and outcomes)
        ▼
AI Factory Orchestrator
        ▼
Requirements → Architecture → API Design → UI Design
  → Frontend → Backend → Infrastructure → Test Generation
  → Security Review → Performance → Documentation → Release
        ▼
Human Approval Gates  →  Production Systems
```

## Factories, not copilots

Today's tools mostly give one developer one assistant. An AI Factory replaces that
with a coordinated workforce — a product engineer directs an AI project
manager/orchestrator, which coordinates 20+ specialist agents into an integrated
solution. Each agent has a single responsibility and can be independently improved
or replaced.

## Types of coding agents

A mature factory mirrors traditional engineering roles:

| Factory area | AI agent |
|---|---|
| Discovery | Requirements Analyst |
| Product | User Story Writer |
| Architecture | Solution Architect |
| APIs | API Designer |
| Frontend | Frontend Engineer |
| Backend | Backend Engineer |
| Database | Schema Designer |
| Infrastructure | Platform Engineer |
| Testing | Test Engineer |
| Security | Security Reviewer |
| Performance | Performance Engineer |
| Documentation | Technical Writer |
| Operations | Release Manager |
| Support | Incident Investigator |
| Modernisation | Refactoring Engineer |

## The changed human role

Engineers stop writing implementation code and spend their time on defining
problems, clarifying requirements, making architectural decisions, setting quality
expectations, reviewing output, approving changes, handling exceptions, and
coaching the factory. The job shifts from **coding** to **engineering the system
that produces code** — the same "typist → reviewer/orchestrator" shift covered in
[A Learning Culture for AI-Augmented Teams](../../leadership/learning-culture-ai-agents.md).

## Reusable production assets

Like any manufacturing system, the factory depends on standard, reusable
components — the equivalent of manufacturing tooling, ensuring consistency and
reducing variability across agent outputs:

coding standards · architecture patterns · prompt libraries · engineering skills ·
internal frameworks · golden paths · templates · design systems · API standards ·
test strategies · security policies · MCP tool catalogue · knowledge base.

## A governed per-agent lifecycle

Every agent runs the same governed delivery loop, making the process predictable
regardless of which agent does the work:

```text
Receive Task → Gather Context → Reason → Plan → Generate Code
  → Run Tests → Run Linters → Execute Build → Review Results
  → Improve → Submit PR
```

## Quality built into the line

Quality is not a final QA phase; checks are gates throughout the pipeline:

```text
Task → Architecture Validation → Policy Checks → Coding Standards
  → Security Scan → Unit Tests → Integration Tests → Performance Tests
  → Accessibility Tests → Human Review → Merge
```

## Operating the factory: thinking is the bottleneck

Benedict Brady's ["software factory" talk](https://www.benedict.dev/software-factory)
(Ellipsis Labs) adds an operator's lens to the architecture above. Its sharpest
claim is a theory-of-constraints reading of the agent workflow: **the model's
*thinking* (reasoning/planning) is the bottleneck, so everything around it should be
fast and parallelisable.** Harder problems warrant *more* thinking time; the way to
go faster is not to shorten reasoning but to strip latency and serialisation out of
every step that surrounds it (context gathering, tool calls, validation, shipping)
and run them concurrently — often as a DAG rather than a fixed pipeline.

Brady also frames the baseline an agent needs to operate like a professional
developer as a small **toolkit**, so it can ship and *self-validate* without a human
in each step:

| Tool | Why the agent needs it |
|---|---|
| **CLI** | Ship, run, and debug independently |
| **Browser** | Exercise and verify its own UI changes |
| **Compute** | Run builds, tests, and long tasks |
| **Wallet** | A budget to self-provision compute and paid services on demand |

The **wallet** is the least obvious: giving an agent spend authority lets it acquire
the resources it needs to finish and verify work, rather than stalling on a human to
provision them. A separate **critic agent** with clean context then judges outputs
and proposes process improvements — the same generation-vs-evaluation split as
[eval-driven development](eval-driven-ai-development.md) and the
[backpressure loop](agent-backpressure-loops.md), applied to the factory itself.

## The control-plane platform

The factory runs on an engineering platform providing shared agent capabilities.
This control plane is a specialised form of the layered
[AI-Native Engineering Stack](ai-native-engineering-stack.md), and its agent
delivery loop is exactly the kind of [harness](harness-engineering.md) that keeps
autonomous agents on rails:

```text
Developer Portal
  ▼
AI Factory Control Plane
  Agent Registry · Skill Registry · Prompt Registry · Policy Engine
  Workflow Engine · Memory · Knowledge Graph · MCP Gateway
  ▼
LLMs
  ▼
Developer Tools:  GitHub · Jira · CI/CD · Kubernetes · Observability · Docs
```

It manages which agents are available, how they collaborate, what tools they can
access, and how governance is enforced.

## Factory metrics

Measure the production system, not individual contributors: lead time from idea to
production, percentage of code generated autonomously, human review effort per
change, AI-generated defect escape rate, first-pass acceptance rate, cost per
feature, agent utilisation, average task completion time, agent rework rate,
knowledge reuse, policy compliance, deployment frequency, and MTTR. See
[The APEX Framework](apex-framework.md) for a structured treatment of AI
engineering measurement.

## Reference architecture

```text
Product Engineer
      ▼
AI Factory Portal
      ├─────────────────────────────┐
Work Orchestrator            Knowledge Platform
      ▼                             ▼
Agent Runtime                  RAG / Memory
      │
  Architect · Backend · Frontend · Testing · Security  (agents)
      ▼
GitHub / CI/CD / Cloud
      ▼
Production Systems
```

## Why it matters

This is the direction of AI-native software engineering. The question shifts from
"How do we give every engineer an AI coding assistant?" to "How do we build a
factory that reliably produces high-quality software using coordinated teams of AI
coding agents?"

For anyone designing enterprise engineering platforms, the AI Factory is the next
evolution of the **Internal Developer Platform (IDP)**. The IDP standardises
infrastructure and delivery; the AI Factory standardises and governs *the
production of software itself* through specialised, orchestrated coding agents,
with humans focused on architecture, product direction, and quality oversight.
The organisational foundations needed to get here are covered in
[Scaling AI Adoption in the SDLC](scaling-ai-adoption.md).
