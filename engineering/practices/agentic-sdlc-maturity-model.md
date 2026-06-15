---
title: Agentic SDLC Maturity Model
tags: [ai-engineering, agentic-workflows]
topic: engineering/practices
status: notes
updated: 2026-06-15
related:
  - engineering/practices/agentic-sdlc.md
  - engineering/practices/ai-dlc-methodology.md
  - engineering/practices/ai-native-engineering-stack.md
  - engineering/practices/ci-cd-ai-engineering.md
  - engineering/practices/agentic-ai-strategy-frameworks.md
  - engineering/practices/ai-augmented-engineering-team.md
source: "https://gist.github.com/fabianmagrini/4862954cd301634ab4bfd595c00ea52c"
---

# Agentic SDLC Maturity Model

A six-level model for assessing and transforming how an organization uses AI in software delivery. The maturity curve is not about how much AI you use — it is about how much entropy you can manage, how well you can formalize intent, how automated your evaluation loops are, and how deeply governance is encoded.

## Summary

| Level | Name | AI Role | Governance | Primary Risk |
|---|---|---|---|---|
| 0 | Traditional | None | Traditional SDLC | Obsolescence |
| 1 | AI-Augmented | Personal tool | None | Entropy |
| 2 | Team-Structured | Workflow enhancer | Informal | Inconsistency |
| 3 | Harness-Oriented | Controlled generator | Policy + evaluation | Platform complexity |
| 4 | AI-Integrated | Embedded in SDLC | Enterprise governance | Overdependence |
| 5 | AI-Native | Systemic intelligence | Automated, adaptive | Systemic risk |

The critical inflection point is **Level 2 → Level 3**: moving from "AI helps developers" to "AI is governed infrastructure."

Most organizations today sit at Level 1 or 2. Very few are truly Level 4. Level 5 is emerging.

---

## Level 0 — Traditional SDLC

**"AI is optional."**

### Characteristics
- Traditional Agile/DevOps lifecycle
- Code authored manually
- CI/CD handles deterministic artifacts
- Code review is human-only
- No AI policy or governance model

### Risks
- Slow iteration relative to AI-native competitors
- No internal AI literacy building
- Cultural resistance grows over time

---

## Level 1 — AI-Augmented Individuals

**"AI is a productivity booster."**

### Characteristics
- Developers use LLMs for code completion, refactoring, boilerplate
- No formal process change
- No governance updates
- AI use is personal and ad hoc

### Benefits
- 10–30% individual productivity improvement
- Faster experimentation
- Reduced friction for simple tasks

### Risks
- Hidden architectural drift
- Prompt inconsistency across the team
- Increased review surface area
- Illusion of speed (feeling fast, delivering slow)

### Signals you're here
- "Everyone uses AI differently"
- No shared prompting standards
- No formal evaluation process

---

## Level 2 — AI-Enabled Team Workflows

**"AI requires discipline."**

### Characteristics
- Shared prompting guidelines
- Spec-first workflows emerge
- AI-assisted code review
- Team-level best practices documented
- Early evaluation checklists

### What changes in the SDLC
- Specs become more detailed
- Testing becomes stricter
- PR review includes AI-assisted reasoning

### Risks
- Evaluation still manual-heavy
- No centralised governance
- Inconsistent policy enforcement

### Signals you're here
- Teams discuss "how to use AI properly"
- AI outputs are reviewed more rigorously
- Some internal docs exist for AI workflows

---

## Level 3 — Harness-Oriented Organization

**"AI must be controlled to scale."**

This is the critical inflection point.

### Characteristics
- Dedicated agent harness systems
- Deterministic test suites gate AI outputs
- Retry + repair loops automated
- Policy-as-code enforcement
- Generation logs and traceability
- AI outputs treated as production artifacts

### SDLC shift

```
Before: Code → CI → Deploy
After:  Spec → Generate → Evaluate → Repair → Gate → Deploy
```

### New roles that emerge
- Evaluation engineers
- Prompt/system designers
- AI governance leads

### Risks
- Increased infrastructure complexity
- Upfront platform investment required
- Risk of over-centralisation

### Signals you're here
- AI outputs must pass automated gates
- Prompt libraries are version-controlled
- Evaluation metrics defined and tracked

---

## Level 4 — AI-Integrated Operating Model

**"AI is infrastructure."**

### Characteristics
- AI embedded across: backlog refinement, architecture design, code generation, testing, incident triage
- Internal agent platforms
- Cross-team AI standards
- Centralised evaluation infrastructure
- Observability for agent behaviour
- AI-specific SLOs defined

### SDLC becomes cybernetic
```
Intent → Context → Generate → Evaluate → Observe → Adapt
```
Feedback loops operate continuously.

### Governance evolution
- Change approval includes prompt and config changes
- AI drift detection systems active
- Audit trails for generation decisions
- Security review includes model behaviour

### Organizational shifts
- Managers become system designers
- Engineers operate at higher abstraction level
- Junior roles transform significantly

### Risks
- Organizational overdependence on AI systems
- Skill atrophy in core fundamentals
- Complex debugging scenarios

### Signals you're here
- AI contributes to architectural decisions
- Production systems depend on agent loops
- AI usage is visible in executive metrics

---

## Level 5 — AI-Native Organization

**"We design systems that design systems."**

This is not "AI everywhere" — it is AI designed into the operating model.

### Characteristics

**System-level intelligence**
- Autonomous coding agents for bounded domains
- Self-improving evaluation harnesses
- Recursive agent improvement (agents improving agents)

**Continuous organizational learning**
- Spec quality tracked as a KPI
- Context engineering as a formal discipline
- Prompt drift monitoring
- Architectural coherence metrics

**Governance as code**
- Policy engines gate generation
- Automated compliance validation
- Risk-tiered generation rules
- Model performance dashboards

**Structural changes**
- Teams organised around capability and orchestration
- Platform teams own agent frameworks
- Evaluation and architecture are core competencies

### SDLC at Level 5

No linear lifecycle — a closed-loop adaptive system:

```
Human Intent
     ↓
Structured Specification
     ↓
Agent Generation
     ↓
Automated Evaluation
     ↓
Policy Enforcement
     ↓
Production
     ↓
Observability + Drift Detection
     ↓
Feedback into Specs + Models
     ↑ (continuously)
```

### Competitive advantage
- Faster safe iteration
- Lower marginal feature cost
- Higher architectural consistency
- Scalable, automated governance

---

## Diagnostic questions

Use these to assess your current level:

1. Are AI outputs gated by automated evaluation? *(No → below Level 3)*
2. Are prompts and versioned context treated as change-controlled artifacts? *(No → below Level 3)*
3. Do you track AI error types as operational incidents? *(No → below Level 4)*
4. Is there a centralised harness platform? *(No → below Level 4)*
5. Do executives see AI governance metrics? *(No → below Level 4)*
6. Do agents improve other agents? *(No → below Level 5)*

If most answers are "no," you are below Level 3 — and Level 2→3 is where the most transformative investment pays off.
