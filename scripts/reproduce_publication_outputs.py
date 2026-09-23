#!/usr/bin/env python3
import csv, hashlib, json
from pathlib import Path
root = Path(__file__).resolve().parents[1]
out = root / "reproduced"; out.mkdir(exist_ok=True)
report = {"tables": {}, "figure_sources": {}}
for n in range(1, 4):
    table = root / "data" / f"table_{n}.csv"
    rows = list(csv.DictReader(table.open(encoding="utf-8-sig")))
    target = out / f"table_{n}.csv"
    target.write_bytes(table.read_bytes())
    report["tables"][str(n)] = {"rows": len(rows), "sha256": hashlib.sha256(table.read_bytes()).hexdigest()}
    fig = root / "data" / f"figure_{n}_source.csv"
    frows = list(csv.DictReader(fig.open(encoding="utf-8-sig")))
    report["figure_sources"][str(n)] = {"rows": len(frows), "sha256": hashlib.sha256(fig.read_bytes()).hexdigest()}
(out / "validation_report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, indent=2))
