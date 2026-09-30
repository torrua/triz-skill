#!/usr/bin/env python3
"""Apply evals/reference_fixes.json to evals/cases.json (keeps a .bak copy)."""
import json, shutil, sys
from pathlib import Path

root = Path(__file__).resolve().parent
cases_path = Path(sys.argv[1]) if len(sys.argv) > 1 else root / "cases.json"
fixes = json.loads((root / "reference_fixes.json").read_text(encoding="utf-8"))
cases = json.loads(cases_path.read_text(encoding="utf-8"))
by_id = {c["id"]: c for c in cases}
missing = [i for i in fixes if i not in by_id]
if missing:
    sys.exit(f"ERROR: unknown case ids in fixes: {missing}")
shutil.copyfile(cases_path, str(cases_path) + ".bak")
for cid, patch in fixes.items():
    for field, value in patch.items():
        if by_id[cid].get(field) != value:
            print(f"{cid}: updated '{field}'")
            by_id[cid][field] = value
cases_path.write_text(json.dumps(cases, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("Done. Re-run: python evals/run_evals.py")
