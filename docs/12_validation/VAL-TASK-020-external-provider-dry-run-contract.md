# Validation Report: TASK-020 External Provider Dry-Run Contract

Validation id: VAL-TASK-020-2026-06-13
Target: TASK-020 / EP-TASK-020
Date: 2026-06-13
Validator: AI agent

## Summary

TASK-020 adds an offline external-provider dry-run contract. The dry-run
provider passes safety gates, emits candidate output compatible with the
comparison harness and reports zero network calls.

## Upstream goal

- `../01_vision/VISION.md`
- `../04_systems/SYS-002-context-engine.md`
- `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- `../07_decisions/ADR-002-use-graph-retrieval-before-rag.md`
- `../09_milestones/MS-005-rag-integration.md`
- `../10_features/FEAT-003-optional-rag-retrieval.md`
- `../11_tasks/TASK-019-add-embedding-provider-safety-gates.md`
- `../22_goal_impact/GOAL-IMPACT-TASK-020.md`

## Criteria checked

| Criterion | Result | Evidence |
|---|---|---|
| Dry-run provider registry entry passes safety gate | Pass | `python3 scripts/embedding_provider_gate.py --root .` passes. |
| Dry-run candidate output emits expected shape | Pass | CLI output includes `retrieval_mode`, `embedding_provider`, `dry_run`, `network_calls` and `cases`. |
| Dry-run reports zero network calls | Pass | CLI output reports `network_calls: 0`. |
| Dry-run candidate output compares through existing harness | Pass | `test_external_provider_dry_run_candidate_results_compare_against_baseline` passes. |
| Dry-run does not require repository document text | Pass | `test_external_provider_dry_run_does_not_require_repository_document_text` passes. |
| Repository gates pass | Pass | Focused tests, `npm run validate`, pre-coding gate and deployment-readiness gate pass. |

## Issues found

No implementation issues remain for the TASK-020 dry-run provider contract
slice.

## Recommendation

Accept TASK-020 as validated. Future provider work can add real provider
candidate generation only after the provider gate, dry-run contract and
comparison thresholds all pass.

## Traceability confirmation

TASK-020 is traceable to optional RAG and provider safety gates because it
validates the external-provider pathway without introducing external data
movement.
