---
title: Agentic AI Strategy Frameworks
tags: [ai-engineering, agentic-workflows]
topic: engineering/ai-native
status: notes
updated: 2026-06-15
related:
  - engineering/ai-native/agentic-sdlc.md
  - engineering/ai-native/agentic-sdlc-maturity-model.md
  - engineering/practices/engineering-playbook.md
  - engineering/ai-native/ai-native-engineering-stack.md
  - leadership/learning-organisation.md
  - engineering/ai-native/apex-framework.md
  - case-studies/microsoft-ai-core-competency.md
source: "https://gist.github.com/fabianmagrini/58ece8f11d73cc33cf5c706ac5d37488"
---

# Agentic AI Strategy Frameworks

Practical frameworks for classifying, planning, and implementing AI participation in engineering. Useful for strategic alignment, backlog classification, and system design decisions.

## 1. AI Collaboration Matrix

A two-axis model for assessing where a team sits and planning trajectory.

**Axes:**
- Who produces the work? (Human ↔ AI)
- Who manages the process? (Human ↔ AI)

```
                  AI manages
                      │
  AI-led execution    │    Autonomous agents
  Human produces      │    AI produces + leads
                      │
──────────────────────┼──────────────────────
  Human-only          │    AI-assisted
  traditional SDLC    │    human-led
                      │
                  Human manages
```

Most organizations are in the bottom-right (AI-assisted, human-led). The strategic question is: which quadrants make sense for which types of work, and what does an intentional trajectory look like?

Unstructured AI adoption — plugging in tools without choosing a quadrant — leads to inconsistent outcomes, technical debt, and cultural resistance.

## 2. Levels of Coding Autonomy

Modeled on the SAE self-driving levels. Useful for classifying tasks, teams, and systems — not for categorizing AI tools as a whole.

| Level | Name | Description |
|---|---|---|
| 0 | Manual | No AI. Human writes every line. |
| 1 | AI-Assisted | Copilot-style suggestions. Human types, AI completes. Human is the pilot. |
| 2 | Partial Automation | Human delegates a specific task ("write a function to validate emails"), reviews output, integrates. |
| 3 | Conditional Autonomy | Agent plans and executes a workflow ("scaffold a microservice from these specs"). Human reviews the plan before execution and the output before merge. |
| 4 | High Autonomy | Agent identifies tasks itself ("found a vulnerability in dependency X, created a PR"). Human acts as final approver only. |
| 5 | Full Agency | Agent autonomously manages a domain (e.g., QA suite that writes, runs, and fixes its own tests). Human receives summary reports. |

Different work types in the same team can operate at different levels simultaneously. The level should match the risk and reversibility of the task — not be applied uniformly across all work.

## 3. Automation Matrix

A quadrant for classifying work before deciding whether to automate it agentically. Classify by **judgment required** and **volume/frequency**.

| | Low Volume | High Volume |
|---|---|---|
| **High Judgment** | Human Only | Human-in-the-Loop |
| **Low Judgment** | Consider later | Fully Agentic |

### Fully Agentic (Low Judgment, High Volume)
Routine, repetitive tasks with clear success criteria. Cost of error is low or easily reversible.

Examples:
- Writing unit tests and boilerplate
- Migrating legacy code (e.g., Java 8 → 17)
- Log analysis and anomaly detection
- Generating documentation from code
- Dependency update PRs

### Human-in-the-Loop (High Judgment, High Volume)
Frequent but nuanced tasks. AI does the heavy lifting (~80%); humans refine and approve (~20%).

Examples:
- Code review and refactoring suggestions
- Writing complex queries
- Generating UI components from design files
- Onboarding context ("chat with codebase")

### Human Only (High Judgment, Low Volume)
Strategic, high-stakes, infrequent decisions requiring deep context, ethical reasoning, or creative architecture.

Examples:
- System architecture and design decisions
- Defining business logic and requirements
- Security policy creation
- Debugging critical production outages

### Practical application

1. Audit your backlog — tag tasks as Agentic / Human-in-Loop / Human Only
2. Assign tooling accordingly:
   - Agentic: autonomous agents (Devin, GitHub Copilot Workspace, custom harnesses)
   - Human-in-Loop: IDE assistants (Cursor, Copilot)
   - Human Only: structured design sessions, architecture forums

## 4. Enterprise agentic design patterns

### Supervisor pattern

A primary AI agent breaks down a goal and delegates sub-tasks to specialised worker agents. A human sits above the Supervisor to approve the final consolidated result.

```
Human (final approver)
     ↓
Supervisor Agent (coordinates)
     ├── Coder Agent
     ├── Reviewer Agent
     └── Tester Agent
```

Best for: complex, multi-step tasks where specialisation improves quality and a single agent would lose context.

### Human-as-Tool pattern

The agent works autonomously but has a tool it can call: `ask_human()`. When the agent's confidence drops below a threshold, it pauses and requests human input via a notification channel.

```
Agent working autonomously
     ↓
Confidence < threshold?
     ↓ Yes
ask_human() → human clarifies
     ↓
Agent resumes
```

Best for: long-running agentic tasks where human interruption should be exception-based, not constant — but total autonomy is too risky.

### Quality Gate pattern

Work is done agentically but cannot proceed to the next stage (e.g., merge, deploy) without passing a deterministic gate (automated tests) and a human manual approval.

```
Agent generates code
     ↓
Automated gate (tests, lint, security scan, policy checks)
     ↓ Pass
Human review and approval
     ↓ Approve
Merge / deploy
```

Best for: any agent work going into production. This is the standard pattern; the others are used in combination with it. See [[ci-cd-ai-engineering]] and [[agentic-sdlc]] for how the evaluation harness implements this.

## Using the frameworks together

| Decision | Framework to use |
|---|---|
| "Where is our team today?" | AI Collaboration Matrix |
| "Which level of autonomy is right for this task?" | Levels of Coding Autonomy |
| "Should we automate this with an agent?" | Automation Matrix |
| "How should we structure the agent system?" | Design patterns |
| "How mature is our overall SDLC?" | Agentic SDLC Maturity Model (see [[agentic-sdlc-maturity-model]]) |
