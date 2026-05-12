use std::fs;
use std::path::PathBuf;

fn main() {
    let manifest_dir =
        PathBuf::from(std::env::var("CARGO_MANIFEST_DIR").expect("missing cargo manifest dir"));
    let header_dir = manifest_dir.join("../finance_enums/include");
    let header_path = header_dir.join("finance_enums.h");

    fs::create_dir_all(&header_dir).expect("failed to create C header output directory");
    fs::write(header_path, render_header()).expect("failed to write generated C header");

    println!("cargo:rerun-if-changed=build.rs");
    println!("cargo:rerun-if-changed=src/lib.rs");
    println!("cargo:rerun-if-changed=src/currency_data.rs");
    println!("cargo:rerun-if-changed=src/exchange_data.rs");
}

fn render_header() -> String {
    String::from(concat!(
        "#ifndef FINANCE_ENUMS_H\n",
        "#define FINANCE_ENUMS_H\n\n",
        "#include <stdbool.h>\n",
        "#include <stddef.h>\n",
        "#include <stdint.h>\n\n",
        "#ifdef __cplusplus\n",
        "extern \"C\" {\n",
        "#endif\n\n",
        "#define FINANCE_ENUMS_CURRENCY_EXPORT_ABI_VERSION 1u\n",
        "#define FINANCE_ENUMS_EXCHANGE_EXPORT_ABI_VERSION 1u\n\n",
        "typedef struct CurrencyRecordRaw {\n",
        "    const char *code;\n",
        "    const char *display_name;\n",
        "    bool is_iso4217;\n",
        "} CurrencyRecordRaw;\n\n",
        "typedef struct CurrencyAliasRecordRaw {\n",
        "    const char *alias;\n",
        "    const char *canonical_code;\n",
        "} CurrencyAliasRecordRaw;\n\n",
        "typedef struct CurrencyDataExportV1 {\n",
        "    uint32_t abi_version;\n",
        "    size_t export_struct_size;\n",
        "    size_t currency_record_size;\n",
        "    size_t currency_alias_record_size;\n",
        "    const CurrencyRecordRaw *records;\n",
        "    size_t records_len;\n",
        "    const CurrencyAliasRecordRaw *aliases;\n",
        "    size_t aliases_len;\n",
        "} CurrencyDataExportV1;\n\n",
        "typedef struct ExchangeRecordRaw {\n",
        "    const char *mic;\n",
        "    const char *market_name;\n",
        "    const char *legal_entity_name;\n",
        "    const char *operating_mic;\n",
        "    const char *parent_mic;\n",
        "    const char *market_category_code;\n",
        "    const char *acronym;\n",
        "    const char *iso_country_code;\n",
        "    const char *city;\n",
        "    const char *website;\n",
        "    const char *status;\n",
        "    const char *region;\n",
        "    const char *subregion;\n",
        "    bool is_segment;\n",
        "    bool is_official;\n",
        "} ExchangeRecordRaw;\n\n",
        "typedef struct ExchangeDataExportV1 {\n",
        "    uint32_t abi_version;\n",
        "    size_t export_struct_size;\n",
        "    size_t exchange_record_size;\n",
        "    const ExchangeRecordRaw *records;\n",
        "    size_t records_len;\n",
        "} ExchangeDataExportV1;\n\n",
        "const CurrencyDataExportV1 *finance_enums_currency_export_v1(void);\n",
        "const ExchangeDataExportV1 *finance_enums_exchange_export_v1(void);\n\n",
        "#ifdef __cplusplus\n",
        "}\n",
        "#endif\n\n",
        "#endif\n",
    ))
}
