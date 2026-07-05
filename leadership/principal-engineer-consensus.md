---
title: Consensus Among Principal Engineers
tags: [leadership, decision-making, governance, communication]
topic: leadership
status: notes
level: advanced
related:
  - leadership/principal-engineer-influence.md
  - leadership/decision-facilitation.md
  - leadership/architecture-decision-forum.md
  - engineering/practices/federated-pr-review.md
  - leadership/first-principles-thinking.md
  - engineering/architecture/adr.md
  - leadership/managing-sideways.md
updated: 2026-06-29
---

# Consensus Among Principal Engineers

For a group of Principal Engineers (PEs), consensus is not unanimity and it is
not a democratic vote. At this level the decisions carry massive scale, high
ambiguity, and deep architectural trade-offs — so consensus has to mean something
sturdier than "everyone agrees." It means **informed consent, a shared
understanding of the trade-offs, and unified commitment to a path forward.**

## Consent, not preference

Consensus rarely means "we all agree this is the best idea." It means: *"I have
been heard, I understand the trade-offs we are making, and I believe this path is
safe enough to proceed."*

- **The "live with it" test.** The operating question is not "Is this your
  favourite solution?" but "Can you live with this, and will you support it?"
- **Disagree and commit.** PEs will often fundamentally disagree on the *best*
  approach. Consensus is reached when the dissenters explicitly drop their
  opposition, adopt the chosen direction, and help it succeed — without saying "I
  told you so" if things get rocky.

## Why it isn't voting

Voting is an anti-pattern for senior engineering leadership.

- **Technical truth is not a democracy.** If four PEs vote for a migration
  strategy and the fifth identifies a flaw that will cause cascading failure, the
  4-to-1 vote is a disaster, not a mandate.
- **It avoids winners and losers.** Voting makes someone's idea "win."
  Engineering is about optimising constraints, not winning arguments.
- **Use the tools instead.** RFCs, design docs, and rigorous peer review beat an
  idea into shape iteratively until the group can align behind it.

## The power and responsibility of the veto

A veto is a real and necessary tool at this level — the architectural equivalent
of pulling the "stop the line" cord — but it carries immense responsibility.

- **What justifies it.** Not disliking a technology or preferring a different
  pattern. A veto is for **unacceptable systemic risk**: violating a
  non-negotiable principle (data security, privacy) or risking catastrophic
  cascading failure across organisational boundaries.
- **The veto tax.** A PE who vetoes cannot just say "no." They must explain
  precisely *why* the risk is unacceptable, back it with data, and actively help
  find an alternative. A hard block puts the vetoer on the hook to help unblock
  it. (Compare the guardian-veto discipline in
  [Federated PR Review](../engineering/practices/federated-pr-review.md): a veto
  must include concrete reasoning and an alternative.)

## Shared ownership of the "why"

Consensus means everyone understands *why* a decision was made — and owns it
collectively. If an outage happens six months later, no PE gets to say "well,
that was Sarah's design." You agreed to the trade-offs (e.g. speed to market over
perfect scalability), so you collectively own the consequences.

## Escalation as a feature, not a bug

Sometimes a PE group genuinely cannot reach consensus: the vetoes are valid, the
trade-offs are contested, stalemate. In a healthy culture **escalation is part of
consensus.** Recognising gridlock and agreeing to escalate (to a Distinguished
Engineer, VP of Engineering, or CTO) is itself a form of consensus: *"We agree
that we cannot agree, we have documented our opposing views clearly, and we are
asking leadership to make a business-level call on which trade-off to
prioritise."*

## Summary

For Principal Engineers, consensus means moving from **"my design vs. your
design"** to **"our shared understanding of the risks."** It requires setting ego
aside, trusting peers' expertise, wielding vetoes only to prevent disaster, and
committing fully once a path is chosen.
