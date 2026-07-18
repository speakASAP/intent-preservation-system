# Coding Prompt: TASK-011 Optional RAG Retrieval Contract

```yaml
id: PROMPT-TASK-011-optional-rag-retrieval-contract
source_task: ../11_tasks/TASK-011-define-optional-rag-retrieval-contract.md
execution_plan: ../21_execution_plans/EP-TASK-011.md
context_package: ../13_context_packages/CP-task-011.md
status: used
```

## Role

You are an implementation agent working on Phase 5 optional retrieval for
Intent Preservation System.

## Task

Implement TASK-011: define and implement deterministic optional retrieval
suggestions that supplement, but do not replace, graph-required context.

## Context

Use the context package at `../13_context_packages/CP-task-011.md`, especially:

- `../11_tasks/TASK-011-define-optional-rag-retrieval-contract.md`
- `../21_execution_plans/EP-TASK-011.md`
- `../22_goal_impact/GOAL-IMPACT-TASK-011.md`
- `../10_features/FEAT-003-optional-rag-retrieval.md`
- `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- `../07_decisions/ADR-002-use-graph-retrieval-before-rag.md`
- `../../scripts/context_package_generator.py`
- `../../scripts/graph_extractor.py`

## Constraints

- Preserve graph-first retrieval.
- Keep required context separate from optional suggestions.
- Use deterministic local keyword scoring for this slice.
- Do not call external APIs or add a vector database.
- Do not include secrets or raw production data in tests, reports or prompts.
- Do not modify protected vision or constitution documents.

## Allowed Changes

- `../../scripts/context_package_generator.py` or a new helper under
  `../../scripts/`.
- Relevant tests under `../../tests/`.
- TASK-011 validation evidence after implementation.

## Forbidden Changes

- `../00_constitution/CONSTITUTION.md`
- `../01_vision/VISION.md`
- Unrelated validated TASK-004, TASK-009 and TASK-010 content.
- Any fixture, prompt or report containing secrets or raw production data.

## Implementation Instructions

1. Define the optional retrieval report shape.
2. Identify required context for the target task through existing graph or
   task/context metadata.
3. Add deterministic keyword scoring over allowed Markdown documents.
4. Exclude required graph documents from optional suggestions unless clearly
   labeled as already required.
5. Return bounded suggestions with path, reason, rank, score and retrieval mode.
6. Add focused tests for deterministic output, missing task findings and
   no-suggestion behavior.

## Parallel Workstream Context

- Prompt type: WS-011-A single-agent implementation prompt from
  `../21_execution_plans/EP-TASK-011.md`.
- Source dispatch: the execution plan declares
  `parallelization_strategy: single_agent` because the optional retrieval
  contract, implementation surface and compatibility tests are shared. WS-011-A
  is the only ready-now implementation workstream.
- Dependencies: none open for WS-011-A. The validation/documentation
  workstream WS-011-V is dependency-gated on WS-011-A implementation and test
  evidence.
- Owned files: use `Allowed Changes` above. WS-011-V owns only the TASK-011
  validation evidence after implementation.
- Expected handoff: return files changed, validation evidence, remaining
  blockers, compatibility notes, dependencies on WS-011-V and deviations.

## Acceptance criteria

- A local command can produce optional suggestions for a task id.
- Output separates required graph context from optional suggestions.
- Each suggestion includes path, reason, score or rank, and retrieval mode.
- Existing graph and context-package outputs remain backward compatible.
- Tests cover deterministic ordering, no-suggestion output and missing task
  findings.
- Repository validation gates pass.

## Validation

Run:

```bash
python3 -m unittest discover -s tests
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-011
```

## Expected Output

The implementation agent must return:

- Files changed.
- Documents created.
- Missing sections filled.
- Remaining missing-information markers.
- Validation evidence.
- Blockers encountered or cleared.
- Dependencies on other agent workstreams.
- Integration or merge notes.
- Deviations from plan.
