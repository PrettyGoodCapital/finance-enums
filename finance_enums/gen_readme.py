#!/usr/bin/env python3
"""Generate the README.md enum reference table.

Unlike a full README owner, this script only manages a single
marker-delimited block so the hand-curated finance-enums README sections
(Currency Metadata, Exchange Metadata, CFI Helpers, ...) are preserved.

The block is delimited by::

    <!-- BEGIN ENUM REFERENCE -->
    ...generated content...
    <!-- END ENUM REFERENCE -->

If the markers are absent, the block is appended to the end of README.md.

Scope note: this table intentionally covers only the human-facing *taxonomy*
families declared with ``#[abi_safe_enum]`` in ``rust/src/enums/``. It deliberately
omits the large reference families (``Currency``, ``ExchangeCode``,
``CountryCodeAlpha2``/``CountryCodeAlpha3``), which would add thousands of rows and are
documented elsewhere. For the complete, ABI-exact family list (every family and
ordinal exported over the C ABI) see ``finance_enums_generated.h``, which is
generated from the runtime ABI by ``gen_enums_header.py``.
"""

import re
from pathlib import Path

root = Path(__file__).resolve().parent.parent

BEGIN_MARKER = "<!-- BEGIN ENUM REFERENCE -->"
END_MARKER = "<!-- END ENUM REFERENCE -->"


_ENUM_RE = re.compile(r"#\[abi_safe_enum(?:\([^)]*\))?\]\s*pub enum (\w+) \{(.*?)\n\}", re.DOTALL)


def _enum_variants(body):
    """Variant names of an ``#[abi_safe_enum]`` body, in declaration order."""
    names = []
    for line in body.splitlines():
        line = line.split("//")[0].strip().rstrip(",")
        if line and not line.startswith("#"):
            names.append(line.split("=")[0].strip())
    return names


def parse_families():
    """``[(family, variants), ...]`` for the taxonomy families, without the ``Invalid`` sentinel."""
    enums_dir = root / "rust/src/enums"
    modules = re.findall(r"^mod (\w+);", (enums_dir / "mod.rs").read_text(), re.MULTILINE)

    families = []
    for module in modules:
        if module == "country":
            continue
        for name, body in _ENUM_RE.findall((enums_dir / f"{module}.rs").read_text()):
            families.append((name, [variant for variant in _enum_variants(body) if variant != "Invalid"]))
    return families


def build_block(families):
    total_variants = sum(len(v) for _, v in families)
    lines = [
        BEGIN_MARKER,
        "",
        "## Enum Reference",
        "",
        f"**{len(families)} families, {total_variants} variants**",
        "",
        "<details>",
        f"<summary>Show all {len(families)} enum families</summary>",
        "",
        "| Family | Count | Variants |",
        "|--------|------:|----------|",
    ]
    for name, variants in families:
        v_str = ", ".join(f"`{v}`" for v in variants)
        lines.append(f"| `{name}` | {len(variants)} | {v_str} |")
    lines += ["", "</details>", "", END_MARKER]
    return "\n".join(lines)


def main():
    families = parse_families()
    block = build_block(families)

    readme_path = root / "README.md"
    readme = readme_path.read_text()

    if BEGIN_MARKER in readme and END_MARKER in readme:
        pattern = re.compile(
            re.escape(BEGIN_MARKER) + r".*?" + re.escape(END_MARKER),
            re.DOTALL,
        )
        readme = pattern.sub(block, readme)
    else:
        readme = readme.rstrip() + "\n\n" + block + "\n"

    readme_path.write_text(readme)
    total_variants = sum(len(v) for _, v in families)
    print(f"README.md: {len(families)} families, {total_variants} variants")


if __name__ == "__main__":
    main()
