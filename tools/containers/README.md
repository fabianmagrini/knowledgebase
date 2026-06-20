---
title: Containers
tags: [meta, docker, kubernetes]
status: complete
updated: 2026-06-20
---

# Containers

Notes on Docker, Kubernetes, and container orchestration.

## Notes

- [Highly Available PostgreSQL on Kubernetes](postgresql-ha-kubernetes.md) — Datadog's hybrid synchronous-replication approach to safe PostgreSQL failover on Kubernetes (Patroni, sync vs async, failure scenarios); a concrete resilience case study
- [Dynamic Configuration Sidecar (Airbnb Sitar)](dynamic-configuration-sidecar.md) — a per-pod sidecar that delivers config to tens of thousands of polyglot pods without redeploys, staying available through control-plane outages (pull model, S3 preload, local SQLite cache, graceful degradation)
