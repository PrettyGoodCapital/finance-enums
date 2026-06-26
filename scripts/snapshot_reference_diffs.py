#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT_PATH = ROOT / "reference_snapshots" / "standards.json"


def _sha256_values(values: list[str]) -> str:
    payload = "\n".join(values).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _rust_variant_values(name: str) -> list[str]:
    text = (ROOT / "rust" / "src" / "data.rs").read_text(encoding="utf-8")
    # ``finance_enum!`` injects an ``Invalid`` sentinel at ordinal 0; mirror that
    # so snapshot ordinals match the runtime/ABI. ``finance_enum_raw!`` families
    # supply their own ordinal-0 sentinel and are read verbatim.
    match = re.search(rf"finance_enum(_raw)?!\({name}:\s*(.*?)\);", text, re.S)
    if match is not None:
        is_raw = match.group(1) is not None
        variants = [v.strip() for v in match.group(2).split(",") if v.strip()]
        if not is_raw:
            variants = ["Invalid", *variants]
        return variants
    # Fall back to old static array format
    match = re.search(rf"pub static {name}_VARIANTS: &\[&str\] = &\[(.*?)\];", text, re.S)
    if match is None:
        raise ValueError(f"missing {name}_VARIANTS in rust/src/data.rs")
    return re.findall(r'"([^"]+)"', match.group(1))


def _currency_values() -> list[str]:
    text = (ROOT / "rust" / "src" / "currency_data.rs").read_text(encoding="utf-8")
    return re.findall(r'\{ code: "([^"]+)"', text)


def _exchange_values() -> list[str]:
    values: list[str] = []
    for path in sorted((ROOT / "rust" / "src" / "exchange_records").glob("exchange_records_part*.tsv")):
        for line in path.read_text(encoding="utf-8").splitlines():
            if line:
                values.append(line.split("\t", 1)[0])
    return values


def _dataset(values: list[str]) -> dict[str, Any]:
    return {
        "count": len(values),
        "sha256": _sha256_values(values),
        "values": values,
    }


def current_snapshot() -> dict[str, Any]:
    return {
        "schema_version": 1,
        "datasets": {
            "mic": _dataset(_exchange_values()),
            "currency": _dataset(_currency_values()),
            "country_code": _dataset(_rust_variant_values("CountryCode")),
            "country_code3": _dataset(_rust_variant_values("CountryCode3")),
            "future_asset_class": _dataset(_rust_variant_values("FutureAssetClass")),
        },
    }


def _diff_lines(expected: dict[str, Any], actual: dict[str, Any]) -> list[str]:
    lines: list[str] = []
    expected_datasets = expected.get("datasets", {})
    actual_datasets = actual.get("datasets", {})
    for name in sorted(set(expected_datasets) | set(actual_datasets)):
        expected_values = expected_datasets.get(name, {}).get("values", [])
        actual_values = actual_datasets.get(name, {}).get("values", [])
        if expected_values == actual_values:
            continue
        added = sorted(set(actual_values) - set(expected_values))
        removed = sorted(set(expected_values) - set(actual_values))
        lines.append(f"{name}: expected {len(expected_values)} values, found {len(actual_values)} values")
        if added:
            lines.append(f"{name}: added {added[:20]}")
        if removed:
            lines.append(f"{name}: removed {removed[:20]}")
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(description="Compare checked-in standards snapshots with current Rust data.")
    parser.add_argument("--check", action="store_true", help="fail if snapshots are stale")
    parser.add_argument("--write", action="store_true", help="write the current snapshot")
    args = parser.parse_args()

    snapshot = current_snapshot()
    rendered = json.dumps(snapshot, indent=2, sort_keys=True) + "\n"

    if args.write:
        SNAPSHOT_PATH.parent.mkdir(parents=True, exist_ok=True)
        SNAPSHOT_PATH.write_text(rendered, encoding="utf-8")

    if args.check:
        if not SNAPSHOT_PATH.exists():
            print(f"missing snapshot: {SNAPSHOT_PATH.relative_to(ROOT)}")
            return 1
        expected = json.loads(SNAPSHOT_PATH.read_text(encoding="utf-8"))
        if expected != snapshot:
            print("standards snapshot is stale; run scripts/snapshot_reference_diffs.py --write")
            for line in _diff_lines(expected, snapshot):
                print(line)
            return 1

    print("reference snapshot diff check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
