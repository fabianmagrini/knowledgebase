---
title: Tools
tags: [meta]
status: complete
updated: 2026-07-11
---

# Tools

Notes on tools, platforms, and infrastructure.

## Notes

- [Git](git.md) — fundamentals, workflow, rebase, stash, bisect, cherry-pick
- [Claude Code Steering Mechanisms](claude-code-steering-mechanisms.md) — the ten places an instruction can live in Claude Code, chosen by scope (cost) and enforcement (reliability): CLAUDE.md, rules, skills, slash commands, subagents, output styles, appended prompts, MCP servers, hooks, and permissions
- [Highly Available PostgreSQL on Kubernetes](postgresql-ha-kubernetes.md) — Datadog's hybrid synchronous-replication approach to safe PostgreSQL failover on Kubernetes (Patroni, sync vs async, failure scenarios); a concrete resilience case study
- [Dynamic Configuration Sidecar (Airbnb Sitar)](dynamic-configuration-sidecar.md) — a per-pod sidecar that delivers config to tens of thousands of polyglot pods without redeploys, staying available through control-plane outages (pull model, S3 preload, local SQLite cache, graceful degradation)
