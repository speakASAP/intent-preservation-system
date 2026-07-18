# Coding Prompt: TASK-015 Local Semantic Candidate Adapter

```yaml
id: PROMPT-TASK-015-local-semantic-candidate-adapter
source_task: ../11_tasks/TASK-015-create-local-semantic-candidate-adapter.md
execution_plan: ../21_execution_plans/EP-TASK-015.md
context_package: ../13_context_packages/CP-task-015.md
status: used
```

## Role

You are an implementation agent adding a local candidate adapter shape for IPS
optional retrieval.

## Task

Implement TASK-015: generate TASK-014-compatible candidate retrieval results
from a baseline file using deterministic local token overlap.

## Context

Use `../13_context_packages/CP-task-015.md` and preserve the TASK-014 candidate
comparison contract.

## Constraints

- Do not add embeddings, vector search or external API calls.
- Use repository-local Markdown only.
- Candidate retrieval remains optional and non-authoritative.
- Keep output deterministic.
- Do not modify protected vision or constitution documents.

## Allowed Changes

- `../../scripts/context_package_generator.py`
- `../../tests/test_context_package_generator.py`
- TASK-015 validation documentation.

## Forbidden Changes

- `../00_constitution/CONSTITUTION.md`
- `../01_vision/VISION.md`
- Any fixture, prompt or report containing secrets or raw production data.

## Implementation Instructions

1. Add candidate generation from baseline cases.
2. Use deterministic local token overlap over repository Markdown.
3. Return candidate JSON with `retrieval_mode` and case `returned_optional_paths`.
4. Add CLI support and focused tests.
5. Validate generated candidates through candidate comparison.

## Parallel Workstream Context

- Prompt type: original used single-agent implementation prompt. The source
  execution plan now also exposes replayable parallel dispatch metadata.
- Parallel dispatch source: `../21_execution_plans/EP-TASK-015.md`
  `Parallel Dispatch List` and `Parallel Agent Handoff Prompts`.
- Workstreams: WS-015-A owns local adapter implementation in
  `../../scripts/context_package_generator.py`; WS-015-B owns focused tests and
  comparison compatibility in `../../tests/test_context_package_generator.py`;
  WS-015-C owns final documentation, gate execution and validation evidence.
- Dependencies: WS-015-C is dependency-gated on WS-015-A and WS-015-B handoff
  evidence. No current blockers remain because TASK-015 is validated.
- Expected handoff: return validation evidence, blockers encountered or
  cleared, dependencies on other agent workstreams and integration notes.

## Acceptance criteria

- A local command generates candidate retrieval results from a baseline file.
- Candidate output is compatible with TASK-014 comparison.
- Candidate generation is deterministic.
- Tests cover successful candidate generation and comparison compatibility.
- Repository validation gates pass.

## Validation

Run:

```bash
python3 -m unittest tests.test_context_package_generator
python3 scripts/context_package_generator.py --root . --generate-candidate-results tests/fixtures/retrieval_baseline.json --pretty
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-015
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
