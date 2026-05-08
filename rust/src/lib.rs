//\! finance-enums data tables.
//\!
//\! All enums are stored as parallel `&'static [&'static str]` arrays
//\! generated from the C++ headers. Python-side `Enum` classes are
//\! constructed dynamically from these tables.

pub mod data;
