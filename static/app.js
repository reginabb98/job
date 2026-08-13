const STATUSES = ["Applied", "Interviewing", "Offer", "Rejected", "Withdrawn"];

let applications = [];
let currentView = "table";

const tableBody = document.getElementById("tableBody");
const kanbanBoard = document.getElementById("kanbanBoard");
const statsEl = document.getElementById("stats");
const searchInput = document.getElementById("searchInput");

async function loadAll() {
  const [appsRes, statsRes] = await Promise.all([
    fetch("/api/applications"),
    fetch("/api/stats"),
  ]);
  applications = await appsRes.json();
  renderStats(await statsRes.json());
  render();
}

function renderStats(stats) {
  const cards = [
    { label: "Total Applications", value: stats.total },
    { label: "Applied", value: stats.by_status.Applied },
    { label: "Interviewing", value: stats.by_status.Interviewing },
    { label: "Offers", value: stats.by_status.Offer },
    { label: "Response Rate", value: stats.response_rate + "%" },
    { label: "Interview Rate", value: stats.interview_rate + "%" },
  ];
  statsEl.innerHTML = cards
    .map(
      (c) => `<div class="stat-card"><div class="stat-value">${c.value}</div><div class="stat-label">${c.label}</div></div>`
    )
    .join("");
}

function filteredApps() {
  const q = searchInput.value.trim().toLowerCase();
  if (!q) return applications;
  return applications.filter(
    (a) => a.company.toLowerCase().includes(q) || a.position.toLowerCase().includes(q)
  );
}

function render() {
  if (currentView === "table") renderTable();
  else renderKanban();
}

function renderTable() {
  const rows = filteredApps();
  tableBody.innerHTML = rows
    .map(
      (a) => `
    <tr data-id="${a.id}">
      <td>${escapeHtml(a.company)}</td>
      <td>${escapeHtml(a.position)}</td>
      <td><span class="badge badge-${a.status}">${a.status}</span></td>
      <td>${formatDate(a.applied_date)}</td>
      <td>${escapeHtml(a.next_step || "—")}</td>
      <td>${escapeHtml(a.source || "—")}</td>
      <td>${a.referral ? "Yes" : "No"}</td>
      <td>${a.job_url ? `<a href="${escapeAttr(a.job_url)}" target="_blank" rel="noopener" onclick="event.stopPropagation()">↗</a>` : ""}</td>
    </tr>`
    )
    .join("");

  tableBody.querySelectorAll("tr").forEach((tr) => {
    tr.addEventListener("click", () => openEdit(Number(tr.dataset.id)));
  });
}

function renderKanban() {
  const rows = filteredApps();
  kanbanBoard.innerHTML = STATUSES.map((status) => {
    const items = rows.filter((a) => a.status === status);
    const cards = items
      .map(
        (a) => `
      <div class="kanban-card" data-id="${a.id}">
        <div class="company">${escapeHtml(a.company)}</div>
        <div class="position">${escapeHtml(a.position)}</div>
        <div class="meta">${formatDate(a.applied_date)}${a.next_step ? " · " + escapeHtml(a.next_step) : ""}</div>
      </div>`
      )
      .join("");
    return `
      <div class="kanban-col">
        <div class="kanban-col-header"><span>${status}</span><span>${items.length}</span></div>
        ${cards}
      </div>`;
  }).join("");

  kanbanBoard.querySelectorAll(".kanban-card").forEach((card) => {
    card.addEventListener("click", () => openEdit(Number(card.dataset.id)));
  });
}

function formatDate(iso) {
  if (!iso) return "—";
  const d = new Date(iso + "T00:00:00");
  if (isNaN(d)) return iso;
  return d.toLocaleDateString(undefined, { year: "numeric", month: "short", day: "numeric" });
}

function escapeHtml(str) {
  const div = document.createElement("div");
  div.textContent = str ?? "";
  return div.innerHTML;
}
function escapeAttr(str) {
  return escapeHtml(str).replace(/"/g, "&quot;");
}

document.querySelectorAll(".view-btn").forEach((btn) => {
  btn.addEventListener("click", () => {
    document.querySelectorAll(".view-btn").forEach((b) => b.classList.remove("active"));
    btn.classList.add("active");
    currentView = btn.dataset.view;
    document.getElementById("tableView").classList.toggle("hidden", currentView !== "table");
    document.getElementById("kanbanView").classList.toggle("hidden", currentView !== "kanban");
    render();
  });
});

searchInput.addEventListener("input", render);

// ---- Add / Edit modal ----
const formModalBackdrop = document.getElementById("formModalBackdrop");
const appForm = document.getElementById("appForm");
const deleteBtn = document.getElementById("deleteBtn");

document.getElementById("addBtn").addEventListener("click", () => openAdd());
document.getElementById("cancelBtn").addEventListener("click", () => closeFormModal());

function openAdd() {
  appForm.reset();
  document.getElementById("appId").value = "";
  document.getElementById("formModalTitle").textContent = "Add Application";
  document.getElementById("fAppliedDate").value = new Date().toISOString().slice(0, 10);
  deleteBtn.classList.add("hidden");
  formModalBackdrop.classList.remove("hidden");
}

function openEdit(id) {
  const a = applications.find((x) => x.id === id);
  if (!a) return;
  document.getElementById("appId").value = a.id;
  document.getElementById("formModalTitle").textContent = "Edit Application";
  document.getElementById("fCompany").value = a.company;
  document.getElementById("fPosition").value = a.position;
  document.getElementById("fStatus").value = a.status;
  document.getElementById("fAppliedDate").value = a.applied_date || "";
  document.getElementById("fNextStep").value = a.next_step || "";
  document.getElementById("fJobUrl").value = a.job_url || "";
  document.getElementById("fSource").value = a.source || "";
  document.getElementById("fReferral").checked = !!a.referral;
  document.getElementById("fNotes").value = a.notes || "";
  deleteBtn.classList.remove("hidden");
  formModalBackdrop.classList.remove("hidden");
}

function closeFormModal() {
  formModalBackdrop.classList.add("hidden");
}

appForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const id = document.getElementById("appId").value;
  const payload = {
    company: document.getElementById("fCompany").value,
    position: document.getElementById("fPosition").value,
    status: document.getElementById("fStatus").value,
    applied_date: document.getElementById("fAppliedDate").value,
    next_step: document.getElementById("fNextStep").value,
    job_url: document.getElementById("fJobUrl").value,
    source: document.getElementById("fSource").value,
    referral: document.getElementById("fReferral").checked,
    notes: document.getElementById("fNotes").value,
  };

  if (id) {
    await fetch(`/api/applications/${id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
  } else {
    await fetch("/api/applications", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
  }
  closeFormModal();
  loadAll();
});

deleteBtn.addEventListener("click", async () => {
  const id = document.getElementById("appId").value;
  if (!id) return;
  if (!confirm("Delete this application?")) return;
  await fetch(`/api/applications/${id}`, { method: "DELETE" });
  closeFormModal();
  loadAll();
});

// ---- Import modal ----
const importModalBackdrop = document.getElementById("importModalBackdrop");
document.getElementById("importBtn").addEventListener("click", () => {
  document.getElementById("importResult").textContent = "";
  document.getElementById("csvFile").value = "";
  importModalBackdrop.classList.remove("hidden");
});
document.getElementById("importCancelBtn").addEventListener("click", () => {
  importModalBackdrop.classList.add("hidden");
  loadAll();
});
document.getElementById("importSubmitBtn").addEventListener("click", async () => {
  const fileInput = document.getElementById("csvFile");
  if (!fileInput.files.length) return;
  const formData = new FormData();
  formData.append("file", fileInput.files[0]);
  const res = await fetch("/api/import", { method: "POST", body: formData });
  const data = await res.json();
  const resultEl = document.getElementById("importResult");
  if (res.ok) {
    resultEl.textContent = `Imported ${data.inserted} rows.` + (data.skipped.length ? ` Skipped ${data.skipped.length}.` : "");
  } else {
    resultEl.textContent = "Error: " + data.error;
  }
});

loadAll();
