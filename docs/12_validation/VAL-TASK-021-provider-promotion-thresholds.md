# Validation Report: TASK-021 Provider Promotion Thresholds

Validation id: VAL-TASK-021-2026-06-13
Target: TASK-021 / EP-TASK-021
Date: 2026-06-13
Validator: AI agent

## Summary

TASK-021 adds provider promotion thresholds and an executable promotion gate.
The gate combines provider safety status, candidate comparison, dry-run markers
and zero-network requirements before a provider candidate can be promoted.

## Upstream goal

- `../01_vision/VISION.md`
- `../04_systems/SYS-002-context-engine.md`
- `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- `../07_decisions/ADR-002-use-graph-retrieval-before-rag.md`
- `../09_milestones/MS-005-rag-integration.md`
- `../10_features/FEAT-003-optional-rag-retrieval.md`
- `../11_tasks/TASK-020-add-external-provider-dry-run-contract.md`
- `../22_goal_impact/GOAL-IMPACT-TASK-021.md`

## Criteria checked

| Criterion | Result | Evidence |
|---|---|---|
| Promotion rules define required thresholds | Pass | `config/provider_promotion_rules.json` defines mode, pass rate and failure limits. |
| Promotion gate checks provider safety status | Pass | Gate invokes `embedding_provider_gate`. |
| Promotion gate checks dry-run and zero-network requirements | Pass | `test_provider_promotion_gate_requires_dry_run_and_zero_network` passes. |
| Promotion gate rejects failed comparisons and wrong modes | Pass | Focused failure tests pass. |
| Promotion gate passes dry-run fixture | Pass | CLI promotion gate passes `retrieval_candidate_dry_run.json`. |
| Repository gates pass | Pass | Focused tests, provider gates, `npm run validate`, pre-coding gate and deployment-readiness gate pass. |

## Issues found

No implementation issues remain for the TASK-021 provider promotion threshold
slice.

## Recommendation

Accept TASK-021 as validated. Future real provider candidates should use this
gate before any promotion beyond experimental status.

## Traceability confirmation

TASK-021 is traceable to optional RAG and dry-run provider work because it adds
the promotion decision layer above provider safety and candidate comparison.
