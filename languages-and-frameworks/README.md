---
type: index
title: Languages & Frameworks
description: "Notes organised by programming language and framework."
tags: [meta]
status: complete
updated: 2026-07-11
---

# Languages & Frameworks

Notes organised by programming language and framework.

## Notes

- [TypeScript Tips](typescript.md)
- [Node.js CLI Apps Best Practices](nodejs-cli-best-practices.md) — Liran Tal's 37-practice checklist for empathic, user-friendly CLIs: POSIX etiquette, distribution/packaging, interoperability, errors, versioning, and security
- [Go as an Agentic Language](go-agentic-language.md) — why Go's reader-first design (fast deterministic builds, compile-enforced types as a *gate*, the Go 1 compatibility promise, low distractor density) suits AI coding agents running the agentic loop at machine frequency
- [Rust for Agentic Development](rust-for-agentic-development.md) — the opposing bet: Niko Matsakis argues constraint strength beats iteration speed, types prevent wrong actions without establishing correctness, and a *proof* obligation is what licenses agent freedom — "do whatever you want, as long as you can prove the result". Read alongside the Go note for the fork neither author states
- [Forms as a State Problem](react-forms.md) — the mental model for React forms (the four jobs; controlled vs uncontrolled; touched vs dirty; the submission lifecycle) and the native-first tool-selection ladder from React 19 server actions to client form libraries
- [Storybook for React Component Development](react-storybook.md) — Storybook as a development practice rather than a test harness: declaring component states instead of engineering them in a running app, what deserves a story, decorators for context, and why story selection is upstream of all visual-regression coverage
- [State Propagation Is Not State Management](react-state-management.md) — Alex Russell's argument that Redux/Zustand/Jotai propagate change notifications rather than manage state, because they carry no model of ordering; what conflict resolution actually requires, and the CRDT/sync tools built around it
