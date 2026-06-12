---
title: Modern Web Engineering Playbook
tags: [architecture, microservices, ci-cd, ai-engineering, testing, observability, security]
topic: engineering/practices
status: notes
updated: 2026-06-13
related:
  - engineering/practices/ci-cd-ai-engineering.md
  - engineering/practices/federated-pr-review.md
  - engineering/practices/trunk-based-development.md
  - engineering/practices/api-contract-functional-testing.md
  - engineering/practices/regulated-service-release-process.md
  - engineering/practices/code-review-policy.md
  - engineering/practices/test-coverage-policy.md
  - engineering/practices/ai-native-engineering-stack.md
  - engineering/practices/agentic-sdlc.md
  - engineering/practices/agentic-ai-strategy-frameworks.md
  - engineering/architecture/c4-model.md
source: "https://gist.github.com/fabianmagrini/a970c210fd3267b50a1484721297c6eb"
---

# Modern Web Engineering Playbook

Engineering standards for enterprise web applications built on microfrontend architecture, BFF services, continuous delivery, and 12-factor principles.

> **AI is a force multiplier, not a substitute for engineering discipline. Teams move faster because of strong guardrails, not despite them.**

Any deviation from these standards must be intentional, explicit, and justified. Accidental deviation is not acceptable.

## Core principles

| Principle | Standard | With AI |
|---|---|---|
| Optimize for flow | Small batches, trunk-based, frequent deploys | AI accelerates throughput but must not increase risk |
| You build it, you run it | Teams own services end-to-end including production | AI assists; humans remain accountable for production outcomes |
| Default to simplicity | Prefer standard patterns over custom solutions | Constrain AI with clear standards and templates |
| Explicit trade-offs | All major decisions documented via ADRs | AI-generated proposals must include trade-offs |
| Trust but verify | — | Treat AI output as untrusted until validated; all AI contributions pass the same quality gates as human code |

## Architecture

### Microfrontend architecture

- Independently deployable frontends, owned by aligned domain teams
- Integrated via shell (app shell pattern)
- No direct coupling between microfrontends
- Communication via URL, events, and shared contracts only
- Shared dependencies minimized and versioned
- AI must not introduce hidden coupling between MFEs

### Backend architecture

- Backend-for-Frontend (BFF) per domain or experience
- APIs are versioned, contract-driven, and backward compatible by default

### Configuration

- All environment-specific values must be configurable; follow 12-factor config
- No secrets, PII, or environment values in source code, logs, or client-side code
- AI must not introduce hardcoded secrets or environment drift

## AI in the SDLC

### What AI agents may do

- Generate code
- Review code
- Write tests
- Propose designs
- Assist in root cause analysis and log summarisation during incidents

### What AI agents must not do

- Bypass governance or approve exceptions
- Deploy directly to production without controls
- Access sensitive data without authorisation
- Self-approve pull requests

### Human-in-the-loop requirements

- All production changes require human accountability
- Critical changes require human approval before merge
- AI suggestions must be reviewed before merge — treat as junior-level output

### Prompt and context management

- Version prompts where critical
- Provide AI with architecture constraints, coding standards, and security requirements as context
- Never expose sensitive data, secrets, PII, or credentials in prompts

### AI output validation

All AI-generated artifacts must:

- Compile and build successfully
- Pass tests
- Pass linting and security scans
- Meet performance expectations
- Not introduce hardcoded values, PII logging, or hidden dependencies

## Code quality

### Code review

- All changes reviewed before merge
- AI-generated code reviewed as junior-level output

Review focus:

```text
Correctness
Security
Maintainability
Adherence to standards
Hidden complexity introduced by AI
```

### Testing strategy

Test pyramid:

```text
Unit tests          → majority
Integration tests   → selective
E2E tests           → critical paths only
```

Coverage policy:

- Minimum 80% for business logic and critical paths
- No strict coverage requirement for UI rendering boilerplate
- AI-generated code must include tests by default
- Tests must be deterministic and run in CI
- Failing tests block deployment

### Static analysis

- Linting required
- TypeScript enforced as default language
- Security scanning integrated into CI
- AI must conform to all static analysis rules

## Security and data protection

- Never log PII (names, emails, tokens); mask or hash sensitive data where required
- Secrets managed via secure stores — never in source code, logs, prompts, or client-side code
- Validate all external inputs; prefer allowlists over denylists
- AI must not generate code that logs sensitive data or exposes credentials

## Observability

### Logging

Structured JSON logging including:

```text
request ID / correlation ID
service name
environment
log level (ERROR / WARN / INFO / DEBUG)
```

### Monitoring

- Define SLIs and SLOs for all services
- Monitor latency, error rate, and throughput

### Distributed tracing

- All services must propagate trace context for end-to-end request visibility

### AI observability

Track AI contributions as first-class metrics:

```text
% of code generated by AI
Defect rate: AI-generated vs human-written code
Rework rate by authorship label
AI-assisted decisions logged where relevant
```

This data identifies where automated checks need strengthening and where AI tooling needs calibration.

## Performance

- Optimize frontend bundle size; lazy load microfrontends
- Set latency budgets for APIs; avoid synchronous chaining of services
- Define thresholds for page load time and API response time

AI failure modes to guard against in review and CI:

```text
Over-engineered solutions
Hidden dependencies
Inefficient algorithms or queries
Unnecessary package additions
```

## Continuous delivery

### Pipeline

Fully automated CI/CD with required checks:

```text
Build
Tests + coverage thresholds
Linting and type checking
Security scanning
```

### AI guardrails in CI

- Detect AI-generated code patterns
- Block unsafe patterns (PII logging, hardcoded secrets, environment values)
- Apply stricter checks where AI authorship is flagged

### Deployment

- Blue/green or canary deployments
- Feature flags for safe rollout
- Deploy multiple times per day
- No manual approvals unless required for compliance

## Resilience and reliability

- Timeouts on all external calls
- Retries with backoff; circuit breakers where needed
- System should fail partially, not completely — provide fallback experiences
- Guard against AI-introduced failure modes: over-engineering, hidden dependencies, inefficient patterns

## Governance

### Architecture Decision Records

- ADRs required for all major decisions
- AI-generated proposals must include explicit trade-offs in the ADR

### Exceptions

- All deviations from standards require architecture forum approval
- Must be documented with clear justification
- AI cannot approve exceptions — humans own governance decisions

## Metrics

DORA core metrics:

```text
Deployment frequency
Lead time for changes
Change failure rate
Mean time to recovery (MTTR)
```

AI-specific additions:

```text
AI contribution effectiveness
% code generated by AI
Defect rate: AI vs human
Rework rate: AI vs human
```
