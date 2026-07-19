---
type: note
title: Agentic Code Review
description: "Review as the new binding constraint when agents write the code: tiered risk-based review, human-on-the-loop, the AI-reviewer landscape, and failure modes."
tags: [ai-engineering, code-review, agentic-workflows, reading]
topic: engineering/ai-native
status: notes
level: intermediate
related:
  - engineering/practices/code-review-policy.md
  - engineering/ai-native/own-the-outer-loop.md
  - engineering/ai-native/quality-first-ai-coding.md
  - engineering/ai-native/agent-backpressure-loops.md
  - engineering/practices/change-absorption-capacity.md
  - engineering/ai-native/ci-cd-ai-engineering.md
  - engineering/ai-native/ai-native-engineering-overview.md
  - engineering/ai-native/ai-engineering-discipline.md
  - engineering/ai-native/apex-framework.md
  - reading/agentic-sdlc-survey.md
  - reading/how-i-use-llms-2026.md
  - case-studies/cloudflare-ai-code-review.md
  - case-studies/doordash-ai-code-review.md
  - case-studies/slack-agentic-e2e-testing.md
  - leadership/learning-culture-ai-agents.md
  - engineering/ai-native/scaling-ai-adoption.md
source: "https://addyo.substack.com/p/agentic-code-review"
updated: 2026-06-20
---

# Agentic Code Review

Addy Osmani argues that the binding constraint in software has moved from writing
code to **verifying** it: generation is machine-fast, so review is now "the most
leveraged skill in software". When an agent writes the code, the reasoning it
produced — the thinking traces — is discarded, so the reviewer is often *the first
human to ever read it*, reconstructing intent that was never documented. This is a
[Theory of Constraints](../../concepts/theory-of-constraints.md) bottleneck shift
made concrete: relieve the coding constraint and review becomes the new one.

## The data (vendor- and study-reported)

The article marshals figures that are worth recording but should be read as
**vendor- or study-reported**, not settled fact:

- *Faros AI* (March 2026, 22k developers): roughly **4× the code for ~10% more
  delivered value**; code churn up 861%; defect rates rising from 9% to 54%.
- *CodeRabbit* (Dec 2025, 470 PRs): AI-written code carries **~1.7× more issues**
  than human code.
- *GitClear*: ~4× output for ~12% real value gain.
- *Anthropic's review tool*: a claimed **sub-1% false-positive rate** and
  substantive-review rate raised from 16% to 54%.

The author's reading: mature teams were **not** protected — process could not
absorb the volume (the [change-absorption](../practices/change-absorption-capacity.md) limit).

## Tiered, risk-based review

Rather than reviewing every PR the same way, Osmani proposes tiering by **risk, not
author**:

1. **Tier by blast radius.** Config changes get linting; core business logic
   demands types, tests, multiple AI reviewers, a security pass, and human
   ownership.
2. **Fast-fail the expensive tail.** Use a *circuit breaker* to predict
   high-maintenance PRs (file types, patch size) before a human invests attention.
3. **Raise the intake bar.** Require a statement of purpose, a reasonable diff
   size, proof of passing tests, and documented intent *before* review starts.
4. **Keep PRs small.** Instruct agents to produce digestible commits; large diffs
   get rejected or rubber-stamped.
5. **Read the test changes first.** Agents often rewrite assertions to match broken
   behaviour instead of fixing the code — mutation testing helps tell the
   difference. See [Test Coverage Policy](../practices/test-coverage-policy.md).
6. **Treat CI as immovable.** Watch for removed tests, skipped lint, lowered
   coverage thresholds, and prompt-injection paths — agents optimise toward green
   checkmarks. The deterministic gates are the
   [CI/CD control plane](ci-cd-ai-engineering.md).
7. **A human owns the merge.** Models cannot be held accountable; a person clicks
   merge.

For a solo project with no users, tests and light review suffice; for a large,
high-traffic system all seven are the baseline.

## What AI reviewers are good and bad at

| Strong at | Weak at |
|---|---|
| Never tiring; consistent across dozens of PRs | Judging whether the change is *worth making* |
| Catching bugs humans read past | Spotting unspecified requirements (a "human-shaped gap") |
| Small, well-defined diffs | Tending toward large, hard-to-review diffs |
| **Uncorrelated blind spots across tools** — 93% of findings caught by exactly one of four tools | **Correlated blind spots within a model family** — confidently and uniformly wrong |

The uncorrelated-blind-spots point cuts both ways: running several tools from
*different* model families catches more; a closed loop of the *same* model can be
"very sure and very wrong". Named tools include CodeRabbit, Greptile (trades
precision for recall), Anthropic's Code Review, Cursor BugBot, and Sentry Seer —
each presented by the author with different precision/recall trade-offs.

## The human moves up a loop

The central shift is **human-in-the-loop → human-on-the-loop**: the reviewer stops
reading every diff and instead **audits the system** — sampling and spot-checking,
owning high-blast-radius decisions, judging architectural soundness, confirming
requirements were actually met, and staying on-call for escalations. Writing
detailed **intent documentation upfront** is what makes high agent throughput
reviewable. *"The human does not leave; the human moves up a loop."*

## Failure modes

- **Borrowed confidence** — the system's certainty becomes yours, but nobody
  understood anything; correlated models can be sure and wrong together.
- **Test manipulation** — assertions rewritten to pass rather than to verify.
- **Prompt injection** — agent-built features piping user input into LLM calls
  without sanitisation; invisible in the diff. See
  [Secure SDLC](../security/secure-sdlc.md).
- **Weak CI** — thresholds lowered, tests removed, lint skipped to get green.
- **Zero-review merges** — when humans can't keep pace, code merges unread and the
  practice normalises ("**AI slop**").

## Distinctive vocabulary

- **Blast radius** — the impact scope if the change breaks (nothing vs angry users
  and exposed PII).
- **Comprehension debt** — un-understood code that becomes someone's on-call
  incident.
- **Intent debt** — deferred work created when reasoning is never documented.
- **Borrowed confidence**, **AI slop**, **human-on-the-loop** (as above).

## Relationship to other notes

- [Code Review Policy](../practices/code-review-policy.md) — the *standards* reviewers enforce;
  this note is the *system and reasoning* of reviewing agent-generated code at
  volume.
- [Quality-First AI Coding](quality-first-ai-coding.md) — the *writing* side
  counterpart; this is the *reviewing* side.
- [Backpressure Loops for Coding Agents](agent-backpressure-loops.md) — moving
  mechanical feedback into agent-actionable loops is how the human gets *onto* the
  loop instead of inside it.
- [Change Absorption Capacity](../practices/change-absorption-capacity.md) — the system property
  whose limits the review-volume data illustrates.
- [CI/CD as the Control Plane](ci-cd-ai-engineering.md) — the immovable
  deterministic gates the tiered pipeline depends on.
