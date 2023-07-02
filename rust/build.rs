fn main() {
    cxx_build::bridge("src/lib.rs")
        .file("finance-enums/finance-enums-rust.cpp")
        .flag_if_supported("-std=c++14")
        .flag("-I.")
        .flag("-DLIB_EXPORTS")
        .compile("finance-enums-rust");
    println!("cargo:rustc-link-lib=finance-enums-rust");
    println!("cargo:rustc-link-lib=finance-enums");
    println!("cargo:rustc-link-search=lib");
}
