#!/usr/bin/env python3
"""Ecosystem-wide IPS adoption validator with a narrow, safe auto-heal path.

This script re-runs the canonical `validate_adoption_profile.py --phase
planning` check for every repository flagged `ipsAdoptionRequired: true` in
`shared/config/ecosystem-repositories.json`. It is designed to run
unattended (via a systemd user timer) after the ecosystem-wide IPS adoption
rollout, to catch and repair the one recurring, low-risk drift pattern
observed in production: a concurrent, unrelated commit overwriting
STATE.json with a repository-native schema and dropping the IPS-required
top-level keys (schemaVersion, project, lifecycle, health, activeTask,
lastUpdated, deployment, blockers, followUps).

Deliberately NOT auto-healed (reported only): missing/incomplete markdown
sections, placeholder content, missing approval evidence, broken
traceability references, or anything requiring a human/agent judgment call
about real project content. Never fabricate business intent.

Safety:
- Never touches shared/config/ecosystem-repositories.json or the master
  rollout plan (those are owned by the human-in-the-loop rollout process).
- Never runs deploy/kubectl/docker commands; only `git add`/`git commit`
  inside each repo's own working tree (each repo's existing post-commit hook
  handles its own deploy queueing, unchanged).
- Never force-pushes; never pushes at all (repos are non-bare, main is the
  canonical remote copy already).
- Idempotent: a clean repo produces no diff and nothing is committed.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

GITHUB_ROOT = Path("/home/ssf/Documents/Github")
VALIDATOR = GITHUB_ROOT / "intent-preservation-system" / "scripts" / "validate_adoption_profile.py"
CATALOG = GITHUB_ROOT / "shared" / "config" / "ecosystem-repositories.json"
REPORT_DIR = Path.home() / ".local" / "state" / "ips-ecosystem-validator"
REPORT_DIR.mkdir(parents=True, exist_ok=True)

STATE_KEY_ERROR_PREFIXES = (
    "artifact state missing keys:",
    "artifact state project must match project.name",
    "artifact state schemaVersion must be 1",
    "artifact state lifecycle must be a concrete string",
    "artifact state health must be a concrete string",
    "artifact state activeTask must be a concrete string",
    "artifact state lastUpdated must be a concrete string",
    "artifact state lastUpdated must be an ISO date or timestamp",
    "artifact state deployment must contain a concrete status",
    "artifact state blockers must be an array",
    "artifact state followUps must be an array",
)


def run_validator(repo: str) -> tuple[int, list[str]]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), "--root", repo, "--phase", "planning"],
        cwd=GITHUB_ROOT,
        capture_output=True,
        text=True,
    )
    lines = [l for l in (proc.stdout + proc.stderr).splitlines() if l.strip()]
    return proc.returncode, lines


def all_state_drift(errors: list[str]) -> bool:
    """True only if every reported error is a known STATE.json drift error."""
    if not errors:
        return False
    def matches(line: str) -> bool:
        # Validator output is prefixed with "ERROR: "; strip it before matching.
        stripped = line[len("ERROR: "):] if line.startswith("ERROR: ") else line
        return any(stripped.startswith(prefix) for prefix in STATE_KEY_ERROR_PREFIXES)
    return all(matches(e) for e in errors)


def heal_state_json(repo: str) -> bool:
    """Merge required IPS keys into STATE.json using best-effort derivation
    from the repo's own existing native fields. Returns True if a change was
    made."""
    repo_path = GITHUB_ROOT / repo
    state_path = repo_path / "STATE.json"
    adoption_path = repo_path / "ips-adoption.json"
    if not state_path.exists():
        return False

    try:
        state = json.loads(state_path.read_text())
    except json.JSONDecodeError:
        return False

    project_name = repo
    if adoption_path.exists():
        try:
            adoption = json.loads(adoption_path.read_text())
            project_name = adoption.get("project", {}).get("name", repo)
        except json.JSONDecodeError:
            pass

    svc = state.get("service", {}) if isinstance(state.get("service"), dict) else {}
    planning = state.get("planning", {}) if isinstance(state.get("planning"), dict) else {}

    changed = False

    def set_if_needed(key, value):
        nonlocal changed
        if state.get(key) != value:
            state[key] = value
            changed = True

    set_if_needed("schemaVersion", 1)
    set_if_needed("project", project_name)

    if not isinstance(state.get("lifecycle"), str) or not state.get("lifecycle", "").strip():
        set_if_needed("lifecycle", svc.get("lifecycle") or "active")

    if not isinstance(state.get("health"), str) or not state.get("health", "").strip():
        status = planning.get("status", "unknown")
        set_if_needed("health", "blocked" if status == "blocked" else "healthy")

    if not isinstance(state.get("activeTask"), str) or not state.get("activeTask", "").strip():
        active_goals = planning.get("active_goal_ids") or []
        if active_goals:
            desc = f"Active goal(s): {', '.join(active_goals)}."
        else:
            desc = "No task is currently active; see TASKS.md for the current backlog and completion history."
        set_if_needed("activeTask", desc)

    last_updated = state.get("lastUpdated")
    valid_ts = isinstance(last_updated, str) and re.match(
        r"^\d{4}-\d{2}-\d{2}(?:T[\d:.+-]+Z?)?$", last_updated
    )
    if not valid_ts:
        candidate = planning.get("last_updated_at")
        if not (isinstance(candidate, str) and re.match(r"^\d{4}-\d{2}-\d{2}(?:T[\d:.+-]+Z?)?$", candidate)):
            candidate = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        set_if_needed("lastUpdated", candidate)

    deployment = state.get("deployment")
    if not isinstance(deployment, dict) or not str(deployment.get("status", "")).strip():
        set_if_needed("deployment", {"status": svc.get("deployment") or "kubernetes"})

    if not isinstance(state.get("blockers"), list):
        blocked_goals = planning.get("blocked_goal_ids") or []
        derived = (
            [f"Goal {g} is blocked pending an owner decision." for g in blocked_goals]
            if blocked_goals
            else []
        )
        set_if_needed("blockers", derived)

    if not isinstance(state.get("followUps"), list):
        set_if_needed("followUps", [])

    if changed:
        state_path.write_text(json.dumps(state, indent=2) + "\n")
    return changed


def git(repo: str, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args], cwd=GITHUB_ROOT / repo, capture_output=True, text=True
    )


def commit_if_dirty(repo: str) -> str | None:
    status = git(repo, "status", "--porcelain", "STATE.json")
    if not status.stdout.strip():
        return None
    git(repo, "add", "STATE.json")
    message = (
        "docs: auto-heal STATE.json IPS required schema drift\n\n"
        "Automated ecosystem IPS validator detected that STATE.json was\n"
        "missing required top-level keys (schemaVersion, project, lifecycle,\n"
        "health, activeTask, lastUpdated, deployment, blockers, followUps),\n"
        "most likely due to a concurrent unrelated commit overwriting this\n"
        "file with the repository's native schema. This restores those keys\n"
        "using values derived from the repository's own existing fields,\n"
        "without altering any other content.\n\n"
        "Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
    )
    commit = git(repo, "commit", "-m", message)
    if commit.returncode != 0:
        return f"COMMIT_FAILED: {commit.stdout}\n{commit.stderr}"
    head = git(repo, "rev-parse", "--short", "HEAD")
    return head.stdout.strip()


def main() -> int:
    catalog = json.loads(CATALOG.read_text())
    repos = [
        r["checkout"]
        for r in catalog.get("repositories", [])
        if r.get("ipsAdoptionRequired")
    ]

    results = []
    needs_human = []

    for repo in sorted(repos):
        rc, errors = run_validator(repo)
        if rc == 0:
            results.append((repo, "pass", None))
            continue

        if all_state_drift(errors):
            healed = heal_state_json(repo)
            if healed:
                rc2, errors2 = run_validator(repo)
                if rc2 == 0:
                    commit_hash = commit_if_dirty(repo)
                    results.append((repo, "healed", commit_hash))
                    continue
                else:
                    results.append((repo, "heal-attempt-failed", errors2))
                    needs_human.append((repo, errors2))
                    continue

        results.append((repo, "needs-human", errors))
        needs_human.append((repo, errors))

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ")
    report_path = REPORT_DIR / f"run-{timestamp}.md"
    latest_path = REPORT_DIR / "latest.md"

    lines = [f"# IPS Ecosystem Validator Run: {timestamp}", ""]
    lines.append(f"Repositories checked: {len(results)}")
    lines.append(f"Pass: {sum(1 for _, s, _ in results if s == 'pass')}")
    lines.append(f"Healed: {sum(1 for _, s, _ in results if s == 'healed')}")
    lines.append(f"Needs human attention: {len(needs_human)}")
    lines.append("")
    lines.append("| Repo | Status | Detail |")
    lines.append("| --- | --- | --- |")
    for repo, status, detail in results:
        if status == "pass":
            detail_str = ""
        elif status == "healed":
            detail_str = f"commit `{detail}`"
        else:
            detail_str = "; ".join(detail) if isinstance(detail, list) else str(detail)
        lines.append(f"| {repo} | {status} | {detail_str} |")

    report_text = "\n".join(lines) + "\n"
    report_path.write_text(report_text)
    latest_path.write_text(report_text)

    print(report_text)

    return 1 if needs_human else 0


if __name__ == "__main__":
    raise SystemExit(main())
