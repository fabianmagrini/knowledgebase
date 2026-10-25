---
type: reference
title: Agent Interoperability Protocols
description: "Agent interoperability is arriving as independent, boundary-specific contracts rather than one standard — a boundary-to-protocol map (Open Responses, MCP, A2A, AG-UI, A2UI, AGENTS.md, Skills, Plugins, OTel GenAI, ACP) and the incremental adoption order."
tags: [ai-engineering, agentic-workflows, api-design, reading]
topic: standards
status: notes
level: intermediate
related:
  - standards/open-knowledge-format.md
  - engineering/ai-native/ai-native-engineering-stack.md
  - engineering/ai-native/skill-engineering-disciplines.md
  - engineering/security/agent-skill-security.md
  - engineering/architecture/data-readiness-for-agents.md
  - engineering/ai-native/ai-gateway-control-plane.md
  - engineering/ai-native/harness-engineering.md
  - tools/claude-code-steering-mechanisms.md
  - case-studies/slack-agentic-e2e-testing.md
  - case-studies/openai-agent-first-harness.md
  - case-studies/stripe-kai-agent-platform.md
  - case-studies/doordash-flag-cleanup-agents.md
  - case-studies/uber-mcp-gateway.md
  - engineering/architecture/llm-platform-engineering.md
  - engineering/architecture/agents-as-distributed-systems.md
source: "https://generativeprogrammer.com/p/the-emerging-standards-behind-ai"
updated: 2026-10-25
---

# Agent Interoperability Protocols

Bilgin Ibryam (September 2026) surveys the specifications forming around AI agents. The
organising claim is the part worth keeping:

**Interoperability is arriving as independent, boundary-specific contracts rather than one
monolithic standard** — so adopting one does not commit you to the others, and teams should take
them on incrementally as they meet each boundary.

**Why this note exists.** These notes use this vocabulary constantly and define almost none of
it. MCP appears across fourteen files and is defined in exactly one clause, in
[The AI-Native Engineering Stack](../engineering/ai-native/ai-native-engineering-stack.md). A2A
appears once, in a parenthetical. AG-UI, A2UI, ACP, Open Responses, Agent Plugins and the
OpenTelemetry GenAI conventions appear nowhere. This is the place to look them up.

> **This will date faster than almost anything else here.** It is a landscape survey of ten
> specifications at very different maturities, several of which will be absorbed or abandoned.
> The author himself lists four more as emerging — Agentic Resource Discovery, Open Agent
> Specification, Agent Format, AAuth — which is itself the evidence of churn. **Treat the
> boundary framing as the durable part and the names as a snapshot**, dated September 2026.

## The boundary map

| Boundary | Contract | What it carries |
|---|---|---|
| Agent → **model** | **Open Responses** | An open, multi-provider model API: messages, tool calls, streaming |
| Agent → **tools and data** | **MCP** (Model Context Protocol, JSON-RPC 2.0) | Tools, resources and prompts. Described as *"the closest thing to a de facto standard"* |
| Agent → **agent** | **A2A** (Agent2Agent) | Delegation and collaboration between independent agents, via **Agent Cards** and stateful **Tasks** |
| Agent → **UI (events)** | **AG-UI** | An event stream between agent backend and user-facing app: lifecycle, messages, interrupts |
| Agent → **UI (components)** | **A2UI** | A declarative component format for agent-generated interfaces, against a **client-owned widget catalogue** |
| Agent → **repository** | **AGENTS.md** | A plain-Markdown convention for repo-level instructions, build commands and constraints |
| Agent → **domain knowledge** | **Agent Skills** | A directory format: a required `SKILL.md` plus supporting assets |
| Agent → **packaged capability** | **Plugins** | Two formats — Claude Code (product-specific) and Agent Plugins (portable MCP + Skills bundles) |
| Agent → **observability** | **OpenTelemetry GenAI** | Vendor-neutral semantic conventions for tracing a run across models, tools and MCP |
| **IDE** → coding agent | **ACP** (Agent Client Protocol, JSON-RPC 2.0) | IDE-to-agent connection with capability negotiation |

Two observations about the shape of that table, rather than its contents.

**The boundaries are more stable than the protocols.** An agent needs a model, tools, peers, a
UI, a repository, knowledge, and observability — that decomposition will outlive any particular
spec filling a row. Reading the landscape as *rows to be filled* rather than *names to adopt* is
what makes it survive the churn.

**Two rows are one boundary split in half.** AG-UI carries events and A2UI carries components;
they are adjacent specifications for the same agent-to-user surface. That is a sign of an
unsettled boundary, and the place to expect consolidation.

## Adoption order

His sequencing: **start with model access, then add contracts as the agent's scope expands.**
That follows from the independence claim — if no boundary is being crossed yet, its contract is
cost without benefit.

Two notes on the model row. OpenAI recommends Open Responses for new projects, and Anthropic
supports Chat Completions through a compatibility layer — so the model boundary is the one with
live competing options rather than a settled default. An
[AI gateway](../engineering/ai-native/ai-gateway-control-plane.md) is the architectural answer
these notes already hold for exactly that: concentrate the fastest-moving concern behind one
seam.

## Vocabulary

| Term | Meaning |
|---|---|
| **Boundary contract** | A reusable specification at a system integration point — the frame the whole survey rests on |
| **Capability negotiation** | Both sides advertise what they support, so optional functions are available only where mutually supported. ACP's mechanism, and the general answer to versioning a protocol with uneven adoption |
| **Progressive disclosure** | Load knowledge only when activated, so domain detail does not swamp the base prompt |

**Progressive disclosure is already held here** and from a better angle — the ~100-line
`AGENTS.md` table of contents in
[OpenAI's Agent-First Harness](../case-studies/openai-agent-first-harness.md), and the pattern
in [Harness Engineering](../engineering/ai-native/harness-engineering.md). Recorded here only
because it is what makes the Skills format work, not as a new idea.

## What this anchors

The reason a reference note pays for itself: several existing notes argue about these protocols
while assuming the reader knows them.

- [Data Readiness for Agents](../engineering/architecture/data-readiness-for-agents.md) argues
  for **"5–10 well-described business capabilities, not 50 thin API wrappers"** over MCP, and
  that naive one-to-one API-to-MCP conversion is on Thoughtworks' Radar at HOLD — a design
  argument about a protocol that note never defines.
- [Skill Engineering Disciplines](../engineering/ai-native/skill-engineering-disciplines.md) and
  [Securing AI Agent Skills](../engineering/security/agent-skill-security.md) both treat Skills
  as a first-class artefact to lint, evaluate and scan. The `SKILL.md`-plus-assets directory
  format is the thing they are disciplining.
- [Slack's Agentic E2E Testing Experiment](../case-studies/slack-agentic-e2e-testing.md) compares
  Playwright MCP against CLI and generated-test execution models.
- [Stripe's Kai Agent Platform](../case-studies/stripe-kai-agent-platform.md) reports 500+
  internal MCP tools and `allowedTools` gating — the scaling behaviour of the tools row.

## Relationship to other notes

- [Open Knowledge Format (OKF)](open-knowledge-format.md) — the other specification in this
  folder, and arguably an eleventh row: a vendor-neutral format for the *knowledge* agents
  consume, where AGENTS.md and Skills are the repo-local conventions for the same need.
- [The AI-Native Engineering Stack](../engineering/ai-native/ai-native-engineering-stack.md) —
  the layered platform view. This is the contract at each seam between its layers, and the home
  of the one-line MCP definition this note expands.
- [The AI Gateway as a Governance Control Plane](../engineering/ai-native/ai-gateway-control-plane.md)
  — opens on the premise that "models, protocols (MCP, A2A) and the threat surface all move
  continuously." This is the inventory of what is moving.
- [Harness Engineering](../engineering/ai-native/harness-engineering.md) — the component anatomy
  of the program an agent runs inside; these are the wire formats between those components and
  the outside world.
- [Securing AI Agent Skills](../engineering/security/agent-skill-security.md) — the supply-chain
  problem that follows once capability is a *distributable package*, which is what the Skills and
  Plugins rows make it.
