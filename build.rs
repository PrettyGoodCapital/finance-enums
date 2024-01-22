use cbindgen;
use std::env;
use std::path::Path;

fn main() {
    let crate_dir = env::var("CARGO_MANIFEST_DIR").unwrap();

    let cbindings = cbindgen::Builder::new()
        .with_no_includes()
        .with_language(cbindgen::Language::C)
        .with_crate(crate_dir.clone())
        .generate()
        .unwrap();
    cbindings.write_to_file(
        Path::new("finance_enums")
            .join("finance_enums")
            .join("include")
            .join("finance-enums.h"),
    );
}
