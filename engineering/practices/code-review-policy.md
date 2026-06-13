---
title: Code Review Policy
tags: [code-review, ci-cd, ai-engineering]
topic: engineering/practices
status: notes
updated: 2026-06-13
related:
  - engineering/practices/federated-pr-review.md
  - engineering/practices/engineering-playbook.md
  - engineering/practices/ci-cd-ai-engineering.md
  - engineering/practices/trunk-based-development.md
  - engineering/practices/test-coverage-policy.md
  - engineering/practices/ai-native-engineering-stack.md
  - engineering/architecture/agile-design-decisions.md
  - engineering/architecture/adr.md
  - engineering/practices/architecture-decision-forum.md
  - tools/git.md
  - engineering/security/secure-sdlc.md
source: "https://gist.github.com/fabianmagrini/e95a24606e7108a7e0673de02d739be3"
---

# Code Review Policy

Code review is a core engineering practice for quality, alignment, and shared ownership. It is not a gate or formality — it is a collaborative design and learning mechanism that improves both the code and the team.

## Principles

**Optimise for system throughput, not individual speed.** Code review exists to improve the overall flow of change: reduce defects escaping to production, maintain consistency, enable safe frequent deployments. Local speed (merging quickly) must not come at the cost of global inefficiency (rework, incidents, divergence).

**Review for intent, not just implementation.** The most valuable reviews focus on problem framing (is this solving the right problem?), design choices (are trade-offs clear and appropriate?), and maintainability (will this be easy to change in six months?).

**Small changes, fast feedback.** Prefer small incremental PRs. Review within same-day SLA where possible. Large PRs reduce review quality and increase cycle time. Practical thresholds: review no more than 200–400 lines at a time; maintain an inspection rate under 500 lines per hour; do not review for more than 60 minutes in a single session without a break.

**Shared ownership over individual ownership.** All code is team-owned. Code review spreads knowledge, reduces reliance on single owners, and enables safer future changes.

## What to look for

**Correctness** — Does the code do what it is supposed to do? Are edge cases handled?

**Design and architecture alignment** — Is this aligned with existing patterns, ADRs, and Solution Design Forum (SDF) decisions? Is a new pattern being introduced unnecessarily?

**Simplicity and maintainability** — Is this the simplest solution that works? Are abstractions appropriate? Is the code readable and well-structured?

**Test coverage** — Are there sufficient tests? Do tests validate behaviour, not just implementation? Are critical paths covered?

**Non-functional concerns** — Performance, security, observability (logging, metrics), error handling.

**AI-specific** — Hidden complexity introduced by AI; hardcoded values or credentials; over-engineered solutions; hidden dependencies.

## Author expectations

- Keep PRs small and focused
- **Self-review first** — read through your own diff before requesting review; catch typos, logic errors, and obvious issues before the reviewer sees them
- Provide clear context: what problem is being solved, why this approach, trade-offs considered
- **Annotate the diff** where reasoning is non-obvious — inline comments explaining why, not what, reduce reviewer cognitive load
- Link relevant ADRs, SDF discussions, and tickets
- Call out areas where feedback is specifically needed
- For AI-generated PRs: validate output, confirm correctness and intent before requesting review

## Reviewer expectations

- Review promptly — same-day SLA preferred
- Prioritise high-signal feedback: design issues, incorrect assumptions, maintainability risks
- Avoid excessive nitpicking — use automation for style and formatting
- Be explicit: label feedback as **blocking** or **non-blocking**
- Suggest improvements, not just identify problems

## Escalation model

Code review is not the right place for fundamental disagreements.

| When | Escalate to |
|---|---|
| Uncertainty about approach during development | Early design discussion with teammates |
| Significant architectural decision | ADR |
| New MFE, new API, new journey, language/framework exception, new platform pattern | Solution Design Forum (SDF) |

Do not wait until a PR to challenge core design decisions.

## Approval policy (risk-based)

Risk determines the level of scrutiny — not whether the code was written by a human or an AI agent.

### Roles

| Role | Responsibilities |
|---|---|
| AI author | Generates or modifies code; output must meet team standards and pass automated checks |
| AI reviewer | Automated review: quality issues, style, simple bug detection, test gaps, common security anti-patterns. **Non-binding** by default. |
| Human author | Validates AI-generated code; ensures correctness and alignment before requesting review |
| Human reviewer | Provides final approval; focuses on design correctness, business intent, trade-offs |

Only **human approvals count toward merge requirements**.

### Approval tiers

| Risk | Examples | Policy |
|---|---|---|
| 🟢 Low | Bug fixes, refactoring (no behaviour change), docs, tests | AI review + 1 human approval |
| 🟡 Medium | New features within established patterns, moderate logic changes | AI review + 1 human approval (2nd optional) |
| 🔴 High | Architectural changes, new patterns/frameworks, auth/payments, cross-team impact | AI review + 2+ human approvals, at least one domain expert, prior ADR/SDF alignment required |

**AI-generated PRs are Medium Risk minimum by default.** Human author must review, validate output, and confirm intent.

**Urgent production fixes:** 1 human approval preferred (can be bypassed if needed). Mandatory post-merge human review.

## Recommended workflow

```text
1. Author (human or AI) creates PR
2. AI review runs automatically
3. Author addresses AI feedback
4. Human reviewer focuses on design, intent, trade-offs
5. Approval granted → merge
```

Shift alignment left: use ADRs and SDF before raising a PR for anything with significant design implications.

## Anti-patterns

| Anti-pattern | Description |
|---|---|
| Rubber stamping | "LGTM" without meaningful review |
| Late surprise feedback | Raising fundamental concerns only at final review |
| Overly large PRs | Difficult to review; high risk of missed issues |
| Bikeshedding | Excessive focus on trivial issues |
| Blind trust in AI output | Merging AI-generated code without understanding it |
| Over-reliance on AI review | Assuming AI catches all issues |
| Ignoring AI signal | AI feedback often catches low-level issues cheaply |
| Inflating process for AI | Adding excessive approvals simply because AI was involved |

## Tooling and automation

Automate what can be automated — linting, formatting, type checking, tests, security scanning. This allows code review to focus on what humans do best: reasoning and judgment.

AI review should **reduce human cognitive load**, not add noise.

## Definition of done

A change is complete when:

- Code has been reviewed and approved per the appropriate risk tier
- Feedback has been addressed or resolved
- Tests pass and coverage is appropriate (see [[test-coverage-policy]])
- Relevant documentation and ADRs are updated
