use pyo3::prelude::*;
use pyo3::types::{PyList, PyTuple};

use ::finance_enums::enum_data;

/// Register enum families as both raw variant lists (enums submodule)
/// and as proper Python IntEnum classes (int_enums submodule).
pub fn register_enum_module(py: Python, parent: &Bound<PyModule>) -> PyResult<()> {
    let enums_module = PyModule::new(py, "enums")?;

    // Raw lists (backward compat)
    for family in enum_data::enum_family_specs() {
        let variants = PyList::new(py, family.variants.iter())?;
        enums_module.setattr(family.name, variants)?;
    }

    // __all_families__ on the enums submodule
    let family_names: Vec<&str> = enum_data::enum_family_specs()
        .iter()
        .map(|f| f.name)
        .collect();
    let names_list = PyList::new(py, family_names.iter())?;
    enums_module.setattr("__all_families__", names_list)?;

    parent.add_submodule(&enums_module)?;

    // Generate IntEnum classes and attach to int_enums submodule
    let int_enums_module = PyModule::new(py, "int_enums")?;
    let int_enum = py.import("enum")?.getattr("IntEnum")?;
    for family in enum_data::enum_family_specs() {
        // IntEnum functional API: IntEnum("Name", [("Variant", ordinal), ...])
        let members = PyList::new(
            py,
            family
                .variants
                .iter()
                .enumerate()
                .map(|(i, v)| {
                    PyTuple::new(py, &[v.into_pyobject(py).unwrap().into_any(), i.into_pyobject(py).unwrap().into_any()])
                        .unwrap()
                }),
        )?;
        let cls = int_enum.call1((family.name, members))?;
        int_enums_module.setattr(family.name, &cls)?;
    }

    // Also expose __all_families__ at the int_enums level
    let names_list2 = PyList::new(py, family_names.iter())?;
    int_enums_module.setattr("__all_families__", names_list2)?;

    parent.add_submodule(&int_enums_module)?;

    // Expose __all_families__ at top level too
    let names_list3 = PyList::new(py, family_names.iter())?;
    parent.setattr("__all_families__", names_list3)?;

    Ok(())
}
