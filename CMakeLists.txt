###############################################################################
# finance-enums C/C++ packaging                                               #
#                                                                             #
# This CMake project does not compile any C/C++ itself. Its sole job is to    #
# drive `cargo build` for the standalone Rust library (rust/Cargo.toml, which #
# exposes the stable C ABI declared in finance_enums/include/finance_enums.h),#
# then install the resulting shared/static libraries, the public headers, and #
# the CMake package-config + pkg-config files so the artifact is consumable   #
# via `find_package(finance-enums CONFIG)` (e.g. from a vcpkg port).          #
###############################################################################
cmake_minimum_required(VERSION 3.16)
project(finance-enums
  VERSION 0.6.0
  DESCRIPTION "Standard financial enumerations"
  LANGUAGES NONE)

# Prefer `lib` over `lib64`, and set this before GNUInstallDirs so it does not
# warn about being unable to infer the libdir without an enabled language.
set(CMAKE_INSTALL_LIBDIR lib)

include(GNUInstallDirs)
include(CMakePackageConfigHelpers)

option(FINANCE_ENUMS_BUILD_SHARED "Build and install the shared library" ON)
option(FINANCE_ENUMS_BUILD_STATIC "Build and install the static library" ON)

if(NOT FINANCE_ENUMS_BUILD_SHARED AND NOT FINANCE_ENUMS_BUILD_STATIC)
  message(FATAL_ERROR "At least one of FINANCE_ENUMS_BUILD_SHARED / FINANCE_ENUMS_BUILD_STATIC must be ON")
endif()


###############################################################################
# Locate cargo                                                                #
###############################################################################
find_program(CARGO_EXECUTABLE cargo
  HINTS ENV CARGO_HOME
  PATH_SUFFIXES bin
  REQUIRED)
message(STATUS "Using cargo: ${CARGO_EXECUTABLE}")

set(_fe_manifest "${CMAKE_CURRENT_SOURCE_DIR}/rust/Cargo.toml")
set(_fe_cargo_dir "${CMAKE_CURRENT_BINARY_DIR}/cargo")
set(_fe_include_dir "${CMAKE_CURRENT_SOURCE_DIR}/finance_enums/include")

###############################################################################
# Platform-specific artifact filenames (as produced by cargo)                 #
###############################################################################
set(FINANCE_ENUMS_SHARED_FILE "${CMAKE_SHARED_LIBRARY_PREFIX}finance_enums${CMAKE_SHARED_LIBRARY_SUFFIX}")
set(FINANCE_ENUMS_STATIC_FILE "${CMAKE_STATIC_LIBRARY_PREFIX}finance_enums${CMAKE_STATIC_LIBRARY_SUFFIX}")
if(WIN32)
  # cargo names the MSVC import library for a cdylib `<name>.dll.lib`.
  set(FINANCE_ENUMS_IMPLIB_FILE "finance_enums.dll${CMAKE_IMPORT_LIBRARY_SUFFIX}")
else()
  set(FINANCE_ENUMS_IMPLIB_FILE "")
endif()

###############################################################################
# Build the Rust library                                                      #
###############################################################################
add_custom_target(finance_enums_cargo ALL
  COMMAND ${CMAKE_COMMAND} -E env CARGO_TARGET_DIR=${_fe_cargo_dir}
          ${CARGO_EXECUTABLE} build --release --manifest-path "${_fe_manifest}"
  WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
  COMMENT "Building finance_enums Rust library (cargo build --release)"
  VERBATIM)

###############################################################################
# Install                                                                     #
###############################################################################
# Public C / C++ headers.
install(DIRECTORY "${_fe_include_dir}/"
  DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}/finance_enums"
  FILES_MATCHING PATTERN "*.h" PATTERN "*.hpp")

# Libraries. cargo writes to <target>/release/, or <target>/<triple>/release/
# when CARGO_BUILD_TARGET is set (e.g. under the conda rust compiler), so each
# artifact is located with a glob over both layouts at install time.
function(_fe_install_artifact filename)
  if(filename STREQUAL "")
    return()
  endif()
  install(CODE "
    set(_direct \"${_fe_cargo_dir}/release/${filename}\")
    if(EXISTS \"\${_direct}\")
      set(_artifact \"\${_direct}\")
    else()
      file(GLOB _matches \"${_fe_cargo_dir}/*/release/${filename}\")
      list(LENGTH _matches _n)
      if(_n EQUAL 0)
        message(FATAL_ERROR \"Expected cargo artifact not found: ${filename}\")
      elseif(_n GREATER 1)
        message(FATAL_ERROR \"Ambiguous cargo artifact for ${filename} across target triples: \${_matches}\")
      endif()
      list(GET _matches 0 _artifact)
    endif()
    message(STATUS \"Installing \${_artifact}\")
    file(INSTALL \"\${_artifact}\"
      DESTINATION \"\${CMAKE_INSTALL_PREFIX}/${CMAKE_INSTALL_LIBDIR}\")
  ")
endfunction()

if(FINANCE_ENUMS_BUILD_SHARED)
  _fe_install_artifact("${FINANCE_ENUMS_SHARED_FILE}")
  if(WIN32)
    _fe_install_artifact("${FINANCE_ENUMS_IMPLIB_FILE}")
  endif()
endif()
if(FINANCE_ENUMS_BUILD_STATIC)
  _fe_install_artifact("${FINANCE_ENUMS_STATIC_FILE}")
endif()

###############################################################################
# Package discovery files                                                     #
###############################################################################
# When a linkage is disabled, blank out the corresponding filename so the
# installed Config does not advertise an artifact that was not installed.
if(NOT FINANCE_ENUMS_BUILD_SHARED)
  set(FINANCE_ENUMS_SHARED_FILE "")
  set(FINANCE_ENUMS_IMPLIB_FILE "")
endif()
if(NOT FINANCE_ENUMS_BUILD_STATIC)
  set(FINANCE_ENUMS_STATIC_FILE "")
endif()

configure_package_config_file(
  "${CMAKE_CURRENT_SOURCE_DIR}/rust/cmake/config/finance-enumsConfig.cmake.in"
  "${CMAKE_CURRENT_BINARY_DIR}/finance-enumsConfig.cmake"
  INSTALL_DESTINATION "${CMAKE_INSTALL_LIBDIR}/cmake/finance-enums"
  PATH_VARS CMAKE_INSTALL_INCLUDEDIR CMAKE_INSTALL_LIBDIR)

write_basic_package_version_file(
  "${CMAKE_CURRENT_BINARY_DIR}/finance-enumsConfigVersion.cmake"
  VERSION "${PROJECT_VERSION}"
  COMPATIBILITY SameMajorVersion)

configure_file(
  "${CMAKE_CURRENT_SOURCE_DIR}/rust/cmake/config/finance-enums.pc.in"
  "${CMAKE_CURRENT_BINARY_DIR}/finance-enums.pc"
  @ONLY)

install(FILES
    "${CMAKE_CURRENT_BINARY_DIR}/finance-enumsConfig.cmake"
    "${CMAKE_CURRENT_BINARY_DIR}/finance-enumsConfigVersion.cmake"
  DESTINATION "${CMAKE_INSTALL_LIBDIR}/cmake/finance-enums")

install(FILES "${CMAKE_CURRENT_BINARY_DIR}/finance-enums.pc"
  DESTINATION "${CMAKE_INSTALL_LIBDIR}/pkgconfig")
