use pyo3::prelude::*;
use pyo3::types::PyCapsule;
use std::ffi::c_void;
use std::ptr::NonNull;

mod enums;
mod ffi;

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

impl From<&ffi::ExchangeRecordRaw> for PyExchangeRecord {
    fn from(record: &ffi::ExchangeRecordRaw) -> Self {
        let text = |value| ffi::library_str(value).to_string();
        Self {
            mic: text(record.mic),
            market_name: text(record.market_name),
            legal_entity_name: text(record.legal_entity_name),
            operating_mic: text(record.operating_mic),
            parent_mic: text(record.parent_mic),
            market_category_code: text(record.market_category_code),
            acronym: text(record.acronym),
            iso_country_code: text(record.iso_country_code),
            city: text(record.city),
            website: text(record.website),
            status: text(record.status),
            region: text(record.region),
            subregion: text(record.subregion),
            is_segment: record.is_segment,
            is_official: record.is_official,
        }
    }
}

#[pyfunction]
fn country_names() -> Vec<&'static str> {
    ffi::country_names()
}

#[pyfunction]
fn currency_aliases() -> Vec<(&'static str, &'static str)> {
    ffi::currency_alias_records()
        .iter()
        .map(|record| {
            (
                ffi::library_str(record.alias),
                ffi::library_str(record.canonical_code),
            )
        })
        .collect()
}

#[pyfunction]
fn currency_records() -> Vec<(&'static str, &'static str, bool)> {
    ffi::currency_records()
        .iter()
        .map(|record| {
            (
                ffi::library_str(record.code),
                ffi::library_str(record.display_name),
                record.is_iso4217,
            )
        })
        .collect()
}

#[pyfunction]
fn currency_alias_records() -> Vec<(&'static str, &'static str)> {
    currency_aliases()
}

#[pyfunction]
fn exchange_records_raw() -> Vec<Vec<&'static str>> {
    ffi::exchange_records()
        .iter()
        .map(|record| {
            let mut row: Vec<&'static str> = [
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
            ]
            .into_iter()
            .map(ffi::library_str)
            .collect();
            row.push(if record.is_segment { "1" } else { "0" });
            row.push(if record.is_official { "1" } else { "0" });
            row
        })
        .collect()
}

#[pyfunction]
fn exchange_records_typed() -> Vec<PyExchangeRecord> {
    ffi::exchange_records()
        .iter()
        .map(PyExchangeRecord::from)
        .collect()
}

#[pyfunction]
fn exchange_record_typed(mic: &str) -> Option<PyExchangeRecord> {
    ffi::exchange_records()
        .iter()
        .find(|record| ffi::library_str(record.mic) == mic)
        .map(PyExchangeRecord::from)
}

#[pyfunction]
fn enum_records_raw() -> Vec<(&'static str, &'static str, usize)> {
    ffi::families()
        .iter()
        .flat_map(|family| {
            family
                .variants
                .iter()
                .map(move |(variant, ordinal)| (family.name, *variant, *ordinal))
        })
        .collect()
}

fn export_capsule<'py, T>(
    py: Python<'py>,
    export: &'static T,
    name: &'static std::ffi::CStr,
) -> PyResult<Bound<'py, PyCapsule>> {
    let pointer = NonNull::from(export).cast::<c_void>();
    unsafe { PyCapsule::new_with_pointer(py, pointer, name) }
}

#[pyfunction]
fn currency_export_capsule(py: Python<'_>) -> PyResult<Bound<'_, PyCapsule>> {
    export_capsule(
        py,
        ffi::currency_export(),
        c"finance_enums.currency_export_v1",
    )
}

#[pyfunction]
fn exchange_export_capsule(py: Python<'_>) -> PyResult<Bound<'_, PyCapsule>> {
    export_capsule(
        py,
        ffi::exchange_export(),
        c"finance_enums.exchange_export_v1",
    )
}

#[pyfunction]
fn enum_export_capsule(py: Python<'_>) -> PyResult<Bound<'_, PyCapsule>> {
    export_capsule(py, ffi::enum_export(), c"finance_enums.enum_export_v1")
}

/// Returns the library's semantic enum-data ABI version as `(major, minor, patch)`.
#[pyfunction]
fn abi_version() -> (u32, u32, u32) {
    ffi::abi_version()
}

/// Returns `True` if a consumer built against `(consumer_major, consumer_minor)`
/// is compatible with this library.
#[pyfunction]
fn abi_compatible(consumer_major: u32, consumer_minor: u32) -> bool {
    ffi::abi_compatible(consumer_major, consumer_minor)
}

/// Raises `RuntimeError` if the consumer ABI version is incompatible.
#[pyfunction]
fn assert_abi_compatible(consumer_major: u32, consumer_minor: u32) -> PyResult<()> {
    if ffi::abi_compatible(consumer_major, consumer_minor) {
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
    ffi::family_variant_count(family)
}

/// Returns the size in bytes (1, 2, or 4) of `family`'s ordinal type, or `None`
/// if the family is unknown.
#[pyfunction]
fn family_ordinal_size(family: &str) -> Option<usize> {
    ffi::family_ordinal_size(family)
}

/// Returns `True` if some variant of `family` has `ordinal`, `False` if none
/// does, or `None` if the family is unknown.
#[pyfunction]
fn validate_ordinal(family: &str, ordinal: usize) -> Option<bool> {
    ffi::validate_ordinal(family, ordinal)
}

/// Returns the ordinal of `variant` within `family`, or `None` if unknown.
#[pyfunction]
fn ordinal_of(family: &str, variant: &str) -> Option<usize> {
    ffi::ordinal_of(family, variant)
}

/// Returns the variant name for `(family, ordinal)`, or `None` if invalid.
#[pyfunction]
fn variant_name(family: &str, ordinal: usize) -> Option<&'static str> {
    ffi::variant_name(family, ordinal)
}

#[pymodule]
fn _finance_enums(py: Python, m: &Bound<PyModule>) -> PyResult<()> {
    ffi::check_layout().map_err(pyo3::exceptions::PyImportError::new_err)?;
    macro_rules! reg {
        ($f:ident) => {
            m.add_function(wrap_pyfunction!($f, m)?)?;
        };
    }
    reg!(abi_version);
    reg!(abi_compatible);
    reg!(assert_abi_compatible);
    reg!(family_variant_count);
    reg!(family_ordinal_size);
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
