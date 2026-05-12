#![allow(non_upper_case_globals)]

use std::ffi::{c_char, CString};
use std::sync::OnceLock;

const EXCHANGE_RECORD_PARTS: &[&str] = &[
    include_str!("exchange_records/exchange_records_part1.tsv"),
    include_str!("exchange_records/exchange_records_part2.tsv"),
    include_str!("exchange_records/exchange_records_part3.tsv"),
    include_str!("exchange_records/exchange_records_part4.tsv"),
    include_str!("exchange_records/exchange_records_part5.tsv"),
    include_str!("exchange_records/exchange_records_part6.tsv"),
];

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub struct ExchangeRecord {
    pub mic: &'static str,
    pub market_name: &'static str,
    pub legal_entity_name: &'static str,
    pub operating_mic: &'static str,
    pub parent_mic: &'static str,
    pub market_category_code: &'static str,
    pub acronym: &'static str,
    pub iso_country_code: &'static str,
    pub city: &'static str,
    pub website: &'static str,
    pub status: &'static str,
    pub region: &'static str,
    pub subregion: &'static str,
    pub is_segment: bool,
    pub is_official: bool,
}

#[repr(C)]
#[derive(Clone, Copy, Debug)]
pub struct ExchangeRecordRaw {
    pub mic: *const c_char,
    pub market_name: *const c_char,
    pub legal_entity_name: *const c_char,
    pub operating_mic: *const c_char,
    pub parent_mic: *const c_char,
    pub market_category_code: *const c_char,
    pub acronym: *const c_char,
    pub iso_country_code: *const c_char,
    pub city: *const c_char,
    pub website: *const c_char,
    pub status: *const c_char,
    pub region: *const c_char,
    pub subregion: *const c_char,
    pub is_segment: bool,
    pub is_official: bool,
}

unsafe impl Sync for ExchangeRecordRaw {}
unsafe impl Send for ExchangeRecordRaw {}

#[repr(C)]
#[derive(Clone, Copy, Debug)]
pub struct ExchangeDataExportV1 {
    pub abi_version: u32,
    pub export_struct_size: usize,
    pub exchange_record_size: usize,
    pub records: *const ExchangeRecordRaw,
    pub records_len: usize,
}

unsafe impl Sync for ExchangeDataExportV1 {}
unsafe impl Send for ExchangeDataExportV1 {}

pub const EXCHANGE_EXPORT_ABI_VERSION: u32 = 1;

struct ExchangeDataExportBacking {
    _records: Box<[ExchangeRecordRaw]>,
    export: ExchangeDataExportV1,
}

unsafe impl Sync for ExchangeDataExportBacking {}
unsafe impl Send for ExchangeDataExportBacking {}

fn leak_c_string(value: &'static str) -> *const c_char {
    CString::new(value)
        .expect("exchange field contained interior NUL")
        .into_raw()
        .cast_const()
}

fn build_exchange_export_v1() -> ExchangeDataExportBacking {
    let records = exchange_records()
        .iter()
        .map(|record| ExchangeRecordRaw {
            mic: leak_c_string(record.mic),
            market_name: leak_c_string(record.market_name),
            legal_entity_name: leak_c_string(record.legal_entity_name),
            operating_mic: leak_c_string(record.operating_mic),
            parent_mic: leak_c_string(record.parent_mic),
            market_category_code: leak_c_string(record.market_category_code),
            acronym: leak_c_string(record.acronym),
            iso_country_code: leak_c_string(record.iso_country_code),
            city: leak_c_string(record.city),
            website: leak_c_string(record.website),
            status: leak_c_string(record.status),
            region: leak_c_string(record.region),
            subregion: leak_c_string(record.subregion),
            is_segment: record.is_segment,
            is_official: record.is_official,
        })
        .collect::<Vec<_>>()
        .into_boxed_slice();

    let export = ExchangeDataExportV1 {
        abi_version: EXCHANGE_EXPORT_ABI_VERSION,
        export_struct_size: std::mem::size_of::<ExchangeDataExportV1>(),
        exchange_record_size: std::mem::size_of::<ExchangeRecordRaw>(),
        records: records.as_ptr(),
        records_len: records.len(),
    };

    ExchangeDataExportBacking {
        _records: records,
        export,
    }
}

fn parse_bool(value: &str, field_name: &str, mic: &str) -> bool {
    match value {
        "0" => false,
        "1" => true,
        _ => panic!("invalid {field_name} flag for exchange {mic}: {value}"),
    }
}

fn parse_exchange_record(line: &'static str) -> ExchangeRecord {
    let fields: Vec<_> = line.split('\t').collect();
    assert_eq!(
        fields.len(),
        15,
        "expected 15 tab-delimited fields for exchange record: {line}"
    );

    ExchangeRecord {
        mic: fields[0],
        market_name: fields[1],
        legal_entity_name: fields[2],
        operating_mic: fields[3],
        parent_mic: fields[4],
        market_category_code: fields[5],
        acronym: fields[6],
        iso_country_code: fields[7],
        city: fields[8],
        website: fields[9],
        status: fields[10],
        region: fields[11],
        subregion: fields[12],
        is_segment: parse_bool(fields[13], "is_segment", fields[0]),
        is_official: parse_bool(fields[14], "is_official", fields[0]),
    }
}

fn build_exchange_records() -> Box<[ExchangeRecord]> {
    let mut records = Vec::new();

    for part in EXCHANGE_RECORD_PARTS {
        for line in part.lines() {
            if line.is_empty() {
                continue;
            }
            records.push(parse_exchange_record(line));
        }
    }

    records.into_boxed_slice()
}

static EXCHANGE_RECORDS_INNER: OnceLock<Box<[ExchangeRecord]>> = OnceLock::new();
static EXCHANGE_EXPORT_V1_INNER: OnceLock<ExchangeDataExportBacking> = OnceLock::new();

pub fn exchange_records() -> &'static [ExchangeRecord] {
    EXCHANGE_RECORDS_INNER
        .get_or_init(build_exchange_records)
        .as_ref()
}

pub fn exchange_record(mic: &str) -> Option<&'static ExchangeRecord> {
    exchange_records().iter().find(|record| record.mic == mic)
}

pub fn exchange_export_v1() -> &'static ExchangeDataExportV1 {
    &EXCHANGE_EXPORT_V1_INNER
        .get_or_init(build_exchange_export_v1)
        .export
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::exchange_codes::ExchangeCode_VARIANTS;
    use std::collections::HashSet;

    #[test]
    fn test_exchange_records_cover_variant_table() {
        assert_eq!(exchange_records().len(), ExchangeCode_VARIANTS.len());

        for mic in ExchangeCode_VARIANTS {
            assert!(
                exchange_record(mic).is_some(),
                "missing exchange record for {mic}"
            );
        }
    }

    #[test]
    fn test_exchange_records_are_unique() {
        let mut seen = HashSet::new();

        for record in exchange_records() {
            assert!(
                seen.insert(record.mic),
                "duplicate exchange MIC: {}",
                record.mic
            );
        }
    }

    #[test]
    fn test_project_defined_exchange_records_are_flagged() {
        let forex = exchange_record("FOREX").unwrap();
        let crypto = exchange_record("CRYPTO").unwrap();

        assert_eq!(forex.status, "PROJECT");
        assert!(!forex.is_official);
        assert_eq!(crypto.region, "Global");
        assert!(!crypto.is_official);
    }
}
