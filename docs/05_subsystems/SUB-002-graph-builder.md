# SUB-002 Graph Builder

Parent system: SYS-002 Context Engine

## Purpose

Build a project knowledge graph from documents and traceability fields.

## Responsibilities

- Parse graph node and edge declarations.
- Validate that graph paths point to real repository artifacts.
- Check required relationships between tasks, plans, prompts, context packages and validation reports.
- Report graph gaps that would prevent deterministic context retrieval.

## Inputs

- Markdown document metadata and trace links.
- `graph/project_graph.example.yaml`.
- Required relationship rules from `graph/GRAPH_SCHEMA.md`.

## Outputs

- Validated graph nodes and edges.
- Audit findings for missing nodes, missing edges and broken graph paths.

## Node types

- Constitution
- VisionGoal
- BusinessRequirement
- System
- Subsystem
- ADR
- RoadmapItem
- Milestone
- Feature
- Task
- ValidationReport
- ContextPackage
- Prompt

## Edge types

- implements
- decomposes_into
- depends_on
- justified_by
- validates
- belongs_to
- blocked_by
- supersedes
- amends

## Validation

The graph is valid when every task has a path to at least one vision goal.
