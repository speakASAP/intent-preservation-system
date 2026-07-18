# Context Package: TASK-011

## Target task

TASK-011: `../11_tasks/TASK-011-define-optional-rag-retrieval-contract.md`

## Upstream traceability

```text
../01_vision/VISION.md -> ../04_systems/SYS-002-context-engine.md -> ../10_features/FEAT-003-optional-rag-retrieval.md -> ../09_milestones/MS-005-rag-integration.md -> TASK-011
```

## Included documents

- `../11_tasks/TASK-011-define-optional-rag-retrieval-contract.md`
- `../21_execution_plans/EP-TASK-011.md`
- `../22_goal_impact/GOAL-IMPACT-TASK-011.md`
- `../12_validation/VAL-TASK-011-optional-rag-retrieval-contract.md`
- `../10_features/FEAT-003-optional-rag-retrieval.md`
- `../04_systems/SYS-002-context-engine.md`
- `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- `../07_decisions/ADR-002-use-graph-retrieval-before-rag.md`
- `../09_milestones/MS-005-rag-integration.md`
- `../11_tasks/TASK-006-generate-context-package-by-task-id.md`
- `../11_tasks/TASK-010-generate-knowledge-graph-dependency-map.md`
- `../../scripts/context_package_generator.py`
- `../../scripts/graph_extractor.py`
- `../../tests/test_context_package_generator.py`
- `../../tests/test_graph_extractor.py`
- `../17_governance/PROJECT_INVARIANTS.md`
- `../23_documentation_contracts/SENSITIVE_DATA_POLICY.md`

## Excluded documents

- External embedding API documentation is excluded.
- Vector database setup is excluded.
- Raw production data, secrets, confidential identifiers and real customer data
  are excluded.
- Protected vision and constitution documents are read-only context.

## Constraints

- Graph-required context remains mandatory and authoritative.
- Optional suggestions must be explicitly labeled as optional.
- Use deterministic local scoring for the first implementation slice.
- Do not call external services.
- Do not modify `../00_constitution/CONSTITUTION.md` or
  `../01_vision/VISION.md`.

## Parallel dispatch status

- Source execution plan: `../21_execution_plans/EP-TASK-011.md`
- Dispatch readiness: the source execution plan now declares
  `parallelization_strategy: single_agent` and includes the required
  `Parallel Dispatch List` and `Parallel Agent Handoff Prompts` sections.
- Ready-now workstream: WS-011-A, owned by a context-engine implementation
  agent. It implements the deterministic optional retrieval contract and
  focused tests in one dedicated session because the retrieval contract,
  implementation surface and compatibility tests are shared.
- Dependency-gated workstream: WS-011-V, owned by a validation/documentation
  agent after WS-011-A. It records command evidence and readiness in the
  TASK-011 validation report.
- Derived prompt treatment: use the coding prompt as the WS-011-A single-agent
  implementation prompt for the already validated implementation slice.
- Blockers: no open blockers are recorded for the validated deterministic
  keyword slice. WS-011-V depends on WS-011-A implementation and test evidence.

## Agent prompt

Implement TASK-011 by adding deterministic optional retrieval suggestions for a
task id. Return required graph context separately from optional suggestions and
include reason metadata for each suggestion.

## Validation instructions

Run:

```bash
python3 -m unittest discover -s tests
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-011
```
