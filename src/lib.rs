use pyo3::prelude::*;
mod security;
use security::SecurityType;

#[pymodule]
fn finance_enums(_py: Python, m: &PyModule) -> PyResult<()> {
    // Security
    m.add_class::<SecurityType>()?;
    Ok(())
}
