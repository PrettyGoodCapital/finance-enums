use finance_enums::*;

fn main() {
    let us = "US".to_owned();
    let cc = ffi::CountryCodeFromString_rust(us);
    println!("{}", ffi::CountryCodeToString_rust(cc));
    println!("{}", ffi::CountryCodeToName_rust(cc));
}
