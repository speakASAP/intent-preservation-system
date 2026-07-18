# TASK-007: Extract knowledge graph from repository documents

```yaml
id: TASK-007
status: validated
owner: knowledge-graph-agent
created: 2026-06-13
last_updated: 2026-06-13
completeness_level: validated
upstream:
  - ../01_vision/VISION.md
  - ../04_systems/SYS-002-context-engine.md
  - ../05_subsystems/SUB-002-graph-builder.md
  - ../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md
  - ../07_decisions/ADR-002-use-graph-retrieval-before-rag.md
  - ../08_roadmap/ROADMAP.md
  - ../09_milestones/MS-004-knowledge-graph.md
goal_impact:
  - ../22_goal_impact/GOAL-IMPACT-TASK-007.md
execution_plan:
  - ../21_execution_plans/EP-TASK-007.md
validation_report:
  - ../12_validation/VAL-TASK-007-knowledge-graph-extraction.md
```

## Objective

Implement the first Phase 4 knowledge-graph extraction capability: a deterministic
repository-local command that scans IPS Markdown documents and extracts graph
nodes and traceability edges from declared metadata and document links.

## Upstream Links

- Vision: `../01_vision/VISION.md`
- Context engine: `../04_systems/SYS-002-context-engine.md`
- Graph builder subsystem: `../05_subsystems/SUB-002-graph-builder.md`
- Context retrieval architecture: `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- Graph-first ADR: `../07_decisions/ADR-002-use-graph-retrieval-before-rag.md`
- Roadmap Phase 4: `../08_roadmap/ROADMAP.md`
- Knowledge graph milestone: `../09_milestones/MS-004-knowledge-graph.md`

## Goal Impact

This task starts Phase 4 by turning graph-first retrieval from documented intent
into an executable extraction step. The extracted nodes and edges become the
input for later trace-path queries, orphan-task detection and dependency maps.

## Project Invariant Impact

- IPS-INV-001: extracted graph records must preserve traceability to upstream
  intent instead of inferring undocumented relationships.
- IPS-INV-002: immutable vision and constitution documents may be read but must
  not be modified.
- IPS-INV-003: implementation must follow `../21_execution_plans/EP-TASK-007.md`.
- IPS-INV-004: validation evidence must be captured before this task is closed.
- IPS-INV-005: tests, fixtures and reports must not include secrets, raw
  production data or confidential identifiers.

## Sensitive-Data Classification

Classification: none

The extractor reads repository-local governance and planning Markdown documents.
Tests must use synthetic fixture documents and must not include secrets, raw
production data, customer data or confidential identifiers.

## Contract/Schema Impact

This task creates the first executable extraction mapping for
`../../graph/GRAPH_SCHEMA.md`. It must not change the graph schema unless the
implementation discovers a schema gap and documents that gap for separate
review.

## Replay/Determinism Impact

Extraction must be deterministic for a fixed repository state. Re-running the
command over the same files must produce stable node and edge output ordering.

## Scope

- Add a dependency-free graph extraction CLI for repository Markdown documents.
- Extract graph nodes from document type, document metadata and file path.
- Extract traceability edges from known metadata fields such as `upstream`,
  `goal_impact`, `execution_plan`, `source_task`, validation links and prompt
  context links.
- Normalize repository-relative paths and report unresolved references.
- Emit deterministic structured output suitable for later validation or query
  work.
- Add focused fixture tests for node extraction, edge extraction, missing-link
  reporting and deterministic output order.

## Non-Goals

- Do not implement graph querying or path traversal beyond extraction output.
- Do not implement vector search, embeddings or RAG.
- Do not generate context packages or coding prompts.
- Do not rewrite existing project documents to satisfy extractor output.
- Do not modify `../00_constitution/CONSTITUTION.md` or `../01_vision/VISION.md`.

## Acceptance Criteria

- [x] A local command extracts graph nodes from IPS Markdown documents.
- [x] The command extracts traceability edges from declared metadata and links.
- [x] Output ordering is deterministic for a fixed input tree.
- [x] Broken or unresolved document references are reported without crashing.
- [x] Fixture tests cover node extraction, edge extraction, broken references
      and deterministic output.
- [x] Repository validation gates pass after implementation evidence is added.

## Required Context

- `../../graph/GRAPH_SCHEMA.md`
- `../../graph/project_graph.example.yaml`
- `../04_systems/SYS-002-context-engine.md`
- `../05_subsystems/SUB-002-graph-builder.md`
- `../06_architecture/CONTEXT_RETRIEVAL_ARCHITECTURE.md`
- `../07_decisions/ADR-002-use-graph-retrieval-before-rag.md`
- `../17_governance/PROJECT_INVARIANTS.md`
- `../23_documentation_contracts/SENSITIVE_DATA_POLICY.md`

## Validation Task

Validate by running focused graph extractor tests, comparing deterministic output
from synthetic fixtures, and then running the strict documentation audit,
pre-coding gate and deployment-readiness gate after a TASK-007 validation report
exists.

## Required Gates

```bash
python3 -m unittest tests.test_graph_extractor
npm run validate
python3 scripts/pre_coding_gate.py --root .
python3 scripts/deployment_readiness_gate.py --root . --target TASK-007
```

## Execution Plan Requirement

This task must not be converted into a coding prompt until
`../21_execution_plans/EP-TASK-007.md` is reviewed or approved.
