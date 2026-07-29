#!/usr/bin/env python3
"""Validate law records and regenerate all derived artifacts.

Reads:   data/json/<id>.json   (one law per file — source of truth)
Writes:  data/laws/<id>.md     (Markdown table per law)
         data/laws/INDEX.md    (human index)
         data/json/laws.json   (aggregate)
         data/csv/laws.csv     (flat index)

Dependency-free validation against tools/schema/law.schema.json
(required fields, enums, id pattern, basic types).
"""

import csv
import json
import re
import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
SCHEMA = json.loads((PROJECT / "tools" / "schema" / "law.schema.json").read_text())

FIELD_ORDER = [
    ("id", "ID"),
    ("title", "Law Name"),
    ("citation", "Citation"),
    ("book", "Book"),
    ("chapter", "Chapter"),
    ("verses", "Verses"),
    ("testament", "Testament"),
    ("categories", "Categories"),
    ("law_type", "Law Type"),
    ("kjv_text", "KJV Text"),
    ("summary", "Summary"),
    ("original_audience", "Original Audience"),
    ("immediate_context", "Immediate Context"),
    ("historical_context", "Historical Context"),
    ("penalty", "Penalty"),
    ("exceptions", "Exceptions"),
    ("cross_references", "Cross References"),
    ("nt_passages", "Related NT Passages"),
    ("internal_contradictions", "Internal Contradictions"),
    ("sab_categories", "SAB Categories"),
    ("usofc_implementation", "USofC Implementation"),
    ("agency", "Agency"),
    ("constitutional_analogue", "Constitutional Analogue"),
    ("scene_ideas", "Scene Ideas"),
    ("satirical_uses", "Satirical Uses"),
    ("bureaucratic_uses", "Bureaucratic Uses"),
    ("confidence", "Confidence"),
]


def validate(rec: dict, fname: str) -> list:
    errors = []
    props = SCHEMA["properties"]
    for req in SCHEMA["required"]:
        if req not in rec or rec[req] in (None, "", []):
            errors.append(f"{fname}: missing required field '{req}'")
    for key, val in rec.items():
        if key not in props:
            errors.append(f"{fname}: unknown field '{key}'")
            continue
        spec = props[key]
        if spec.get("type") == "string" and not isinstance(val, str):
            errors.append(f"{fname}: '{key}' must be a string")
        if spec.get("type") == "integer" and not isinstance(val, int):
            errors.append(f"{fname}: '{key}' must be an integer")
        if spec.get("type") == "array" and not isinstance(val, list):
            errors.append(f"{fname}: '{key}' must be an array")
        if "enum" in spec and val not in spec["enum"]:
            errors.append(f"{fname}: '{key}' value {val!r} not in {spec['enum']}")
        if key == "categories" and isinstance(val, list):
            allowed = props["categories"]["items"]["enum"]
            for c in val:
                if c not in allowed:
                    errors.append(f"{fname}: category {c!r} not in {allowed}")
    if "pattern" in props["id"] and isinstance(rec.get("id"), str):
        if not re.match(props["id"]["pattern"], rec["id"]):
            errors.append(f"{fname}: id {rec['id']!r} does not match pattern")
    if rec.get("id") and fname != f"{rec['id']}.json":
        errors.append(f"{fname}: filename does not match id '{rec['id']}'")
    return errors


def md_escape(s: str) -> str:
    return s.replace("|", "\\|").replace("\n", "<br>")


def fmt(val) -> str:
    if val is None:
        return "—"
    if isinstance(val, list):
        if not val:
            return "—"
        if all(isinstance(x, str) for x in val):
            return "<br>".join("• " + md_escape(x) for x in val)
        parts = []
        for x in val:  # internal_contradictions objects
            ref = f" [{', '.join(x.get('refs', []))}]" if x.get("refs") else ""
            sab = f" ({x['sab_id']})" if x.get("sab_id") else ""
            parts.append("• " + md_escape(x["issue"]) + ref + sab)
        return "<br>".join(parts)
    return md_escape(str(val))


def render_law(rec: dict) -> str:
    lines = [
        f"# {rec['title']}",
        "",
        f"> *{md_escape(rec.get('kjv_text', ''))}*  ",
        f"> — {rec['citation']} (KJV)",
        "",
        "| Field | Value |",
        "|---|---|",
    ]
    for key, label in FIELD_ORDER:
        if key in ("title", "kjv_text"):
            continue
        lines.append(f"| **{label}** | {fmt(rec.get(key))} |")
    lines += ["", "```json", json.dumps(rec, indent=2, ensure_ascii=False), "```", ""]
    return "\n".join(lines)


def main():
    json_dir = PROJECT / "data" / "json"
    laws_dir = PROJECT / "data" / "laws"
    csv_dir = PROJECT / "data" / "csv"
    laws_dir.mkdir(parents=True, exist_ok=True)
    csv_dir.mkdir(parents=True, exist_ok=True)

    records, errors = [], []
    for f in sorted(json_dir.glob("*.json")):
        if f.name == "laws.json":
            continue
        try:
            rec = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errors.append(f"{f.name}: invalid JSON ({e})")
            continue
        errors.extend(validate(rec, f.name))
        records.append(rec)

    if errors:
        print("VALIDATION ERRORS:")
        for e in errors:
            print(" -", e)
        sys.exit(1)

    records.sort(key=lambda r: r["id"])
    ids = [r["id"] for r in records]
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        sys.exit(f"Duplicate ids: {dupes}")

    # Per-law Markdown
    for old in laws_dir.glob("*.md"):
        old.unlink()
    for rec in records:
        (laws_dir / f"{rec['id']}.md").write_text(render_law(rec), encoding="utf-8")

    # Aggregate JSON
    (json_dir / "laws.json").write_text(
        json.dumps({"count": len(records), "laws": records}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    # CSV
    cols = ["id", "title", "citation", "testament", "categories", "law_type",
            "penalty", "agency", "confidence", "summary"]
    with open(csv_dir / "laws.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(cols)
        for r in records:
            w.writerow([
                "; ".join(r[c]) if isinstance(r.get(c), list) else r.get(c, "")
                for c in cols
            ])

    # Human index
    lines = [
        "# Law Index — United States of Christ",
        "",
        f"{len(records)} laws extracted. Generated by `tools/build_index.py` — do not hand-edit.",
        "",
        "| ID | Law | Citation | Categories | Penalty | Agency |",
        "|---|---|---|---|---|---|",
    ]
    for r in records:
        lines.append(
            f"| [{r['id']}]({r['id']}.md) | {md_escape(r['title'])} | {r['citation']} "
            f"| {', '.join(r['categories'])} | {md_escape(r.get('penalty') or '—')} "
            f"| {md_escape(r.get('agency') or '—')} |"
        )
    (laws_dir / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"OK: {len(records)} laws validated and rendered.")


if __name__ == "__main__":
    main()
