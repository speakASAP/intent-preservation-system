# Coding Prompt: TASK-017 Local Embedding Index

```yaml
id: PROMPT-TASK-017-local-embedding-index
source_task: ../11_tasks/TASK-017-implement-local-embedding-index.md
execution_plan: ../21_execution_plans/EP-TASK-017.md
context_package: ../13_context_packages/CP-task-017.md
status: used
```

## Role

You are an implementation agent adding a deterministic local embedding-style
index for IPS optional retrieval.

## Task

Implement TASK-017: generate optional retrieval candidates through a local
embedding-index mode that remains compatible with the TASK-014 comparison
harness.

## Context

Use `../13_context_packages/CP-task-017.md` and preserve graph-first retrieval.

## Constraints

- Do not add external embedding APIs.
- Do not add a vector database.
- Do not replace graph-required context.
- Keep output deterministic.
- Do not modify protected vision or constitution documents.

## Allowed Changes

- `../../scripts/context_package_generator.py`
- `../../tests/test_context_package_generator.py`
- TASK-017 validation documentation.
- `../../graph/project_graph.example.yaml`

## Forbidden Changes

- `../00_constitution/CONSTITUTION.md`
- `../01_vision/VISION.md`
- Any fixture, prompt or report containing secrets or raw production data.

## Implementation Instructions

1. Add deterministic hashed token vector helpers.
2. Build a local embedding index over optional Markdown candidates.
3. Exclude mandatory graph context from optional vector ranking.
4. Add `local-embedding-index` candidate generation.
5. Add focused tests and comparison validation.

## Parallel Workstream Context

This prompt is the source-backed handoff for the single validated
`WS-017-implementation-integration` workstream in
`../21_execution_plans/EP-TASK-017.md`.

- Ready-now parallel goals: none; the EP states this already implemented and
  validated task has no independent parallel workstream beyond the single
  implementation/integration owner.
- Dependency-gated goals: none remaining.
- Blockers: none remaining.
- Dependencies: TASK-014 comparison harness and TASK-015 local semantic adapter
  context are resolved inputs.
- Owned files from source EP: `../../scripts/context_package_generator.py`,
  `../../tests/test_context_package_generator.py` and
  `../../graph/project_graph.example.yaml`.
- Integration guidance: keep implementation, focused tests, graph traceability
  and validation evidence in the single workstream. If future follow-up work
  splits this area, merge generator changes before tests, graph traceability
  and validation documentation.
- Handoff output expected: files changed, tests run, validation evidence,
  blockers encountered or cleared, dependency notes, integration notes,
  deviations and remaining documentation gaps.

## Acceptance criteria

- A local embedding-style index can be built deterministically.
- Required graph context is excluded from optional candidate ranking.
- Candidate generation supports `local-embedding-index`.
- Generated embedding candidates compare through the TASK-014 harness.
- Focused tests cover deterministic output and report metadata.
- Repository validation gates pass.

## Validation

Run:

```bash
python3 -m unittest tests.test_context_package_generator
python3 scripts/context_package_generator.py --root . --generate-candidate-results tests/fixtures/retrieval_baseline.json --candidate-mode local-embedding-index --pretty
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-017
```

## Expected Output

The implementation agent must return files changed, tests run, validation
evidence, blockers encountered or cleared, dependencies on other workstreams,
integration notes, deviations and remaining documentation gaps.
