---
type: note
title: The Substitution Myth in Code Review
description: "John Allspaw's resilience-engineering objection to replacing review with agents: decompose, replicate, declare redundant — while the contribution that mattered was the integration across functions. Seven non-detection functions enumerated, plus Laycock's proposal for where they relocate."
tags: [ai-engineering, code-review, culture, reading]
topic: engineering/ai-native
status: notes
level: intermediate
related:
  - engineering/ai-native/review-replacement.md
  - concepts/control-and-complexity.md
  - engineering/ai-native/agentic-code-review.md
  - engineering/practices/code-review-policy.md
  - engineering/ai-native/linters-over-ai-review.md
  - case-studies/intercom-ai-pr-approval.md
  - engineering/architecture/comprehension-as-architecture.md
  - leadership/learning-culture-ai-agents.md
  - reading/ai-productivity-research.md
  - engineering/ai-native/accountability-for-unread-code.md
  - reading/state-of-tech-2026.md
  - leadership/decision-facilitation.md
source: "https://www.adaptivecapacitylabs.com/2026/08/24/there-is-more-to-code-review-than-automatable-detection/; https://martinfowler.com/rachels-ramblings/code-review.html"
updated: 2026-10-25
---

# The Substitution Myth in Code Review

John Allspaw (Adaptive Capacity Labs, August 2026) responds to the preprint *"The End of Code
Review: Coding Agents Supersede Human Inspection"* (arXiv:2606.13175) with an objection from
resilience engineering rather than from practice.

His diagnosis of the argument's structure:

> The most fundamental issue I have with the article is that it assumes code review is first
> and foremost a **detection** process.

Grant that premise and the conclusion follows mechanically — a **three-step substitution
pattern**: decompose the practice into measurable functions, demonstrate that machines replicate
each one, declare the human redundant. Allspaw's counter is that "the human contribution that
mattered most was the **integration** across functions", which no decomposition captures because
it is not one of the parts.

**Two notes on the source.** The thing being critiqued is an **arXiv preprint, not peer-reviewed
work**, which is worth knowing given how strong its title's claim is. And Allspaw links to "the
substitution myth" as an established idea but does not define or attribute it here — it belongs
to the automation-and-human-work literature this consultancy works in, and this note does not
assert a provenance the article itself does not give.

## The seven functions

The reusable artefact. Each is something peer review does that a detector does not, so each is a
thing silently given up when review is replaced rather than extended.

| Function | Why substitution does not cover it |
|---|---|
| **Confusion as signal** | *"When an experienced engineer reads a diff and says 'I don't understand this.', their confusion **is** the finding. It means the code is either too complex, the abstraction is wrong, or the intent is not clear."* |
| **Scepticism about necessity** | "Should this be two PRs?" — questioning intent and scope *before* correctness. Often the last moment at which whether-to-build-this-at-all can still be raised |
| **Detecting absence** | *"A human reviewer can notice that an API contract has changed but the error handling didn't. They can notice what is missing"* — the agent reviews what is there |
| **Calibrated attention** | Scrutiny adjusted to the author's experience and the organisational risk context, rather than every diff treated alike |
| **Bidirectional cognition** | Review as **coactive work**: the discussion changes *both* parties' mental models. Not information transmission in one direction |
| **Contextual knowledge** | Incidents, deprecations and legal constraints that live outside the repository entirely |
| **Accountability** | *"Being aware that you are personally responsible for approving a change shapes how you review it. It is the 'skin in the game.' An agent that 'signs off' on a pull request bears no consequences and certainly has no incentive structure."* |

**Confusion as signal is the sharpest**, because it identifies something structurally
unavailable rather than merely harder. A reviewer's incomprehension is a measurement of the
*code*, taken using the reviewer as the instrument. An LLM always processes the diff — it has no
state corresponding to "this does not make sense to a competent reader", so the signal is not
degraded by automation, it is absent. **Absence blindness** names the parallel gap on the fourth
row: a detector scores what is present.

## The pairing worth reading it with

[Control and Complexity](../../concepts/control-and-complexity.md) — Fred Hebert, from the same
tradition — objects that proposals to replace a practice with automated barriers "rarely question
what emergent roles the practice may have nor how static barriers may qualitatively differ from
more adaptive ones."

**That is the question; this is the answer.** Hebert poses the gap abstractly and gives code
review as a one-row example in his table (defect-finding and accountability under control,
"build awareness and provide a space for feedback" under complexity). Allspaw fills the row in
with seven entries. Read in sequence, the two notes supply a general mechanism and then its
worked instance, which is why they are more useful together than apart.

## Where the repo already corroborates him

The accountability argument is the one these notes can check independently, and it holds up:

- [Replacing Code Review With Upstream Verification](review-replacement.md) arrives at the same
  observation from the opposite direction, surveying the spectrum of positions and noting that
  "every middle position retains something both endpoints lack: **a named human accountable for
  a specific change**."
- [Intercom's AI PR Approval](../../case-studies/intercom-ai-pr-approval.md) is the practical
  version: accountability does not vanish under auto-approval, it **relocates from reviewer to
  author**. That is consistent with Allspaw — the function is real and someone must hold it —
  while showing it need not be the reviewer specifically.

So the strongest form of his point is not "humans must review" but **"these functions must be
held by someone, and a detector holds none of them."** Where a team moves a function elsewhere
deliberately, the objection is answered; where it is dropped silently because a benchmark
covered the detection half, it is not.

## Where the functions could go

Allspaw names the bill without paying it (below). **Rachel Laycock** (CTO at Thoughtworks,
September 2026) supplies a destination in
[*Maybe We Shouldn't Be Reviewing All This Code*](https://martinfowler.com/rachels-ramblings/code-review.html),
and the two pieces fit together more tightly than either author appears to intend.

Her move is to relocate the functions rather than automate or abandon them:

> "If we want **knowledge transfer**, pair. Sitting next to someone, physically or virtually,
> while they reason through a problem teaches you far more than reading their completed solution
> afterwards."

Pairing and mob programming supply **bidirectional cognition** and knowledge transfer directly —
the discussion *is* the practice rather than a by-product of inspecting a finished diff. Team
design sessions supply **scepticism about necessity** earlier, while the change is still a
proposal. Her slogan for the target: **"We need engineers to understand systems, not diffs."**

The complement is **review by exception** — a human reviewer reserved for changes crossing a
sensitive security boundary, carrying a large blast radius, touching an unfamiliar part of a
critical system, "or simply something where the team says, *'I'm not confident about this.'*"

**That last trigger is the sharpest thing in her piece**, because it closes a loop with the
table above: it turns **confusion-as-signal from a review output into a review input**.
Allspaw's point is that a reviewer's incomprehension is a finding; Laycock's is that a self-
declared lack of confidence should be what routes the change to a reviewer in the first place.
Same signal, read before the work rather than after it.

Two caveats on her piece. The risk-tiering half is **well-held ground here** — it is
[Agentic Code Review](agentic-code-review.md)'s tiering and
[Rootly's risk labels](../../case-studies/rootly-pr-size-risk-labels.md) — and her "cognitive
and intent debt" framing is already carried from the peer-reviewed side in
[Five Studies on AI Productivity](../../reading/ai-productivity-research.md), which holds Brian
Houck, the source she attributes it to. Her motivating figures — Meta's "significant lines of
code per human-landed diff reportedly increased 106% in a year" and DX's "median pull request
size increasing 64%" — also arrive via Houck, and **she gives no direct citation for either**,
so they are second-hand and worth treating as indicative rather than as evidence.

What pairing does *not* obviously supply is **accountability** — the skin-in-the-game function.
Two people at one keyboard both authored the change; neither is the independent party signing
off on it. Laycock's review-by-exception half covers the high-risk cases, but for everything
routed away from review the question of who is answerable is left where
[Intercom](../../case-studies/intercom-ai-pr-approval.md) puts it: on the author.

## What Allspaw's piece does not do

Recorded because the absence shapes how much weight it carries: **there is no closing statement
of what Allspaw is and is not claiming**, and no positive proposal. It is a critique of one
preprint, not an account of what review should become as volume rises — which is the live
problem the rest of this cluster is working on. Read alone it tells a team what the bill is, not
how to pay it; the Laycock section above is one answer, and the spectrum in
[Replacing Code Review With Upstream Verification](review-replacement.md) is where teams whose
throughput genuinely cannot match agent output still have to place themselves.

## Relationship to other notes

- [Replacing Code Review With Upstream Verification](review-replacement.md) — the position being
  argued against, and the holder of the five-position spectrum. This is its principled
  counter-endpoint: the others on that spectrum are empirical reports, this is an argument about
  what the practice *is*.
- [Control and Complexity](../../concepts/control-and-complexity.md) — the general mechanism
  (above); this is its worked instance in one practice.
- [Agentic Code Review](agentic-code-review.md) — the tiered middle position, which already holds
  "the human does not leave; the human moves up a loop". Allspaw supplies the reason that
  relocation is necessary rather than merely cautious.
- [Code Review Policy](../practices/code-review-policy.md) — asserts in one line that review is
  "a collaborative design and learning mechanism that improves both the code and the team". This
  is the theory under that assertion, and the argument for why it is not decoration.
- [Linters Over AI Review](linters-over-ai-review.md) — compatible rather than opposed. Moving
  deterministic checks into the editor removes work review should never have been doing; the
  seven functions are what remains once it is removed.
- [Comprehension as an Architectural Characteristic](../architecture/comprehension-as-architecture.md)
  — confusion-as-signal is comprehension decay made audible at the moment it occurs. That note
  measures understanding with fitness functions after the fact; a reviewer saying "I don't
  understand this" is the same property reporting itself in real time.
