---
type: case-study
title: Intercom's AI PR Approval
description: "AI auto-approving ~19% of pull requests with no human reviewer: the sub-agent guardrails, accountability moving from reviewer to author, and why the headline revert-rate comparison doesn't show what it appears to."
tags: [ai-engineering, code-review, agentic-workflows, reading]
topic: case-studies
status: notes
level: intermediate
related:
  - engineering/ai-native/agentic-code-review.md
  - engineering/practices/code-review-policy.md
  - case-studies/rootly-pr-size-risk-labels.md
  - case-studies/cloudflare-ai-code-review.md
  - case-studies/doordash-ai-code-review.md
  - engineering/ai-native/own-the-outer-loop.md
  - engineering/ai-native/agentic-autonomy-levels.md
  - engineering/practices/change-absorption-capacity.md
  - engineering/security/secure-sdlc.md
  - case-studies/rewind-ai-pr-approval.md
  - engineering/ai-native/dark-factories-examined.md
source: "https://www.intercom.com/blog/ai-is-approving-our-pull-requests-heres-how-we-made-it-safe/"
updated: 2026-08-08
---

# Intercom's AI PR Approval

Kesha Mykhailov and Niamh Young (Intercom, April 2026) describe an AI reviewer that
**approves pull requests outright** — roughly **19%** of PRs across two codebases merge
without a human approver. An engineering narrative with supporting data rather than a
technical deep-dive.

The motivation is the **impedance mismatch**: with 93% of PRs agent-driven, human reviewers
could not keep pace, and the pressure produced rubber-stamping. Their argument is that a
review nobody has capacity to perform properly is not a safety control, so the honest options
are to remove it or to automate it. This is the
[change-absorption](../engineering/practices/change-absorption-capacity.md) limit reached and
acted on.

## It contradicts a position held three times over

Worth stating plainly, because these notes take the other side:

| Note | Position |
|---|---|
| [Code Review Policy](../engineering/practices/code-review-policy.md) | "Only **human approvals count toward merge requirements**" |
| [Agentic Code Review](../engineering/ai-native/agentic-code-review.md) | "**A human owns the merge.** Models cannot be held accountable; a person clicks merge" |
| [Secure SDLC](../engineering/security/secure-sdlc.md) | High-risk changes are never auto-merged |

Rootly relaxed a *heuristic* — see [Rootly](rootly-pr-size-risk-labels.md). Intercom relaxes an
*accountability principle*, which is the larger claim.

**But the contradiction is narrower than the headline.** Accountability does not disappear: the
**shipping engineer remains accountable**, with post-merge monitoring required. What is removed
is the second pair of eyes, not the responsible human. Read against
[Own the Outer Loop](../engineering/ai-native/own-the-outer-loop.md) — which requires that
someone can explain what changed and why it was safe — that requirement still holds. Ownership
moves from *reviewer* to *author*.

## The guardrails

- **Sub-agents per review dimension**, running in parallel: problem-description quality, diff
  alignment with the stated problem, safety, logic, and best practices. Described as
  simulating "a dozen tenured engineers" reviewing at once — the same multi-agent shape as
  [Cloudflare](cloudflare-ai-code-review.md), pointed at approval rather than commentary.
- **Execution-path tracing** through the codebase, rather than reading the diff in isolation.
- **Intercom-specific guidance**, continuously refined from engineer feedback.
- **Human override available at any time.**
- **Accountability plus monitoring** after merge.

## The safety mechanism is the refusal, not the approval

The most interesting claim, and the one that generalises: the system **declines to approve**
large, complex or broadly-scoped changes, which pushes engineers to decompose them.

The gate therefore improves the *inputs* rather than catching bad *outputs*. That is a
different kind of safety argument from "the reviewer is good enough to trust" — it works even
where the reviewer is mediocre, because the population of changes reaching auto-approval is
constrained to those that are simple enough to reason about.

### The tension with Rootly

Two AI-heavy engineering organisations reach opposite conclusions from the same premise:

| | On small PRs |
|---|---|
| **[Rootly](rootly-pr-size-risk-labels.md)** | Retired the small-PR rule; splitting agent-authored features is "busywork with no upside" |
| **Intercom** | Pressure toward small PRs is the *point* — it is what makes unattended approval defensible |

They are partially reconcilable: Rootly's objection is to size as a **gate applied to humans**,
while Intercom uses size as a **precondition for removing humans**. But they genuinely disagree
about whether decomposition is overhead or safety, and both are reasoning from production
experience.

## The numbers, and what they actually show

| | |
|---|---|
| Pilot | zero reverts across 100+ PRs; **6–16× faster** approval |
| Post-rollout, 497 PRs — backend | AI-authored reverted **0.53%** vs **5.39%** human-authored |
| Post-rollout — frontend | **0.22%** vs **2.00%** |
| PRs agent-driven overall | **93%** |

**The revert comparison does not demonstrate what it is used to suggest.** Two problems:

1. It compares AI-**authored** against human-**authored** code. The claim being defended is
   about AI *approval*. Those are different variables, and the data speaks to the first.
2. The auto-approved population is **selected for simplicity by construction** — the system
   refuses large, complex and broad changes. That small, well-scoped changes revert less is a
   long-standing result and not evidence about review quality.

The honest reading is that the figures show the *overall* system shipping safely, not that
unattended AI approval is as good as human approval. The authors do concede the 10× gap may
not persist, and that PR review cannot catch infrastructure problems or unanticipated usage
patterns.

## Relationship to other notes

- [Agentic Code Review](../engineering/ai-native/agentic-code-review.md) — holds that a human
  owns the merge; this is the strongest published counter-case, and the accountability-moves-to-
  the-author framing is how the two can both be right.
- [Code Review Policy](../engineering/practices/code-review-policy.md) — its human-approval
  requirement is the rule being tested here. Note that Intercom's refusal behaviour is itself a
  risk tier: simple changes auto-approve, everything else escalates to a human.
- [Agentic Autonomy Levels](../engineering/ai-native/agentic-autonomy-levels.md) — auto-approval
  is high autonomy justified by cheap detection (revert monitoring) and cheap undo, which is
  exactly the calibration that note prescribes.
- [Cloudflare](cloudflare-ai-code-review.md) and [DoorDash](doordash-ai-code-review.md) — the
  same multi-agent reviewer built and tuned, but stopping short of granting it authority.
