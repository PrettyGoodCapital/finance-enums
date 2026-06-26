//! Polars `DataType::Enum` integration for finance enum families.
//!
//! This module is available when the `polars` feature is enabled:
//!
//! ```toml
//! [dependencies]
//! finance-enums = { version = "0.6", features = ["polars"] }
//! ```
//!
//! # Usage
//!
//! ```rust,ignore
//! use finance_enums::polars::enum_dtype;
//!
//! let currency_dtype = enum_dtype("Currency").unwrap();
//! let side_dtype = enum_dtype("Side").unwrap();
//! ```

use polars_core::prelude::*;

use crate::enum_data;

/// Returns a Polars `DataType::Enum` for the given enum family name,
/// with categories matching the canonical variant ordering.
///
/// Returns `None` if the family name is not registered.
pub fn enum_dtype(family: &str) -> Option<DataType> {
    let spec = enum_data::enum_family_spec(family)?;
    Some(create_enum_dtype(spec.variants))
}

/// Returns a `Vec` of `(family_name, DataType::Enum)` for every registered family.
pub fn all_enum_dtypes() -> Vec<(&'static str, DataType)> {
    enum_data::enum_family_specs()
        .iter()
        .map(|spec| (spec.name, create_enum_dtype(spec.variants)))
        .collect()
}

/// Build a `DataType::Enum` from a slice of variant strings.
fn create_enum_dtype(variants: &[&str]) -> DataType {
    let categories: Vec<Option<&str>> = variants.iter().map(|v| Some(*v)).collect();
    let ca = StringChunked::from_iter_options(
        PlSmallStr::from_static("category"),
        categories.into_iter(),
    );
    // RevMapping::build_local expects the underlying Utf8ViewArray (Arrow)
    let arr = ca.downcast_iter().next().unwrap().clone();
    let rev_map = RevMapping::build_local(arr);
    DataType::Enum(Some(Arc::new(rev_map)), CategoricalOrdering::Physical)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_enum_dtype_currency() {
        let dt = enum_dtype("Currency").expect("Currency should exist");
        assert!(matches!(dt, DataType::Enum(..)));
    }

    #[test]
    fn test_enum_dtype_unknown() {
        assert!(enum_dtype("Bogus").is_none());
    }

    #[test]
    fn test_all_enum_dtypes_count() {
        let all = all_enum_dtypes();
        assert_eq!(all.len(), crate::enum_data::ENUM_FAMILY_SPECS.len());
    }
}
