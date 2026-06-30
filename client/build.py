#!/usr/bin/env python3
"""Build solutions.json from leetcode/ directory."""
import os, re, json

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEETCODE_DIR = os.path.join(REPO_ROOT, "leetcode")
OUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "solutions.json")

CPP_HEADER = re.compile(r"//\s*LC\s*(\d+)\.\s*(.+?)\s*\|\s*(Easy|Medium|Hard)(.*)")

def slug_to_title(slug):
    return " ".join(w.capitalize() for w in re.split(r"[-_]", slug))

def parse_filename(name):
    """Returns (number, title_slug) or None."""
    # NNNN_slug.ext (topic files)
    m = re.match(r"^(\d{4})_(.+)\.(cpp|py)$", name)
    if m:
        return int(m.group(1)), m.group(2).replace("_", "-"), m.group(3)
    # NNNN-Slug.ext (daily question)
    m = re.match(r"^(\d+)-(.+)\.(cpp|py)$", name)
    if m:
        return int(m.group(1)), m.group(2).lower(), m.group(3)
    return None

def category_from_path(rel_path):
    parts = rel_path.replace("\\", "/").split("/")
    # parts[0] is always "leetcode", parts[1] is category
    if len(parts) >= 3:
        cat = parts[1]
        if cat == "company-wise" and len(parts) >= 4:
            return f"company-wise/{parts[2]}"
        if cat == "dp" and len(parts) >= 4:
            return f"dp/{parts[2]}"
        return cat
    return "other"

solutions = []

for dirpath, _, files in os.walk(LEETCODE_DIR):
    for fname in sorted(files):
        if not (fname.endswith(".cpp") or fname.endswith(".py")):
            continue

        parsed = parse_filename(fname)
        if not parsed:
            continue

        num, slug, lang = parsed
        fpath = os.path.join(dirpath, fname)
        rel = os.path.relpath(fpath, REPO_ROOT)
        cat = category_from_path(rel)

        with open(fpath, encoding="utf-8", errors="replace") as f:
            code = f.read()

        title = slug_to_title(slug)
        difficulty = "Medium"
        company = None

        # try cpp header comment
        first = code.split("\n")[0].strip()
        m = CPP_HEADER.match(first)
        if m:
            title = m.group(2).strip()
            difficulty = m.group(3).strip()
            extra = m.group(4).strip(" |")
            if extra:
                company = extra

        solutions.append({
            "id": num,
            "title": title,
            "difficulty": difficulty,
            "category": cat,
            "lang": lang,
            "path": rel.replace("\\", "/"),
            "code": code,
            **({"company": company} if company else {}),
        })

solutions.sort(key=lambda x: (x["id"], x["lang"]))

with open(OUT_FILE, "w", encoding="utf-8") as f:
    json.dump(solutions, f, ensure_ascii=False, separators=(",", ":"))

print(f"wrote {len(solutions)} solutions -> {OUT_FILE}")
