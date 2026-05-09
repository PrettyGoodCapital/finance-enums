#![allow(non_upper_case_globals)]

use std::ffi::c_char;

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub struct CurrencyRecord {
    pub code: &'static str,
    pub display_name: &'static str,
    pub is_iso4217: bool,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub struct CurrencyAliasRecord {
    pub alias: &'static str,
    pub canonical_code: &'static str,
}

#[repr(C)]
#[derive(Clone, Copy, Debug)]
pub struct CurrencyRecordRaw {
    pub code: *const c_char,
    pub display_name: *const c_char,
    pub is_iso4217: bool,
}

unsafe impl Sync for CurrencyRecordRaw {}

#[repr(C)]
#[derive(Clone, Copy, Debug)]
pub struct CurrencyAliasRecordRaw {
    pub alias: *const c_char,
    pub canonical_code: *const c_char,
}

unsafe impl Sync for CurrencyAliasRecordRaw {}

#[repr(C)]
#[derive(Clone, Copy, Debug)]
pub struct CurrencyDataExportV1 {
    pub abi_version: u32,
    pub export_struct_size: usize,
    pub currency_record_size: usize,
    pub currency_alias_record_size: usize,
    pub records: *const CurrencyRecordRaw,
    pub records_len: usize,
    pub aliases: *const CurrencyAliasRecordRaw,
    pub aliases_len: usize,
}

unsafe impl Sync for CurrencyDataExportV1 {}

pub const CURRENCY_EXPORT_ABI_VERSION: u32 = 1;

pub fn currency_record(code: &str) -> Option<&'static CurrencyRecord> {
    CURRENCY_RECORDS.iter().find(|record| record.code == code)
}

macro_rules! currency_table {
    ($({ code: $code:literal, display_name: $display_name:literal, is_iso4217: $is_iso4217:expr, aliases: [$($alias:literal),* $(,)?] }),* $(,)?) => {
        pub static CURRENCY_RECORDS: &[CurrencyRecord] = &[
            $(CurrencyRecord {
                code: $code,
                display_name: $display_name,
                is_iso4217: $is_iso4217,
            }),*
        ];

        pub static Currency_CODES_ARRAY: &[&str] = &[$($code),*];
        pub static Currency_VARIANTS: &[&str] = &[$($code),*];
        pub static CurrencyName_ARRAY: &[&str] = &[$($display_name),*];
        pub static Currency_names_ARRAY: &[&str] = &[$($code),*];

        pub static CURRENCY_RECORDS_RAW: &[CurrencyRecordRaw] = &[
            $(CurrencyRecordRaw {
                code: concat!($code, "\0").as_ptr() as *const c_char,
                display_name: concat!($display_name, "\0").as_ptr() as *const c_char,
                is_iso4217: $is_iso4217,
            }),*
        ];

        pub static CURRENCY_ALIAS_RECORDS: &[CurrencyAliasRecord] = &[
            $($(CurrencyAliasRecord {
                alias: $alias,
                canonical_code: $code,
            },)*)*
        ];

        pub static Currency_ALIASES: &[(&str, &str)] = &[
            $($(($alias, $code),)*)*
        ];

        pub static CURRENCY_ALIAS_RECORDS_RAW: &[CurrencyAliasRecordRaw] = &[
            $($(CurrencyAliasRecordRaw {
                alias: concat!($alias, "\0").as_ptr() as *const c_char,
                canonical_code: concat!($code, "\0").as_ptr() as *const c_char,
            },)*)*
        ];
    };
}

currency_table!(
    { code: "AED", display_name: "United Arab Emirates dirham", is_iso4217: true, aliases: [] },
    { code: "AFN", display_name: "Afghan afghani", is_iso4217: true, aliases: [] },
    { code: "ALL", display_name: "Albanian lek", is_iso4217: true, aliases: [] },
    { code: "AMD", display_name: "Armenian dram", is_iso4217: true, aliases: [] },
    { code: "ANG", display_name: "Netherlands Antillean guilder", is_iso4217: true, aliases: [] },
    { code: "AOA", display_name: "Angolan kwanza", is_iso4217: true, aliases: [] },
    { code: "ARS", display_name: "Argentine peso", is_iso4217: true, aliases: [] },
    { code: "AUD", display_name: "Australian dollar", is_iso4217: true, aliases: [] },
    { code: "AWG", display_name: "Aruban florin", is_iso4217: true, aliases: [] },
    { code: "AZN", display_name: "Azerbaijani manat", is_iso4217: true, aliases: [] },
    { code: "BAM", display_name: "Bosnia and Herzegovina convertible mark", is_iso4217: true, aliases: [] },
    { code: "BBD", display_name: "Barbados dollar", is_iso4217: true, aliases: [] },
    { code: "BDT", display_name: "Bangladeshi taka", is_iso4217: true, aliases: [] },
    { code: "BGN", display_name: "Bulgarian lev", is_iso4217: true, aliases: [] },
    { code: "BHD", display_name: "Bahraini dinar", is_iso4217: true, aliases: [] },
    { code: "BIF", display_name: "Burundian franc", is_iso4217: true, aliases: [] },
    { code: "BMD", display_name: "Bermudian dollar", is_iso4217: true, aliases: [] },
    { code: "BND", display_name: "Brunei dollar", is_iso4217: true, aliases: [] },
    { code: "BOB", display_name: "Boliviano", is_iso4217: true, aliases: [] },
    { code: "BOV", display_name: "Bolivian Mvdol", is_iso4217: true, aliases: [] },
    { code: "BRL", display_name: "Brazilian real", is_iso4217: true, aliases: [] },
    { code: "BSD", display_name: "Bahamian dollar", is_iso4217: true, aliases: [] },
    { code: "BTN", display_name: "Bhutanese ngultrum", is_iso4217: true, aliases: [] },
    { code: "BWP", display_name: "Botswana pula", is_iso4217: true, aliases: [] },
    { code: "BYN", display_name: "Belarusian ruble", is_iso4217: true, aliases: [] },
    { code: "BZD", display_name: "Belize dollar", is_iso4217: true, aliases: [] },
    { code: "CAD", display_name: "Canadian dollar", is_iso4217: true, aliases: [] },
    { code: "CDF", display_name: "Congolese franc", is_iso4217: true, aliases: [] },
    { code: "CHE", display_name: "WIR euro", is_iso4217: true, aliases: [] },
    { code: "CHF", display_name: "Swiss franc", is_iso4217: true, aliases: [] },
    { code: "CHW", display_name: "WIR franc", is_iso4217: true, aliases: [] },
    { code: "CLF", display_name: "Unidad de Fomento", is_iso4217: true, aliases: [] },
    { code: "CLP", display_name: "Chilean peso", is_iso4217: true, aliases: [] },
    { code: "CNY", display_name: "Renminbi", is_iso4217: true, aliases: [] },
    { code: "COP", display_name: "Colombian peso", is_iso4217: true, aliases: [] },
    { code: "COU", display_name: "Unidad de Valor Real (UVR)", is_iso4217: true, aliases: [] },
    { code: "CRC", display_name: "Costa Rican colon", is_iso4217: true, aliases: [] },
    { code: "CUC", display_name: "Cuban convertible peso", is_iso4217: true, aliases: [] },
    { code: "CUP", display_name: "Cuban peso", is_iso4217: true, aliases: [] },
    { code: "CVE", display_name: "Cape Verdean escudo", is_iso4217: true, aliases: [] },
    { code: "CZK", display_name: "Czech koruna", is_iso4217: true, aliases: [] },
    { code: "DJF", display_name: "Djiboutian franc", is_iso4217: true, aliases: [] },
    { code: "DKK", display_name: "Danish krone", is_iso4217: true, aliases: [] },
    { code: "DOP", display_name: "Dominican peso", is_iso4217: true, aliases: [] },
    { code: "DZD", display_name: "Algerian dinar", is_iso4217: true, aliases: [] },
    { code: "EGP", display_name: "Egyptian pound", is_iso4217: true, aliases: [] },
    { code: "ERN", display_name: "Eritrean nakfa", is_iso4217: true, aliases: [] },
    { code: "ETB", display_name: "Ethiopian birr", is_iso4217: true, aliases: [] },
    { code: "EUR", display_name: "Euro", is_iso4217: true, aliases: [] },
    { code: "EUX", display_name: "Euro (cents)", is_iso4217: false, aliases: ["EUr"] },
    { code: "FJD", display_name: "Fiji dollar", is_iso4217: true, aliases: [] },
    { code: "FKP", display_name: "Falkland Islands pound", is_iso4217: true, aliases: [] },
    { code: "GBP", display_name: "Pound sterling", is_iso4217: true, aliases: [] },
    { code: "GBX", display_name: "Penny sterling", is_iso4217: false, aliases: ["GBp"] },
    { code: "GEL", display_name: "Georgian lari", is_iso4217: true, aliases: [] },
    { code: "GHS", display_name: "Ghanaian cedi", is_iso4217: true, aliases: [] },
    { code: "GIP", display_name: "Gibraltar pound", is_iso4217: true, aliases: [] },
    { code: "GMD", display_name: "Gambian dalasi", is_iso4217: true, aliases: [] },
    { code: "GNF", display_name: "Guinean franc", is_iso4217: true, aliases: [] },
    { code: "GTQ", display_name: "Guatemalan quetzal", is_iso4217: true, aliases: [] },
    { code: "GYD", display_name: "Guyanese dollar", is_iso4217: true, aliases: [] },
    { code: "HKD", display_name: "Hong Kong dollar", is_iso4217: true, aliases: [] },
    { code: "HNL", display_name: "Honduran lempira", is_iso4217: true, aliases: [] },
    { code: "HTG", display_name: "Haitian gourde", is_iso4217: true, aliases: [] },
    { code: "HUF", display_name: "Hungarian forint", is_iso4217: true, aliases: [] },
    { code: "IDR", display_name: "Indonesian rupiah", is_iso4217: true, aliases: [] },
    { code: "ILS", display_name: "Israeli new shekel", is_iso4217: true, aliases: [] },
    { code: "INR", display_name: "Indian rupee", is_iso4217: true, aliases: [] },
    { code: "IQD", display_name: "Iraqi dinar", is_iso4217: true, aliases: [] },
    { code: "IRR", display_name: "Iranian rial", is_iso4217: true, aliases: [] },
    { code: "ISK", display_name: "Icelandic króna", is_iso4217: true, aliases: [] },
    { code: "JMD", display_name: "Jamaican dollar", is_iso4217: true, aliases: [] },
    { code: "JOD", display_name: "Jordanian dinar", is_iso4217: true, aliases: [] },
    { code: "JPY", display_name: "Japanese yen", is_iso4217: true, aliases: [] },
    { code: "KES", display_name: "Kenyan shilling", is_iso4217: true, aliases: [] },
    { code: "KGS", display_name: "Kyrgyzstani som", is_iso4217: true, aliases: [] },
    { code: "KHR", display_name: "Cambodian riel", is_iso4217: true, aliases: [] },
    { code: "KMF", display_name: "Comoro franc", is_iso4217: true, aliases: [] },
    { code: "KPW", display_name: "North Korean won", is_iso4217: true, aliases: [] },
    { code: "KRW", display_name: "South Korean won", is_iso4217: true, aliases: [] },
    { code: "KWD", display_name: "Kuwaiti dinar", is_iso4217: true, aliases: [] },
    { code: "KYD", display_name: "Cayman Islands dollar", is_iso4217: true, aliases: [] },
    { code: "KZT", display_name: "Kazakhstani tenge", is_iso4217: true, aliases: [] },
    { code: "LAK", display_name: "Lao kip", is_iso4217: true, aliases: [] },
    { code: "LBP", display_name: "Lebanese pound", is_iso4217: true, aliases: [] },
    { code: "LKR", display_name: "Sri Lankan rupee", is_iso4217: true, aliases: [] },
    { code: "LRD", display_name: "Liberian dollar", is_iso4217: true, aliases: [] },
    { code: "LSL", display_name: "Lesotho loti", is_iso4217: true, aliases: [] },
    { code: "LYD", display_name: "Libyan dinar", is_iso4217: true, aliases: [] },
    { code: "MAD", display_name: "Moroccan dirham", is_iso4217: true, aliases: [] },
    { code: "MDL", display_name: "Moldovan leu", is_iso4217: true, aliases: [] },
    { code: "MGA", display_name: "Malagasy ariary", is_iso4217: true, aliases: [] },
    { code: "MKD", display_name: "Macedonian denar", is_iso4217: true, aliases: [] },
    { code: "MMK", display_name: "Myanmar kyat", is_iso4217: true, aliases: [] },
    { code: "MNT", display_name: "Mongolian tögrög", is_iso4217: true, aliases: [] },
    { code: "MOP", display_name: "Macanese pataca", is_iso4217: true, aliases: [] },
    { code: "MRU", display_name: "Mauritanian ouguiya", is_iso4217: true, aliases: [] },
    { code: "MUR", display_name: "Mauritian rupee", is_iso4217: true, aliases: [] },
    { code: "MVR", display_name: "Maldivian rufiyaa", is_iso4217: true, aliases: [] },
    { code: "MWK", display_name: "Malawian kwacha", is_iso4217: true, aliases: [] },
    { code: "MXN", display_name: "Mexican peso", is_iso4217: true, aliases: [] },
    { code: "MXV", display_name: "Mexican Unidad de Inversion", is_iso4217: true, aliases: [] },
    { code: "MYR", display_name: "Malaysian ringgit", is_iso4217: true, aliases: [] },
    { code: "MZN", display_name: "Mozambican metical", is_iso4217: true, aliases: [] },
    { code: "NAD", display_name: "Namibian dollar", is_iso4217: true, aliases: [] },
    { code: "NGN", display_name: "Nigerian naira", is_iso4217: true, aliases: [] },
    { code: "NIO", display_name: "Nicaraguan córdoba", is_iso4217: true, aliases: [] },
    { code: "NOK", display_name: "Norwegian krone", is_iso4217: true, aliases: [] },
    { code: "NPR", display_name: "Nepalese rupee", is_iso4217: true, aliases: [] },
    { code: "NZD", display_name: "New Zealand dollar", is_iso4217: true, aliases: [] },
    { code: "OMR", display_name: "Omani rial", is_iso4217: true, aliases: [] },
    { code: "PAB", display_name: "Panamanian balboa", is_iso4217: true, aliases: [] },
    { code: "PEN", display_name: "Peruvian sol", is_iso4217: true, aliases: [] },
    { code: "PGK", display_name: "Papua New Guinean kina", is_iso4217: true, aliases: [] },
    { code: "PHP", display_name: "Philippine peso", is_iso4217: true, aliases: [] },
    { code: "PKR", display_name: "Pakistani rupee", is_iso4217: true, aliases: [] },
    { code: "PLN", display_name: "Polish złoty", is_iso4217: true, aliases: [] },
    { code: "PYG", display_name: "Paraguayan guaraní", is_iso4217: true, aliases: [] },
    { code: "QAR", display_name: "Qatari riyal", is_iso4217: true, aliases: [] },
    { code: "RON", display_name: "Romanian leu", is_iso4217: true, aliases: [] },
    { code: "RSD", display_name: "Serbian dinar", is_iso4217: true, aliases: [] },
    { code: "RUB", display_name: "Russian ruble", is_iso4217: true, aliases: [] },
    { code: "RWF", display_name: "Rwandan franc", is_iso4217: true, aliases: [] },
    { code: "SAR", display_name: "Saudi riyal", is_iso4217: true, aliases: [] },
    { code: "SBD", display_name: "Solomon Islands dollar", is_iso4217: true, aliases: [] },
    { code: "SCR", display_name: "Seychelles rupee", is_iso4217: true, aliases: [] },
    { code: "SDG", display_name: "Sudanese pound", is_iso4217: true, aliases: [] },
    { code: "SEK", display_name: "Swedish krona", is_iso4217: true, aliases: [] },
    { code: "SGD", display_name: "Singapore dollar", is_iso4217: true, aliases: [] },
    { code: "SHP", display_name: "Saint Helena pound", is_iso4217: true, aliases: [] },
    { code: "SLE", display_name: "Sierra Leonean leone", is_iso4217: true, aliases: [] },
    { code: "SLL", display_name: "Sierra Leonean leone (legacy)", is_iso4217: true, aliases: [] },
    { code: "SOS", display_name: "Somali shilling", is_iso4217: true, aliases: [] },
    { code: "SRD", display_name: "Surinamese dollar", is_iso4217: true, aliases: [] },
    { code: "SSP", display_name: "South Sudanese pound", is_iso4217: true, aliases: [] },
    { code: "STN", display_name: "São Tomé and Príncipe dobra", is_iso4217: true, aliases: [] },
    { code: "SVC", display_name: "Salvadoran colón", is_iso4217: true, aliases: [] },
    { code: "SYP", display_name: "Syrian pound", is_iso4217: true, aliases: [] },
    { code: "SZL", display_name: "Swazi lilangeni", is_iso4217: true, aliases: [] },
    { code: "THB", display_name: "Thai baht", is_iso4217: true, aliases: [] },
    { code: "TJS", display_name: "Tajikistani somoni", is_iso4217: true, aliases: [] },
    { code: "TMT", display_name: "Turkmenistan manat", is_iso4217: true, aliases: [] },
    { code: "TND", display_name: "Tunisian dinar", is_iso4217: true, aliases: [] },
    { code: "TOP", display_name: "Tongan paʻanga", is_iso4217: true, aliases: [] },
    { code: "TRY", display_name: "Turkish lira", is_iso4217: true, aliases: [] },
    { code: "TTD", display_name: "Trinidad and Tobago dollar", is_iso4217: true, aliases: [] },
    { code: "TWD", display_name: "New Taiwan dollar", is_iso4217: true, aliases: [] },
    { code: "TZS", display_name: "Tanzanian shilling", is_iso4217: true, aliases: [] },
    { code: "UAH", display_name: "Ukrainian hryvnia", is_iso4217: true, aliases: [] },
    { code: "UGX", display_name: "Ugandan shilling", is_iso4217: true, aliases: [] },
    { code: "USD", display_name: "United States dollar", is_iso4217: true, aliases: [] },
    { code: "USN", display_name: "United States dollar (next day)", is_iso4217: true, aliases: [] },
    { code: "USX", display_name: "United States penny", is_iso4217: false, aliases: ["USd"] },
    { code: "UYI", display_name: "Uruguay Peso en Unidades Indexadas", is_iso4217: true, aliases: [] },
    { code: "UYU", display_name: "Uruguayan peso", is_iso4217: true, aliases: [] },
    { code: "UYW", display_name: "Unidad previsional", is_iso4217: true, aliases: [] },
    { code: "UZS", display_name: "Uzbekistan sum", is_iso4217: true, aliases: [] },
    { code: "VED", display_name: "Venezuelan digital bolívar", is_iso4217: true, aliases: [] },
    { code: "VES", display_name: "Venezuelan sovereign bolívar", is_iso4217: true, aliases: [] },
    { code: "VND", display_name: "Vietnamese đồng", is_iso4217: true, aliases: [] },
    { code: "VUV", display_name: "Vanuatu vatu", is_iso4217: true, aliases: [] },
    { code: "WST", display_name: "Samoan tala", is_iso4217: true, aliases: [] },
    { code: "XAF", display_name: "CFA franc BEAC", is_iso4217: true, aliases: [] },
    { code: "XAG", display_name: "Silver", is_iso4217: true, aliases: [] },
    { code: "XAU", display_name: "Gold", is_iso4217: true, aliases: [] },
    { code: "XBA", display_name: "European Composite Unit", is_iso4217: true, aliases: [] },
    { code: "XBB", display_name: "European Monetary Unit", is_iso4217: true, aliases: [] },
    { code: "XBC", display_name: "European Unit of Account 9", is_iso4217: true, aliases: [] },
    { code: "XBD", display_name: "European Unit of Account 17", is_iso4217: true, aliases: [] },
    { code: "XCD", display_name: "East Caribbean dollar", is_iso4217: true, aliases: [] },
    { code: "XDR", display_name: "Special drawing rights", is_iso4217: true, aliases: [] },
    { code: "XOF", display_name: "CFA franc BCEAO", is_iso4217: true, aliases: [] },
    { code: "XPD", display_name: "Palladium", is_iso4217: true, aliases: [] },
    { code: "XPF", display_name: "CFP franc", is_iso4217: true, aliases: [] },
    { code: "XPT", display_name: "Platinum", is_iso4217: true, aliases: [] },
    { code: "XSU", display_name: "SUCRE Unified System for Regional Compensation", is_iso4217: true, aliases: [] },
    { code: "XTS", display_name: "Code reserved for testing", is_iso4217: true, aliases: [] },
    { code: "XUA", display_name: "ADB Unit of Account", is_iso4217: true, aliases: [] },
    { code: "XXX", display_name: "No currency", is_iso4217: true, aliases: [] },
    { code: "YER", display_name: "Yemeni rial", is_iso4217: true, aliases: [] },
    { code: "ZAR", display_name: "South African rand", is_iso4217: true, aliases: [] },
    { code: "ZMW", display_name: "Zambian kwacha", is_iso4217: true, aliases: [] },
    { code: "ZWL", display_name: "Zimbabwean dollar", is_iso4217: true, aliases: [] },
    { code: "CNH", display_name: "Offshore renminbi", is_iso4217: false, aliases: [] },
    { code: "ECNY", display_name: "Digital yuan (e-CNY)", is_iso4217: false, aliases: ["e-CNY"] }
);

pub static CURRENCY_EXPORT_V1: CurrencyDataExportV1 = CurrencyDataExportV1 {
    abi_version: CURRENCY_EXPORT_ABI_VERSION,
    export_struct_size: std::mem::size_of::<CurrencyDataExportV1>(),
    currency_record_size: std::mem::size_of::<CurrencyRecordRaw>(),
    currency_alias_record_size: std::mem::size_of::<CurrencyAliasRecordRaw>(),
    records: CURRENCY_RECORDS_RAW.as_ptr(),
    records_len: CURRENCY_RECORDS_RAW.len(),
    aliases: CURRENCY_ALIAS_RECORDS_RAW.as_ptr(),
    aliases_len: CURRENCY_ALIAS_RECORDS_RAW.len(),
};

#[cfg(test)]
mod tests {
    use super::*;
    use std::collections::HashSet;

    #[test]
    fn test_currency_records_align_with_legacy_exports() {
        assert_eq!(CURRENCY_RECORDS.len(), Currency_VARIANTS.len());
        assert_eq!(CURRENCY_RECORDS.len(), CurrencyName_ARRAY.len());
        assert_eq!(CURRENCY_RECORDS.len(), Currency_names_ARRAY.len());
    }

    #[test]
    fn test_currency_codes_are_unique() {
        let mut seen = HashSet::new();
        for record in CURRENCY_RECORDS {
            assert!(
                seen.insert(record.code),
                "Duplicate currency code: {}",
                record.code
            );
        }
    }

    #[test]
    fn test_currency_aliases_point_to_known_codes() {
        let known_codes: HashSet<_> = CURRENCY_RECORDS.iter().map(|record| record.code).collect();
        for alias in CURRENCY_ALIAS_RECORDS {
            assert!(known_codes.contains(alias.canonical_code));
        }
    }

    #[test]
    fn test_currency_iso_flags_cover_extensions() {
        assert!(currency_record("USD").unwrap().is_iso4217);
        assert!(!currency_record("EUX").unwrap().is_iso4217);
        assert!(!currency_record("GBX").unwrap().is_iso4217);
        assert!(!currency_record("USX").unwrap().is_iso4217);
        assert!(!currency_record("CNH").unwrap().is_iso4217);
        assert!(!currency_record("ECNY").unwrap().is_iso4217);
    }
}
