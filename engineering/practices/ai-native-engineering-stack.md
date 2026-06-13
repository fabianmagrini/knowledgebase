---
title: The AI-Native Engineering Stack
tags: [ai-engineering, architecture]
topic: engineering/practices
status: notes
updated: 2026-06-13
related:
  - engineering/practices/ci-cd-ai-engineering.md
  - engineering/practices/engineering-playbook.md
  - engineering/practices/federated-pr-review.md
  - engineering/practices/code-review-policy.md
  - engineering/practices/agentic-sdlc.md
  - engineering/practices/agentic-sdlc-maturity-model.md
  - engineering/practices/eval-driven-ai-development.md
  - engineering/architecture/design-systems-ai-control-plane.md
  - engineering/practices/ai-augmented-engineering-team.md
source: "https://gist.github.com/fabianmagrini/9543a6a750d904f66744d7fbfb3d3ec3"
---

# The AI-Native Engineering Stack

AI-native engineering is not just AI writing code. It is engineering systems that allow AI to build software **safely, consistently, and repeatedly**. Developers shift from writing implementation to designing the system that produces it.

```
Traditional:  developers write code → CI tests → deploy
AI-native:    developers design skills + policies → agents implement → harness validates → policies enforce
```

Repositories shift from **code storage** to **software factories**. Developers design the factory; AI agents run it.

## The 7-layer stack

```
Human Intent
     ↓
Agent Orchestration
     ↓
Skills
     ↓
Tools
     ↓
Governance Policies
     ↓
Execution Harness
     ↓
Infrastructure Platform
```

## 1. Human Intent

Developers express intent rather than writing implementation:

```
Create a user service
Add a signup API endpoint
Implement password reset
```

Coding agents (Claude Code, Amp, GitHub Copilot CLI) translate intent into structured workflows by selecting and executing the appropriate skill.

## 2. Agent Orchestration

Advanced systems use multiple specialised agents rather than one agent doing everything. Typical agent roles:

```
Architect Agent   → design, ADRs, patterns
Coding Agent      → implementation
Testing Agent     → test generation and validation
Review Agent      → code review, policy checks
DevOps Agent      → CI/CD, infrastructure
```

Each agent is configured with a declared set of skills, allowed tools, and repo access scope — an AgentRC-style definition:

```yaml
agent: coding-agent

skills:
  - create-microservice
  - add-rest-endpoint
  - write-tests

tools:
  - filesystem
  - git
  - test-runner
```

This creates a **virtual engineering team** with bounded responsibilities.

## 3. Skills

Skills are **reusable engineering capabilities** — the agent's playbook. A skill describes how to complete a specific task using team best practices.

Common skills:

```
create-microservice
generate-openapi
add-rest-endpoint
create-react-component
write-unit-tests
add-ci-pipeline
```

A skill contains instructions, rules, templates, examples, and validation checks:

```yaml
name: add-rest-endpoint

inputs:
  resource
  fields

steps:
  - generate-openapi
  - create-controller
  - create-service
  - create-tests
```

Skills are versioned, stored in the repository, and shared across agents. They encode team standards so agents don't need to infer them.

## 4. Tools

Agents use tools to interact with the system. Tool access is declared per agent and scoped to what that agent needs:

```
filesystem     → read/write source files
git            → branch, commit, push
terminal       → run commands
test runner    → execute tests
database       → query or migrate
browser        → UI testing
```

Tool integration is standardised via the **Model Context Protocol (MCP)**, which provides a consistent interface for agents across different environments.

## 5. Governance Policies

Policies enforce engineering standards automatically, without relying on manual review to catch violations. They run in CI as hard gates.

Common enforcement tools: **Open Policy Agent**, **Spectral**.

Example rules:

```
All APIs must include an OpenAPI specification
Breaking API changes are blocked
Secrets cannot appear in source code
Architecture boundaries must not be violated
Risk-tier routing applies to all PRs
```

The governance layer is what makes it safe to let agents generate large volumes of code. See [[ci-cd-ai-engineering]] and [[engineering-playbook]] for how these policies integrate into the pipeline.

## 6. Execution Harness

AI-generated code must be validated before it is accepted. The harness is the automated feedback loop:

```
Agent writes code
     ↓
Harness runs tests (unit, integration, E2E, security, performance)
     ↓
Failures returned to agent as structured input
     ↓
Agent fixes code
     ↓
Repeat until passing
```

This **automated debugging loop** allows agents to self-correct without human intervention for mechanical failures. Humans intervene when the loop cannot converge — a signal that the task needs reframing, not just fixing.

## 7. Infrastructure Platform

The base layer that runs and observes the application:

```
Containers        → Docker
Orchestration     → Kubernetes
Infrastructure    → Terraform
Observability     → OpenTelemetry
CI/CD             → pipeline platform
```

Agents can generate infrastructure definitions. The same governance policies that apply to application code apply to infrastructure-as-code.

## Repository structure

An AI-native repository exposes structure that agents can navigate and understand:

```
repo/
 ├── agents/          agent configurations (skills, tools, scope)
 ├── skills/          skill definitions
 ├── policies/        governance rules (OPA, Spectral)
 ├── architecture/    ADRs, diagrams, constraints
 ├── services/        backend services
 ├── apps/            frontend applications
 ├── packages/        shared libraries
 ├── tests/           test harnesses
 ├── infrastructure/  Terraform, Kubernetes manifests
 ├── observability/   dashboards, SLOs, alert rules
 ├── openapi/         API specifications
 └── .github/         CI/CD workflows, CODEOWNERS
```

This structure allows agents to understand architecture, follow policies, and generate code that fits the system — rather than generating code in isolation.

## Developer role in an AI-native system

| Traditional | AI-native |
|---|---|
| Write implementation | Design skills and policies |
| Debug code | Debug agent loops and skill definitions |
| Review line by line | Review intent, design, and governance gaps |
| Maintain code | Maintain the factory that generates code |

The leverage point shifts from individual productivity to **system design quality**. A well-designed skill and a strong governance policy produce correct code at scale; a poorly designed one produces incorrect code at scale.
