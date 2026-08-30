---
type: note
title: Control and Complexity
description: "Two incompatible philosophies of systems design — decomposition and control versus complexity and emergence — and why the same practice serves different purposes depending on which one you are actually running."
tags: [system-design, architecture, decision-making, reading]
topic: concepts
status: notes
level: advanced
related:
  - concepts/constraints-as-a-lens.md
  - concepts/resilient-software-design.md
  - engineering/ai-native/review-replacement.md
  - engineering/ai-native/linters-over-ai-review.md
  - engineering/ai-native/spec-driven-development.md
  - engineering/architecture/comprehension-as-architecture.md
  - sre/self-blame-in-incident-reviews.md
  - sre/heroic-saves-are-near-misses.md
  - engineering/architecture/runtime-architecture-verification.md
source: "https://ferd.ca/control-and-complexity-tension-in-systems-design.html"
updated: 2026-08-30
---

# Control and Complexity

Fred Hebert (August 2026) names two philosophies of systems design that most organisations hold
simultaneously without noticing, and argues that the incoherence between them is where policy
goes wrong.

| | **Analytical decomposition / control** | **Complexity / emergence** |
|---|---|---|
| How you understand a system | Break it into analysable parts; causality is traceable | The system "resists analytical decomposition" — interconnected, history-dependent, dynamic |
| What you can do to it | Predict and control through "division, analysis, and understanding" | It is "influenced more than controlled" |
| What intervention looks like | Top-down enforcement, deterministic guarantees | Adaptive and iterative rather than predictive |
| Characteristic failure | Fewer large failures, but brittleness | Adaptation is possible, but alignment can drift |

The label for the first is **Cartesian-Newtonian**: the assumption that a whole is the sum of
analysable parts. It is not wrong — it is what makes deterministic software possible — and the
argument is not that one view defeats the other.

**Provenance.** An essay from a practitioner in resilience engineering, grounded in outside
literature (Le Coze, George Box, cybernetics, human factors) rather than in reported experience.
No data, and none claimed; the piece is doing conceptual work.

## The same practice, two purposes

The reusable part. Hebert's table sets out activities that look identical on a calendar and are
doing entirely different jobs depending on which philosophy is actually running. A selection:

| Activity | Under control | Under complexity |
|---|---|---|
| **Code review** | "Find bugs and flaws; track and assign accountability; ensure quality" | "Build awareness and provide a space for feedback within and across teams" |
| **SLOs** | "Organizational tool to ensure all teams manage their reliability adequately" | "Prioritization tool whose value comes from having teams discuss and define what is an acceptable level of reliability" |
| **Safety** | "Prevent undesirable behaviours that lead to failure. Hazards are to be contained or designed out" | "Foster positive behaviours that lead to success. Find how people bridge gaps in processes, work around obstacles, and recover" |
| **Correctness** | "The software does what the specification or API says it should" | "Users or customers are able to successfully accomplish their tasks; goals can shift based on their needs" |
| **Incident response** | "Runbooks define best practices. Protocols and processes are defined to investigate and triage problems efficiently" | "Surprises may require improvisation. Build capacity to deal with the unknown. Investigations must look into normal work" |
| **Standards** | "Written unambiguously based on verifiable processes and outcomes to make enforcement tractable" | "Written in a goal-oriented manner as to support and guide the people who execute the work and who need to adapt rules" |
| **Chaos engineering** | "Validating that expected failure cases are properly tolerated or recovered from" | "Experimentation-driven exercise in which participants form theories about their system's behaviour" |
| **Refactoring** | "Pay down technical debt, reduce complexity, improve maintainability" | "Countering entropy, adapting a code base to changing contexts based on new information" |

The practical use is diagnostic. A team that believes it runs code review for feedback and
awareness, while its policy, metrics and tooling are all built for defect-catching and
accountability, will keep being surprised by what its review process does. The mismatch is
between *stated intent* and *the machinery actually installed*, and neither half is visible from
inside the other.

## Hidden adaptations

The concept that gives the table its teeth: practitioners quietly repurpose a control for
benefits it was never designed to deliver. A review gate becomes the place a junior engineer
learns the codebase; a runbook step becomes the moment someone notices the dashboard is stale.

These adaptations are invisible in any description of what the control is *for*, which means
**they are invisible in the business case for replacing it**. Swap the control for an automated
equivalent that satisfies the stated purpose, and the unstated ones vanish without anyone having
decided to give them up.

## Le Coze's three unpredictabilities

Borrowed to explain why accidents keep evading prevention:

| Category | What it says |
|---|---|
| **Deterministic** | "Properties of the technological systems themselves (such as tight coupling and complexity) will eventually defeat efforts to prevent accidents" |
| **Epistemic** | Organisations suffer "failures of foresight where weak signals and indicators that accidents are incubating will not be seen or accepted by the structures of power" |
| **Self-organising** | Systems are adaptive, so successes and failures alike emerge as "consequences emerging from systems' self-organization" |

Only the first is a technical property. The second is about power — who is permitted to notice —
and the third is about adaptation producing outcomes nobody designed.

## What this says about AI-driven process change

The essay's occasion is LLM adoption, which has led "countless organizations to rapidly change
their practices and structures" without examining the design assumptions underneath. Hebert
names two proposals directly, and both have notes here:

- **Replacing code review with automated barriers.** His objection is that such proposals rarely
  ask "what emergent roles the practice may have nor how static barriers may qualitatively
  differ from more adaptive ones." This is the general form of the specific objections in
  [Replacing Code Review With Upstream Verification](../engineering/ai-native/review-replacement.md)
  and [Linters Over AI Review](../engineering/ai-native/linters-over-ai-review.md) — a static
  check can satisfy the control-column purpose while silently deleting the complexity-column one.
- **Black-box specs.** He objects to "splitting software work into high-level specs to be
  translated to code in a black box with external checks only, without offering explanations
  around how the specs may cover varying abstraction layers" — a caution worth reading against
  [Spec-Driven Development](../engineering/ai-native/spec-driven-development.md).

**He is not arguing for the complexity view.** The recommendation is a combined approach: use
complexity-aware methods to understand how the system's parts actually interact, then design
"simple but high-leverage checks and barriers such that minimal control yields high rewards."
Control is the cheap and durable instrument once you know where to put it; the error is choosing
where to put it by decomposition alone.

The question he offers for any proposed change is the portable takeaway: **what depends on the
current behaviour, and what are the second-order impacts of removing it?** He invokes Box —
all models are wrong, and the useful question is whether yours is *importantly* wrong — and
closes with "systems are systems. They will keep acting like systems, and failing like systems."

## Relationship to other notes

- [Constraints as a Lens](constraints-as-a-lens.md) — the other cross-cutting frame in this
  folder, and a useful contrast. That hub unifies three senses of one idea; this one holds two
  genuinely incompatible ideas apart and argues the value is in knowing which you are using.
- [Resilient Software Design](resilient-software-design.md) — the same problem approached from
  engineering. Friedrichsen's designing-for-failure is control-flavoured by comparison: it
  enumerates failure modes to contain them, where the complexity view attends to how operators
  recover from the ones nobody enumerated. Complementary rather than opposed.
- [Replacing Code Review With Upstream Verification](../engineering/ai-native/review-replacement.md)
  and [Linters Over AI Review](../engineering/ai-native/linters-over-ai-review.md) — those notes
  argue against the review-replacement proposal on evidence; this supplies the theory that
  explains the class of error, and is the more portable of the two.
- [Comprehension as an Architectural Characteristic](../engineering/architecture/comprehension-as-architecture.md)
  — shared understanding is exactly the kind of emergent good that decomposition-thinking cannot
  see, because no component is responsible for it.
- [Runtime Architecture Verification](../engineering/architecture/runtime-architecture-verification.md)
  — a concrete instance of the static-barrier objection, arrived at independently: an import rule
  satisfied its stated purpose while a synchronous HTTP call walked around the architecture it
  was meant to enforce, visible only by observing the running system.
- [Self-Blame in Post-Incident Reviews](../sre/self-blame-in-incident-reviews.md) — already
  borrows Hebert's "superficial blamelessness". Redirecting toward local rationality *is* the
  complexity view applied to one conversation; "be more careful" is the control view's answer.
- [Heroic Saves Are Near Misses](../sre/heroic-saves-are-near-misses.md) — the Safety row in
  practice. Chapman's argument that a save should be investigated like an outage is complexity
  reasoning: study how people actually bridged the gap, rather than only designing hazards out.
