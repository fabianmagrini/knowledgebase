---
type: case-study
title: Uber's MCP Gateway
description: "800+ MCP servers and 5,000+ tools behind a registry/proxy split, with 'discovery doesn't imply exposure' as the governance rule, the resolution of the auto-generated-MCP HOLD, and the surrounding platform — including PR categorisation instead of velocity counting."
tags: [ai-engineering, architecture, agentic-workflows, governance, reading]
topic: case-studies
status: notes
level: intermediate
related:
  - concepts/control-plane-data-plane.md
  - case-studies/stripe-kai-agent-platform.md
  - engineering/architecture/data-readiness-for-agents.md
  - standards/agent-interop-protocols.md
  - engineering/ai-native/ai-gateway-control-plane.md
  - engineering/ai-native/model-routing-and-ai-gateways.md
  - engineering/ai-native/cress-context-engineering.md
  - case-studies/portkey-product-engineer-company.md
  - engineering/ai-native/ai-factory.md
  - concepts/latency-patterns.md
  - engineering/architecture/llm-platform-engineering.md
  - engineering/ai-native/activity-metrics-obsolete.md
  - case-studies/ramp-inspect-agent-platform.md
  - case-studies/rootly-pr-size-risk-labels.md
  - engineering/ai-native/agentic-code-review.md
  - engineering/ai-native/linters-over-ai-review.md
  - engineering/ai-native/ci-speed-with-ai-agents.md
  - reading/state-of-tech-2026.md
  - engineering/architecture/agents-as-distributed-systems.md
  - sre/ai-sre-and-the-incident-path.md
source: "https://www.uber.com/gb/en/blog/designing-mcp-gateway/; https://newsletter.pragmaticengineer.com/p/ubers-ai-infra-from-the-inside"
updated: 2026-10-31
---

# Uber's MCP Gateway

Alok Srivastava, Deepanshu Mehndiratta, Gaurav Gill and four colleagues (Uber, October 2026) on
the platform that standardises how agents reach internal services — built because teams were
independently creating MCP integrations, producing inconsistent tooling, duplicated
infrastructure and security gaps.

**"Over 800 MCP servers and over 5000 tools"**, across hundreds of teams and thousands of
internal services. An order of magnitude past anything else recorded here — Stripe's platform
reports 500+ MCP tools.

**Why this note exists.** "MCP Gateway" appears twice in these notes as an **unexplained stack
component**: a box in [The AI Factory](../engineering/ai-native/ai-factory.md)'s diagram, and a
step in [Portkey](portkey-product-engineer-company.md)'s "AI gateway → MCP gateway → agent
gateway" roadmap. Neither says what one is. This is the same gap
[Agent Interoperability Protocols](../standards/agent-interop-protocols.md) filled for MCP
itself — vocabulary in use with nothing behind it.

**Provenance.** Uber on Uber's own platform, self-reported. Every figure is **scale**, not
**outcome** — no latency numbers, no adoption-effect measurement, no cost results. See the
limits section.

## Control plane and data plane, at the tools layer

The architecture is a clean instance of a concept these notes already hold.
[Control Plane and Data Plane](../concepts/control-plane-data-plane.md) defines the split: the
data plane is the capability, the control plane is the bookkeeping that reconciles desired
against actual state.

| Component | Plane | Responsibility |
|---|---|---|
| **MCP Registry** | Control | The catalogue of 800+ servers and 5,000+ tools; review and enablement; the record of what *should* be exposed |
| **Proxy Gateway** | Data | Runtime execution; protocol translation; refreshes configuration **in-memory without restarts** |

The in-memory refresh is what makes the split real rather than nominal — enabling a tool is a
control-plane edit that the data plane picks up without a deploy.

## "Discovery doesn't imply exposure"

The governance rule, and the best thing in the piece. Every server and tool begins **disabled**
and *"must be explicitly reviewed and enabled by the owning team."*

This is a materially different answer to tool sprawl from the one these notes already hold:

| | Gate | When | Who decides |
|---|---|---|---|
| [Stripe's Kai](stripe-kai-agent-platform.md) | `allowedTools` — the model selects skills, then the corresponding tools load | **Per session, at load time** | The model, within a bounded set |
| **Uber, here** | Disabled-by-default registration | **Per organisation, at registration time** | The **owning team**, once |

They operate at different layers and are complementary rather than competing. Stripe's keeps any
single session's context small; Uber's keeps the catalogue from exposing 5,000 tools to anyone
in the first place. A platform at Uber's scale plausibly needs both — the registration gate
bounds what *could* be loaded, and a session gate bounds what *is*.

The second-order benefit is organisational: enablement sits with the **service owner**, so the
platform team never becomes the arbiter of what 5,000 tools should be visible. That is the
federated-ownership pattern Stripe uses for skills, applied to tools.

## AutoCrawler, and the HOLD it appears to violate

`AutoCrawler` is a Cadence-powered workflow that scans Uber's **IDL registry** for new services
and APIs. For each one it creates or updates an MCP server representation, parses Protobuf and
Thrift files for method names, schemas and documentation, uses **an LLM to generate enriched,
agent-friendly tool descriptions**, translates schemas to JSON-RPC 2.0, and registers everything
**disabled by default**. Native MCP servers are detected by heartbeat metrics and proxied
transparently. Service teams then review and approve.

**This looks like a direct contradiction of a note here, and the resolution is the useful part.**

[Data Readiness for Agents](../engineering/architecture/data-readiness-for-agents.md) records
that **naive one-to-one API-to-MCP conversion sits on Thoughtworks' Radar at HOLD**, and argues
for "5–10 well-described business capabilities, not 50 thin API wrappers" — because an interface
auto-derived from an existing API surface inherits decisions made for a different consumer and
pushes the composition work onto the agent.

Uber is doing exactly that mass conversion, at 5,000 tools.

The reconciliation: **the HOLD is about exposure, not generation.** Thoughtworks' objection is
that an agent confronted with 50 thin wrappers must do the composing. Disabled-by-default breaks
the link between the two — generation is cheap, bulk and automated, while exposure stays curated
and human-gated, so no agent ever faces 5,000 auto-derived wrappers. Read that way the guidance
sharpens rather than fails: **do not auto-*expose*.** Auto-generating a catalogue nobody can see
until someone opts in is a different act, and arguably the cheaper path to the curated set the
HOLD actually wants.

What remains unanswered is whether an LLM-written description of a Thrift method ever becomes a
*well-described business capability*, or only a better-worded thin wrapper. The article does not
address it, and it is the question the HOLD was really about.

## Three answers to context bloat

Their own framing of the problem: configuring agents for hundreds of servers means *"all this
context would eat up the model context limit."* Three mitigations, none of which appears
elsewhere in these notes:

| Mechanism | What it does |
|---|---|
| **Omni MCP** | A single proxy server fronting all gateway servers, supporting **incremental discovery** — agents progressively discover servers and tools rather than loading everything upfront |
| **Response Projection** | *"a GraphQL-like calling pattern for MCP tools"* — inject a field instructing the gateway to return "only the needed fields, not all", trimming responses at runtime |
| **Code Mode** | For shell environments: three CLI commands (list, search, call), agents write tool output straight to files, and **no local MCP server installation** is needed |

**Response Projection is the sharpest.** It treats token cost as a **response-shape** problem
rather than a model-choice or prompt-length problem — an angle both
[Model Routing](../engineering/ai-native/model-routing-and-ai-gateways.md) (route to a cheaper
model) and [Latency Patterns](../concepts/latency-patterns.md) (selective data processing, the
same idea one domain over) approach from elsewhere. The agent's context is being managed at the
*reply* boundary, which is the one place nobody else here looks.

Omni MCP is the structural answer to the ceiling Stripe measured — quality degrading past ~150
skills in context. Stripe's fix was gating at load; this is making the catalogue searchable so
nothing needs loading until it is wanted.

## Reusing existing infrastructure

Two decisions worth recording because they are about *not* building things:

- **Protocol translation** — the gateway converts between MCP and HTTP, gRPC and TChannel, so
  **downstream services need no modification** to become agent-reachable. The adaptation happens
  once at the seam rather than thousands of times in the services.
- **Muttley integration** — request execution is delegated to their existing service-mesh
  sidecar, inheriting routing and observability rather than reimplementing them for agent
  traffic.

That second one is the generalisable move: agent traffic is still traffic, and a mature service
mesh already solves routing, retries and telemetry. Building parallel plumbing for agents is a
cost many organisations will pay by default.

## The platform around the gateway

A later interview — [Gergely Orosz with Uday Kiran Medisetty, Uber Distinguished
Engineer](https://newsletter.pragmaticengineer.com/p/ubers-ai-infra-from-the-inside) (October
2026, not paywalled) — covers the same platform at lower resolution but supplies the surrounding
system, which the blog post above does not.

| Component | What it is |
|---|---|
| **Model Gateway** | One abstraction over Anthropic, OpenAI and proprietary models, with embedded security checks (**AI Guard**), spend tracking and audit logging |
| **AIFX** | A wrapper letting engineers switch between Claude Code, Codex and OpenCode **without losing settings or plugins** |
| **DevPods** | Containerised dev environments, built **2017**, now hosting agent work |
| **Context Graph / Cortana** | Maps relationships between code, services and engineers to inform agent decisions |
| **Minion** | Background agent system, built 2025 |
| **Slate** | Testing and review assistance |
| **Agent Skills repository** | Centralised capability catalogue |

Three things here sharpen notes held elsewhere.

**The Model Gateway is the AI-gateway pattern in production.**
[The AI Gateway as a Governance Control Plane](../engineering/ai-native/ai-gateway-control-plane.md)
is a *pattern proposal* listing what the seam should hold — model routing, identity, action
policy, guardrails, audit. This is a running instance with the same contents. These notes had the
pattern and no production example of it.

**Spend governance: tiered allocations with manager approval for overages**, rather than
unlimited budgets. That same pattern note cites an organisation reaching **$500M monthly Claude
spend with no usage limits on employee licences** as its cautionary case — this is the control
that case was missing, and the first concrete budget-governance mechanism recorded here.

**PR categorisation instead of velocity counting.** Tags for feature, bugfix, maintenance,
testing and docs replaced simple velocity metrics, and revealed **feature PRs rising while
maintenance PRs declined**. That is a better answer to the authorship-count problem running
through [Activity Metrics Under AI](../engineering/ai-native/activity-metrics-obsolete.md),
[Ramp's 75%](ramp-inspect-agent-platform.md) and
[Rootly's 80%](rootly-pr-size-risk-labels.md): **categorise the PRs rather than count them**, so
the measure reports *composition* rather than volume. Worth noting what it leaves open — whether
declining maintenance means less debt or more debt accruing unattended is exactly the question
the measure raises, and the interview does not answer it.

Smaller: **`afx validate`** moved lint and build checks into the inner loop after the CI system's
workload doubled — [Linters Over AI Review](../engineering/ai-native/linters-over-ai-review.md)
and [CI Speed When Agents Write the Code](../engineering/ai-native/ci-speed-with-ai-agents.md)
instantiated at scale. And the ~50% per-token cost reduction is the figure already recorded in
[The State of the Tech Industry in 2026](../reading/state-of-tech-2026.md).

### The insider's caveats

Two, and both are more useful than the component list.

> "Code review has become a big bottleneck inside the company"

Said by a Distinguished Engineer about his own employer — which is
[Agentic Code Review](../engineering/ai-native/agentic-code-review.md)'s central claim confirmed
from inside a large deployment rather than argued from outside. He adds that engineers now
multitask harder and must verify agent output to avoid shipping regressions.

And the line that bounds the whole case study: the infrastructure was **"built on top of a decade
worth of dev tooling investment"** — DevPods from 2017, M3DB built for an observability problem
of 500 million metrics per second. **None of this is replicable by a team starting now**, and the
registry/proxy architecture above should be read with that in mind. What transfers is the
*reasoning*; the implementation rests on prerequisites most organisations do not have.

## What the piece does not cover

Worth stating, because this is a data-plane component sitting in front of thousands of services:

- **No failure modes.** What happens when the gateway is unavailable, or a translation fails.
- **No latency figures.** Protocol translation plus a proxy hop plus mesh forwarding is at least
  three layers; the cost is not quantified. [The AI Gateway as a Governance Control
  Plane](../engineering/ai-native/ai-gateway-control-plane.md) explicitly names latency as the
  trade-off of centralisation, and this account does not engage with it.
- **No multi-region consistency discussion** for a registry whose state determines what is
  exposed.
- **No outcome metrics.** The context-bloat mitigations are presented as mitigations, and nothing
  measures whether they worked.

## Relationship to other notes

- [Control Plane and Data Plane](../concepts/control-plane-data-plane.md) — the concept this
  instantiates at the agent-tools layer, with in-memory config refresh as the mechanism that
  makes the separation operational.
- [Stripe's Kai Agent Platform](stripe-kai-agent-platform.md) — the contrast that matters:
  session-time `allowedTools` gating against registration-time disabled-by-default. Different
  layers, and Stripe's ~150-skill degradation threshold is the ceiling Omni MCP is designed
  around.
- [Data Readiness for Agents](../engineering/architecture/data-readiness-for-agents.md) — the
  API-to-MCP HOLD this appears to violate, and the exposure-versus-generation distinction that
  resolves it.
- [Agent Interoperability Protocols](../standards/agent-interop-protocols.md) — MCP as the
  agent-to-tools boundary contract; this is that boundary operated at 5,000 tools.
- [The AI Gateway as a Governance Control Plane](../engineering/ai-native/ai-gateway-control-plane.md)
  — the same control-plane argument at the **model-call** seam rather than the **tools** seam.
  Read together they describe two gateways an organisation ends up needing, which is the
  progression [Portkey](portkey-product-engineer-company.md) sketches as a roadmap.
- [CRESS Principles](../engineering/ai-native/cress-context-engineering.md) — context minimalism
  as a principle; incremental discovery and response projection are two mechanisms for it.
- [The AI Factory](../engineering/ai-native/ai-factory.md) — lists MCP Gateway as a stack
  component; this is what sits in that box.
