use std::ffi::CString;

pub static VERSION: &'static str = "0.3.0";

pub fn get_version() -> CString {
    CString::new(VERSION).unwrap()
}
