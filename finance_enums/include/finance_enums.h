#ifndef FINANCE_ENUMS_H
#define FINANCE_ENUMS_H

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

#define FINANCE_ENUMS_CURRENCY_EXPORT_ABI_VERSION 1u
#define FINANCE_ENUMS_EXCHANGE_EXPORT_ABI_VERSION 1u

#define FINANCE_ENUMS_ENUM_EXPORT_ABI_VERSION 1u

/*
 * Semantic version of the enum *data* ABI — the ordinal layout exposed to
 * foreign consumers. Distinct from the per-export *_EXPORT_ABI_VERSION macros
 * above, which only track the binary layout of each export struct.
 *
 * These constants mirror the package version in pyproject.toml and are kept in
 * sync by bump-my-version — do not edit them by hand. The release process picks
 * the bump using this ABI-compatibility policy:
 *   MAJOR - backwards-incompatible change: a variant or family was reordered,
 *           removed, or renamed, or an export struct layout changed. Consumers
 *           built against a different major MUST NOT use the library.
 *   MINOR - backwards-compatible append: new variants at the end of a family,
 *           or new families. Existing ordinals never move.
 *   PATCH - any other change that does not affect the ordinal layout.
 *
 * A consumer bakes these compile-time constants into its binary and calls
 * finance_enums_abi_compatible() (or finance_enums_abi_header_compatible())
 * against the loaded library to verify compatibility.
 */
#define FINANCE_ENUMS_ABI_VERSION_MAJOR 0u
#define FINANCE_ENUMS_ABI_VERSION_MINOR 6u
#define FINANCE_ENUMS_ABI_VERSION_PATCH 0u

typedef struct CurrencyRecordRaw {
    const char *code;
    const char *display_name;
    bool is_iso4217;
} CurrencyRecordRaw;

typedef struct CurrencyAliasRecordRaw {
    const char *alias;
    const char *canonical_code;
} CurrencyAliasRecordRaw;

typedef struct CurrencyDataExportV1 {
    uint32_t abi_version;
    size_t export_struct_size;
    size_t currency_record_size;
    size_t currency_alias_record_size;
    const CurrencyRecordRaw *records;
    size_t records_len;
    const CurrencyAliasRecordRaw *aliases;
    size_t aliases_len;
} CurrencyDataExportV1;

typedef struct ExchangeRecordRaw {
    const char *mic;
    const char *market_name;
    const char *legal_entity_name;
    const char *operating_mic;
    const char *parent_mic;
    const char *market_category_code;
    const char *acronym;
    const char *iso_country_code;
    const char *city;
    const char *website;
    const char *status;
    const char *region;
    const char *subregion;
    bool is_segment;
    bool is_official;
} ExchangeRecordRaw;

typedef struct ExchangeDataExportV1 {
    uint32_t abi_version;
    size_t export_struct_size;
    size_t exchange_record_size;
    const ExchangeRecordRaw *records;
    size_t records_len;
} ExchangeDataExportV1;

typedef struct EnumVariantRecordRaw {
    const char *enum_name;
    const char *variant;
    size_t ordinal;
} EnumVariantRecordRaw;

typedef struct EnumDataExportV1 {
    uint32_t abi_version;
    size_t export_struct_size;
    size_t enum_variant_record_size;
    const EnumVariantRecordRaw *records;
    size_t records_len;
    size_t family_count;
    /* Highest ordinal value across all families. Consumers compiled against an
     * older header can compare their *_COUNT constants against this to detect
     * whether the library has newer variants they don't know about. */
    size_t max_ordinal;
} EnumDataExportV1;

const CurrencyDataExportV1 *finance_enums_currency_export_v1(void);
const ExchangeDataExportV1 *finance_enums_exchange_export_v1(void);

const EnumDataExportV1 *finance_enums_enum_export_v1(void);

/* --- Semantic ABI version & compatibility helpers ----------------------- */

/* Writes the library's runtime enum-data ABI version into the out-pointers.
 * Any pointer that is NULL is skipped. */
void finance_enums_abi_version(uint32_t *major, uint32_t *minor, uint32_t *patch);

/* Returns 1 if a consumer built against (consumer_major, consumer_minor) is
 * compatible with the loaded library, 0 otherwise. Compatible iff the majors
 * match and the library's minor is >= the consumer's. */
int32_t finance_enums_abi_compatible(uint32_t consumer_major, uint32_t consumer_minor);

/* Convenience: checks the compile-time header version this translation unit was
 * built against against the loaded library. Returns 1 if compatible. */
static inline int finance_enums_abi_header_compatible(void) {
    return finance_enums_abi_compatible(FINANCE_ENUMS_ABI_VERSION_MAJOR,
                                        FINANCE_ENUMS_ABI_VERSION_MINOR);
}

/* --- Runtime enum helpers ----------------------------------------------- */

/* Number of variants in `family`, or -1 if the family is unknown. */
intptr_t finance_enums_family_variant_count(const char *family);

/* Returns 1 if `ordinal` is a valid variant of `family`, 0 if out of range,
 * or -1 if the family is unknown. */
int32_t finance_enums_validate_ordinal(const char *family, size_t ordinal);

/* Ordinal of `variant` within `family`, or -1 if either is unknown. */
intptr_t finance_enums_ordinal_of(const char *family, const char *variant);

/* NUL-terminated variant name for (family, ordinal), or NULL if invalid. The
 * pointer is valid for the lifetime of the library. */
const char *finance_enums_variant_name(const char *family, size_t ordinal);

#ifdef __cplusplus
}
#endif

#endif
