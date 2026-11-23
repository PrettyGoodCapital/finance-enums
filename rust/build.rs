#[cfg(feature = "capi")]
use std::env;
#[cfg(feature = "capi")]
use std::path::PathBuf;

// Only the C ABI build (the `capi` feature) generates the header.
fn main() {
    generate_header();
}

#[cfg(feature = "capi")]
fn generate_header() {
    let crate_dir = PathBuf::from(env::var("CARGO_MANIFEST_DIR").unwrap());
    let capi_dir = crate_dir.join("capi");
    let header = capi_dir.join("include").join("finance_enums.h");
    println!("cargo:rerun-if-changed=src/capi.rs");
    println!("cargo:rerun-if-changed=capi/cbindgen.toml");

    // cbindgen reads `cargo metadata`, which is unavailable inside a packaged
    // crate (`cargo publish`, `cargo install`). Those builds use the checked-in
    // header, which `make lint-rs` keeps in sync with the source.
    let generated = cbindgen::Config::from_file(capi_dir.join("cbindgen.toml"))
        .map_err(|error| error.to_string())
        .and_then(|config| {
            cbindgen::Builder::new()
                .with_crate(&crate_dir)
                .with_config(config)
                .generate()
                .map_err(|error| error.to_string())
        });
    match generated {
        Ok(bindings) => {
            bindings.write_to_file(&header);
        }
        Err(error) if header.is_file() => {
            println!("cargo:warning=using the checked-in finance_enums.h; cbindgen could not run: {error}");
        }
        Err(error) => panic!(
            "cbindgen failed to generate finance_enums.h and no checked-in copy exists: {error}"
        ),
    }
}

#[cfg(not(feature = "capi"))]
fn generate_header() {}
