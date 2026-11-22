vcpkg_check_linkage(ONLY_DYNAMIC_LIBRARY)

# Local overlay scaffold. Replace this path with vcpkg_from_github plus a
# release archive SHA512 when submitting the port to the vcpkg registry.
set(SOURCE_PATH "${CURRENT_PORT_DIR}/../..")

vcpkg_cmake_configure(
    SOURCE_PATH "${SOURCE_PATH}"
    OPTIONS
        -DFINANCE_ENUMS_BUILD_SHARED=ON
        -DFINANCE_ENUMS_BUILD_STATIC=OFF
)
vcpkg_cmake_install()
vcpkg_cmake_config_fixup(
    PACKAGE_NAME finance-enums
    CONFIG_PATH lib/cmake/finance-enums
)
vcpkg_fixup_pkgconfig()
vcpkg_copy_pdbs()

file(REMOVE_RECURSE
    "${CURRENT_PACKAGES_DIR}/debug/include"
    "${CURRENT_PACKAGES_DIR}/debug/share"
)

file(INSTALL "${CURRENT_PORT_DIR}/usage"
    DESTINATION "${CURRENT_PACKAGES_DIR}/share/${PORT}")
vcpkg_install_copyright(FILE_LIST "${SOURCE_PATH}/LICENSE")
