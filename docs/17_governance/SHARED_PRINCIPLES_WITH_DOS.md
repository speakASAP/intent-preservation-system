# Shared Principles With DOS

## Purpose

This document records the durable relationship between the Intent Preservation System (IPS) and DOS without merging their identities.

IPS remains the general framework for preserving original intent across AI-assisted projects. DOS remains a TDOS-specific decision operating system and a concrete reference project that uses IPS governance to protect its own product intent.

## Relationship

IPS provides the general governance layer:

- immutable intent documents;
- controlled amendment paths;
- traceability from vision to validation;
- auditability for AI-assisted delivery;
- operational gates that prevent undocumented coding and closure.

DOS provides a reference implementation target and operational-pattern source:

- contract-first implementation;
- gate-driven development;
- synthetic-data-safe validation;
- replay and determinism expectations;
- product invariants tied to a protected TDOS vision.

DOS is not authoritative over IPS. IPS may learn from DOS only by abstracting DOS-specific controls into reusable intent-preservation patterns.

## Shared Principles

| Principle | IPS expression | DOS expression |
|---|---|---|
| Immutable intent | Constitution and vision are protected from direct AI edits. | TDOS constitution and vision are protected from unmanaged product drift. |
| Traceability | Work flows from vision through goal impact, systems, features, tasks, execution plans and validation. | TDOS work maps protected intent to goal impact, runtime phases, schemas, gates and validation reports. |
| Operational gates | Pre-coding and deployment-readiness gates check traceability, invariants, validation plans and data safety. | Phase gates check coding readiness, integration readiness and intent preservation before work proceeds. |
| Data safety | Sensitive data is excluded from prompts, examples, tests, logs and reports. | Local and synthetic examples prevent raw customer data from entering AI-assisted workflows. |
| Contract validation | Contract and schema impacts must be declared before implementation. | Decision artefacts, policy results, intake events and projections are schema-governed. |
| Replay and auditability | Validation evidence is recorded so implementation can be reviewed against upstream intent. | Replay-oriented artifacts and lineage preserve explainability for TDOS decisions. |
| Project invariants | Each IPS project declares non-negotiable rules or explicitly marks them not applicable. | TDOS product invariants preserve governed decision infrastructure rather than generic automation. |

## Boundaries

IPS must not become TDOS-specific. DOS examples may inform IPS templates, gates and validation language only when the reusable principle is clear.

DOS must not become detached from IPS governance. DOS can make TDOS product decisions through its own amendment and decision process, but those decisions do not rewrite the IPS constitution, vision or general rules.

Neither repository is required to block all change until the other repository changes. Cross-references are used for auditability and learning, not circular governance.

## Validation

The IPS pre-coding gate checks this document when cross-repository mode is enabled or when this file exists. The check is intentionally lightweight and requires the document to contain these sections:

- `Purpose`
- `Relationship`
- `Shared Principles`
- `Boundaries`
- `Validation`

Validation should confirm that DOS is described as a reference project and operational-pattern source, not as the source of truth for IPS.
