---
type: note
title: Agentic Verification
description: "Three verification techniques for agent-written code: E2E as ground truth because mocks enshrine the agent's own misunderstanding, property-based tests for invariants agents never consider, and differential tests treating the legacy system as the oracle."
tags: [ai-engineering, testing, agentic-workflows, reading]
topic: engineering/ai-native
status: notes
level: intermediate
related:
  - engineering/practices/test-coverage-policy.md
  - engineering/ai-native/accountability-for-unread-code.md
  - engineering/ai-native/brownfield-agentic-engineering.md
  - case-studies/github-copilot-rust-migration.md
  - engineering/ai-native/agent-backpressure-loops.md
  - engineering/ai-native/tdd-in-the-agent-loop.md
  - case-studies/slack-agentic-e2e-testing.md
  - engineering/ai-native/ci-speed-with-ai-agents.md
  - engineering/ai-native/eval-driven-ai-development.md
  - engineering/ai-native/agentic-code-review.md
  - engineering/ai-native/activity-metrics-obsolete.md
  - engineering/ai-native/linters-over-ai-review.md
  - engineering/ai-native/spec-driven-development.md
  - engineering/architecture/comprehension-as-architecture.md
  - case-studies/anthropic-claude-ai-performance-sprint.md
  - concepts/latency-patterns.md
  - engineering/practices/change-absorption-capacity.md
  - engineering/ai-native/ci-cd-ai-engineering.md
  - reading/fintech-engineering-handbook.md
  - languages-and-frameworks/rust-for-agentic-development.md
  - reading/ultimate-self-extending-harness.md
  - case-studies/airbnb-database-workload-replay.md
  - engineering/architecture/functional-core-imperative-shell.md
source: "https://addyo.substack.com/p/agentic-verification"
updated: 2026-10-26
---

# Agentic Verification

Addy Osmani (October 2026) argues that *"the major bottleneck is not code-writing but the ability
to verify that the code they've written is correct"*, and that the answer is equipping agents
with verification they can run themselves before a human sees anything.

**The thesis is the most-repeated claim in these notes** — held by
[Accountability for Unread Code](accountability-for-unread-code.md) (the two costs: check it or
undo it), [Agentic Code Review](agentic-code-review.md) (review as the new bottleneck),
[Activity Metrics Under AI](activity-metrics-obsolete.md) (the work moved downstream into review,
validation and security), and [Backpressure Loops](agent-backpressure-loops.md) (mechanical
feedback in fast loops the agent can act on). **That is not why this note exists.**

It exists for three verification techniques, two of which were measurably absent here.

**Provenance.** No studies cited; these are practitioner patterns. The named tooling is a
point-in-time snapshot. This is also the tenth Osmani source in these notes — worth weighting
future ones accordingly, as recorded for [Ibryam](../../concepts/latency-patterns.md).

## E2E as ground truth — the argument, not the ranking

The sharpest thing in the piece, and genuinely new here.

[Test Coverage Policy](../practices/test-coverage-policy.md) already holds the orthodox pyramid:
"End-to-end tests — validate critical user journeys. Fewer in number, high value." The *ranking*
is familiar. Osmani's **reason** for inverting the weighting when the code is agent-written is
not:

**A mock encodes the agent's own model of the dependency.** If the agent misunderstood the
contract, the mock enshrines that misunderstanding, the unit test passes, and the suite confirms
the error rather than catching it. Unit tests written alongside the code by the same agent share
its misconceptions. E2E tests exercise real workflows, so they *"act as the ground truth"* and
are harder to trick.

This is **oracle independence applied to the test pyramid**. The principle is already here —
[Accountability for Unread Code](accountability-for-unread-code.md) carries Carlini's *"the task
verifier is nearly perfect, otherwise Claude will solve the wrong problem"*, and the rule that
tests written by the system that wrote the code prove little. What is new is noticing that the
rule **ranks the pyramid differently for agent-written code than for human-written code**: the
mock is the leak, and the mock is exactly what makes unit tests cheap.

His practical advice follows: prefer a few high-value E2E tests to a comprehensive suite.

## Property-based testing — absent from these notes until now

A real gap. "Invariant" appears as a word in several notes —
[CATS](../practices/change-absorption-capacity.md)' "domain-invariant tests",
[CI/CD as the Control Plane](ci-cd-ai-engineering.md) on agents having "no situational awareness
of system-wide invariants", the money invariants in
[the fintech handbook](../../reading/fintech-engineering-handbook.md) — but **property-based
testing as a technique appeared nowhere**.

The idea: rather than hand-picking cases, generate thousands of inputs and assert properties that
must always hold. The property families named:

| Property | What it asserts |
|---|---|
| **Round-trip** | Encode then decode returns the original |
| **Invariants** | Something true before remains true after |
| **Idempotency** | Applying twice equals applying once |
| **Equivalence** | Two paths to the same result agree |

Tools: **fast-check** (JS/TS), **Hypothesis** (Python), **proptest** (Rust).

**Why it suits agents specifically:** these are invariants an agent will not naturally think to
test, because they are properties of the *problem* rather than of the implementation it just
wrote. An agent generating test cases tends to generate cases its implementation handles. A
property-based generator does not consult the implementation at all — which makes it, again, an
independent oracle, and cheap to run thousands of times inside a loop.

## Differential testing — two instances here, no name until now

Run the old and new systems side by side on identical inputs and compare. **Treat the legacy
system as the oracle.**

These notes already contain two instances of this and never named the category:

- [Migrating the Copilot Runtime to Rust](../../case-studies/github-copilot-rust-migration.md) —
  agents performing *"exhaustive old-versus-new comparisons"* across the port
- [Carlini's C compiler](accountability-for-unread-code.md) — **GCC as the reference**, with the
  lesson that an imperfect verifier means solving the wrong problem

Having the term matters because it reframes a failure the repo holds as a *measurement gap rather
than a mystery*. [Brownfield Agentic Engineering](brownfield-agentic-engineering.md) reports
**28 of 520** agent migration runs passing a full audit, with "migration blindness" — tests green
while replacements still call legacy implementations. **That is what a missing differential test
looks like.** A suite written against the new code cannot detect that the old path is still
live; a differential harness comparing both on the same inputs would surface it immediately,
because the old path answering is the thing being compared.

Practical note from the piece: **normalise outputs before comparing**, or incidental formatting
differences drown the real ones.

## Deterministic, fast loops — and the behaviour they prevent

Speed and reliability are already argued here —
[CI Speed When Agents Write the Code](ci-speed-with-ai-agents.md) makes it a throughput lever,
[Linters Over AI Review](linters-over-ai-review.md) contrasts 27 seconds against PR-time
feedback. Osmani adds a behavioural consequence these notes do not name:

**A slow or flaky loop teaches the agent that retrying beats fixing.**

If a test run is slow enough or unreliable enough that re-running sometimes passes, re-running is
the cheaper move from the agent's position — and it will take it. The suite stops being a
correction signal and becomes a lottery. His target is **subsecond execution** for core loops.

That is a more specific argument for fast tests than "developers lose flow", and it survives in
exactly the case where the flow argument dissolves —
[when the agent waits rather than the human](ci-speed-with-ai-agents.md).

## Two smaller contributions

**Feature maps** — user-perspective inventories recording what features exist, how users reach
them, what the expected outcome is, and the gotchas. Adjacent to
[Comprehension as an Architectural Characteristic](../architecture/comprehension-as-architecture.md)
and [Spec-Driven Development](spec-driven-development.md), but framed from the *user's* side
rather than the system's, which is the part those notes do not cover.

**Making taste compound** — when an agent fails, capture the failure as a shared configuration or
a test so it cannot recur. That is the [ratchet](../../case-studies/anthropic-claude-ai-performance-sprint.md)
instinct applied to judgement: each correction becomes a constraint rather than a conversation.

## An ambiguity worth flagging

Osmani advises writing verification checks **before** requesting implementation.

[TDD Inside the Agent Loop](tdd-in-the-agent-loop.md) holds Böckeler's experiment finding that
**agent-authored test-first produced worse solutions at 3–8× the tokens**, because the forcing
function and the psychology both depend on a human performing the ritual.

**These reconcile only if the human writes the checks**, and the piece does not clearly say
which. Read as "the human specifies the oracle before delegating", it is consistent with
everything above — and with Carlini's lesson. Read as "instruct the agent to write tests first",
it is the thing Böckeler measured as counterproductive. The distinction is load-bearing and the
article leaves it open.

## Relationship to other notes

- [Test Coverage Policy](../practices/test-coverage-policy.md) — the orthodox pyramid this
  reweights for agent-written code, and the reason: mocks share the author's misunderstanding.
- [Accountability for Unread Code](accountability-for-unread-code.md) — oracle independence as
  the principle; this supplies three concrete techniques for achieving it.
- [Brownfield Agentic Engineering](brownfield-agentic-engineering.md) — migration blindness
  reframed as a missing differential test.
- [Migrating the Copilot Runtime to Rust](../../case-studies/github-copilot-rust-migration.md) —
  differential testing in production, at 128 PRs.
- [TDD Inside the Agent Loop](tdd-in-the-agent-loop.md) — the write-checks-first ambiguity above.
- [Slack's Agentic E2E Testing Experiment](../../case-studies/slack-agentic-e2e-testing.md) — the
  complement rather than the same thing: that note is agents *running* E2E tests ("tests enforce
  journeys; agents verify goals"), this is E2E tests *verifying agents*.
- [Backpressure Loops for Coding Agents](agent-backpressure-loops.md) and
  [CI Speed When Agents Write the Code](ci-speed-with-ai-agents.md) — the loop-placement and
  loop-speed arguments this extends with the retry-over-fix failure mode.
- [Eval-Driven Development](eval-driven-ai-development.md) — verification for *model-defined*
  capabilities; this is verification for the *code* agents write. Sibling disciplines.
