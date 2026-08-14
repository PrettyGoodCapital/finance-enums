cmake_minimum_required(VERSION 3.16)
project(finance-enums-consumer LANGUAGES C CXX)

set(FINANCE_ENUMS_REQUIRED_VERSION "0.7" CACHE STRING "Required finance-enums version")
find_package(finance-enums ${FINANCE_ENUMS_REQUIRED_VERSION} CONFIG REQUIRED)

add_executable(finance_enums_c ../../finance_enums/tests/ffi/test.c)
target_compile_features(finance_enums_c PRIVATE c_std_11)
target_link_libraries(finance_enums_c PRIVATE finance-enums::finance-enums ${CMAKE_DL_LIBS})

add_executable(finance_enums_cpp ../../finance_enums/tests/ffi/test.cpp)
target_compile_features(finance_enums_cpp PRIVATE cxx_std_20)
target_link_libraries(finance_enums_cpp PRIVATE finance-enums::finance-enums ${CMAKE_DL_LIBS})

enable_testing()
add_test(NAME finance_enums_c
  COMMAND finance_enums_c "$<TARGET_FILE:finance-enums::finance-enums>")
add_test(NAME finance_enums_cpp
  COMMAND finance_enums_cpp "$<TARGET_FILE:finance-enums::finance-enums>")

if(WIN32)
  set_tests_properties(finance_enums_c finance_enums_cpp PROPERTIES
    ENVIRONMENT_MODIFICATION "PATH=path_list_prepend:$<TARGET_FILE_DIR:finance-enums::finance-enums>")
endif()
