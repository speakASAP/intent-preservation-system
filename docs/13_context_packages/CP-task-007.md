# Context Package: TASK-007

## Target task

TASK-007: `../11_tasks/TASK-007-extract-knowledge-graph-from-documents.md`

## Upstream traceability

```text
../01_vision/VISION.md -> ../04_systems/SYS-002-context-engine.md -> ../05_subsystems/SUB-002-graph-builder.md -> ../09_milestones/MS-004-knowledge-graph.md -> TASK-007
```

## Included documents

- `../11_tasks/TASK-007-extract-knowledge-graph-from-documents.md`
- `../21_execution_plans/EP-TASK-007.md`
- `../22_goal_impact/GOAL-IMPACT-TASK-007.md`
- `../12_validation/VAL-TASK-007-knowledge-graph-extraction.md`
- `../../graph/GRAPH_SCHEMA.md`
- `../../graph/project_graph.example.yaml`
- `../04_systems/SYS-002-context-engine.md`
- `../05_subsystems/SUB-002-graph-builder.md`
- `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- `../07_decisions/ADR-002-use-graph-retrieval-before-rag.md`
- `../17_governance/PROJECT_INVARIANTS.md`
- `../23_documentation_contracts/SENSITIVE_DATA_POLICY.md`

## Excluded documents

- Unrelated task scopes and implementation plans are excluded.
- Vector search, embeddings and optional RAG documents are excluded from this
  first graph extraction slice.
- Raw production data, secrets, confidential identifiers and real customer data
  are excluded.

## Constraints

- Extract only declared graph relationships from metadata, target lines and
  explicit Markdown references.
- Keep output deterministic for a fixed repository state.
- Do not modify `../00_constitution/CONSTITUTION.md` or `../01_vision/VISION.md`.
- Use synthetic fixture documents in tests.

## Parallel execution context

- Execution plan: `../21_execution_plans/EP-TASK-007.md`
- Plan status: validated.
- Parallelization status: `EP-TASK-007.md` includes Parallel Execution Strategy, Goal Blockers And Dependencies, Parallel Dispatch List and Parallel Agent Handoff Prompts.
- Ready-now workstreams: `WS-007-A` implements deterministic graph extraction.
- Dependency-gated workstreams: `WS-007-D` updates the TASK-007 artifact chain; `WS-007-V` validates after implementation and documentation handoffs.
- Integration owner and merge order: validation agent integrates after `WS-007-A`, then `WS-007-D`, then `WS-007-V`.

## Agent prompt

Implement TASK-007 using the included documents. Build a deterministic,
dependency-free extractor for graph nodes, traceability edges and reference
findings from IPS Markdown documents.

## Validation instructions

Run the focused graph extractor tests, run the extractor against the repository,
and then run:

```bash
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-007
```
