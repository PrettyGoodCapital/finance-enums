#!/usr/bin/env python3
"""Generate finance_enums_generated.h with compile-time enum constants.

Produces C enums of the form:
    typedef enum { FE_Currency_USD = 151, ... } FE_Currency;

And for C++, sized like the Rust enum, with an ``fe::enum_traits`` specialization:
    namespace fe { enum class Currency : std::uint8_t { USD = 151, ... }; }

These compile-time constants complement the runtime C ABI in
``finance_enums.h``: consumers that know a family at compile time pay zero
overhead and need not load the shared library.

The family/variant/ordinal data is read from the **runtime ABI** itself
(``finance_enums.enum_variant_records()``), so the generated header is always a
1:1 mirror of the compiled enum families exported over the C ABI — including the
``Currency`` and ``ExchangeCode`` families, which are name tables rather than
``#[abi_safe_enum]`` types.
"""

import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
include_dir = root / "rust" / "capi" / "include"


def parse_families():
    """Return ``[(family, [(ordinal, variant), ...], ordinal_size), ...]`` from the runtime ABI.

    Families keep the C ABI export order and variants their declaration order, so
    the generated values match the runtime/ABI exactly. Ordinals can have gaps.
    """
    sys.path.insert(0, str(root))
    import finance_enums

    families: dict[str, list[tuple[int, str]]] = {}
    for record in finance_enums.enum_variant_records():
        families.setdefault(record.enum_name, []).append((record.ordinal, record.variant))
    return [(name, items, finance_enums.family_ordinal_size(name)) for name, items in families.items()]


def _cpp_enumerator(variant):
    """Sanitize a variant into a valid C++ enum-class enumerator.

    A handful of ISO 10383 MICs (e.g. ``21XX``, ``360D``) start with a digit and
    cannot name a C++ enumerator, so they are prefixed with an underscore. The C
    macro form (``FE_<Family>_<Variant>``) is already a valid identifier thanks to
    its prefix and needs no sanitization.
    """
    return variant if variant[:1].isalpha() or variant[:1] == "_" else f"_{variant}"


def _valid_expression(items):
    """C constant expression that is nonzero when ``o`` is one of the family's ordinals."""
    ordinals = sorted(ordinal for ordinal, _ in items)
    if ordinals == list(range(len(ordinals))):
        return f"((size_t)(o) < {len(ordinals)}u)"
    return "(" + " || ".join(f"(size_t)(o) == {ordinal}u" for ordinal in ordinals) + ")"


_CPP_TYPES = {1: "std::uint8_t", 2: "std::uint16_t", 4: "std::uint32_t"}


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

    for family, items, _ in families:
        # typedef enum { FE_<Family>_<Variant> = <ordinal>, ... } FE_<Family>;
        lines.append("typedef enum {")
        for i, (ordinal, v) in enumerate(items):
            comma = "," if i < len(items) - 1 else ""
            lines.append(f"    FE_{family}_{v} = {ordinal}{comma}")
        lines.append(f"}} FE_{family};")
        lines.append("")

    # Per-family size, largest ordinal, and validity check. Ordinals can have
    # gaps, so FE_<Family>_COUNT is not an upper bound on valid ordinals.
    for family, items, _ in families:
        lines.append(f"#define FE_{family}_COUNT {len(items)}u")
        lines.append(f"#define FE_{family}_MAX_ORDINAL {max(ordinal for ordinal, _ in items)}u")
        lines.append(f"#define FE_{family}_ORDINAL_VALID(o) {_valid_expression(items)}")
    lines.append("")

    # Compile-time ordinal validation for a family known at the call site.
    lines.append("/*")
    lines.append(" * Compile-time ordinal validation for a family known at the call site.")
    lines.append(" * Evaluates to nonzero when `ordinal` is one of `family`'s ordinals:")
    lines.append(" *")
    lines.append(" *     FE_ENUMS_ORDINAL_VALID(Currency, ord)")
    lines.append(" *")
    lines.append(" * Families with gaps in their ordinals compare `ordinal` several times, so")
    lines.append(" * pass an expression without side effects.")
    lines.append(" */")
    lines.append("#define FE_ENUMS_ORDINAL_VALID(family, ordinal) FE_##family##_ORDINAL_VALID(ordinal)")
    lines.append("")

    lines.append("#ifdef __cplusplus")
    lines.append('} /* extern "C" */')
    lines.append("")
    lines.append("#include <cstddef>")
    lines.append("#include <cstdint>")
    lines.append("")

    # C++ enum class definitions in namespace fe, sized like the Rust enums.
    lines.append("namespace fe {")
    lines.append("")
    lines.append("// Size and ordinal facts for each fe::<Family>; see <finance_enums_convert.hpp>.")
    lines.append("template <typename Enum>")
    lines.append("struct enum_traits;")
    lines.append("")
    for family, items, ordinal_size in families:
        lines.append(f"enum class {family} : {_CPP_TYPES[ordinal_size]} {{")
        for i, (ordinal, v) in enumerate(items):
            comma = "," if i < len(items) - 1 else ""
            lines.append(f"    {_cpp_enumerator(v)} = {ordinal}{comma}")
        lines.append("};")
        lines.append("")
        lines.append("template <>")
        lines.append(f"struct enum_traits<{family}> {{")
        lines.append(f"    static constexpr std::size_t count = FE_{family}_COUNT;")
        lines.append(f"    static constexpr std::size_t max_ordinal = FE_{family}_MAX_ORDINAL;")
        lines.append(f"    static constexpr bool is_valid(std::size_t o) noexcept {{ return FE_{family}_ORDINAL_VALID(o); }}")
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
    out.write_text(header, encoding="utf-8")
    total = sum(len(items) for _, items, _ in families)
    print(f"Generated {out.name}: {len(families)} families, {total} variants")


if __name__ == "__main__":
    main()
