#[cxx::bridge(namespace = "finance_enums")]
pub mod ffi {
    extern "Rust" {}

    #[repr(i32)]
    #[derive(Debug)]
    enum CountryCode {}

    unsafe extern "C++" {
        include!("finance-enums/finance-enums-rust.hpp");

        type CountryCode;

        fn CountryCodeFromString_rust(st: String) -> CountryCode;

        fn CountryCodeToString_rust(cc: CountryCode) -> String;

        fn CountryCodeToName_rust(cc: CountryCode) -> String;
    }
}

/*********************************/
#[cfg(test)]
mod float_tests {
    use super::*;

    #[test]
    fn test_round_trips() {
        let us = "US".to_owned();
        let cc = ffi::CountryCodeFromString_rust(us);
        println!("{}", ffi::CountryCodeToString_rust(cc));
        println!("{}", ffi::CountryCodeToName_rust(cc));
        assert_eq!("US", ffi::CountryCodeToString_rust(cc));
        assert_eq!("United States of America", ffi::CountryCodeToName_rust(cc));
    }
}
