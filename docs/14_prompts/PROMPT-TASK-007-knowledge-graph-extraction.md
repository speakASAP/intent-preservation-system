# Coding Prompt: TASK-007 Knowledge Graph Extraction

```yaml
id: PROMPT-TASK-007-knowledge-graph-extraction
source_task: ../11_tasks/TASK-007-extract-knowledge-graph-from-documents.md
execution_plan: ../21_execution_plans/EP-TASK-007.md
context_package: ../13_context_packages/CP-task-007.md
status: used
```

## Role

You are an implementation agent working on the Phase 4 knowledge-graph slice of
the Intent Preservation System.

## Task

Implement TASK-007: extract graph nodes, traceability edges and reference
findings from repository Markdown documents.

## Context

Use the context package at `../13_context_packages/CP-task-007.md`, especially:

- `../11_tasks/TASK-007-extract-knowledge-graph-from-documents.md`
- `../21_execution_plans/EP-TASK-007.md`
- `../22_goal_impact/GOAL-IMPACT-TASK-007.md`
- `../../graph/GRAPH_SCHEMA.md`
- `../05_subsystems/SUB-002-graph-builder.md`
- `../07_decisions/ADR-002-use-graph-retrieval-before-rag.md`

## Constraints

- Do not modify `../00_constitution/CONSTITUTION.md` or `../01_vision/VISION.md`.
- Do not infer semantic relationships that are not declared in repository
  metadata or explicit Markdown references.
- Do not implement graph querying, path traversal, embeddings or RAG.
- Keep output ordering deterministic.
- Use synthetic fixture documents in tests.

## Allowed Changes

- `../../scripts/graph_extractor.py`
- `../../tests/test_graph_extractor.py`
- `../../package.json`
- TASK-007 documentation, context package, coding prompt, validation report and
  graph entries.

## Forbidden Changes

- Protected baseline documents under `../00_constitution/` and `../01_vision/`.
- Unrelated task, execution-plan, prompt, context-package or validation scopes.
- Any prompt, fixture, report or generated output containing secrets, raw
  production data, confidential identifiers or real customer data.

## Implementation Instructions

1. Classify known IPS Markdown artifacts into graph node types.
2. Extract stable node ids from metadata when present and file names otherwise.
3. Extract edges from task, execution-plan, goal-impact, coding-prompt and
   validation-report metadata.
4. Resolve Markdown references relative to the repository root and source file.
5. Report missing or unresolved references without crashing.
6. Emit JSON-compatible `nodes`, `edges` and `findings` collections.
7. Add tests for node extraction, edge extraction, missing references and
   deterministic output.

## Parallel Workstream Context

This prompt is a standalone single-agent prompt because `../21_execution_plans/EP-TASK-007.md` does not expose refactored parallel workstreams.

- Execution-plan status: validated.
- Parallel dispatch list: `WS-007-A` graph extraction implementation, `WS-007-D` TASK-007 artifact chain, `WS-007-V` final validation.
- Goal blockers and dependencies: `WS-007-D` depends on final extractor fields and findings from `WS-007-A`; `WS-007-V` depends on implementation and artifact handoffs.
- Owned files: `../../scripts/graph_extractor.py`, `../../tests/test_graph_extractor.py`, `../../package.json`, TASK-007 documentation, context package, coding prompt, validation report and graph entries.
- Forbidden files: `../00_constitution/CONSTITUTION.md`, `../01_vision/VISION.md`, unrelated task, execution-plan, prompt, context-package or validation scopes.
- Expected handoff output: files changed, validation evidence, blockers, dependencies on other workstreams, integration notes, deviations and remaining documentation gaps.

## Acceptance criteria

- A local command extracts graph nodes from IPS Markdown documents.
- The command extracts traceability edges from declared metadata and links.
- Output ordering is deterministic for a fixed input tree.
- Broken or unresolved document references are reported without crashing.
- Fixture tests cover node extraction, edge extraction, broken references and
  deterministic output.
- Repository validation gates pass after implementation evidence is added.

## Validation

Run:

```bash
python3 -m unittest tests.test_graph_extractor
python3 scripts/graph_extractor.py --root . --pretty
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-007
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
