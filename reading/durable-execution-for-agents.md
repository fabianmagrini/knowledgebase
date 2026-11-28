---
type: reading
title: Long-Horizon Agents and Durable Execution
description: "Durable execution makes an agent survive failure, not behave correctly — the five failure classes the runtime leaves to the harness, and the versioning problem of replaying new code against old logs."
tags: [ai-engineering, agentic-workflows, architecture, system-design, reading]
topic: reading
status: notes
level: intermediate
related:
  - engineering/ai-native/long-running-agents.md
  - engineering/architecture/agents-as-distributed-systems.md
  - engineering/ai-native/agentic-autonomy-levels.md
  - engineering/practices/database-migration-strategies.md
  - engineering/practices/rollback-and-roll-forward.md
  - engineering/architecture/cell-based-architecture.md
  - reading/reactive-reducer-orchestration.md
  - engineering/ai-native/agentic-sdlc.md
source: "https://martinfowler.com/articles/durable-execution-agents.html"
updated: 2026-11-28
---

# Long-Horizon Agents and Durable Execution

Kiran Prakash (Director of Data and AI, Thoughtworks; martinfowler.com, 10 November 2026) argues
that durable execution is what lets an agent work on a goal for days or weeks across people and
external systems — and that **durability is not correctness**. The runtime handles the generic
failures (crashes, failed calls, retries). A set of domain failures it cannot see stays with the
harness, and has to be designed for explicitly.

"Long horizon" here is deliberately **not** the benchmark sense of how long a model can work
uninterrupted. It means *multi-day or multi-week work involving people and external systems* — a
purchase order waiting on a manager, a supplier who replies on Thursday. The economic claim: work
that was uneconomical because it needed scarce human attention spread over weeks (onboarding,
sales-to-legal handoffs, patient administration) becomes viable.

> **Provenance.** A single constructed example — a **Stock Replenisher** ordering parts for a
> manufacturer — implemented on both Temporal and Cloudflare Workflows; code snippets are
> simplified with arguments elided. Performance figures are the **author's own tests** on a local
> Temporal server and Cloudflare, not benchmarks. Thoughtworks' Agent/works platform is mentioned
> as a possible future topic. Prompt injection is explicitly out of scope beyond partial harness
> defences, deferred to a separate article. The citations are the strong part: Joshi's *Patterns of
> Distributed Systems*, Garcia-Molina & Salem's Sagas, Armstrong's Erlang thesis, Brooks, and
> Fowler's own pattern catalogue.

## The mechanism, briefly

The durable-execution mechanism — record progress so a failed run resumes rather than restarts,
with an idempotency key on side effects — is already held in
[Long-Running Agents](../engineering/ai-native/long-running-agents.md). Prakash's version adds the
vocabulary needed for the rest of the argument:

- **Agentic loop** = goal + tools + state + a model choosing the next tool; the code around the
  model is the **harness**.
- **Steps vs code.** Anything that touches the outside world is a *step*, named with a stable ID
  and recorded in the log. Code between steps only reads and writes local state.
- **Replay.** On wake or recovery, completed steps return their recorded results and program state
  is rebuilt from the log — Joshi's **Write-Ahead Log** and Fowler's **Event Sourcing**, applied to
  a single workflow.
- **Waiting is free; waking is not.** A logged wait holds no process or memory (no CPU on either
  platform), but a rebuilt-from-log wake grows with log length. The author's figures: an in-memory
  wake in 14 ms on Temporal and ~0.1 s on Cloudflare; a wake rebuilt from the log under 0.1 s on
  Temporal and ~2 s on Cloudflare.
- **Two models.** A fast, cheap classification model picks the next tool; a generation model
  (Claude in the example) reads supplier emails and drafts replies. The decision step and the
  language step have different cost profiles, so they get different models.

## Entity vs process workflows

| | Process workflow | Entity workflow |
|---|---|---|
| **Represents** | One piece of work — a replenishment | One business entity — a SKU |
| **Lifetime** | Finishes when the work is done | As long as the entity exists |
| **Example** | `Replenish` child workflow per order | `SkuAgent` with stable ID `agent-SKU-123` |

The entity workflow checks stock, spawns a process workflow per replenishment, then restarts itself
with **`continue_as_new`** to keep its own log short. This is the distinction the repo lacked
between a *task* agent and the *standing agents* held from
[Ultimate](ultimate-self-extending-harness.md): a standing agent is an entity workflow, and the
`continue_as_new` reset is how it avoids the history-growth problem below.

## What durability does not solve

The central contribution. Drawing on Brooks, some of these are **essential** complexity (from the
real-world task) and some **accidental** (from the runtime and the model):

| Failure | Why the runtime can't help | Harness response |
|---|---|---|
| **Unseen outcomes** | The log records what the agent *observed*, not what happened | Idempotency key (the PO number); compensating tools (`cancel_order`) |
| **Stale facts** | A decision made on Monday may be wrong by Thursday | Decisions carry an **expiry**; **re-check facts before any hard-to-undo action** |
| **Code changes mid-run** | Replay runs *new* code against *old* records | Treat the log as a **Published Interface**; record `rules_version`; migrate with **parallel change** |
| **History growth** | Wake cost and context both grow with the log | Snapshots, `continue_as_new`; tiered memory (MemGPT/Letta) |
| **Untrusted input** | Any email can claim anything | Validate the **source of authority** — approval comes from the manager; a supplier email cannot grant it |

### The duplicate order

The worked failure that makes the first row concrete. Supplier A accepted an order, then went
unreachable; after six attempts the `place_order` step failed, so the agent started a new
replenishment and ordered from supplier C. Supplier A later confirmed the first order by email; the
agent matched PO numbers and called `cancel_order`.

> The agent found the duplicate only because supplier A wrote.

At-least-once semantics are the runtime's contract. **Exactly-once effects in the world are not**,
and a log of observations cannot tell you what you failed to observe. The compensating tool is a
**Saga** compensation, recovered here for agents — the mistake is discovered late and undone
forward rather than prevented, the same move as
[roll-forward](../engineering/practices/rollback-and-roll-forward.md) for deploys.

### Versioning: the log is a published interface

The finding most specific to durable execution, and one the repo did not hold. A workflow that has
been waiting for a week will be replayed by whatever code is deployed when it wakes. So the log is
an interface between versions of your own program, and changing workflow code is a
**schema migration on in-flight state**. The mitigation is three-step
[parallel change](../engineering/practices/database-migration-strategies.md) — add the new rule
beside the old, let new workflows take the new rule while running ones finish under the old, remove
the old once nothing uses it — exactly expand/contract, applied to business rules rather than
columns.

**The runtimes disagreed.** The rule was raised to require four quotes before a draft order while
PO 4471, drafted after three, was waiting on approval. Temporal let the replenishment continue under
the old rule; Cloudflare, which re-checks recorded decisions against current rules, left
*"PO 4471 stayed a draft."* Neither is wrong — but **the choice of runtime is a choice of business
semantics**, and the author's advice is to test which one you have before shipping a rule change.

## Two harness practices worth keeping

- **Business rules in code, not the prompt.** Each tool has an `allowed()` predicate over state —
  `PlaceOrder` only when a PO exists, no order has been placed, and the price is within the
  approved ceiling. The model can only select from tools the rules permit. This is the
  deterministic gate [Agentic Autonomy Levels](../engineering/ai-native/agentic-autonomy-levels.md)
  calls for, at the granularity of a single tool call, and a milder form of
  [Reactive Reducer Orchestration](reactive-reducer-orchestration.md)'s removal of the model from
  control flow: the model still chooses, but within a set code computed.
- **Approve a range, not a value.** "Up to 5% above the quote" lets the agent act on a
  reasonable counter-offer without a fresh round-trip to a human — the approval is a bound, not a
  point. It is the difference between a human-in-the-loop that serialises the workflow and one that
  delegates a decision space.

## Relationship to other notes

- [Long-Running Agents](../engineering/ai-native/long-running-agents.md) — holds the durable
  execution *mechanism* (via Ibryam) and the three walls; this is what remains after the mechanism
  works. Its checkpoint-and-resume pattern assumes the retry safety this note shows is
  domain-specific.
- [Agents as Distributed Systems](../engineering/architecture/agents-as-distributed-systems.md) —
  the same framing argued without evidence; this supplies a worked system, two runtimes and named
  patterns. Prakash's distinction — the model at the core can *decide how to recover* — is the
  inverse of Rao's warning that it can also decide to degrade.
- [Cell-Based Architecture](../engineering/architecture/cell-based-architecture.md) — the
  idempotency key again, as the precondition for retry and failover.
- [Database Migration Strategies](../engineering/practices/database-migration-strategies.md) —
  expand/contract, which this note applies to in-flight workflow state.
- [The Agentic SDLC](../engineering/ai-native/agentic-sdlc.md) — lists "durable execution" as a
  requirement for agent-ready architecture; this is what meeting it involves.

## Open question from the author

> When an agent decides to cancel a confirmed order, should it optimise for cost or supplier
> relations?

Durable execution makes the cancellation possible; it says nothing about which objective the
compensating action should serve. His closing position is that **domain expertise and software
architecture matter more than ever**, and that tactical fixes and vibe coding will create more
problems than they solve.
