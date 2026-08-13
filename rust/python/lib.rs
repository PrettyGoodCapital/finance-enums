use pyo3::prelude::*;
use pyo3::types::PyCapsule;
use std::ffi::c_void;
use std::ptr::NonNull;

use ::finance_enums::data::*;

mod enums;

#[pyclass(frozen, name = "_ExchangeRecordRaw", skip_from_py_object)]
#[derive(Clone)]
struct PyExchangeRecord {
    #[pyo3(get)]
    mic: String,
    #[pyo3(get)]
    market_name: String,
    #[pyo3(get)]
    legal_entity_name: String,
    #[pyo3(get)]
    operating_mic: String,
    #[pyo3(get)]
    parent_mic: String,
    #[pyo3(get)]
    market_category_code: String,
    #[pyo3(get)]
    acronym: String,
    #[pyo3(get)]
    iso_country_code: String,
    #[pyo3(get)]
    city: String,
    #[pyo3(get)]
    website: String,
    #[pyo3(get)]
    status: String,
    #[pyo3(get)]
    region: String,
    #[pyo3(get)]
    subregion: String,
    #[pyo3(get)]
    is_segment: bool,
    #[pyo3(get)]
    is_official: bool,
}

impl From<&ExchangeRecord> for PyExchangeRecord {
    fn from(record: &ExchangeRecord) -> Self {
        Self {
            mic: record.mic.to_string(),
            market_name: record.market_name.to_string(),
            legal_entity_name: record.legal_entity_name.to_string(),
            operating_mic: record.operating_mic.to_string(),
            parent_mic: record.parent_mic.to_string(),
            market_category_code: record.market_category_code.to_string(),
            acronym: record.acronym.to_string(),
            iso_country_code: record.iso_country_code.to_string(),
            city: record.city.to_string(),
            website: record.website.to_string(),
            status: record.status.to_string(),
            region: record.region.to_string(),
            subregion: record.subregion.to_string(),
            is_segment: record.is_segment,
            is_official: record.is_official,
        }
    }
}

macro_rules! variant_fn {
    ($name:ident, $arr:ident) => {
        #[pyfunction]
        fn $name() -> Vec<&'static str> {
            $arr.to_vec()
        }
    };
}

variant_fn!(country_names, CountryNames_ARRAY);

#[pyfunction]
fn currency_aliases() -> Vec<(&'static str, &'static str)> {
    Currency_ALIASES.to_vec()
}

#[pyfunction]
fn currency_records() -> Vec<(&'static str, &'static str, bool)> {
    CURRENCY_RECORDS
        .iter()
        .map(|record| (record.code, record.display_name, record.is_iso4217))
        .collect()
}

#[pyfunction]
fn currency_alias_records() -> Vec<(&'static str, &'static str)> {
    CURRENCY_ALIAS_RECORDS
        .iter()
        .map(|record| (record.alias, record.canonical_code))
        .collect()
}

#[pyfunction]
fn exchange_records_raw() -> Vec<Vec<&'static str>> {
    exchange_records()
        .iter()
        .map(|record| {
            vec![
                record.mic,
                record.market_name,
                record.legal_entity_name,
                record.operating_mic,
                record.parent_mic,
                record.market_category_code,
                record.acronym,
                record.iso_country_code,
                record.city,
                record.website,
                record.status,
                record.region,
                record.subregion,
                if record.is_segment { "1" } else { "0" },
                if record.is_official { "1" } else { "0" },
            ]
        })
        .collect()
}

#[pyfunction]
fn exchange_records_typed() -> Vec<PyExchangeRecord> {
    exchange_records().iter().map(PyExchangeRecord::from).collect()
}

#[pyfunction]
fn exchange_record_typed(mic: &str) -> Option<PyExchangeRecord> {
    exchange_record(mic).map(PyExchangeRecord::from)
}

#[pyfunction]
fn enum_records_raw() -> Vec<(&'static str, &'static str, usize)> {
    ::finance_enums::enum_data::enum_variant_records()
}

#[pyfunction]
fn currency_export_capsule(py: Python<'_>) -> PyResult<Bound<'_, PyCapsule>> {
    let pointer = NonNull::from(&::finance_enums::currency_data::CURRENCY_EXPORT_V1).cast::<c_void>();

    unsafe { PyCapsule::new_with_pointer(py, pointer, c"finance_enums.currency_export_v1") }
}

#[pyfunction]
fn exchange_export_capsule(py: Python<'_>) -> PyResult<Bound<'_, PyCapsule>> {
    let pointer = NonNull::from(::finance_enums::exchange_data::exchange_export_v1()).cast::<c_void>();

    unsafe { PyCapsule::new_with_pointer(py, pointer, c"finance_enums.exchange_export_v1") }
}

#[pyfunction]
fn enum_export_capsule(py: Python<'_>) -> PyResult<Bound<'_, PyCapsule>> {
    let pointer = NonNull::from(::finance_enums::enum_data::enum_export_v1()).cast::<c_void>();

    unsafe { PyCapsule::new_with_pointer(py, pointer, c"finance_enums.enum_export_v1") }
}

/// Returns the library's semantic enum-data ABI version as `(major, minor, patch)`.
#[pyfunction]
fn abi_version() -> (u32, u32, u32) {
    (
        ::finance_enums::ENUM_ABI_VERSION_MAJOR,
        ::finance_enums::ENUM_ABI_VERSION_MINOR,
        ::finance_enums::ENUM_ABI_VERSION_PATCH,
    )
}

/// Returns `True` if a consumer built against `(consumer_major, consumer_minor)`
/// is compatible with this library.
#[pyfunction]
fn abi_compatible(consumer_major: u32, consumer_minor: u32) -> bool {
    ::finance_enums::abi_compatible(consumer_major, consumer_minor)
}

/// Raises `RuntimeError` if the consumer ABI version is incompatible.
#[pyfunction]
fn assert_abi_compatible(consumer_major: u32, consumer_minor: u32) -> PyResult<()> {
    if ::finance_enums::abi_compatible(consumer_major, consumer_minor) {
        Ok(())
    } else {
        let (lib_major, lib_minor, lib_patch) = abi_version();
        Err(pyo3::exceptions::PyRuntimeError::new_err(format!(
            "finance_enums ABI incompatible: consumer built against {consumer_major}.{consumer_minor}, \
             library exports {lib_major}.{lib_minor}.{lib_patch}"
        )))
    }
}

/// Returns the number of variants in `family`, or `None` if the family is unknown.
#[pyfunction]
fn family_variant_count(family: &str) -> Option<usize> {
    ::finance_enums::enum_data::enum_variants(family).map(<[&str]>::len)
}

/// Returns `True` if `ordinal` is a valid variant of `family`, `False` if it is
/// out of range, or `None` if the family is unknown.
#[pyfunction]
fn validate_ordinal(family: &str, ordinal: usize) -> Option<bool> {
    ::finance_enums::enum_data::enum_variants(family).map(|variants| ordinal < variants.len())
}

/// Returns the ordinal of `variant` within `family`, or `None` if unknown.
#[pyfunction]
fn ordinal_of(family: &str, variant: &str) -> Option<usize> {
    ::finance_enums::enum_data::enum_variant_ordinal(family, variant)
}

/// Returns the variant name for `(family, ordinal)`, or `None` if invalid.
#[pyfunction]
fn variant_name(family: &str, ordinal: usize) -> Option<String> {
    let variants = ::finance_enums::enum_data::enum_variants(family)?;
    variants.get(ordinal).map(|s| (*s).to_string())
}

#[pymodule]
fn _finance_enums(py: Python, m: &Bound<PyModule>) -> PyResult<()> {
    macro_rules! reg {
        ($f:ident) => {
            m.add_function(wrap_pyfunction!($f, m)?)?;
        };
    }
    reg!(abi_version);
    reg!(abi_compatible);
    reg!(assert_abi_compatible);
    reg!(family_variant_count);
    reg!(validate_ordinal);
    reg!(ordinal_of);
    reg!(variant_name);
    reg!(country_names);
    reg!(currency_aliases);
    reg!(currency_records);
    reg!(currency_alias_records);
    reg!(currency_export_capsule);
    reg!(exchange_export_capsule);
    reg!(enum_records_raw);
    reg!(enum_export_capsule);
    reg!(exchange_records_raw);
    reg!(exchange_records_typed);
    reg!(exchange_record_typed);
    m.add_class::<PyExchangeRecord>()?;
    // Register enums + int_enums submodules
    enums::register_enum_module(py, m)?;
    Ok(())
}
