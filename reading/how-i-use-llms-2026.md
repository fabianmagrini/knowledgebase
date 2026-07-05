---
title: How I Use LLMs as a Staff Engineer (2026)
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
source: "https://www.seangoedecke.com/how-i-use-llms-in-2026/"
updated: 2026-06-27
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
