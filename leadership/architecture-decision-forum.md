---
title: Architecture Decision Forum
tags: [architecture, system-design, leadership, decision-making, governance]
topic: leadership
status: notes
related:
  - engineering/architecture/agile-design-decisions.md
  - engineering/architecture/adr.md
  - engineering/practices/federated-pr-review.md
  - engineering/practices/code-review-policy.md
  - leadership/decision-facilitation.md
  - leadership/principal-engineer-influence.md
  - leadership/principal-engineer-consensus.md
  - engineering/architecture/design-systems-ai-control-plane.md
  - engineering/practices/ai-augmented-engineering-team.md
  - leadership/senior-ic-role.md
source: "https://gist.github.com/fabianmagrini/15ea9a5d1d053a42b1d22ab788290e91"
updated: 2026-06-15
---

# Architecture Decision Forum

An **architecture decision forum** is a standing, cross-team body that advises on
high-blast-radius design decisions. Its defining choice is to be **advisory, not a
gatekeeper**: it exists to raise the quality and consistency of decisions while preserving
team autonomy — not to approve or block work.

It is the operational home for the **global / cross-cutting (Tier C)** decisions in
[agile design decisions](../engineering/architecture/agile-design-decisions.md): the guild sets
guardrails, teams move freely between them. Its currency is the [ADR](../engineering/architecture/adr.md).

## Principles

The framing matters more than the mechanics. Lead with intent:

1. **Advisory first, governance second** — guide, don't approve.
2. **Consensus over authority** — decisions come from informed agreement, not hierarchy.
3. **Context over dogma** — judge proposals on their situation, not rule adherence.
4. **Pragmatism over perfection** — delivery timelines and business value are first-class.
5. **Transparency by default** — decisions and rationale are discoverable.
6. **Decentralised ownership, central alignment** — teams own their decisions; the forum
   keeps them coherent.

## What it reviews — and what it doesn't

The forum's reach must be *deliberately limited* or it becomes a bottleneck. Define a small
set of **mandatory triggers** — decisions whose blast radius justifies a cross-team
conversation. Typically these are choices that are hard to reverse or that cross team
boundaries, e.g.:

- New or significantly restructured **cross-team components** (shared services, frontends).
- New **integration boundaries / APIs**, or major changes to existing ones (prevents domain
  leakage and duplication).
- **Exceptions to a standard** — a waiver from an agreed default (a non-standard language,
  a component outside the design system). The standard is the guardrail; the forum reviews
  the *exception*, not every conformant choice.

**Explicitly out of scope** (state this in the charter):

- Low-risk, team-local implementation details.
- Routine development decisions.
- Purely stylistic or coding-convention choices.

If a team can reverse it cheaply on their own, it doesn't belong here — see Type 2 (two-way
door) decisions in [agile design decisions](../engineering/architecture/agile-design-decisions.md).

## Roles

Define roles, not a fixed roster:

| Role | Responsibility |
|---|---|
| **Facilitator** | Organises sessions, drives toward consensus, keeps it constructive |
| **Architecture representatives** | Bring cross-domain context and consistency |
| **Proposing team** | Owns the problem context and the quality of the proposal |
| **Participants** | Engage constructively — objections must be specific and evidence-based |

## Process

1. The proposing team submits an **ADR** stating problem, constraints, and trade-offs.
2. Pre-read materials are circulated; participants review **in advance**.
3. Structured discussion: context → proposal → questions → objections → convergence.
4. Outcome: **Accepted** / **Accepted with conditions** / **Rework required**.
5. The decision is recorded in the central ADR repository.

**Healthy-objection rule:** objections must be specific, evidence-based, and constructive.
Consensus means *no strong, reasoned objection remains* after everyone is heard — not
unanimous enthusiasm.

**Disagree and commit:** once consensus is reached, everyone supports the decision, even if
it wasn't their preference. Escalation to leadership should be rare.

## Measuring it

Measure **outcomes, not activity** — a forum optimising for volume has missed the point:

- Reduced lead time for complex decisions.
- Decreased rework and architectural drift.
- Increased adoption of shared patterns.
- Improved engineering satisfaction and trust.
- High-quality, discoverable decision records.

## Relationship to PR review

This forum decides *direction* (should we build it this way?); code review and
[federated PR review](../engineering/practices/federated-pr-review.md) govern *implementation* (was it built well?).
Keep them separate — pushing architectural debate into PRs is slow and late; pushing
line-level review into the forum wastes everyone's time.
