# GitLab Protection Setup for Immutable Files

This document defines the GitLab-level configuration required to protect immutable project documents and require human review before any change can be merged.

## Protected documents

- `00_constitution/CONSTITUTION.md`
- `01_vision/VISION.md`

## Goal

- Prevent direct commits to protected documents on the default branch.
- Require a GitLab merge request for every protected-document change.
- Require human Code Owner approval before merge.
- Keep CI visible when an immutable document is touched.

GitLab calls pull requests **merge requests**. In this repository, protected-document changes must be made only through merge requests approved by a human maintainer or another explicitly assigned Code Owner.

---

## Repository files

The repository contains these GitLab-facing files:

- `.gitlab/CODEOWNERS`: assigns required Code Owners for immutable documents and governance controls.
- `.gitlab-ci.yml`: runs documentation validation and immutable-document guard jobs.
- `scripts/check_immutable_gitlab_changes.sh`: detects protected-document edits in merge requests and blocks non-MR/default-branch protected edits.

The current `.gitlab/CODEOWNERS` uses `@@maintainer`, which makes direct project members with the Maintainer role Code Owners. If your GitLab version is older than 17.9, replace `@@maintainer` with explicit owners such as `@username`, `@group/subgroup`, or a verified GitLab email address.

---

## GitLab setup task list

### 1. Commit GitLab configuration files

- [ ] Commit `.gitlab/CODEOWNERS`.
- [ ] Commit `.gitlab-ci.yml`.
- [ ] Commit `scripts/check_immutable_gitlab_changes.sh`.
- [ ] Confirm `.gitlab/CODEOWNERS` is the only Code Owners file in the repository. GitLab uses the first file found in this order: root `CODEOWNERS`, `docs/CODEOWNERS`, then `.gitlab/CODEOWNERS`.
- [ ] In GitLab, open `.gitlab/CODEOWNERS` and confirm GitLab reports no syntax or eligibility errors.

### 2. Protect the default branch

Location: **Settings -> Repository -> Branch rules** or **Settings -> Repository -> Protected branches**.

- [ ] Protect branch `main`, or the actual default branch if different.
- [ ] Set **Allowed to push and merge** to a human maintainer-only policy.
- [ ] Disable force pushes.
- [ ] Enable **Require approval from Code Owners** for the protected branch rule.
- [ ] Do not allow AI/bot users to push directly to the protected branch.

Recommended policy:

```text
Branch: main
Allowed to push: No one, or Maintainers only if operationally required
Allowed to merge: Maintainers
Force push: Disabled
Code Owner approval: Required
```

### 3. Configure merge request approvals

Location: **Settings -> Merge requests -> Merge request approvals**.

- [ ] Require at least `1` approval for merge requests targeting `main`.
- [ ] Disable author self-approval.
- [ ] Disable approval by users who added commits to the merge request.
- [ ] Require re-approval when new commits are pushed.
- [ ] Require all discussions to be resolved before merge.
- [ ] Require successful pipeline before merge if CI is enabled.

For stricter governance, require `2` approvals for changes to `01_vision/VISION.md`.

### 4. Verify immutable-file enforcement

- [ ] Create a test branch.
- [ ] Edit `01_vision/VISION.md`.
- [ ] Open a merge request targeting `main`.
- [ ] Confirm GitLab requests Code Owner approval from maintainers or the configured owner.
- [ ] Confirm the `immutable_document_guard` CI job reports the protected file change.
- [ ] Confirm the merge button is blocked until a human Code Owner approves.
- [ ] Confirm the merge button remains blocked if the author tries to approve their own merge request.

### 5. Optional hardening

- [ ] Add a project approval rule named `Protect Immutable Documents` for merge requests targeting `main`.
- [ ] Add a push rule or server-side hook if your GitLab tier supports the exact policy you need.
- [ ] Protect `.gitlab/CODEOWNERS`, `.gitlab-ci.yml`, `17_governance/CHANGE_CONTROL.md`, and this setup document through Code Owners as governance controls.
- [ ] Audit project members so AI/bot accounts have no Maintainer or Owner role.

---

## Verification

**To verify the protection is working:**

1. Create a feature branch
2. Modify `01_vision/VISION.md`
3. Push and create a merge request
4. Observe:
   - Merge request shows Code Owner approval is required
   - Merge is blocked without human approval
   - `immutable_document_guard` reports the protected file change
   - `.gitlab/CODEOWNERS` owners are requested as reviewers or approvers

If these checks do not appear, the most likely missing GitLab setting is **Require approval from Code Owners** on the protected branch rule.

---

## Related Documentation

- [ADR-003: Protect Vision and Constitution](../07_decisions/ADR-003-protect-vision-and-constitution.md)
- [Change Control Policy](./CHANGE_CONTROL.md)
- [Local Workflow](./LOCAL_WORKFLOW.md)

---

## References

- [GitLab protected branches](https://docs.gitlab.com/user/project/repository/branches/protected/)
- [GitLab branch rules](https://docs.gitlab.com/user/project/repository/branches/branch_rules/)
- [GitLab Code Owners](https://docs.gitlab.com/ee/user/project/codeowners/)
- [GitLab CODEOWNERS syntax](https://docs.gitlab.com/user/project/codeowners/reference/)
