---
type: note
title: Agents as Distributed Systems
description: "Decision decomposition as the successor to functional decomposition, and the failure mode that follows: quality degrading silently while latency and error rate stay flat — plus retry amplification, where the evaluation loop that improves output is also the thing that multiplies it."
tags: [architecture, system-design, ai-engineering, observability, agentic-workflows, reading]
topic: engineering/architecture
status: notes
level: intermediate
related:
  - engineering/ai-native/ai-gateway-control-plane.md
  - engineering/ai-native/eval-driven-ai-development.md
  - engineering/ai-native/harness-design-experiments.md
  - engineering/ai-native/agentic-autonomy-levels.md
  - reading/building-effective-agents.md
  - reading/agentic-ai-architecture-emag.md
  - engineering/ai-native/long-running-agents.md
  - engineering/architecture/llm-platform-engineering.md
  - engineering/architecture/runtime-architecture-verification.md
  - concepts/progressive-delivery.md
  - leadership/decision-facilitation.md
  - standards/agent-interop-protocols.md
  - case-studies/uber-mcp-gateway.md
  - case-studies/airbnb-database-workload-replay.md
  - engineering/architecture/data-readiness-for-agents.md
source: "https://www.infoq.com/articles/distributed-systems-microservices-agentic-ai/"
updated: 2026-10-25
---

# Agents as Distributed Systems

Mallika Rao (InfoQ, October 2026, reviewed by Rafał Gancarz) argues that agentic systems are a
continuation of distributed-systems practice rather than a departure from it, with one
substitution at the centre:

> Microservices solved a fundamental problem: how to decompose functionality across services and
> teams… Agentic systems enable the **decomposition of decision-making**.

This is chapter one of the eMag recorded in
[Agentic AI Architecture](../../reading/agentic-ai-architecture-emag.md), published standalone.
That signpost note named this framing as the material worth capturing from the full text.

> **Provenance.** No data, no case studies and no citations. The piece draws on stated
> *"experience operating large-scale distributed systems in domains such as search,
> recommendation, and serving infrastructure"*, and **no limitations are acknowledged anywhere in
> it** — worth noting because the value is vocabulary rather than evidence. Same character as
> [the AI gateway pattern proposal](../ai-native/ai-gateway-control-plane.md), also InfoQ and
> also an experience-grounded argument.

## Three dimensions, two of which are already held more sharply

| Dimension | Traditional | Agentic |
|---|---|---|
| **Control flow** | *"execution paths are designed and encoded ahead of time"* | *"execution paths are determined at runtime based on context"* |
| **State management** | *"explicit state transitions and well-defined persistence models"* | *"an evolving execution context continuously updated as reasoning progresses"* |
| **Failure semantics** | *"failures are typically binary: a request succeeds or fails"* | *"failures often manifest as degraded decision quality"* |

**Stated plainly: control flow and failure semantics are already in these notes, in a sharper
form.** [The AI Gateway as a Governance Control Plane](../ai-native/ai-gateway-control-plane.md)
sets out the same contrasts as the three assumptions an ordinary API gateway makes and agents
violate — deterministic services, schema-level failures, and a client that specifies intent
rather than a goal. The difference is **altitude**: that note is about one seam and what it must
hold; this is about the architecture around it. The genuinely additional row is **state** — an
execution context that is continuously rewritten has no persistence model to reason about, which
is a different problem from non-determinism.

## The failure mode worth the note

The reason to keep this piece is that it names what going wrong actually looks like, which these
notes did not hold:

> Infrastructure metrics such as latency and error rate may remain stable, while user-facing
> quality deteriorates due to changes in decision-making behavior… Small shifts in tool
> selection, reasoning strategies, or context interpretation can accumulate over time.

**Nothing alerts.** The classic distributed-systems failure announces itself — a 5xx, a timeout,
a saturated queue. This one is invisible to every signal an SRE practice is built on, and the
conclusion follows directly:

> Decision quality becomes a **first-class reliability concern alongside latency, availability,
> and throughput.**

That lands in a measured hole. The `sre/` folder holds five notes, all on incident-review
culture, with **no SLO or service-level content at all** — so there is nowhere in these notes
that treats quality as a reliability target rather than as a code-review concern. The closest
existing machinery is the `grounded` / `out_of_scope` response flagging in
[LLM Platform Engineering](llm-platform-engineering.md), which is this idea implemented for one
failure class without being generalised.

### Cascading decision degradation

> Early incorrect decisions can subtly influence downstream reasoning, compounding degradation in
> output quality… Small shifts in early decisions can lead to noticeable changes in system
> outcomes.

Worth distinguishing from **context rot** in
[Long-Running Agents](../ai-native/long-running-agents.md): rot is degradation caused by
accumulated history filling the window, this is degradation caused by a **wrong premise
propagating**. Different cause, different fix — rot argues for keeping the window lean,
cascading degradation argues for checking early decisions hardest.

It is also the same mechanism Goedecke describes for human conversations in
[Facilitating Technical Decisions](../../leadership/decision-facilitation.md) — *"a small
misunderstanding early on balloons into a big misunderstanding later, because all the things you
misinterpret based on the first misunderstanding will become misunderstandings in their own
right"* — which is his argument for interrupting immediately rather than saving questions up. The
agent-chain version has the same remedy shape: verify at the point of the decision, not at the
end of the chain.

### Retry amplification

The sharpest observation in the piece, and an uncomfortable one for the repo's own prescriptions.
Evaluation loops improve adaptability and *"can also lead to excessive iteration cycles"*:

> Unlike traditional retry mechanisms tied to explicit errors, these retries are driven by
> subjective quality judgments, making them harder to bound and control.

A conventional retry has a termination condition someone wrote down. A retry triggered by a model
judging quality insufficient does not, which is why it is unbounded in a way a retry storm is
not.

**This has a measured counterpart here.**
[Harness Design for Long-Running App Development](../ai-native/harness-design-experiments.md)
reports a **22× cost multiple** for an elaborate planner/generator/evaluator harness over a solo
agent — $200 against $9 for the same application. Rao names the mechanism; Anthropic priced it.
Read together, the evaluator-optimizer pattern in
[Building Effective Agents](../../reading/building-effective-agents.md) and the eval loops in
[Eval-Driven Development](../ai-native/eval-driven-ai-development.md) are both subject to it:
**the loop that improves the output is the same loop that multiplies the work**, and nothing in
either note bounds it.

## The prescriptions, mostly held elsewhere

Recorded for completeness, with pointers rather than restatement:

| Prescription | Where it already lives |
|---|---|
| **Bounded autonomy** — *"latency budgets, retry limits, and reasoning depth boundaries"* (no figures given) | The execution contract in [Agentic Autonomy Levels](../ai-native/agentic-autonomy-levels.md) |
| Separation of planning and execution; agent specialisation | Orchestrator–workers and evaluator–optimizer in [Building Effective Agents](../../reading/building-effective-agents.md) |
| Integrated evaluation loops | [Eval-Driven Development](../ai-native/eval-driven-ai-development.md) — now with the amplification caveat above |
| Tool abstraction layers | [Agent Interop Protocols](../../standards/agent-interop-protocols.md); [Uber's MCP Gateway](../../case-studies/uber-mcp-gateway.md) as the production instance |
| Progressive rollout via *"experimentation, shadow execution, and controlled deployment"* | [Progressive Delivery](../../concepts/progressive-delivery.md); shadow execution as practised in [Airbnb's workload replay](../../case-studies/airbnb-database-workload-replay.md) |

Two that are genuinely additive:

- **Hybrid architectures with deterministic fallbacks** — *"deterministic execution paths provide
  stability when agentic reasoning becomes uncertain or when system confidence is low."* Note the
  tension with [Data Readiness for Agents](data-readiness-for-agents.md), whose position is that a
  contract breach must override the model's own confidence: a fallback triggered *by* low model
  confidence inherits the problem that a model is equally confident on both sides of the
  frontier. The fallback trigger needs to be external to the model's self-assessment.
- **Decision-level tracing** — *"visibility into how system behavior evolves over time and where
  degradation originates."* The unit of observability moves from the request to the decision,
  which is the same move as the **Request → Decision → Action** semantic logging in
  [the AI gateway note](../ai-native/ai-gateway-control-plane.md), arrived at for reliability
  rather than for audit.

## What the piece does not cover

- **No evidence of any kind** — no measurement, no case, no citation, and no acknowledgement that
  any of this is unvalidated.
- **No figures for the bounds it recommends.** Latency budgets, retry limits and reasoning-depth
  boundaries are named as the mechanism without a single number or a method for choosing one,
  which is the whole difficulty.
- **No account of how to measure decision quality in production** — which, given that making it a
  first-class reliability concern is the central conclusion, is the missing half. Declaring
  quality an SLO is easy; the hard part is the signal, and that is where
  [Eval-Driven Development](../ai-native/eval-driven-ai-development.md) and the hallucination-rate
  flags in [LLM Platform Engineering](llm-platform-engineering.md) have more to offer than this.
- **Nothing on cost**, despite naming retry amplification.

## Relationship to other notes

- [The AI Gateway as a Governance Control Plane](../ai-native/ai-gateway-control-plane.md) — the
  same contrasts at the altitude of one seam; read that for what the boundary must hold and this
  for the system shape around it.
- [Harness Design for Long-Running App Development](../ai-native/harness-design-experiments.md) —
  retry amplification with a price on it, at 22×.
- [Eval-Driven Development](../ai-native/eval-driven-ai-development.md) and
  [Building Effective Agents](../../reading/building-effective-agents.md) — the patterns this
  supplies the failure modes for.
- [Long-Running Agents](../ai-native/long-running-agents.md) — context rot, which cascading
  decision degradation is distinct from.
- [LLM Platform Engineering](llm-platform-engineering.md) — quality as a platform metric,
  implemented for one failure class; this is the general claim that it should be a reliability
  target.
- [Runtime Architecture Verification](runtime-architecture-verification.md) — *"structure is
  checkable statically; topology is not"*, which is the same asymmetry one layer down: a
  decomposition of decisions cannot be verified from the source.
- [Agentic AI Architecture (InfoQ eMag)](../../reading/agentic-ai-architecture-emag.md) — the
  collection this is chapter one of, and the note that asked for this capture.
