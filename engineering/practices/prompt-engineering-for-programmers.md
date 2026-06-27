---
title: Prompt Engineering for Programmers
tags: [ai-engineering, reading]
topic: engineering/practices
status: notes
level: intermediate
related:
  - engineering/practices/loop-driven-development.md
  - engineering/practices/quality-first-ai-coding.md
  - engineering/practices/harness-engineering.md
  - engineering/practices/ai-native-engineering-stack.md
  - reading/how-i-use-llms-2026.md
source: "https://addyo.substack.com/p/the-prompt-engineering-playbook-for"
updated: 2026-06-14
---

# Prompt Engineering for Programmers

Prompt quality directly determines the quality of an AI assistant's output. Because these tools
know nothing about a project beyond what they are told, the developer's job is to supply that
context deliberately — turning a generic suggestion engine into a reliable pair programmer. The
stance throughout is that prompting is an **interactive dialogue, not a one-shot instruction**:
treat the model like an attentive junior developer or a rubber duck that needs coaching,
feedback, and clarification, and ask it to explain its reasoning so you learn alongside it.

## Five foundational principles

1. **Rich context.** Assume the AI knows nothing about your project beyond what you provide —
   language, framework, error messages, expected behaviour.
2. **Specificity.** Replace "why isn't my code working?" with the exact function, input, error,
   and expected vs. actual result.
3. **Task decomposition.** Split complex problems into smaller steps ("first generate X, then add
   Y") rather than feeding everything at once.
4. **Concrete examples (few-shot).** Provide input/output illustrations or test cases to pin down
   requirements.
5. **Role-play / personas.** "Act as a senior React developer" or "a JavaScript performance
   expert" shifts the tone and depth of the answer.

## Patterns by use case

**Debugging**
- Describe the problem as *expected behaviour + actual output + exact error message*.
- **Rubber-duck**: ask for a line-by-line execution walkthrough to expose logic errors.
- Extract a **minimal reproducible example** that still triggers the bug.
- Use focused follow-ups: "what might cause this, and how do I fix it?"

> Example: a vague "why isn't `mapUsersById` working?" returns generic guesses; including the code,
> the error (`TypeError: Cannot read property 'id' of undefined`), the expected output, and a
> sample input lets the model pinpoint the real cause (a loop using `<=` instead of `<`).

**Refactoring and optimisation**
- State goals explicitly — define what "better" means (performance, readability, less duplication,
  API modernisation) rather than "refactor this".
- Include context: language, framework version, idiomatic expectations ("functional React
  components with Hooks").
- Request explanations alongside the code to verify understanding.
- Role-play as an expert for more rigorous improvements.

**Feature implementation**
- High-level outline first, then drill into each piece with focused prompts.
- Provide reference code from the project to establish style and conventions.
- Use inline comments as prompts (`// TODO: validate request payload…`) and let the model
  autocomplete from intent.
- Give usage examples ("`formatPrice(2.5)` should return `'$2.50'`").
- Refine iteratively — "use a filter instead of a loop", "use Hooks, not class components".

## Memorable formulas

- **Debugging:** "It's expected to do [X] but instead does [Y] given [input]. Where is the bug?"
- **Refactoring:** "Issues I'd like to address: 1) … 2) … 3) …"
- **Role-play:** "Act as [persona]. [Task]. [Expected output format]."
- **Iterate like commits:** build → review → refine → extend, each prompt a small step.

## Anti-patterns

| Anti-pattern | Problem | Fix |
|---|---|---|
| Vague prompt | "It doesn't work" lacks context | Add errors, code, expected vs. actual |
| Overloaded prompt | Several tasks in one request | Split into sequential prompts; prioritise |
| Missing the question | A code dump with no ask | State explicit intent ("identify bugs in…") |
| Vague success criteria | "Make it faster" is undefined | Quantify ("reduce to linear time") |
| Ignoring AI clarification | Dismissing the model's questions | Answer them — it is signalling missing context |
| Inconsistent style | Mixed formats confuse parsing | Keep a consistent structure; use Markdown code blocks |

When results miss, identify the discrepancy, re-emphasise that requirement in a new prompt, break
the task down further, or start fresh if the conversation has become confused.

## Trade-offs

- **Specificity vs. brevity** — more detail aids accuracy but lengthens the prompt.
- **Iteration vs. efficiency** — refining over several prompts costs time but avoids misaligned
  output.
- **Scaffolding vs. judgement** — lean on the AI for boilerplate, but keep judgement on sensitive
  or domain-specific logic.
- **One large prompt vs. decomposition** — breaking work down reduces focus errors at the cost of
  more conversational overhead.

## Relationship to other notes

- [Loop-Driven Development](loop-driven-development.md) — prompt engineering is era 2 of its
  leverage stack; leverage has moved "up" to loops, but good prompting still happens inside every
  harness and loop. This note is that ground-level technique.
- [Quality-First AI Coding](quality-first-ai-coding.md) — the "lazy prompting" and review
  practices there assume the prompt fundamentals collected here.
- [Harness Engineering](harness-engineering.md) — "a 2–10 line prompt is not a harness"; this note
  is about writing those prompts well, the harness is the system around them.
- [The AI-Native Engineering Stack](ai-native-engineering-stack.md) — skills encode reusable
  prompts so the fundamentals here are not re-applied from scratch each session.

> Reference: Addy Osmani, with techniques drawn from community guides; a companion to his
> forthcoming O'Reilly book *Vibe Coding: The AI-Assisted Engineering*.
