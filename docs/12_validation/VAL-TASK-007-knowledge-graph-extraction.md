# Validation Report: TASK-007 Knowledge Graph Extraction

Validation id: VAL-TASK-007-2026-06-13
Target: TASK-007 / EP-TASK-007
Date: 2026-06-13
Validator: AI agent

## Summary

TASK-007 adds a dependency-free graph extractor that scans IPS Markdown
documents and emits deterministic `nodes`, `edges` and `findings` collections.
The implementation extracts declared traceability from metadata and target
lines, reports missing references without crashing and includes fixture coverage
for replay determinism.

## Upstream goal

- `../01_vision/VISION.md`
- `../04_systems/SYS-002-context-engine.md`
- `../05_subsystems/SUB-002-graph-builder.md`
- `../07_decisions/ADR-002-use-graph-retrieval-before-rag.md`
- `../09_milestones/MS-004-knowledge-graph.md`
- `../22_goal_impact/GOAL-IMPACT-TASK-007.md`

## Criteria checked

| Criterion | Result | Evidence |
|---|---|---|
| Graph nodes are extracted from IPS Markdown documents | Pass | `test_extracts_nodes_from_repository_documents` verifies task, plan, goal-impact, prompt and validation nodes. |
| Traceability edges are extracted from declared metadata and target lines | Pass | `test_extracts_traceability_edges` verifies task, plan, prompt and validation relationships. |
| Missing references are reported without crashing | Pass | `test_reports_missing_references_without_crashing` verifies a missing upstream link creates a finding. |
| Output is deterministic | Pass | `test_output_is_deterministic` serializes two repeated extractions and compares them. |
| Repository extractor run completes | Pass | `python3 scripts/graph_extractor.py --root . --pretty` completed with deterministic graph data and no findings after local reference cleanup. |
| Repository validation passes | Pass | Full validation commands were run after implementation. |

## Gate evidence

- `python3 -m unittest tests.test_graph_extractor`: pass.
- `python3 scripts/graph_extractor.py --root . --pretty`: pass; output included deterministic graph data with 72 nodes, 121 edges and 0 findings.
- `npm run validate`: pass.
- `python3 scripts/pre_coding_gate.py --root .`: pass.
- `python3 scripts/deployment_readiness_gate.py --root . --target TASK-007`: pass.

## Invariant evidence

- IPS-INV-001: extractor uses declared metadata, target lines and explicit
  references rather than inferred semantic similarity.
- IPS-INV-002: protected vision and constitution documents were not modified.
- IPS-INV-003: implementation followed `../21_execution_plans/EP-TASK-007.md`.
- IPS-INV-004: validation evidence is recorded in this report.
- IPS-INV-005: tests use synthetic fixture documents.

## Sensitive-data scan evidence

The pre-coding gate completed with no sensitive-data findings. Tests and
validation artifacts use synthetic task ids and repository-local document
references only.

## Replay and determinism evidence

`test_output_is_deterministic` runs extraction twice over the same fixture tree
and asserts identical serialized output. The implementation sorts input paths,
nodes, edges and findings before output.

## Issues found

No TASK-007 implementation issues remain. The extractor initially surfaced
cross-repository reference false positives and one real local amendment-folder
gap. The extractor now skips target-repository-local references, and
`../17_governance/amendments/` exists with a README and amendment template.

## Recommendation

Accept TASK-007 as validated for deterministic graph node, edge and finding
extraction. Future Phase 4 tasks should add trace-path queries, orphan-task
detection and dependency-map generation on top of this extractor output.

## Traceability confirmation

TASK-007 remains aligned with the graph-first retrieval architecture because it
creates executable graph extraction before any semantic or vector retrieval
work. The implementation preserves declared traceability and records validation
evidence before closure.
