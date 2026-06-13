---
title: Federated PR Review and Governance
tags: [code-review, ci-cd, microservices, ai-engineering]
topic: engineering/practices
status: notes
updated: 2026-06-12
related:
  - engineering/practices/ci-cd-ai-engineering.md
  - engineering/practices/polyrepo-branching-strategy.md
  - engineering/practices/trunk-based-development.md
  - engineering/practices/regulated-service-release-process.md
  - engineering/practices/engineering-playbook.md
  - engineering/practices/code-review-policy.md
  - engineering/practices/ai-native-engineering-stack.md
  - engineering/practices/architecture-decision-forum.md
source: "https://gist.github.com/fabianmagrini/a44c8ec5efdee0ebf57a4c7d31ed2f4d"
---

# Federated PR Review and Governance

PR review in multi-team codebases must function as a coordination, safety, and ownership system — not a universal quality gate. The core principle: **ownership defines who must review, not who can contribute**.

With agentic coding agents in the picture, this model must also absorb high PR volume, inconsistent context, and new failure modes that human review alone cannot catch at speed.

## Three planes

| Plane | Responsibility |
|---|---|
| Control | CODEOWNERS maps guardians to domains; branch protection enforces approvals |
| Automation | CI gates, contract validation, PR classification bots reduce manual burden |
| Workflow | Risk-based tier routing sends low-risk changes fast and flags cross-boundary changes for guardian review |

## Guardianship, not gatekeeping

Guardians maintain architectural integrity within their domain but cannot arbitrarily block changes. Any veto must include concrete reasoning and an alternative. Contribution stays open; accountability is assigned.

This is the key distinction from a gatekeeping model: the goal is flow with accountability, not control.

## Two-tier review routing

| Tier | Applies when | Requirement |
|---|---|---|
| Fast (Tier 1) | Low-risk, local, same-team change | Single reviewer |
| Safe (Tier 2) | Cross-domain, API/schema change, critical path, security-sensitive | Guardian approval |

Avoid the anti-pattern of requiring the same approval count for every PR — it makes low-risk work slow without making high-risk work safer.

### Agent PRs default to Tier 2 in sensitive domains

An agent PR touching authentication, payments, customer data, API contracts, or shared infrastructure should automatically route to Tier 2 regardless of apparent scope. Agents lack system-wide situational awareness; guardians provide it.

## PR intent declaration

Every PR — human or agent — should document:

```text
- What problem does this solve?
- What changed and why?
- What areas are impacted?
- Risk level and rollback strategy
- Test evidence
```

For agent PRs, the **prompt or task description is the spec**. Include it verbatim in the PR body. This makes intent auditable, reproducible, and reviewable — reviewers assess whether the agent interpreted the intent correctly, not just whether the code compiles.

```text
## Agent task
<paste the original prompt or task description>

## Implementation summary
<what the agent actually did>

## Files generated or modified
<list>

## Test evidence
<CI results, coverage delta>
```

## PR labelling

Label every PR by authorship so metrics and routing are unambiguous:

| Label | Meaning |
|---|---|
| `human-authored` | Written entirely by a human |
| `ai-assisted` | Human wrote it with AI help (Copilot, chat) |
| `ai-authored` | Generated end-to-end by a coding agent |

Label the agent identity too where possible (`agent:github-copilot`, `agent:claude-code`). This feeds audit sampling and metric correlation.

## What automation must handle

Human reviewers should not spend time on mechanical checks. Automate:

```text
Linting, formatting, type checking
Unit and integration test results
Security scanning (SAST, SCA, secrets detection)
API contract compatibility checks
Dependency vulnerability and licence checks
PR size and scope validation
Automatic tier classification
```

For agent PRs, add:

```text
Hallucinated API detection (grep for non-existent internal methods/endpoints)
Credential pattern scanning (agents may reproduce training data patterns)
Outdated package version flagging
Architectural boundary violation checks
```

## What humans must handle

After automation, reviewers focus on:

- Correctness of logic and business rules
- System-wide impact the author (human or agent) may not have context for
- Design decisions and maintainability
- Whether the agent interpreted the intent correctly
- Whether the stated risk and rollback plan are credible

Reviewers should not debate style (automation owns that), request unnecessary rewrites, or approve without understanding the change.

## Guardian responsibilities for agent PRs

When an agent PR enters a guardian's domain:

1. Verify the task description matches what was built
2. Check for silent contract changes — agents may change behaviour without changing signatures
3. Assess whether the change fits the domain's architectural direction
4. Confirm test coverage covers the actual risk, not just surface paths
5. No agent PR self-approves — a human guardian must be the final approver in their domain

## Contract discipline

APIs, events, and schemas are versioned contracts. Before merging any change to a contract boundary:

- Confirm backward compatibility or explicit versioning
- Identify all consumers and assess impact
- Require contract tests to pass
- Agents are particularly likely to silently break contracts — they optimise locally without awareness of downstream consumers

## Audit system

Audits are distributed, not centralised. Domain guardians sample PRs from their area based on:

- Risk tier (higher tier = higher sample rate)
- Outcome triggers: incidents, rollbacks, escaped defects, high revert rate
- Agent authorship (agent PRs sampled at a higher base rate until calibrated)

Audits assess decision quality, not activity. Questions:

```text
Did the reviewer understand the change?
Did they detect the real risks?
Was the feedback signal or noise?
Did the guardian enforce boundary integrity?
For agent PRs: was the intent correctly interpreted?
```

## Maturity levels

| Level | Characteristics |
|---|---|
| 1 | PR templates, basic CI, CODEOWNERS in place |
| 2 | Risk-based tier routing, automated classification, agent PR labelling |
| 3 | Contract-aware review, agent-specific checks, distributed auditing |
| 4 | Governance fully embedded in automation; humans focus on judgment calls only |

## Metrics

Track delivery and quality signals, with agent-specific breakdowns:

```text
Lead time per tier (Tier 1 vs Tier 2)
Review turnaround time
Change failure rate (human vs AI-authored)
Rollback rate (human vs AI-authored)
Escaped defect rate by authorship label
Review comment density per PR (signal vs noise ratio)
Guardian veto rate and resolution time
Agent PR rework rate
Percentage of agent PRs requiring major rewrite
```

Correlating defect and rework rates by authorship label tells you where automated checks need strengthening and where agent tooling needs calibration.

## Policy summary

> Teams use a two-tier review system rooted in CODEOWNERS guardianship. All PRs — human or agent — pass the same automated gates. Agent PRs are labelled, include the originating task description, and require human guardian approval in sensitive domains. No agent self-approves. Guardians protect boundaries without blocking flow; vetoes require reasoning and alternatives.
