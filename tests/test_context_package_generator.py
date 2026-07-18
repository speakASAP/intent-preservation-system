from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path


from scripts.context_package_generator import (
    build_local_embedding_index,
    compare_candidate_retrieval,
    embedding_provider_for,
    EmbeddingInput,
    evaluate_retrieval_baseline,
    generate_candidate_results,
    generate,
    local_embedding_retrieval_report,
    optional_retrieval_report,
)


class ContextPackageGeneratorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp(prefix="ips-context-package-test-"))
        self.write(
            "docs/11_tasks/TASK-999-synthetic.md",
            """# TASK-999: Synthetic package generation

```yaml
id: TASK-999
status: approved
upstream:
  - ../01_vision/VISION.md
  - ../04_systems/SYS-002-context-engine.md
goal_impact:
  - ../22_goal_impact/GOAL-IMPACT-TASK-999.md
execution_plan:
  - ../21_execution_plans/EP-TASK-999.md
validation_report:
  - ../12_validation/VAL-TASK-999.md
```

## Acceptance Criteria

- Generated context package names the task.
- Generated context package includes upstream links.

## Required Context

- `../18_templates/CONTEXT_PACKAGE_TEMPLATE.md`
""",
        )

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp)

    def write(self, rel: str, text: str) -> None:
        path = self.tmp / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def write_json(self, rel: str, text: str) -> Path:
        path = self.tmp / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def test_generate_context_package_from_task_metadata(self) -> None:
        target = generate(self.tmp, "TASK-999")

        text = target.read_text(encoding="utf-8")
        self.assertEqual(
            target.relative_to(self.tmp.resolve()).as_posix(),
            "docs/13_context_packages/CP-task-999.md",
        )
        self.assertIn("TASK-999: `../11_tasks/TASK-999-synthetic.md`", text)
        self.assertIn("- `../01_vision/VISION.md`", text)
        self.assertIn("- `../04_systems/SYS-002-context-engine.md`", text)
        self.assertIn("- `../22_goal_impact/GOAL-IMPACT-TASK-999.md`", text)
        self.assertIn("- `../21_execution_plans/EP-TASK-999.md`", text)
        self.assertIn("- `../12_validation/VAL-TASK-999.md`", text)
        self.assertIn("- `../18_templates/CONTEXT_PACKAGE_TEMPLATE.md`", text)
        self.assertIn("Generated context package includes upstream links.", text)

    def test_generate_refuses_existing_output_without_force(self) -> None:
        target = generate(self.tmp, "TASK-999")

        with self.assertRaises(FileExistsError):
            generate(self.tmp, "TASK-999")

        changed = generate(self.tmp, "TASK-999", force=True)
        self.assertEqual(changed, target)

    def test_optional_retrieval_suggests_supporting_documents(self) -> None:
        self.write("docs/01_vision/VISION.md", "# Vision\n\nSynthetic required vision.\n")
        self.write("docs/04_systems/SYS-002-context-engine.md", "# Context Engine\n")
        self.write(
            "docs/06_architecture/OPTIONAL_RETRIEVAL.md",
            "# Optional Retrieval\n\nKeyword retrieval supports optional context suggestions.\n",
        )

        report = optional_retrieval_report(self.tmp, "TASK-999", query="keyword retrieval", limit=3)
        suggestions = report["optional_suggestions"]
        required_context = report["required_context"]

        self.assertEqual(report["task_id"], "TASK-999")
        self.assertEqual(report["retrieval_mode"], "keyword")
        self.assertEqual(report["query_terms"], ["keyword", "retrieval"])
        self.assertIsInstance(suggestions, list)
        self.assertIn("../01_vision/VISION.md", required_context)
        self.assertNotIn(
            "docs/01_vision/VISION.md",
            {suggestion["path"] for suggestion in suggestions},
        )
        self.assertEqual(suggestions[0]["path"], "docs/06_architecture/OPTIONAL_RETRIEVAL.md")
        self.assertEqual(suggestions[0]["retrieval_mode"], "keyword")
        self.assertIn("keyword", suggestions[0]["matched_terms"])
        self.assertIn("score_components", suggestions[0])
        self.assertGreaterEqual(suggestions[0]["score_components"]["body"], 1)
        self.assertGreaterEqual(report["scan_summary"]["documents_scanned"], 3)
        self.assertGreaterEqual(report["scan_summary"]["required_documents_excluded"], 2)

    def test_optional_retrieval_reports_missing_task(self) -> None:
        report = optional_retrieval_report(self.tmp, "TASK-DOES-NOT-EXIST")

        self.assertEqual(report["optional_suggestions"], [])
        self.assertEqual(report["required_context"], [])
        self.assertEqual(report["scan_summary"]["documents_scanned"], 0)
        self.assertEqual(report["findings"][0]["type"], "missing_task")

    def test_optional_retrieval_reports_no_suggestions(self) -> None:
        report = optional_retrieval_report(self.tmp, "TASK-999", query="nonmatchingterm")

        self.assertEqual(report["optional_suggestions"], [])
        self.assertEqual(report["findings"][0]["type"], "no_optional_suggestions")
        self.assertEqual(report["scan_summary"]["candidate_documents"], 0)

    def test_optional_retrieval_filters_by_minimum_score(self) -> None:
        self.write(
            "docs/06_architecture/OPTIONAL_RETRIEVAL.md",
            "# Optional Retrieval\n\nkeyword retrieval\n",
        )

        included = optional_retrieval_report(self.tmp, "TASK-999", query="keyword retrieval", min_score=2)
        excluded = optional_retrieval_report(self.tmp, "TASK-999", query="keyword retrieval", min_score=20)

        self.assertEqual(included["optional_suggestions"][0]["path"], "docs/06_architecture/OPTIONAL_RETRIEVAL.md")
        self.assertEqual(excluded["optional_suggestions"], [])
        self.assertEqual(excluded["scan_summary"]["min_score"], 20)
        self.assertEqual(excluded["findings"][0]["type"], "no_optional_suggestions")

    def test_optional_retrieval_output_is_deterministic(self) -> None:
        self.write(
            "docs/06_architecture/OPTIONAL_RETRIEVAL_A.md",
            "# Optional Retrieval A\n\nkeyword retrieval support\n",
        )
        self.write(
            "docs/06_architecture/OPTIONAL_RETRIEVAL_B.md",
            "# Optional Retrieval B\n\nkeyword retrieval support\n",
        )

        first = optional_retrieval_report(self.tmp, "TASK-999", query="keyword retrieval", limit=5)
        second = optional_retrieval_report(self.tmp, "TASK-999", query="keyword retrieval", limit=5)

        self.assertEqual(first, second)
        self.assertEqual(
            [suggestion["path"] for suggestion in first["optional_suggestions"]],
            [
                "docs/06_architecture/OPTIONAL_RETRIEVAL_A.md",
                "docs/06_architecture/OPTIONAL_RETRIEVAL_B.md",
            ],
        )

    def test_evaluate_retrieval_baseline_passes_expected_case(self) -> None:
        self.write(
            "docs/06_architecture/OPTIONAL_RETRIEVAL.md",
            "# Optional Retrieval\n\nkeyword retrieval support\n",
        )
        baseline = self.write_json(
            "tests/fixtures/retrieval_baseline.json",
            """{
  "cases": [
    {
      "id": "keyword-support",
      "task_id": "TASK-999",
      "query": "keyword retrieval",
      "limit": 1,
      "expected_optional_paths": ["docs/06_architecture/OPTIONAL_RETRIEVAL.md"]
    }
  ]
}
""",
        )

        report = evaluate_retrieval_baseline(self.tmp, baseline)

        self.assertEqual(report["total_cases"], 1)
        self.assertEqual(report["passed_cases"], 1)
        self.assertEqual(report["failed_cases"], 0)
        self.assertEqual(report["findings"], [])

    def test_evaluate_retrieval_baseline_reports_failures(self) -> None:
        self.write(
            "docs/06_architecture/OPTIONAL_RETRIEVAL.md",
            "# Optional Retrieval\n\nkeyword retrieval support\n",
        )
        baseline = self.write_json(
            "tests/fixtures/retrieval_baseline.json",
            """{
  "cases": [
    {
      "id": "wrong-path",
      "task_id": "TASK-999",
      "query": "keyword retrieval",
      "limit": 1,
      "expected_optional_paths": ["docs/06_architecture/WRONG.md"]
    }
  ]
}
""",
        )

        report = evaluate_retrieval_baseline(self.tmp, baseline)
        case = report["cases"][0]

        self.assertEqual(report["failed_cases"], 1)
        self.assertEqual(case["missing_optional_paths"], ["docs/06_architecture/WRONG.md"])
        self.assertEqual(case["unexpected_optional_paths"], ["docs/06_architecture/OPTIONAL_RETRIEVAL.md"])
        self.assertEqual(report["findings"][0]["type"], "retrieval_baseline_failed")

    def test_evaluate_retrieval_baseline_accepts_expected_missing_task_finding(self) -> None:
        baseline = self.write_json(
            "tests/fixtures/retrieval_baseline.json",
            """{
  "cases": [
    {
      "id": "missing-task",
      "task_id": "TASK-DOES-NOT-EXIST",
      "expected_findings": ["missing_task"]
    }
  ]
}
""",
        )

        report = evaluate_retrieval_baseline(self.tmp, baseline)

        self.assertEqual(report["passed_cases"], 1)
        self.assertEqual(report["cases"][0]["actual_findings"], ["missing_task"])

    def test_evaluate_retrieval_baseline_is_deterministic(self) -> None:
        self.write(
            "docs/06_architecture/OPTIONAL_RETRIEVAL.md",
            "# Optional Retrieval\n\nkeyword retrieval support\n",
        )
        baseline = self.write_json(
            "tests/fixtures/retrieval_baseline.json",
            """{
  "cases": [
    {
      "id": "keyword-support",
      "task_id": "TASK-999",
      "query": "keyword retrieval",
      "limit": 1,
      "expected_optional_paths": ["docs/06_architecture/OPTIONAL_RETRIEVAL.md"]
    }
  ]
}
""",
        )

        first = evaluate_retrieval_baseline(self.tmp, baseline)
        second = evaluate_retrieval_baseline(self.tmp, baseline)

        self.assertEqual(first, second)

    def test_compare_candidate_retrieval_passes_expected_case(self) -> None:
        baseline = self.write_json(
            "tests/fixtures/retrieval_baseline.json",
            """{
  "cases": [
    {
      "id": "keyword-support",
      "expected_optional_paths": ["docs/06_architecture/OPTIONAL_RETRIEVAL.md"]
    }
  ]
}
""",
        )
        candidate = self.write_json(
            "tests/fixtures/retrieval_candidate.json",
            """{
  "retrieval_mode": "candidate-semantic-fixture",
  "cases": [
    {
      "id": "keyword-support",
      "returned_optional_paths": ["docs/06_architecture/OPTIONAL_RETRIEVAL.md"]
    }
  ]
}
""",
        )

        report = compare_candidate_retrieval(baseline, candidate)

        self.assertEqual(report["candidate_retrieval_mode"], "candidate-semantic-fixture")
        self.assertEqual(report["passed_cases"], 1)
        self.assertEqual(report["failed_cases"], 0)
        self.assertEqual(report["findings"], [])

    def test_compare_candidate_retrieval_reports_failures(self) -> None:
        baseline = self.write_json(
            "tests/fixtures/retrieval_baseline.json",
            """{
  "cases": [
    {
      "id": "keyword-support",
      "expected_optional_paths": ["docs/06_architecture/OPTIONAL_RETRIEVAL.md"]
    }
  ]
}
""",
        )
        candidate = self.write_json(
            "tests/fixtures/retrieval_candidate.json",
            """{
  "cases": [
    {
      "id": "keyword-support",
      "returned_optional_paths": ["docs/06_architecture/WRONG.md"]
    }
  ]
}
""",
        )

        report = compare_candidate_retrieval(baseline, candidate)
        case = report["cases"][0]

        self.assertEqual(report["failed_cases"], 1)
        self.assertEqual(case["missing_expected_paths"], ["docs/06_architecture/OPTIONAL_RETRIEVAL.md"])
        self.assertEqual(case["unexpected_candidate_paths"], ["docs/06_architecture/WRONG.md"])
        self.assertEqual(report["findings"][0]["type"], "candidate_retrieval_comparison_failed")

    def test_compare_candidate_retrieval_reports_missing_candidate_case(self) -> None:
        baseline = self.write_json(
            "tests/fixtures/retrieval_baseline.json",
            """{
  "cases": [
    {
      "id": "keyword-support",
      "expected_optional_paths": ["docs/06_architecture/OPTIONAL_RETRIEVAL.md"]
    }
  ]
}
""",
        )
        candidate = self.write_json("tests/fixtures/retrieval_candidate.json", """{"cases": []}""")

        report = compare_candidate_retrieval(baseline, candidate)
        case = report["cases"][0]

        self.assertEqual(report["failed_cases"], 1)
        self.assertEqual(case["findings"], ["missing_candidate_case"])

    def test_compare_candidate_retrieval_is_deterministic(self) -> None:
        baseline = self.write_json(
            "tests/fixtures/retrieval_baseline.json",
            """{
  "cases": [
    {
      "id": "keyword-support",
      "expected_optional_paths": ["docs/06_architecture/OPTIONAL_RETRIEVAL.md"]
    }
  ]
}
""",
        )
        candidate = self.write_json(
            "tests/fixtures/retrieval_candidate.json",
            """{
  "cases": [
    {
      "id": "keyword-support",
      "returned_optional_paths": ["docs/06_architecture/OPTIONAL_RETRIEVAL.md"]
    }
  ]
}
""",
        )

        first = compare_candidate_retrieval(baseline, candidate)
        second = compare_candidate_retrieval(baseline, candidate)

        self.assertEqual(first, second)

    def test_generate_candidate_results_from_baseline(self) -> None:
        self.write(
            "docs/06_architecture/OPTIONAL_RETRIEVAL.md",
            "# Optional Retrieval\n\nkeyword retrieval support\n",
        )
        baseline = self.write_json(
            "tests/fixtures/retrieval_baseline.json",
            """{
  "cases": [
    {
      "id": "keyword-support",
      "task_id": "TASK-999",
      "query": "keyword retrieval",
      "limit": 1,
      "expected_optional_paths": ["docs/06_architecture/OPTIONAL_RETRIEVAL.md"]
    }
  ]
}
""",
        )

        candidate = generate_candidate_results(self.tmp, baseline)

        self.assertEqual(candidate["retrieval_mode"], "local-semantic-token-overlap")
        self.assertEqual(candidate["cases"][0]["id"], "keyword-support")
        self.assertEqual(candidate["cases"][0]["returned_optional_paths"], ["docs/06_architecture/OPTIONAL_RETRIEVAL.md"])

    def test_generated_candidate_results_compare_against_baseline(self) -> None:
        self.write(
            "docs/06_architecture/OPTIONAL_RETRIEVAL.md",
            "# Optional Retrieval\n\nkeyword retrieval support\n",
        )
        baseline = self.write_json(
            "tests/fixtures/retrieval_baseline.json",
            """{
  "cases": [
    {
      "id": "keyword-support",
      "task_id": "TASK-999",
      "query": "keyword retrieval",
      "limit": 1,
      "expected_optional_paths": ["docs/06_architecture/OPTIONAL_RETRIEVAL.md"]
    }
  ]
}
""",
        )
        candidate = generate_candidate_results(self.tmp, baseline)
        candidate_path = self.write_json("tests/fixtures/retrieval_candidate.json", json.dumps(candidate))

        report = compare_candidate_retrieval(baseline, candidate_path)

        self.assertEqual(report["failed_cases"], 0)
        self.assertEqual(report["passed_cases"], 1)

    def test_generate_candidate_results_is_deterministic(self) -> None:
        self.write(
            "docs/06_architecture/OPTIONAL_RETRIEVAL.md",
            "# Optional Retrieval\n\nkeyword retrieval support\n",
        )
        baseline = self.write_json(
            "tests/fixtures/retrieval_baseline.json",
            """{
  "cases": [
    {
      "id": "keyword-support",
      "task_id": "TASK-999",
      "query": "keyword retrieval",
      "limit": 1,
      "expected_optional_paths": ["docs/06_architecture/OPTIONAL_RETRIEVAL.md"]
    }
  ]
}
""",
        )

        first = generate_candidate_results(self.tmp, baseline)
        second = generate_candidate_results(self.tmp, baseline)

        self.assertEqual(first, second)

    def test_local_embedding_index_excludes_required_documents(self) -> None:
        self.write("docs/01_vision/VISION.md", "# Vision\n\nSynthetic required vision.\n")
        self.write(
            "docs/06_architecture/OPTIONAL_RETRIEVAL.md",
            "# Optional Retrieval\n\nembedding retrieval support\n",
        )

        documents, summary = build_local_embedding_index(
            self.tmp,
            required_rels={"docs/01_vision/VISION.md"},
        )

        self.assertEqual(summary["dimensions"], 64)
        self.assertEqual(summary["provider"], "local-hash")
        self.assertEqual(summary["required_documents_excluded"], 1)
        self.assertIn("docs/06_architecture/OPTIONAL_RETRIEVAL.md", {document.path for document in documents})
        self.assertNotIn("docs/01_vision/VISION.md", {document.path for document in documents})
        self.assertTrue(all(len(document.vector) == 64 for document in documents))

    def test_embedding_provider_boundary_returns_deterministic_vectors(self) -> None:
        provider = embedding_provider_for("local-hash")
        item = EmbeddingInput(
            body="embedding retrieval support",
            path="docs/06_architecture/OPTIONAL_RETRIEVAL.md",
            title="Optional Retrieval",
        )

        first = provider.embed(item)
        second = provider.embed(item)

        self.assertEqual(provider.name, "local-hash")
        self.assertEqual(first, second)
        self.assertEqual(first.provider, "local-hash")
        self.assertEqual(first.dimensions, 64)
        self.assertEqual(len(first.vector), 64)

    def test_embedding_provider_boundary_rejects_unknown_provider(self) -> None:
        with self.assertRaises(ValueError):
            embedding_provider_for("external-provider")

    def test_local_embedding_retrieval_suggests_supporting_documents(self) -> None:
        self.write("docs/01_vision/VISION.md", "# Vision\n\nSynthetic required vision.\n")
        self.write(
            "docs/06_architecture/OPTIONAL_RETRIEVAL.md",
            "# Optional Retrieval\n\nembedding retrieval support\n",
        )

        report = local_embedding_retrieval_report(self.tmp, "TASK-999", query="embedding retrieval", limit=1)
        suggestions = report["optional_suggestions"]

        self.assertEqual(report["retrieval_mode"], "local-embedding-index")
        self.assertEqual(report["embedding_index"]["provider"], "local-hash")
        self.assertEqual(report["embedding_index"]["dimensions"], 64)
        self.assertEqual(suggestions[0]["path"], "docs/06_architecture/OPTIONAL_RETRIEVAL.md")
        self.assertEqual(suggestions[0]["retrieval_mode"], "local-embedding-index")
        self.assertIn("cosine_similarity_x10000", suggestions[0]["score_components"])

    def test_generate_embedding_candidate_results_compare_against_baseline(self) -> None:
        self.write(
            "docs/06_architecture/OPTIONAL_RETRIEVAL.md",
            "# Optional Retrieval\n\nembedding retrieval support\n",
        )
        baseline = self.write_json(
            "tests/fixtures/retrieval_baseline.json",
            """{
  "cases": [
    {
      "id": "embedding-support",
      "task_id": "TASK-999",
      "query": "embedding retrieval",
      "limit": 1,
      "expected_optional_paths": ["docs/06_architecture/OPTIONAL_RETRIEVAL.md"]
    }
  ]
}
""",
        )
        candidate = generate_candidate_results(self.tmp, baseline, retrieval_mode="local-embedding-index")
        candidate_path = self.write_json("tests/fixtures/retrieval_candidate.json", json.dumps(candidate))

        report = compare_candidate_retrieval(baseline, candidate_path)

        self.assertEqual(candidate["retrieval_mode"], "local-embedding-index")
        self.assertEqual(candidate["embedding_provider"], "local-hash")
        self.assertEqual(report["failed_cases"], 0)
        self.assertEqual(report["passed_cases"], 1)

    def test_local_embedding_candidate_results_are_deterministic(self) -> None:
        self.write(
            "docs/06_architecture/OPTIONAL_RETRIEVAL.md",
            "# Optional Retrieval\n\nembedding retrieval support\n",
        )
        baseline = self.write_json(
            "tests/fixtures/retrieval_baseline.json",
            """{
  "cases": [
    {
      "id": "embedding-support",
      "task_id": "TASK-999",
      "query": "embedding retrieval",
      "limit": 1,
      "expected_optional_paths": ["docs/06_architecture/OPTIONAL_RETRIEVAL.md"]
    }
  ]
}
""",
        )

        first = generate_candidate_results(self.tmp, baseline, retrieval_mode="local-embedding-index")
        second = generate_candidate_results(self.tmp, baseline, retrieval_mode="local-embedding-index")

        self.assertEqual(first, second)

    def test_external_provider_dry_run_candidate_results_compare_against_baseline(self) -> None:
        baseline = self.write_json(
            "tests/fixtures/retrieval_baseline.json",
            """{
  "cases": [
    {
      "id": "dry-run-support",
      "task_id": "TASK-999",
      "query": "external provider dry run",
      "limit": 1,
      "expected_optional_paths": ["docs/06_architecture/OPTIONAL_RETRIEVAL.md"]
    }
  ]
}
""",
        )
        candidate = generate_candidate_results(self.tmp, baseline, retrieval_mode="external-provider-dry-run")
        candidate_path = self.write_json("tests/fixtures/retrieval_candidate.json", json.dumps(candidate))

        report = compare_candidate_retrieval(baseline, candidate_path)

        self.assertEqual(candidate["retrieval_mode"], "external-provider-dry-run")
        self.assertEqual(candidate["embedding_provider"], "external-provider-dry-run")
        self.assertTrue(candidate["dry_run"])
        self.assertEqual(candidate["network_calls"], 0)
        self.assertTrue(candidate["cases"][0]["dry_run"])
        self.assertEqual(report["failed_cases"], 0)

    def test_external_provider_dry_run_does_not_require_repository_document_text(self) -> None:
        baseline = self.write_json(
            "tests/fixtures/retrieval_baseline.json",
            """{
  "cases": [
    {
      "id": "dry-run-missing-doc",
      "task_id": "TASK-999",
      "expected_optional_paths": ["docs/06_architecture/NOT_PRESENT.md"]
    }
  ]
}
""",
        )

        candidate = generate_candidate_results(self.tmp, baseline, retrieval_mode="external-provider-dry-run")

        self.assertEqual(candidate["cases"][0]["returned_optional_paths"], ["docs/06_architecture/NOT_PRESENT.md"])
        self.assertEqual(candidate["network_calls"], 0)


if __name__ == "__main__":
    unittest.main()
