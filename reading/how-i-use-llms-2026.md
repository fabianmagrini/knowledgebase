---
type: reading
title: How I Use LLMs as a Staff Engineer (2026)
description: "Notes on Sean Goedecke's account of his personal 2026 LLM workflow — the delegation boundary, the human-signal practices, and the interrogation habit aimed at design errors that compilers and tests cannot catch."
tags: [ai-engineering, agentic-workflows, reading]
topic: reading
status: notes
level: intermediate
related:
  - engineering/ai-native/quality-first-ai-coding.md
  - engineering/ai-native/modern-engineering-values.md
  - reading/building-effective-agents.md
  - engineering/ai-native/prompt-engineering-for-programmers.md
  - engineering/ai-native/agentic-code-review.md
  - engineering/ai-native/ai-native-engineering-overview.md
  - reading/offloading-thinking-to-ai.md
  - reading/ai-productivity-research.md
  - reading/the-capability-overhang.md
  - leadership/decision-facilitation.md
  - case-studies/github-copilot-rust-migration.md
  - languages-and-frameworks/rust-for-agentic-development.md
  - engineering/ai-native/accountability-for-unread-code.md
source: "https://www.seangoedecke.com/how-i-use-llms-in-2026/; https://www.seangoedecke.com/you-should-all-be-asking-way-more-questions/"
updated: 2026-10-25
---

# How I Use LLMs as a Staff Engineer (2026)

Notes on Sean Goedecke's account of his personal 2026 LLM workflow. It is one
practitioner's opinionated practice, not a framework, but it is a useful
**delegation map**: where a staff engineer draws the line between work to hand to
agents and work to keep. Its organising idea is to *"shift as much work onto AI
agents as possible, without going too far."*

It is the human-workflow counterpart to the *when not to use agents* guidance in
[Building Effective Agents](building-effective-agents.md): the same boundary,
drawn task by task from daily practice.

## The delegation map

| Posture | Work | Notes |
|---|---|---|
| **Delegate first** | Bug investigation; integration tests; setup/config automation; local troubleshooting | Agents diagnose ~80% of bugs autonomously; config troubleshooting is "a quicker Google" |
| **Delegate, then review hard** | Code changes | Start *every* change with an agent; ~30s triage; reject across 5–6+ iterations on hard tasks; strip "LLM-isms" / over-commenting; careful human review when it looks promising |
| **Never delegate** | PR descriptions, ADRs, Slack messages, issues, blog posts; untested AI code; UI work | Public communication and architecture writing stay human; agents "over-communicate and are bad at expressing the core idea" |

## Distinctive reframings

- **Finder vs. solver.** Even when an agent fixes a bug, Goedecke counts himself
  the "finder" — his value is *narrowing the search space* and curating context
  (logs, Slack threads, independent reproductions), not typing the fix. A tricky
  recent bug took 14 agent sessions.
- **Test code is cheap.** He reads test code with a "more generous eye" than
  production code and delegates integration tests liberally — while avoiding UI
  test automation.
- **Human-written comms as a signal.** Writing PR descriptions and ADRs by hand is
  deliberate: it signals that a human reviewed the change and conveys the core idea
  the agent would bury. This is a social, not just a quality, choice.
- **Context curation is the job.** His leverage comes from feeding the agent the
  right context, echoing
  [Prompt Engineering for Programmers](../engineering/ai-native/prompt-engineering-for-programmers.md).

## Evolution from a year earlier

- Previously **avoided agent-driven PRs entirely**; now they are his default.
- Reliance on agents for **bug investigation grew sharply**.
- Testing philosophy shifted toward **treating test code as cheap and delegating
  it liberally**.

Tools named: the GitHub Copilot app (used heavily, tens of sessions a day) and
Copilot CLI; models including GPT-5.5 and Anthropic models. As with any personal
workflow, the tool choices are incidental — the transferable content is the
*delegation boundary* and the *human-signal* practices.

## Interrogating the model, and the error class it targets

A [later post](https://www.seangoedecke.com/you-should-all-be-asking-way-more-questions/)
(September 2026) supplies the verification habit behind the "review hard" posture, and names the
failure it is aimed at:

> They make design mistakes all the time. They assume that two services can talk to each other
> when in fact they can't, or they forget about the fact that their code has to run both in the
> cloud and on-premises.

**Both examples are design errors, not code errors** — and that is exactly the class these notes
have measured automated gates missing.
[The Copilot Rust migration](../case-studies/github-copilot-rust-migration.md) found ownership,
borrowing and lifetime errors at **1.7%** of diagnostics while the dozens of real regressions
were *"semantic, not type errors"*;
[Rust for Agentic Development](../languages-and-frameworks/rust-for-agentic-development.md)
carries Matsakis conceding that type systems prevent wrong actions without establishing that the
right thing happened. A compiler cannot know that two services are on different networks, or that
a flagship guarantee forbids a topology.

His questions are therefore aimed at assumptions rather than correctness — *"Do we do X elsewhere
in this codebase? Does service Y really support this type of authentication, or are you assuming
we'd have to go build that too?"* — with a self-reported hit rate worth recording precisely
because nothing else here has one:

> About half the questions I ask get answers that convince me the model has made a mistake.

Self-reported, unmeasured, and from the same practitioner-account genre as the rest of this note.
Taken at face value it says the design-error rate is high enough that interrogation is not an
optional polish step, which is the practical form of the *"can I explain this?"* test in
[Accountability for Unread Code](../engineering/ai-native/accountability-for-unread-code.md) —
that note has the test and no technique for applying it. The listener-side mechanics, including
simulating the implementation while the plan is described, are folded into
[Facilitating Technical Decisions](../leadership/decision-facilitation.md).

## Relationship to other notes

- [Quality-First AI Coding](../engineering/ai-native/quality-first-ai-coding.md) —
  a complementary practitioner note: that one is a *technique* (multi-model bug
  review, quality over velocity); this is a *delegation taxonomy* (what to hand
  over at all). Both treat careful human review as the non-negotiable.
- [Modern Engineering Values](../engineering/ai-native/modern-engineering-values.md)
  — the values (taste, guardrails, ownership) behind where this engineer draws the
  line.
- [Building Effective Agents](building-effective-agents.md) — the principled
  "when not to use agents"; this note is the lived version.
- [Agentic Code Review](../engineering/ai-native/agentic-code-review.md) — the
  human-on-the-loop review that his "review hard" posture depends on.
