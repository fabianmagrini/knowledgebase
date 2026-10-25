---
type: note
title: Platform Engineering for Production LLMs
description: "Hallucination as a platform-controllable metric via grounded/out_of_scope schema flags, a prompt registry with rollback without redeploy, a three-way failure taxonomy for retries, and authorisation enforced at the resource server rather than only the gateway."
tags: [ai-engineering, architecture, observability, governance, reading]
topic: engineering/architecture
status: notes
level: intermediate
related:
  - engineering/ai-native/ai-gateway-control-plane.md
  - engineering/architecture/data-readiness-for-agents.md
  - engineering/ai-native/eval-driven-ai-development.md
  - engineering/practices/feature-flags-and-branch-by-abstraction.md
  - engineering/ai-native/activity-metrics-obsolete.md
  - case-studies/uber-mcp-gateway.md
  - engineering/security/agent-skill-security.md
  - standards/agent-interop-protocols.md
  - engineering/ai-native/brownfield-agentic-engineering.md
  - engineering/architecture/over-engineering.md
  - concepts/control-and-complexity.md
  - engineering/architecture/agile-design-decisions.md
  - engineering/architecture/layered-architecture.md
  - engineering/architecture/reversibility-decays.md
  - engineering/architecture/agents-as-distributed-systems.md
source: "https://www.infoq.com/articles/platform-engineering-playbook-production-llms/"
updated: 2026-10-25
---

# Platform Engineering for Production LLMs

Aditya Mulik (InfoQ, October 2026, reviewed by Srini Penchikala) argues that organisations
running several LLM applications should stop treating LLM concerns as application-level problems
and move them into a shared platform layer. ~8,500 words with a working code repository.

**This occupies a subject these notes have been circling without naming.** The AI-native cluster
is about *building software with agents*; this is about **operating LLM applications in
production** — a different concern. It sits beside
[Data Readiness for Agents](data-readiness-for-agents.md) as the serving layer to that note's
data layer.

## Hallucination as a platform-controllable metric

The repo had nothing on measuring or reducing hallucination as an *engineering* rather than a
*model* concern. The reframe is what makes it tractable:

> "A hallucinated response isn't a stack trace. It passes every traditional health check. The
> downstream service consumes it, takes action on it, and only much later does someone notice
> the suggested output doesn't exist."

Same structure as the migration-blindness failure in
[Brownfield Agentic Engineering](../ai-native/brownfield-agentic-engineering.md) — every check
green over a wrong result — and the reason neither is caught by ordinary monitoring.

**The mechanism is the contribution.** Rather than trying to detect hallucination after the
fact, the output schema forces the model to declare it:

| Field | Meaning |
|---|---|
| `grounded` | *"True if every claim is backed by the fetched docs; False if the docs did not cover the question"* |
| `out_of_scope` | *"True if the request fell outside documentation lookup"* |

Described as *"the highest-precision hallucination signal."* **Groundedness becomes a validated
field rather than a judgement**, which is what lets the platform act on it — a model that must
set `grounded: false` has said something checkable, where a model that merely answers has not.

This is adjacent to but distinct from
[Data Readiness for Agents](data-readiness-for-agents.md)'s *"retrieved text informs, it never
gates"*. That rule is about **decisions** — don't let prose decide whether an action proceeds.
This is about **claims** — require the model to state whether its assertions are backed. Two
different uses of retrieved context, and both need the discipline.

### The headline figure, which is unsubstantiated

> "we cut production hallucination rate from fifteen percent to 1.5 percent without touching the
> foundation model"

A retail inventory recommendation system, attributed to an automated retry loop catching
formatting, grounding and infrastructure errors.

**Checked specifically: there is no sample size, no time period, no methodology, no statement of
whether this covers all requests or a subset, and no baseline conditions for the 15%.** A
ten-fold improvement with nothing behind it. The *mechanism* below is worth adopting on its own
reasoning; the number should not be quoted.

## A failure taxonomy for retries

Three categories, each with a different response — which is the point, since a single blanket
retry treats them identically:

| Failure | Response |
|---|---|
| **Schema violation** | Re-prompt with the validation error appended |
| **Hallucination signal** | Re-prompt with stronger grounding context |
| **Infrastructure error** (429, 503) | Exponential backoff |

With *"every request needs a hard cap"* — three tries as the baseline before abandoning
recovery. These notes hold no retry taxonomy for model calls, and the distinction matters
because re-prompting an overloaded endpoint and backing off from a schema violation are both
wrong.

## Prompt registry: rollback without redeployment

Prompts stored with ID, version, creation timestamp and tags, resolved at runtime, with full
history preserved and rollback repointing the "active" version.

**That is deploy/release decoupling applied to prompts.**
[Feature Flags and Branch by Abstraction](../practices/feature-flags-and-branch-by-abstraction.md)
makes the general case — code ships inert, a separate decision releases it — and this is the
same separation for the artefact that most changes model behaviour.

It also upgrades a practice
[Eval-Driven Development](../ai-native/eval-driven-ai-development.md) already prescribes.
That note says "version everything — capability definitions, assertions, and harness live in the
repo and change through review." True, and insufficient on its own: repo-versioned means a bad
prompt needs a deploy to undo. A runtime registry makes the rollback as fast as the regression.

## The intent validation gate

A cheap classifier runs *before* the expensive foundation-model call, and the sharp part is what
it does when uncertain: it returns **"unclassified" rather than defaulting to the
highest-scoring agent.**

Defaulting to the best available match is the natural implementation and it manufactures
confident wrong answers — the router always picks *something*, so an out-of-scope request gets
handled by whichever specialist scored least badly. Refusing to answer is the correct behaviour
and it has to be built deliberately.

Same discipline as [Data Readiness for Agents](data-readiness-for-agents.md)'s preference for
**hard gates** over weighted confidence composites, and as the **abduction** point in
[Control and Complexity](../../concepts/control-and-complexity.md) — holding a question open
beats closing it on the strongest weak signal.

## Authorisation: at the resource, not only the gateway

A direct qualification of a note these notes hold.

> "Enforce tool authorization directly at the resource server with a strict default-deny policy;
> **relying solely on API gateway checks means any single bug in your orchestrator can instantly
> expose every connected tool.**"

Each MCP server independently verifies tokens and checks policy. Mechanics: stateless JWTs
signed with role claims, default-deny YAML policies.

[The AI Gateway as a Governance Control Plane](../ai-native/ai-gateway-control-plane.md) argues
for concentrating identity, action policy, guardrails and audit at **one** seam, on the sound
reasoning that those are the fastest-moving concerns. This does not contradict that so much as
bound it: **centralise the policy, enforce at the resource.** The gateway remains the right place
to *define* who may do what; it is the wrong place to be the only thing checking.

That echoes a caveat already recorded in
[Securing AI Agent Skills](../security/agent-skill-security.md) — *"middleware sharing a process
boundary with the agent is not isolation"* — reached from threat modelling rather than from
architecture, which is some independent support.

## Cost attribution as infrastructure

Tag every request for cost attribution **upfront**, per team, application and use case, with
per-user metrics capturing requests, errors, hallucinations, tokens, cost and latency.

These notes are full of cost *figures* — per review, per run, per worker fleet, per token — and
hold nothing on the attribution *plumbing* that produces them. It is also a precondition for
something the repo already prescribes:
[Activity Metrics Under AI](../ai-native/activity-metrics-obsolete.md)'s **rework per AI spend**
cannot be computed at all without per-team attribution in place.

Observability metrics named: hallucination rate (schema plus grounding failures), token spend by
attribution, tool invocation patterns, and behavioural correctness sampled against **golden
sets** — the last being [eval-driven development](../ai-native/eval-driven-ai-development.md) run
continuously against production rather than before shipping.

## The ordering claim, and the tension it creates

Six prioritised decisions, with the timing as the actual contribution: observability before the
first production deployment; **platform thinking at application #2, not #10**; ID-based prompt
versioning from day one; schema enforcement at the platform boundary on the first call; cost
tagging upfront; golden-set evaluation before the first prompt change.

> "The decision point for building this platform isn't the first LLM application. It's the
> second. By the time you have ten teams each shipping LLM features, retrofitting a platform
> underneath them is long and difficult migration work."

**This cuts against the repo's general bias**, which is emergent and anti-speculative —
[Over-Engineering Is Solving the Wrong Problem](over-engineering.md),
[Agile Design Decisions](agile-design-decisions.md)'s emergent architecture,
[Layered Architecture](layered-architecture.md)'s "add structure when it pays for itself."

The argument for the exception is **retrofit cost**, which is
[Reversibility Decays](reversibility-decays.md) reasoning applied to platform timing: the exit
cost from ten teams' independent implementations only rises, and nothing about that accumulation
is decided. Worth holding as a bounded exception rather than a general licence — the claim is
about *shared cross-cutting concerns under known multiplication*, not about building platforms
early in general.

## Their own limitations

Unusually candid, and worth recording:

- The prompt registry shown is **in-memory**; production needs database backing.
- The accompanying repo deliberately runs a **local model (Ollama/llama3.1)** to avoid API costs,
  diverging from the hosted production setup.
- The intent classifier in the repo is **keyword-based and deterministic**, where production would
  use a trained model — which matters, because the "unclassified" behaviour above is easier to
  guarantee with keywords than with a classifier that always produces scores.

Tooling named (a point-in-time snapshot): Google ADK, LiteLLM, Ollama, MCP with FastMCP, Pydantic,
PyJWT, OpenTelemetry, ADK's AgentEvaluator.

## Relationship to other notes

- [Data Readiness for Agents](data-readiness-for-agents.md) — the sibling layer. That note covers
  the data agents read; this covers the platform they run on. Their rules are complementary:
  retrieved text must not *gate decisions*, and model claims must *declare grounding*.
- [The AI Gateway as a Governance Control Plane](../ai-native/ai-gateway-control-plane.md) — the
  centralisation argument this bounds: centralise policy, enforce at the resource.
- [Eval-Driven Development](../ai-native/eval-driven-ai-development.md) — golden sets and
  versioning, upgraded here from repo-versioned to runtime-switchable with rollback.
- [Feature Flags and Branch by Abstraction](../practices/feature-flags-and-branch-by-abstraction.md)
  — deploy/release decoupling, applied to prompts.
- [Activity Metrics Under AI](../ai-native/activity-metrics-obsolete.md) — cost attribution is the
  precondition for its rework-per-AI-spend metric.
- [Uber's MCP Gateway](../../case-studies/uber-mcp-gateway.md) — the same MCP boundary at much
  larger scale, and a compatible position on gating: Uber gates exposure at registration, this
  gates authorisation at the resource.
- [Securing AI Agent Skills](../security/agent-skill-security.md) — independent support for
  enforcement below the orchestrator, from threat modelling rather than architecture.
- [Over-Engineering](over-engineering.md) and [Reversibility Decays](reversibility-decays.md) —
  the emergent-design default this argues an exception to, and the reasoning that justifies the
  exception.
