#!/usr/bin/env python3
"""Generate finance_enums_generated.h with compile-time enum constants.

Produces C enums of the form:
    typedef enum { FE_Currency_USD = 151, ... } FE_Currency;

And for C++:
    namespace fe { enum class Currency : size_t { USD = 151, ... }; }

These compile-time constants complement the runtime C ABI in
``finance_enums.h``: consumers that know a family at compile time pay zero
overhead and need not load the shared library.

The family/variant/ordinal data is read from the **runtime ABI** itself
(``finance_enums.enum_variant_records()``), so the generated header is always a
1:1 mirror of the compiled enum families exported over the C ABI — including the
``Currency`` and ``ExchangeCode`` families, whose variants live outside
``data.rs``.
"""

import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
include_dir = root / "finance_enums" / "include"


def parse_families():
    """Return ``[(family_name, [variant, ...]), ...]`` from the runtime ABI.

    Families and variants preserve the ordinal order of the C ABI export, so the
    generated ordinals match the runtime/ABI exactly.
    """
    sys.path.insert(0, str(root))
    import finance_enums

    families: dict[str, list[tuple[int, str]]] = {}
    for record in finance_enums.enum_variant_records():
        families.setdefault(record.enum_name, []).append((record.ordinal, record.variant))

    result = []
    for name, items in families.items():
        items.sort(key=lambda pair: pair[0])
        variants = [variant for _, variant in items]
        if [ordinal for ordinal, _ in items] != list(range(len(items))):
            raise ValueError(f"family {name!r} has non-contiguous ordinals: {items}")
        result.append((name, variants))
    return result


def _cpp_enumerator(variant):
    """Sanitize a variant into a valid C++ enum-class enumerator.

    A handful of ISO 10383 MICs (e.g. ``21XX``, ``360D``) start with a digit and
    cannot name a C++ enumerator, so they are prefixed with an underscore. The C
    macro form (``FE_<Family>_<Variant>``) is already a valid identifier thanks to
    its prefix and needs no sanitization.
    """
    return variant if variant[:1].isalpha() or variant[:1] == "_" else f"_{variant}"


def generate_header(families):
    lines = [
        "/* AUTO-GENERATED — do not edit. Run: python finance_enums/gen_enums_header.py */",
        "#ifndef FINANCE_ENUMS_GENERATED_H",
        "#define FINANCE_ENUMS_GENERATED_H",
        "",
        "#include <stddef.h>",
        "",
    ]

    # C enum definitions
    lines.append("#ifdef __cplusplus")
    lines.append('extern "C" {')
    lines.append("#endif")
    lines.append("")

    for family, variants in families:
        # typedef enum { FE_<Family>_<Variant> = 0, ... } FE_<Family>;
        lines.append("typedef enum {")
        for i, v in enumerate(variants):
            comma = "," if i < len(variants) - 1 else ""
            lines.append(f"    FE_{family}_{v} = {i}{comma}")
        lines.append(f"}} FE_{family};")
        lines.append("")

    # Helper: count of variants per family
    for family, variants in families:
        lines.append(f"#define FE_{family}_COUNT {len(variants)}u")
    lines.append("")

    # Compile-time ordinal validation for a family known at the call site.
    lines.append("/*")
    lines.append(" * Compile-time ordinal validation for a family known at the call site.")
    lines.append(" * Evaluates to nonzero when `ordinal` is a valid variant of `family`:")
    lines.append(" *")
    lines.append(" *     FE_ENUMS_ORDINAL_VALID(Currency, ord)  // ord < FE_Currency_COUNT")
    lines.append(" */")
    lines.append("#define FE_ENUMS_ORDINAL_VALID(family, ordinal) \\")
    lines.append("    ((size_t)(ordinal) < (size_t)(FE_##family##_COUNT))")
    lines.append("")

    lines.append("#ifdef __cplusplus")
    lines.append('} /* extern "C" */')
    lines.append("")

    # C++ enum class definitions in namespace fe
    lines.append("namespace fe {")
    lines.append("")
    for family, variants in families:
        lines.append(f"enum class {family} : size_t {{")
        for i, v in enumerate(variants):
            comma = "," if i < len(variants) - 1 else ""
            lines.append(f"    {_cpp_enumerator(v)} = {i}{comma}")
        lines.append("};")
        lines.append("")
    lines.append("} // namespace fe")
    lines.append("")
    lines.append("#endif /* __cplusplus */")
    lines.append("")
    lines.append("#endif /* FINANCE_ENUMS_GENERATED_H */")
    lines.append("")
    return "\n".join(lines)


def main():
    families = parse_families()
    header = generate_header(families)
    out = include_dir / "finance_enums_generated.h"
    out.write_text(header)
    total = sum(len(v) for _, v in families)
    print(f"Generated {out.name}: {len(families)} families, {total} variants")


if __name__ == "__main__":
    main()
