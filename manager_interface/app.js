const traceItems = [
  { label: "Vision", value: "Protected", icon: "eye", note: "Original intent stays stable." },
  { label: "Goal Impact", value: "Mapped", icon: "target", note: "Each task explains why it matters." },
  { label: "System", value: "SYS-002", icon: "layers", note: "Context engine owns this slice." },
  { label: "Feature", value: "FEAT-004", icon: "grid", note: "Manager visibility interface." },
  { label: "Task", value: "TASK-016", icon: "list", note: "Static interface implementation." },
  { label: "Plan", value: "EP-TASK-016", icon: "file", note: "Approved implementation path." },
  { label: "Prompt", value: "Used", icon: "message", note: "Coding prompt preserves scope." },
  { label: "Validation", value: "Passed", icon: "shield", note: "Evidence recorded before closure." },
];

const readouts = [
  {
    title: "The original intent is protected.",
    body: "Agents can build features, but they cannot silently rewrite the constitution or original vision.",
    icon: "shield",
  },
  {
    title: "Work is traceable before it becomes code.",
    body: "A task should connect upward to a feature, system and goal impact, then downward to a plan, prompt and validation report.",
    icon: "link",
  },
  {
    title: "Retrieval changes are compared first.",
    body: "A new context candidate is checked against the baseline so managers can see whether it improves support or introduces drift.",
    icon: "bars",
  },
  {
    title: "The current dashboard is static.",
    body: "This interface reports the current repository evidence. Live repository parsing can be added after managers accept the view.",
    icon: "warning",
    warning: true,
  },
];

const providerStatuses = [
  {
    label: "Active provider",
    value: "local-hash",
    state: "Approved",
    tone: "pass",
    manager: "Required and local retrieval checks stay inside the repository boundary.",
    technical: "config/embedding_provider_gates.json marks local-hash approved with credential_mode none and no external network.",
  },
  {
    label: "Dry-run provider gate",
    value: "external-provider-dry-run",
    state: "Passed",
    tone: "pass",
    manager: "The external-provider simulation is offline, has no credentials and cannot make network calls.",
    technical: "embedding_provider_gate validates offline dry_run, credential_mode none, no external network and human_review_required true.",
  },
  {
    label: "Promotion status",
    value: "approved_candidate",
    state: "Promotable",
    tone: "pass",
    manager: "The dry-run candidate can advance only as an approved candidate, not as a real external provider.",
    technical: "provider_promotion_gate requires pass_rate 1.0, zero failed cases, zero unexpected paths, dry_run true and network_calls 0.",
  },
  {
    label: "External network",
    value: "0 calls",
    state: "Blocked",
    tone: "caution",
    manager: "No provider output shown here depends on live external calls.",
    technical: "retrieval_candidate_dry_run.json reports network_calls 0 and dry_run true.",
  },
];

const comparisonRows = [
  {
    check: "Required trace context",
    baseline: "Graph-linked documents",
    candidate: "Same required set",
    result: "Pass",
    manager: "The candidate cannot replace mandatory intent documents.",
    technical: "Required graph context remains authoritative.",
  },
  {
    check: "Optional supporting context",
    baseline: "Manual fixture",
    candidate: "Local semantic adapter",
    result: "Pass",
    manager: "Extra suggestions are measured before they are trusted.",
    technical: "Candidate output is compatible with TASK-014 comparison.",
  },
  {
    check: "Unexpected drift",
    baseline: "Known expected paths",
    candidate: "Deterministic token overlap",
    result: "Pass",
    manager: "The system checks for unrelated material before adoption.",
    technical: "Unexpected paths are reported by the comparison harness.",
  },
  {
    check: "Operational readiness",
    baseline: "Governance gates",
    candidate: "TASK-016 validation",
    result: "Pass",
    manager: "The visible dashboard is backed by repository checks.",
    technical: "Audit, pre-coding and deployment-readiness gates pass.",
  },
];

const managerFlow = [
  {
    label: "Baseline",
    value: "Expected context",
    icon: "file",
    note: "Required trace stays fixed.",
  },
  {
    label: "Candidate",
    value: "Extra support",
    icon: "bars",
    note: "Optional suggestions are measured.",
  },
  {
    label: "Gate",
    value: "No drift",
    icon: "shield",
    note: "Unrelated material is blocked.",
  },
  {
    label: "Decision",
    value: "Pass",
    icon: "check",
    note: "Safe to keep as candidate evidence.",
  },
];

const managerScorecards = [
  { label: "Trace protected", value: "100%", detail: "Required documents unchanged." },
  { label: "Cases passed", value: "4 / 4", detail: "Every comparison check passed." },
  { label: "Unexpected drift", value: "0", detail: "No unrelated paths accepted." },
];

const gates = [
  { title: "Unit tests", body: "Repository test suite passes through Python unittest discovery." },
  { title: "Strict audit", body: "Markdown and graph governance checks pass through npm validation." },
  { title: "Pre-coding gate", body: "Traceability and required planning material are present." },
  { title: "Readiness gate", body: "TASK-022 has validation evidence and operational gates named." },
  { title: "Provider safety gate", body: "Embedding providers are checked for credentials, network access and data boundary rules." },
  { title: "Promotion gate", body: "Dry-run provider candidates must pass safety, comparison and zero-network thresholds." },
];

const iconPaths = {
  eye: '<path d="M12 5c5 0 8.7 4.1 10 7-1.3 2.9-5 7-10 7S3.3 14.9 2 12c1.3-2.9 5-7 10-7Zm0 2c-3.4 0-6.2 2.5-7.7 5 1.5 2.5 4.3 5 7.7 5s6.2-2.5 7.7-5C18.2 9.5 15.4 7 12 7Zm0 2a3 3 0 1 1 0 6 3 3 0 0 1 0-6Z"/>',
  target: '<path d="M12 2h2v3.1a7 7 0 1 1-5.1 1.8L7.5 5.5A9 9 0 1 0 16 3.3V2h2v5h-5V5h1V4.1A7 7 0 1 0 12 19a7 7 0 0 0 6.7-5h-2.1a5 5 0 1 1-4.6-7v2a3 3 0 1 0 2.8 4h-3.6V2Z"/>',
  layers: '<path d="m12 2 9 5-9 5-9-5 9-5Zm0 2.3L7.1 7 12 9.7 16.9 7 12 4.3ZM4 10l8 4.4 8-4.4 1 1.8-9 5-9-5L4 10Zm0 4.3 8 4.4 8-4.4 1 1.8-9 5-9-5 1-1.8Z"/>',
  grid: '<path d="M4 4h7v7H4V4Zm2 2v3h3V6H6Zm7-2h7v7h-7V4Zm2 2v3h3V6h-3ZM4 13h7v7H4v-7Zm2 2v3h3v-3H6Zm7-2h7v7h-7v-7Zm2 2v3h3v-3h-3Z"/>',
  list: '<path d="M5 6h2v2H5V6Zm4 0h10v2H9V6Zm-4 5h2v2H5v-2Zm4 0h10v2H9v-2Zm-4 5h2v2H5v-2Zm4 0h10v2H9v-2Z"/>',
  file: '<path d="M6 2h8l5 5v15H6V2Zm2 2v16h9V8h-4V4H8Zm7 1.4V6h.6L15 5.4ZM10 11h5v2h-5v-2Zm0 4h5v2h-5v-2Z"/>',
  message: '<path d="M4 4h16v12H8.8L4 20V4Zm2 2v9.7L8.1 14H18V6H6Z"/>',
  shield: '<path d="M12 2 4 5v6c0 5.1 3.3 9.8 8 11 4.7-1.2 8-5.9 8-11V5l-8-3Zm0 3.2 5 1.9v3.8c0 3.4-2 6.7-5 7.9-3-1.2-5-4.5-5-7.9V7.1l5-1.9Z"/>',
  link: '<path d="M7.8 13.9a4 4 0 0 1 0-5.7l2.1-2.1a4 4 0 0 1 5.7 5.7l-.8.8-1.4-1.4.8-.8A2 2 0 0 0 11.3 7L9.2 9.2a2 2 0 0 0 2.8 2.8l.7-.7 1.4 1.4-.7.7a4 4 0 0 1-5.6.5Zm8.4-3.8a4 4 0 0 1 0 5.7l-2.1 2.1a4 4 0 1 1-5.7-5.7l.8-.8 1.4 1.4-.8.8A2 2 0 0 0 12.7 17l2.1-2.2a2 2 0 0 0-2.8-2.8l-.7.7-1.4-1.4.7-.7a4 4 0 0 1 5.6-.5Z"/>',
  bars: '<path d="M4 19h16v2H2V3h2v16Zm3-2v-5h3v5H7Zm5 0V7h3v10h-3Zm5 0v-8h3v8h-3Z"/>',
  warning: '<path d="M12 3 2 21h20L12 3Zm0 4.1L18.6 19H5.4L12 7.1ZM11 10h2v5h-2v-5Zm0 6h2v2h-2v-2Z"/>',
  check: '<path d="m10.8 15.4 6-7 1.5 1.3-7.4 8.5-4.3-4.3L8 12.5l2.8 2.9Z"/>',
};

function icon(name) {
  return `<svg viewBox="0 0 24 24" aria-hidden="true">${iconPaths[name]}</svg>`;
}

function renderTrace() {
  const target = document.querySelector(".trace-chain");
  target.innerHTML = traceItems
    .map(
      (item) => `
        <article class="trace-node">
          ${icon(item.icon)}
          <strong>${item.label}</strong>
          <span>${item.value}</span>
          <span>${item.note}</span>
        </article>
      `,
    )
    .join("");
}

function renderReadouts() {
  const target = document.querySelector(".readout-list");
  target.innerHTML = readouts
    .map(
      (item) => `
        <article class="readout-item">
          <span class="readout-icon ${item.warning ? "warning" : ""}">${icon(item.icon)}</span>
          <div>
            <h3>${item.title}</h3>
            <p>${item.body}</p>
          </div>
        </article>
      `,
    )
    .join("");
}

function renderComparison(mode = "manager") {
  const summary = document.querySelector(".comparison-summary");
  const panel = document.querySelector(".comparison-panel");
  const visual = document.querySelector(".comparison-visual");
  const body = document.querySelector(".comparison-body");
  panel.dataset.mode = mode;
  summary.textContent =
    mode === "manager"
      ? "The candidate is allowed only when it adds support without changing the required intent trace."
      : "Candidate results remain optional and are checked against TASK-014-compatible baseline cases before future retrieval changes are accepted.";
  visual.innerHTML = `
    <svg class="manager-map" viewBox="0 0 760 190" role="img" aria-label="Baseline to candidate to gate to pass decision diagram">
      <defs>
        <marker id="arrowhead" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">
          <path d="M0 0 10 4 0 8Z"></path>
        </marker>
      </defs>
      <path class="map-link" d="M155 92h88"></path>
      <path class="map-link" d="M337 92h88"></path>
      <path class="map-link" d="M519 92h88"></path>
      <g class="map-node">
        <circle cx="92" cy="92" r="58"></circle>
        <text x="92" y="78">Baseline</text>
        <text x="92" y="106">Locked trace</text>
      </g>
      <g class="map-node">
        <circle cx="274" cy="92" r="58"></circle>
        <text x="274" y="78">Candidate</text>
        <text x="274" y="106">Extra support</text>
      </g>
      <g class="map-node">
        <circle cx="456" cy="92" r="58"></circle>
        <text x="456" y="78">Gate</text>
        <text x="456" y="106">No drift</text>
      </g>
      <g class="map-node decision">
        <circle cx="638" cy="92" r="58"></circle>
        <text x="638" y="78">Decision</text>
        <text x="638" y="106">Pass</text>
      </g>
    </svg>
    <div class="manager-scoreboard" aria-label="Comparison scorecards">
      ${managerScorecards
        .map(
          (item) => `
            <article class="score-card">
              <span>${item.label}</span>
              <strong>${item.value}</strong>
              <p>${item.detail}</p>
            </article>
          `,
        )
        .join("")}
    </div>
    <div class="manager-flow" aria-label="Retrieval comparison flow">
      ${managerFlow
        .map(
          (step) => `
            <article class="flow-step">
              <span class="flow-icon">${icon(step.icon)}</span>
              <div>
                <span>${step.label}</span>
                <strong>${step.value}</strong>
                <p>${step.note}</p>
              </div>
            </article>
          `,
        )
        .join("")}
    </div>
    <div class="drift-diagram" aria-label="Context drift diagram">
      <div class="drift-lane">
        <span>Required trace</span>
        <strong>Locked</strong>
        <div class="lane-bar locked"><span></span></div>
      </div>
      <div class="drift-lane">
        <span>Optional support</span>
        <strong>Added</strong>
        <div class="lane-bar support"><span></span></div>
      </div>
      <div class="drift-lane">
        <span>Drift risk</span>
        <strong>0 found</strong>
        <div class="lane-bar drift"><span></span></div>
      </div>
    </div>
  `;
  body.innerHTML = comparisonRows
    .map(
      (row) => `
        <tr>
          <td>${row.check}</td>
          <td>${row.baseline}</td>
          <td>${row.candidate}</td>
          <td class="result-pass">${row.result}</td>
          <td>${mode === "manager" ? row.manager : row.technical}</td>
        </tr>
      `,
    )
    .join("");
}

function renderProviderStatus(mode = "manager") {
  const body = document.querySelector(".provider-status-body");
  body.innerHTML = providerStatuses
    .map(
      (item) => `
        <article class="provider-status-card">
          <div class="provider-status-topline">
            <span>${item.label}</span>
            <strong class="status-pill ${item.tone}">${item.state}</strong>
          </div>
          <h3>${item.value}</h3>
          <p>${mode === "manager" ? item.manager : item.technical}</p>
        </article>
      `,
    )
    .join("");
}

function renderGates() {
  const target = document.querySelector(".gate-grid");
  target.innerHTML = gates
    .map(
      (gate) => `
        <article class="gate-card">
          <span class="gate-status">${icon("check")} Passed</span>
          <h3>${gate.title}</h3>
          <p>${gate.body}</p>
        </article>
      `,
    )
    .join("");
}

function bindControls() {
  document.querySelectorAll(".segment").forEach((button) => {
    button.addEventListener("click", () => {
      document.querySelectorAll(".segment").forEach((item) => item.classList.remove("active"));
      button.classList.add("active");
      renderComparison(button.dataset.mode);
      renderProviderStatus(button.dataset.mode);
    });
  });

  document.querySelectorAll(".nav-item").forEach((button) => {
    button.addEventListener("click", () => {
      document.querySelectorAll(".nav-item").forEach((item) => item.classList.remove("active"));
      button.classList.add("active");
      const panel = document.getElementById(button.dataset.section);
      panel?.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  });
}

renderTrace();
renderReadouts();
renderComparison();
renderProviderStatus();
renderGates();
bindControls();
