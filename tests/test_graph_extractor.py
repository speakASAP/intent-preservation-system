from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.graph_extractor import dependency_map, detect_orphan_tasks, extract_graph, trace_paths


class GraphExtractorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp(prefix="ips-graph-extractor-test-"))
        self.write("docs/01_vision/VISION.md", "# Vision\n")
        self.write("docs/04_systems/SYS-999-context.md", "# SYS-999 Context\n")
        self.write("docs/07_decisions/ADR-999-graph-first.md", "# ADR-999\n")
        self.write("docs/09_milestones/MS-999-graph.md", "# MS-999 Graph\n")
        self.write(
            "docs/11_tasks/TASK-999-extract.md",
            """# TASK-999: Extract graph

```yaml
id: TASK-999
status: approved
upstream:
  - ../09_milestones/MS-999-graph.md
  - ../04_systems/SYS-999-context.md
goal_impact:
  - ../22_goal_impact/GOAL-IMPACT-TASK-999.md
execution_plan:
  - ../21_execution_plans/EP-TASK-999.md
```
""",
        )
        self.write(
            "docs/21_execution_plans/EP-TASK-999.md",
            """# EP-TASK-999: Extract graph

```yaml
id: EP-TASK-999
status: approved
source_task: ../11_tasks/TASK-999-extract.md
coding_prompt: ../14_prompts/PROMPT-TASK-999.md
context_package: ../13_context_packages/CP-task-999.md
```

## Upstream Traceability

```yaml
vision: ../01_vision/VISION.md
constitution: ../00_constitution/CONSTITUTION.md
feature: ../09_milestones/MS-999-graph.md
goal_impact: ../22_goal_impact/GOAL-IMPACT-TASK-999.md
adr: ../07_decisions/ADR-999-graph-first.md
```
""",
        )
        self.write(
            "docs/22_goal_impact/GOAL-IMPACT-TASK-999.md",
            """# GOAL-IMPACT-TASK-999

```yaml
id: GOAL-IMPACT-TASK-999
artifact_type: task
artifact_id: TASK-999
artifact_path: ../11_tasks/TASK-999-extract.md
primary_goal: Synthetic graph extraction
impact_level: high
upstream_links:
  - ../01_vision/VISION.md
status: approved
```

## Explanation

Synthetic explanation.

## Evidence

- `../01_vision/VISION.md`

## Validation

Synthetic validation.
""",
        )
        self.write(
            "docs/14_prompts/PROMPT-TASK-999.md",
            """# Prompt

```yaml
id: PROMPT-TASK-999
source_task: ../11_tasks/TASK-999-extract.md
execution_plan: ../21_execution_plans/EP-TASK-999.md
context_package: ../13_context_packages/CP-task-999.md
status: used
```
""",
        )
        self.write("docs/13_context_packages/CP-task-999.md", "# Context package\n")
        self.write(
            "docs/12_validation/VAL-TASK-999.md",
            """# Validation Report

Target: TASK-999 / EP-TASK-999

## Summary

Synthetic validation.
""",
        )

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp)

    def write(self, rel: str, text: str) -> None:
        path = self.tmp / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def test_extracts_nodes_from_repository_documents(self) -> None:
        graph = extract_graph(self.tmp)
        nodes = {(node["id"], node["type"]) for node in graph["nodes"]}

        self.assertIn(("TASK-999", "Task"), nodes)
        self.assertIn(("EP-TASK-999", "ExecutionPlan"), nodes)
        self.assertIn(("GOAL-IMPACT-TASK-999", "GoalImpact"), nodes)
        self.assertIn(("PROMPT-TASK-999", "CodingPrompt"), nodes)
        self.assertIn(("VAL-TASK-999", "ValidationReport"), nodes)

    def test_extracts_traceability_edges(self) -> None:
        graph = extract_graph(self.tmp)
        edges = {(edge["from"], edge["type"], edge["to"]) for edge in graph["edges"]}

        self.assertIn(("TASK-999", "derives_from", "MS-999-graph"), edges)
        self.assertIn(("TASK-999", "impacts_goal", "GOAL-IMPACT-TASK-999"), edges)
        self.assertIn(("TASK-999", "decomposes_into", "EP-TASK-999"), edges)
        self.assertIn(("EP-TASK-999", "derives_from", "TASK-999"), edges)
        self.assertIn(("EP-TASK-999", "generates", "PROMPT-TASK-999"), edges)
        self.assertIn(("EP-TASK-999", "included_in_context", "CP-task-999"), edges)
        self.assertIn(("PROMPT-TASK-999", "included_in_context", "CP-task-999"), edges)
        self.assertIn(("VAL-TASK-999", "validates", "TASK-999"), edges)
        self.assertIn(("VAL-TASK-999", "validates", "EP-TASK-999"), edges)

    def test_reports_missing_references_without_crashing(self) -> None:
        self.write(
            "docs/11_tasks/TASK-998-broken.md",
            """# TASK-998: Broken

```yaml
id: TASK-998
status: draft
upstream:
  - ../09_milestones/MS-DOES-NOT-EXIST.md
```
""",
        )

        graph = extract_graph(self.tmp)
        findings = {(finding["type"], finding["reference"]) for finding in graph["findings"]}

        self.assertIn(("missing_reference", "../09_milestones/MS-DOES-NOT-EXIST.md"), findings)

    def test_skips_cross_repository_local_paths(self) -> None:
        self.write(
            "docs/21_execution_plans/EP-CROSS-999.md",
            """# EP-CROSS-999: Cross repository

```yaml
id: EP-CROSS-999
status: draft
source_task: cross-repository-alignment
target_repository: /external/repository
```

Implement `scripts/external_validator.py` in the target repository.
""",
        )

        graph = extract_graph(self.tmp)
        references = {finding["reference"] for finding in graph["findings"]}

        self.assertNotIn("cross-repository-alignment", references)
        self.assertNotIn("scripts/external_validator.py", references)

    def test_output_is_deterministic(self) -> None:
        first = json.dumps(extract_graph(self.tmp), sort_keys=True)
        second = json.dumps(extract_graph(self.tmp), sort_keys=True)

        self.assertEqual(first, second)

    def test_traces_task_to_upstream_vision(self) -> None:
        graph = extract_graph(self.tmp)
        trace = trace_paths(graph, "TASK-999", {"Vision"})

        self.assertEqual(trace["findings"], [])
        self.assertIn(["TASK-999", "GOAL-IMPACT-TASK-999", "VISION"], [path["nodes"] for path in trace["paths"]])

    def test_trace_reports_missing_start_node(self) -> None:
        graph = extract_graph(self.tmp)
        trace = trace_paths(graph, "TASK-DOES-NOT-EXIST", {"Vision"})

        self.assertEqual(trace["paths"], [])
        self.assertEqual(trace["findings"][0]["type"], "missing_start_node")

    def test_detects_orphan_task_without_upstream_trace_path(self) -> None:
        self.write(
            "docs/11_tasks/TASK-997-orphan.md",
            """# TASK-997: Orphan

```yaml
id: TASK-997
status: draft
```
""",
        )

        graph = extract_graph(self.tmp)
        report = detect_orphan_tasks(graph, {"Vision"})
        orphan_ids = {task["id"] for task in report["orphan_tasks"]}
        task_results = {task["id"]: task for task in report["tasks"]}

        self.assertIn("TASK-997", orphan_ids)
        self.assertNotIn("TASK-999", orphan_ids)
        self.assertTrue(task_results["TASK-997"]["is_orphan"])
        self.assertFalse(task_results["TASK-999"]["is_orphan"])
        self.assertIn(("orphan_task", "TASK-997"), {(finding["type"], finding["reference"]) for finding in report["findings"]})

    def test_orphan_task_report_is_deterministic(self) -> None:
        self.write(
            "docs/11_tasks/TASK-997-orphan.md",
            """# TASK-997: Orphan

```yaml
id: TASK-997
status: draft
```
""",
        )

        graph = extract_graph(self.tmp)
        first = json.dumps(detect_orphan_tasks(graph, {"Vision"}), sort_keys=True)
        second = json.dumps(detect_orphan_tasks(graph, {"Vision"}), sort_keys=True)

        self.assertEqual(first, second)

    def test_dependency_map_includes_upstream_and_downstream_edges(self) -> None:
        graph = extract_graph(self.tmp)
        report = dependency_map(graph, "TASK-999", max_depth=1)
        mapped_nodes = {node["id"]: node for node in report["nodes"]}
        mapped_edges = {(edge["from"], edge["type"], edge["to"], edge["direction"]) for edge in report["edges"]}

        self.assertEqual(report["findings"], [])
        self.assertEqual(mapped_nodes["TASK-999"]["directions"], ["start"])
        self.assertIn("GOAL-IMPACT-TASK-999", mapped_nodes)
        self.assertIn("EP-TASK-999", mapped_nodes)
        self.assertIn("VAL-TASK-999", mapped_nodes)
        self.assertIn(("TASK-999", "impacts_goal", "GOAL-IMPACT-TASK-999", "upstream"), mapped_edges)
        self.assertIn(("EP-TASK-999", "derives_from", "TASK-999", "downstream"), mapped_edges)
        self.assertIn(("VAL-TASK-999", "validates", "TASK-999", "downstream"), mapped_edges)

    def test_dependency_map_reports_missing_start_node(self) -> None:
        graph = extract_graph(self.tmp)
        report = dependency_map(graph, "TASK-DOES-NOT-EXIST")

        self.assertEqual(report["nodes"], [])
        self.assertEqual(report["edges"], [])
        self.assertEqual(report["findings"][0]["type"], "missing_start_node")

    def test_dependency_map_report_is_deterministic(self) -> None:
        graph = extract_graph(self.tmp)
        first = json.dumps(dependency_map(graph, "TASK-999", max_depth=2), sort_keys=True)
        second = json.dumps(dependency_map(graph, "TASK-999", max_depth=2), sort_keys=True)

        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
