// finance_enums general-purpose conversion + type-checking helpers (header-only).
//
// A finance-enums value is its ordinal, so passing one into C++ from any
// language is zero-cost: you carry a single integer. These helpers turn that
// ordinal into a strongly-typed `fe::<Family>` enum class (from
// <finance_enums_generated.h>), optionally checked against the family's
// ordinals through `fe::enum_traits<Family>`. Ordinals can have gaps, so the
// check is membership, not a range.
//
// Nothing here loads the shared library or depends on any framework -- it is
// pure, constexpr, compile-time conversion. For runtime-dynamic families
// (chosen by name) use the C ABI functions declared in <finance_enums.h>, or
// the fe::EnumRegistry in <finance_enums.hpp>.
//
// Example (family known at compile time):
//
//     #include <finance_enums_convert.hpp>
//
//     size_t ord = /* received from Python: int(Currency.USD) == 151 */;
//
//     // Zero-cost, unchecked (use when the producer already guarantees validity):
//     fe::Currency c = fe::convert::from_ordinal_unchecked<fe::Currency>(ord);
//
//     // Checked against the family's ordinals:
//     if (auto c = fe::convert::checked_from_ordinal<fe::Currency>(ord))
//         use(*c);
//     else
//         handle_invalid();

#ifndef FINANCE_ENUMS_CONVERT_HPP
#define FINANCE_ENUMS_CONVERT_HPP

#include <cstddef>
#include <optional>

#include "finance_enums_generated.h"

namespace fe {
namespace convert {

// The ordinal backing an enum class value (e.g. to send back to Python).
template <typename Enum>
constexpr std::size_t to_ordinal(Enum value) noexcept {
    return static_cast<std::size_t>(value);
}

// Zero-cost cast of an ordinal to the typed enum class. Unchecked: the caller is
// responsible for ensuring `ordinal` is a valid variant of `Enum`.
template <typename Enum>
constexpr Enum from_ordinal_unchecked(std::size_t ordinal) noexcept {
    return static_cast<Enum>(ordinal);
}

// Checked conversion. Returns false (leaving `out` untouched) when no variant of
// `Enum` has `ordinal`.
template <typename Enum>
constexpr bool try_from_ordinal(std::size_t ordinal, Enum &out) noexcept {
    if (!enum_traits<Enum>::is_valid(ordinal))
        return false;
    out = static_cast<Enum>(ordinal);
    return true;
}

// Checked conversion returning an optional instead of a bool + out-param.
template <typename Enum>
constexpr std::optional<Enum> checked_from_ordinal(std::size_t ordinal) noexcept {
    if (!enum_traits<Enum>::is_valid(ordinal))
        return std::nullopt;
    return static_cast<Enum>(ordinal);
}

} // namespace convert
} // namespace fe

#endif // FINANCE_ENUMS_CONVERT_HPP
