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

const CurrencyDataExportV1 *finance_enums_currency_export_v1(void);
const ExchangeDataExportV1 *finance_enums_exchange_export_v1(void);

#ifdef __cplusplus
}
#endif

#endif
