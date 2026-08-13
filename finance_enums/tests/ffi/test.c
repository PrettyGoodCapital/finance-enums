/*
 * C integration test for the finance_enums native ABI helpers.
 *
 * Exercises:
 *   - the compile-time FINANCE_ENUMS_ABI_VERSION_* macros + header compat helper
 *   - the runtime C ABI functions exported by the shared library
 *
 * Build: cc -std=c11 -I<include-dir> -o ffi_c test.c -ldl
 * Run:   ./ffi_c <path-to-libfinance_enums.so|.dylib>
 */

#include <assert.h>
#include <stddef.h>
#include <stdint.h>
#include <string.h>

#include <finance_enums.h>

#ifdef _WIN32
#include <windows.h>
#else
#include <dlfcn.h>
#endif

typedef void (*abi_version_fn)(uint32_t *, uint32_t *, uint32_t *);
typedef int32_t (*abi_compatible_fn)(uint32_t, uint32_t);
typedef int32_t (*validate_fn)(const char *, size_t);
typedef const char *(*variant_name_fn)(const char *, size_t);
typedef intptr_t (*ordinal_of_fn)(const char *, const char *);
typedef intptr_t (*count_fn)(const char *);

int main(int argc, char *argv[]) {
    if (argc < 2) {
        return 0; /* nothing to link against */
    }

#ifdef _WIN32
    HMODULE h = LoadLibraryA(argv[1]);
    assert(h);
#define SYM(name) GetProcAddress(h, name)
#else
    void *h = dlopen(argv[1], RTLD_NOW);
    assert(h);
#define SYM(name) dlsym(h, name)
#endif

    abi_version_fn abi_version = (abi_version_fn)SYM("finance_enums_abi_version");
    abi_compatible_fn abi_compatible = (abi_compatible_fn)SYM("finance_enums_abi_compatible");
    validate_fn validate = (validate_fn)SYM("finance_enums_validate_ordinal");
    variant_name_fn variant_name = (variant_name_fn)SYM("finance_enums_variant_name");
    ordinal_of_fn ordinal_of = (ordinal_of_fn)SYM("finance_enums_ordinal_of");
    count_fn family_count = (count_fn)SYM("finance_enums_family_variant_count");
    assert(abi_version && abi_compatible && validate && variant_name && ordinal_of && family_count);

    /* ABI version + compatibility. */
    uint32_t major = 0, minor = 0, patch = 0;
    abi_version(&major, &minor, &patch);
    assert(major == FINANCE_ENUMS_ABI_VERSION_MAJOR);
    assert(minor == FINANCE_ENUMS_ABI_VERSION_MINOR);
    assert(patch == FINANCE_ENUMS_ABI_VERSION_PATCH);

    /* Null out-pointers must be skipped. */
    abi_version(NULL, NULL, NULL);

    assert(abi_compatible(major, minor) == 1);
    assert(abi_compatible(major, minor + 1) == 0);
    assert(abi_compatible(0, 6) == 0);
    assert(abi_compatible(major + 1, minor) == 0);

    /* Runtime helpers for a dynamically chosen family. */
    assert(validate("Side", 0) == 1);
    assert(validate("Side", 99999) == 0);
    assert(validate("Bogus", 0) == -1);

    assert(strcmp(variant_name("Side", 2), "Buy") == 0);
    assert(variant_name("Side", 99999) == NULL);

    assert(ordinal_of("Side", "Buy") == 2);
    assert(ordinal_of("Side", "NOPE") == -1);

    assert(family_count("Side") == 4);
    assert(family_count("Bogus") == -1);

    return 0;
}
