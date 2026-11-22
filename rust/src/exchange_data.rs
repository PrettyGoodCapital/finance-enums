#![allow(non_upper_case_globals)]

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

pub fn exchange_records() -> &'static [ExchangeRecord] {
    EXCHANGE_RECORDS_INNER
        .get_or_init(build_exchange_records)
        .as_ref()
}

pub fn exchange_record(mic: &str) -> Option<&'static ExchangeRecord> {
    exchange_records().iter().find(|record| record.mic == mic)
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
