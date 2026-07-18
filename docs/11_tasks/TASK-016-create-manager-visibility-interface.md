# TASK-016: Create manager visibility interface

```yaml
id: TASK-016
status: validated
owner: context-engine-agent
created: 2026-06-13
last_updated: 2026-06-13
completeness_level: validated
upstream:
  - ../01_vision/VISION.md
  - ../04_systems/SYS-002-context-engine.md
  - ../07_decisions/ADR-001-use-markdown-and-git-as-source-of-truth.md
  - ../07_decisions/ADR-002-use-graph-retrieval-before-rag.md
  - ../10_features/FEAT-004-manager-visibility.md
goal_impact:
  - ../22_goal_impact/GOAL-IMPACT-TASK-016.md
execution_plan:
  - ../21_execution_plans/EP-TASK-016.md
validation_report:
  - ../12_validation/VAL-TASK-016-manager-visibility-interface.md
```

## Objective

Create a basic local web interface that makes the Intent Preservation System
visible and understandable for managers. The interface should show what is
happening, how work traces to intent and how retrieval candidates are compared.

## Upstream Links

- Vision: `../01_vision/VISION.md`
- Context engine: `../04_systems/SYS-002-context-engine.md`
- Markdown source-of-truth ADR: `../07_decisions/ADR-001-use-markdown-and-git-as-source-of-truth.md`
- Graph-first retrieval ADR: `../07_decisions/ADR-002-use-graph-retrieval-before-rag.md`
- Manager visibility feature: `../10_features/FEAT-004-manager-visibility.md`

## Goal Impact

TASK-016 improves managerial understanding by turning the IPS chain, validation
gates and retrieval comparison into a single readable dashboard.

## Project Invariant Impact

- IPS-INV-001: dashboard content preserves the Vision to Validation chain.
- IPS-INV-002: protected vision and constitution documents remain read-only.
- IPS-INV-003: implementation follows `../21_execution_plans/EP-TASK-016.md`.
- IPS-INV-004: validation evidence is recorded before closure.
- IPS-INV-005: the interface uses synthetic, repository-local status examples
  only.

## Sensitive-Data Classification

Classification: synthetic

The interface contains repository status labels, sample comparison values and
manager explanations. It must not include secrets, customer data or raw
production data.

## Contract/Schema Impact

This task adds a static web interface. It does not change IPS document schemas,
retrieval result schemas or validation gate contracts.

## Replay/Determinism Impact

The interface is deterministic for a fixed source state because it uses static
HTML, CSS and local JavaScript data.

## Scope

- Add a static manager-facing interface under `../../manager_interface/`.
- Explain the IPS trace chain in normal business language.
- Show retrieval comparison and validation evidence panels.
- Add responsive desktop and mobile layout behavior.
- Add governance documents and graph traceability for TASK-016.

## Non-Goals

- Do not add a backend service.
- Do not connect to production systems.
- Do not add live repository parsing.
- Do not modify protected vision or constitution documents.

## Acceptance Criteria

- [x] Managers can open a basic web page and see the IPS status.
- [x] The page shows traceability from vision to validation.
- [x] The page shows how baseline and candidate retrieval are compared.
- [x] The page explains manager-relevant risks and next checks.
- [x] The page is responsive and visually verified.
- [x] Repository validation gates pass.

## Required Context

- `../10_features/FEAT-004-manager-visibility.md`
- `../21_execution_plans/EP-TASK-016.md`
- `../22_goal_impact/GOAL-IMPACT-TASK-016.md`
- `../12_validation/VAL-TASK-016-manager-visibility-interface.md`
- `../12_validation/VALIDATION_PYRAMID.md`
- `../11_tasks/TASK-014-compare-candidate-retrieval-results.md`
- `../11_tasks/TASK-015-create-local-semantic-candidate-adapter.md`

## Validation Task

Validate with local static serving, desktop and mobile browser inspection,
repository audit, pre-coding gate and deployment-readiness gate for TASK-016.

## Required Gates

```bash
python3 -m unittest discover -s tests
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-016
```

## Execution Plan Requirement

This task was implemented under `../21_execution_plans/EP-TASK-016.md`.
Validation evidence is recorded in
`../12_validation/VAL-TASK-016-manager-visibility-interface.md`.
