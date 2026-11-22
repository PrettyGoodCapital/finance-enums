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


_ENUM_RE = re.compile(r"#\[abi_safe_enum(?:\([^)]*\))?\]\s*pub enum (\w+) \{(.*?)\n\}", re.S)


def _enum_variants(body):
    """Variant names of an ``#[abi_safe_enum]`` body, in declaration order."""
    names = []
    for line in body.splitlines():
        line = line.split("//")[0].strip().rstrip(",")
        if line and not line.startswith("#"):
            names.append(line.split("=")[0].strip())
    return names


def _rust_variant_values(name: str) -> list[str]:
    """Variant names of the ``#[abi_safe_enum]`` family ``name``, including its sentinel."""
    for path in sorted((ROOT / "rust" / "src" / "enums").glob("*.rs")):
        for enum_name, body in _ENUM_RE.findall(path.read_text(encoding="utf-8")):
            if enum_name == name:
                return _enum_variants(body)
    raise ValueError(f"missing #[abi_safe_enum] {name} in rust/src/enums")


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
            "country_code_alpha2": _dataset(_rust_variant_values("CountryCodeAlpha2")),
            "country_code_alpha3": _dataset(_rust_variant_values("CountryCodeAlpha3")),
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
