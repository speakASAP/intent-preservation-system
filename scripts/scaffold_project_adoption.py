#!/usr/bin/env python3
"""Create a non-destructive IPS project-adoption document skeleton."""

from __future__ import annotations

import argparse
import json
import subprocess
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "docs" / "18_templates"

FILE_TEMPLATES = {
    "README_TEMPLATE.md": "README.md",
    "BUSINESS_TEMPLATE.md": "BUSINESS.md",
    "SYSTEM_TEMPLATE.md": "SYSTEM.md",
    "AGENTS_TEMPLATE.md": "AGENTS.md",
    "AGENT_OPERATIONS_TEMPLATE.md": "AGENT_OPERATIONS.md",
    "CLAUDE_TEMPLATE.md": "CLAUDE.md",
    "TASKS_ROOT_TEMPLATE.md": "TASKS.md",
    "STATE_TEMPLATE.json": "STATE.json",
    "CONSTITUTION_TEMPLATE.md": "docs/00_constitution/CONSTITUTION.md",
    "VISION_TEMPLATE.md": "docs/01_vision/VISION.md",
    "INTEGRATION_CONTRACT_TEMPLATE.md": "docs/06_architecture/INTEGRATION_CONTRACT.md",
    "PROJECT_INVARIANTS_TEMPLATE.md": "docs/17_governance/PROJECT_INVARIANTS.md",
    "ADOPTION_VALIDATION_DEBT_TEMPLATE.md": "docs/orchestrator/VALIDATION_DEBT.md",
    "BOOTSTRAP_TASK_TEMPLATE.md": "docs/11_tasks/TASK-001-bootstrap-service.md",
    "BOOTSTRAP_GOAL_IMPACT_TEMPLATE.md": "docs/22_goal_impact/GOAL-IMPACT-TASK-001.md",
    "BOOTSTRAP_EXECUTION_PLAN_TEMPLATE.md": "docs/21_execution_plans/EP-TASK-001-bootstrap-service.md",
    "BOOTSTRAP_VALIDATION_TEMPLATE.md": "docs/12_validation/VAL-TASK-001-bootstrap-service.md",
}


def current_revision() -> str:
    result = subprocess.run(
        ["git", "-C", str(ROOT), "rev-parse", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def render(text: str, project: str) -> str:
    rendered = text.replace("{{PROJECT_NAME}}", project)
    rendered = rendered.replace("{{DATE}}", date.today().isoformat())
    return rendered


def write_new(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def create_profile(
    destination: Path,
    project: str,
    repository: str,
    revision: str,
) -> bool:
    profile_path = destination / "ips-adoption.json"
    if profile_path.exists():
        return False
    profile = json.loads(
        (TEMPLATES / "IPS_ADOPTION_PROFILE_TEMPLATE.json").read_text(encoding="utf-8")
    )
    profile["project"]["name"] = project
    profile["project"]["repository"] = repository
    profile["standard"]["revision"] = revision
    profile_path.write_text(json.dumps(profile, indent=2) + "\n", encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, help="Adopting repository root")
    parser.add_argument("--project", required=True, help="Repository/project name")
    parser.add_argument("--repository", required=True, help="Canonical Git repository URL")
    parser.add_argument(
        "--standard-revision",
        help="Reviewed IPS Git revision; defaults to the current IPS HEAD",
    )
    args = parser.parse_args()

    destination = Path(args.root).resolve()
    if not destination.is_dir():
        parser.error(f"project root does not exist: {destination}")

    revision = args.standard_revision or current_revision()
    created: list[str] = []
    skipped: list[str] = []

    for template_name, relative_path in FILE_TEMPLATES.items():
        content = render(
            (TEMPLATES / template_name).read_text(encoding="utf-8"),
            args.project,
        )
        target = destination / relative_path
        (created if write_new(target, content) else skipped).append(relative_path)

    profile_relative = "ips-adoption.json"
    if create_profile(destination, args.project, args.repository, revision):
        created.append(profile_relative)
    else:
        skipped.append(profile_relative)

    for relative_path in sorted(created):
        print(f"created: {relative_path}")
    for relative_path in sorted(skipped):
        print(f"kept existing: {relative_path}")

    print(
        "Skeleton created. Resolve protected intent and planning placeholders, then "
        "run validate_adoption_profile.py with --phase planning."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
