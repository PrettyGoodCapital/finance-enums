#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCHANGE_CODES_PATH = ROOT / "rust" / "src" / "exchange_codes.rs"
EXCHANGE_RECORDS_DIR = ROOT / "rust" / "src" / "exchange_records"


def _exchange_record_paths() -> list[Path]:
    return sorted(EXCHANGE_RECORDS_DIR.glob("exchange_records_part*.tsv"))


def load_exchange_record_codes() -> list[str]:
    codes: list[str] = []
    for path in _exchange_record_paths():
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line:
                continue
            fields = line.split("\t")
            if len(fields) != 15:
                raise ValueError(f"{path} contains a non-canonical exchange record with {len(fields)} fields")
            codes.append(fields[0])
    return codes


def load_exchange_code_variants() -> list[str]:
    return re.findall(r'"([^"]+)"', EXCHANGE_CODES_PATH.read_text(encoding="utf-8"))


def render_exchange_codes(codes: list[str]) -> str:
    lines = ["#![allow(non_upper_case_globals)]", "", "pub static ExchangeCode_VARIANTS: &[&str] = &["]
    for offset in range(0, len(codes), 10):
        chunk = codes[offset : offset + 10]
        lines.append("    " + ", ".join(f'"{code}"' for code in chunk) + ",")
    lines.append("];")
    return "\n".join(lines) + "\n"


def validate_exchange_records() -> list[str]:
    errors: list[str] = []
    record_codes = load_exchange_record_codes()
    code_variants = load_exchange_code_variants()

    if len(record_codes) != len(set(record_codes)):
        errors.append("exchange records contain duplicate MIC values")
    if record_codes != code_variants:
        missing_from_variants = sorted(set(record_codes) - set(code_variants))
        missing_from_records = sorted(set(code_variants) - set(record_codes))
        errors.append(
            "ExchangeCode_VARIANTS is not aligned with exchange_records/*.tsv "
            f"(missing_from_variants={missing_from_variants[:20]}, missing_from_records={missing_from_records[:20]})"
        )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Regenerate deterministic reference-data derivatives.")
    parser.add_argument("--check", action="store_true", help="validate that generated outputs are up to date")
    parser.add_argument("--write", action="store_true", help="write generated outputs")
    parser.add_argument("--strict-text", action="store_true", help="also require generated text to match exactly")
    args = parser.parse_args()

    errors = validate_exchange_records()
    rendered = render_exchange_codes(load_exchange_record_codes())

    if args.write:
        EXCHANGE_CODES_PATH.write_text(rendered, encoding="utf-8")

    if args.check and args.strict_text and EXCHANGE_CODES_PATH.read_text(encoding="utf-8") != rendered:
        errors.append("rust/src/exchange_codes.rs is stale; run scripts/generate_reference_data.py --write")

    if errors:
        for error in errors:
            print(error)
        return 1

    print("reference data generator check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
