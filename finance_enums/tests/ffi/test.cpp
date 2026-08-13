/*
 * C++ integration test for the finance_enums header-only wrapper.
 *
 * Exercises the fe::EnumLibrary loader and its ABI version/compat helpers, plus
 * the indexed EnumRegistry lookups.
 *
 * Build: c++ -std=c++20 -I<include-dir> -o ffi_cpp test.cpp -ldl
 * Run:   ./ffi_cpp <path-to-libfinance_enums.so|.dylib>
 */

#include <cassert>
#include <cstddef>
#include <cstdint>
#include <string_view>

#include <finance_enums.hpp>

int main(int argc, char *argv[]) {
    // Header-only compile-time compatibility helper.
    static_assert(fe::abi_compatible(FINANCE_ENUMS_ABI_VERSION_MAJOR,
                                     FINANCE_ENUMS_ABI_VERSION_MINOR,
                                     fe::kHeaderAbiVersion));
    static_assert(!fe::abi_compatible(FINANCE_ENUMS_ABI_VERSION_MAJOR + 1,
                                      FINANCE_ENUMS_ABI_VERSION_MINOR,
                                      fe::kHeaderAbiVersion));
    static_assert(!fe::abi_compatible(0, 6, fe::kHeaderAbiVersion));

    if (argc < 2) {
        return 0; // header-only checks
    }

    fe::EnumLibrary lib(argv[1]);

    // ABI version reported by the loaded library matches the header.
    fe::AbiVersion v = lib.abi_version();
    assert(v.major == FINANCE_ENUMS_ABI_VERSION_MAJOR);
    assert(v.minor == FINANCE_ENUMS_ABI_VERSION_MINOR);
    assert(v.patch == FINANCE_ENUMS_ABI_VERSION_PATCH);

    assert(lib.abi_compatible());                    // defaults to header version
    assert(lib.abi_compatible(v.major, v.minor));
    assert(!lib.abi_compatible(v.major, v.minor + 1));
    assert(!lib.abi_compatible(0, 6));
    assert(!lib.abi_compatible(v.major + 1, v.minor));
    lib.assert_abi_compatible();                     // must not throw

    bool threw = false;
    try {
        lib.assert_abi_compatible(v.major + 1, v.minor);
    } catch (const std::runtime_error &) {
        threw = true;
    }
    assert(threw);

    // Registry lookups for a dynamically chosen family.
    const auto &reg = lib.registry();
    auto side = reg.family("Side");
    assert(side != nullptr);
    assert(side->variants.size() == 4);
    assert(reg.ordinal("Side", "Buy") == 2u);
    assert(reg.variant_at("Side", 2) == std::string_view("Buy"));
    assert(!reg.ordinal("Side", "NOPE").has_value());
    assert(!reg.variant_at("Side", 99999).has_value());
    assert(reg.family("Bogus") == nullptr);

    return 0;
}
