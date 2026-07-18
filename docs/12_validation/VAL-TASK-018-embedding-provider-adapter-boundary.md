# Validation Report: TASK-018 Embedding Provider Adapter Boundary

Validation id: VAL-TASK-018-2026-06-13
Target: TASK-018 / EP-TASK-018
Date: 2026-06-13
Validator: AI agent

## Summary

TASK-018 adds an embedding provider adapter boundary behind optional
embedding-index retrieval. The current provider is `local-hash`, which preserves
the deterministic hashed-vector behavior from TASK-017 while making future
providers an explicit adapter choice.

## Upstream goal

- `../01_vision/VISION.md`
- `../04_systems/SYS-002-context-engine.md`
- `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- `../07_decisions/ADR-002-use-graph-retrieval-before-rag.md`
- `../09_milestones/MS-005-rag-integration.md`
- `../10_features/FEAT-003-optional-rag-retrieval.md`
- `../22_goal_impact/GOAL-IMPACT-TASK-018.md`

## Criteria checked

| Criterion | Result | Evidence |
|---|---|---|
| Provider selection is explicit | Pass | CLI exposes `--embedding-provider local-hash` for embedding candidate generation. |
| Local hash provider implements the boundary | Pass | `test_embedding_provider_boundary_returns_deterministic_vectors` passes. |
| Unknown providers fail clearly | Pass | `test_embedding_provider_boundary_rejects_unknown_provider` passes. |
| Candidate output records selected provider | Pass | Candidate JSON includes `embedding_provider: local-hash`. |
| Existing embedding candidate comparison still passes | Pass | Provider-selected candidate generation returns the expected baseline prompt. |
| Repository gates pass | Pass | Focused tests, `npm run validate`, pre-coding gate and deployment-readiness gate pass. |

## Issues found

No implementation issues remain for the TASK-018 provider boundary slice.

## Recommendation

Accept TASK-018 as validated. The next provider task can add a real embedding
adapter only after defining credential handling, sensitive-data policy gates and
comparison acceptance thresholds.

## Traceability confirmation

TASK-018 is traceable to the optional RAG feature and graph-first retrieval ADR
because it makes provider choice explicit without changing mandatory graph
context behavior.
