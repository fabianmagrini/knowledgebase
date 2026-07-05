---
title: Test Coverage Policy
tags: [testing, ci-cd, ai-engineering, governance]
topic: engineering/practices
status: notes
updated: 2026-06-15
related:
  - engineering/practices/api-contract-functional-testing.md
  - engineering/practices/engineering-playbook.md
  - engineering/ai-native/ci-cd-ai-engineering.md
  - engineering/practices/code-review-policy.md
  - engineering/ai-native/eval-driven-ai-development.md
  - engineering/practices/performance-testing-strategy.md
  - engineering/practices/change-absorption-capacity.md
  - engineering/ai-native/loop-driven-development.md
  - concepts/continuous-delivery.md
source: "https://gist.github.com/fabianmagrini/e95a24606e7108a7e0673de02d739be3"
---

# Test Coverage Policy

Code coverage is a means to an end — **confidence in changes** — not a goal in itself. High coverage does not guarantee good tests. A single global percentage target is the wrong instrument.

> The goal is not to maximise coverage %, but to maximise confidence per change.

## Core principles

**Coverage ≠ quality.** Prioritise meaningful behaviour-focused tests over artificially high percentages.

**Optimise for confidence, not metrics.** Can we change this code safely and quickly? Coverage should reflect risk and criticality.

**Test behaviour, not implementation.** Prefer black-box/behavioural tests. Avoid brittle tests tied to internal implementation details.

**Scale coverage with risk.** Not all code requires the same level of coverage.

**AI-assisted testing is encouraged, not trusted blindly.** AI can generate test scaffolding and suggest edge cases, but humans must validate relevance and correctness.

## Risk-based coverage targets

These are guidelines, not hard absolutes.

| Risk level | Examples | Target | Scope |
|---|---|---|---|
| 🟢 Low | UI rendering, simple transformations, non-critical utilities | 60–70% | Key paths only |
| 🟡 Medium | Core business logic, APIs within established patterns | 70–85% | Happy paths + key edge cases |
| 🔴 High | Auth, payments, data integrity, shared libraries, complex domain logic | 85–95%+ | Edge cases, failure scenarios, integration tests |

## Coverage by test type

**Unit tests** — fast, isolated, validate logic and edge cases. Form the foundation of coverage.

**Integration tests** — validate interactions between components and services. Critical for APIs, data flows, and persistence layers.

**End-to-end tests** — validate critical user journeys. Fewer in number, high value. Do not attempt to achieve high coverage through E2E tests alone.

## What good coverage looks like

- Critical paths are well-tested
- Edge cases are explicitly validated
- Tests are readable and maintainable
- Failures provide clear, actionable signals

## AI-augmented testing guidelines

**Appropriate uses:**
- Generate initial test scaffolding
- Suggest edge cases
- Fill obvious coverage gaps

**Required human oversight:**
- Validate test intent and assertions
- Confirm edge case relevance
- Remove redundant or low-value tests

**Anti-patterns:**
- Accepting AI-generated tests without review
- Inflating coverage with shallow assertions
- Coverage inflation: AI generates many trivial tests that pass CI but add no confidence

## Enforcement

Use soft thresholds, not hard blocks, as the default:

- Alert if coverage drops more than 2–5% in a PR
- Hard gates are optional and reserved for critical systems

**At PR review, assess:**
- Are the right things tested?
- Are edge cases covered?
- Are tests meaningful and maintainable?

Do not approve PRs with missing critical test coverage or superficial/misleading tests.

## Anti-patterns

| Anti-pattern | Description |
|---|---|
| Gaming the metric | Writing trivial tests (getters, setters) solely to increase % |
| Over-testing low-value code | Excessive tests on simple or low-risk logic |
| Under-testing critical paths | Missing tests on high-impact areas |
| Brittle tests | Tests that break with minor refactoring |
| Coverage inflation | Blindly accepting AI-generated tests with shallow assertions |

## Definition of done

A change is complete when:

- Appropriate tests are added or updated
- Critical paths are covered to the appropriate risk tier threshold
- Tests pass reliably in CI
- Coverage is sufficient for the level of risk — not necessarily maximised
