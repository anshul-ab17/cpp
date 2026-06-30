interface Solution {
  id: number;
  title: string;
  difficulty: "Easy" | "Medium" | "Hard";
  category: string;
  lang: "cpp" | "py";
  path: string;
  code: string;
  company?: string;
}

let ALL: Solution[] = [];
let filtered: Solution[] = [];
let activeCategory = "all";
let activeDiffs = new Set<string>(["Easy", "Medium", "Hard"]);
let activeLangs = new Set<string>(["cpp", "py"]);
let searchQ = "";
let activeIdx = -1;

const categoryCounts: Record<string, number> = {};

function esc(str: string): string {
  return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

function buildSidebar(): void {
  for (const s of ALL) {
    categoryCounts[s.category] = (categoryCounts[s.category] ?? 0) + 1;
  }
  const cats = Object.keys(categoryCounts).sort();

  const aside = document.getElementById("sidebar")!;
  aside.innerHTML = `
    <div class="sidebar-label">Category</div>
    <button class="filter-btn active" data-cat="all">all<span class="pill">${ALL.length}</span></button>
    ${cats.map(c => `<button class="filter-btn" data-cat="${esc(c)}">${esc(c)}<span class="pill">${categoryCounts[c]}</span></button>`).join("")}
  `;

  aside.addEventListener("click", (e) => {
    const btn = (e.target as Element).closest<HTMLButtonElement>(".filter-btn");
    if (!btn) return;
    aside.querySelectorAll(".filter-btn").forEach(b => b.classList.remove("active"));
    btn.classList.add("active");
    activeCategory = btn.dataset.cat!;
    applyFilters();
  });
}

function applyFilters(): void {
  filtered = ALL.filter(s => {
    if (activeCategory !== "all" && s.category !== activeCategory) return false;
    if (!activeDiffs.has(s.difficulty)) return false;
    if (!activeLangs.has(s.lang)) return false;
    if (searchQ) {
      const q = searchQ.toLowerCase();
      if (!String(s.id).includes(q) && !s.title.toLowerCase().includes(q)) return false;
    }
    return true;
  });

  document.getElementById("result-count")!.textContent = `${filtered.length} solutions`;
  renderList();
}

function renderList(): void {
  const pane = document.getElementById("list-pane")!;
  const codePaneEl = document.getElementById("code-pane")!;

  if (filtered.length === 0) {
    pane.innerHTML = `<div style="padding:24px;font-size:11px;color:var(--muted)">no results</div>`;
    codePaneEl.innerHTML = `<div class="empty-state">no results</div>`;
    activeIdx = -1;
    return;
  }

  pane.innerHTML = filtered.map((s, i) => `
    <div class="sol-item" data-i="${i}">
      <div class="sol-num">#${String(s.id).padStart(4, "0")}</div>
      <div class="sol-title">${esc(s.title)}</div>
      <div class="sol-meta">
        <span class="tag ${esc(s.difficulty.toLowerCase())}">${esc(s.difficulty)}</span>
        <span class="tag lang">${s.lang === "cpp" ? "C++" : "py"}</span>
        <span class="tag cat">${esc(s.category)}</span>
      </div>
    </div>
  `).join("");

  pane.addEventListener("click", (e) => {
    const item = (e.target as Element).closest<HTMLElement>(".sol-item");
    if (!item) return;
    selectSolution(Number(item.dataset.i));
  });

  if (activeIdx >= 0 && activeIdx < filtered.length) {
    selectSolution(activeIdx);
  } else {
    codePaneEl.innerHTML = `<div class="empty-state">select a solution</div>`;
    activeIdx = -1;
  }
}

function selectSolution(i: number): void {
  activeIdx = i;
  const s = filtered[i];
  document.querySelectorAll(".sol-item").forEach((el, idx) => {
    el.classList.toggle("active", idx === i);
  });

  const lang = s.lang === "cpp" ? "cpp" : "python";
  const codePaneEl = document.getElementById("code-pane")!;
  codePaneEl.innerHTML = `
    <div class="code-header">
      <button class="back-btn" id="back-btn">← back</button>
      <span class="tag ${esc(s.difficulty.toLowerCase())}">${esc(s.difficulty)}</span>
      <span class="code-title">${esc(s.title)}</span>
      <span class="code-path">${esc(s.path)}</span>
      <button class="copy-btn" id="copy-btn">copy</button>
    </div>
    <div class="code-body">
      <pre class="language-${lang}"><code class="language-${lang}">${esc(s.code)}</code></pre>
    </div>
  `;

  (window as any).Prism.highlightAllUnder(codePaneEl);

  codePaneEl.classList.add("open");
  document.getElementById("back-btn")!.addEventListener("click", () => {
    codePaneEl.classList.remove("open");
  });

  document.getElementById("copy-btn")!.addEventListener("click", () => {
    navigator.clipboard.writeText(s.code).then(() => {
      const btn = document.getElementById("copy-btn") as HTMLButtonElement;
      btn.textContent = "copied!";
      btn.classList.add("copied");
      setTimeout(() => { btn.textContent = "copy"; btn.classList.remove("copied"); }, 1500);
    });
  });

  const el = document.querySelectorAll(".sol-item")[i] as HTMLElement | undefined;
  el?.scrollIntoView({ block: "nearest" });
}

// toolbar: difficulty toggles
document.querySelectorAll<HTMLButtonElement>(".diff-btn").forEach(btn => {
  btn.addEventListener("click", () => {
    const d = btn.dataset.d!;
    if (activeDiffs.has(d)) {
      activeDiffs.delete(d);
      btn.classList.remove("active");
    } else {
      activeDiffs.add(d);
      btn.classList.add("active");
    }
    activeIdx = 0;
    applyFilters();
  });
});

// toolbar: lang toggles
document.querySelectorAll<HTMLButtonElement>(".lang-btn").forEach(btn => {
  btn.addEventListener("click", () => {
    const l = btn.dataset.l!;
    if (activeLangs.has(l) && activeLangs.size > 1) {
      activeLangs.delete(l);
      btn.classList.remove("active");
    } else {
      activeLangs.add(l);
      btn.classList.add("active");
    }
    activeIdx = 0;
    applyFilters();
  });
});

// search
document.getElementById("search")!.addEventListener("input", (e) => {
  searchQ = (e.target as HTMLInputElement).value.trim();
  activeIdx = 0;
  applyFilters();
});

// keyboard nav
document.addEventListener("keydown", (e) => {
  if (e.target === document.getElementById("search")) return;
  if (e.key === "ArrowDown") {
    e.preventDefault();
    if (activeIdx < filtered.length - 1) selectSolution(activeIdx + 1);
  } else if (e.key === "ArrowUp") {
    e.preventDefault();
    if (activeIdx > 0) selectSolution(activeIdx - 1);
  }
});

// init
fetch("solutions.json")
  .then(r => r.json())
  .then((data: Solution[]) => {
    ALL = data;
    document.getElementById("hdr-count")!.textContent = `${ALL.length} solutions`;
    buildSidebar();
    applyFilters();
    if (filtered.length > 0) selectSolution(0);
  })
  .catch(() => {
    document.getElementById("list-pane")!.innerHTML =
      `<div style="padding:24px;font-size:11px;color:#f87171">failed to load solutions.json — run: python client/build.py</div>`;
  });
