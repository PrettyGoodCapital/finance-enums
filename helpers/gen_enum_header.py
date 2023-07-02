# MSVC limits to 127
COUNT = 100

RANGES = (
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    25,  # industry groups
    74,  # industries
    96,  # exchanges
    163,  # subindustries
    183,  # currencies
    250,  # country codes
)

enum_str = """
#pragma once

#include <string>
#include <vector>
#include <unordered_map>

#define ENUM_TO_STRING(type)                                                                     \\
  inline std::string type##_to_string(const type& typ) { return type##_names[static_cast<int>(typ)]; } \\
  inline std::string type##_to_repr(const type& typ) { return std::string(#type) + std::string("<") + type##_names[static_cast<int>(typ)] + std::string(">"); }

#ifdef BUILD_PYTHON
#include <pybind11/pybind11.h>
#define ENUM_FROM_STRING(type)                                 \\
  type inline type##_from_string(const char* s) {              \\
    if(_##type##_mapping.find(s) == _##type##_mapping.end()) { \\
      throw pybind11::value_error(s);                          \\
    }                                                          \\
    return _##type##_mapping[s];                               \\
  };
#else
#define ENUM_FROM_STRING(type)                                 \\
  type inline type##_from_string(const char* s) {              \\
    if(_##type##_mapping.find(s) == _##type##_mapping.end()) { \\
      throw FinanceEnumsCPPException(s);                       \\
    }                                                          \\
    return _##type##_mapping[s];                               \\
  };
#endif

"""

enum_str += "#define GET_ENUM_MACRO(" + ", ".join(f"_{_}" for _ in range(0, COUNT)) + ", NAME, ...) NAME\n"
enum_str += "#define ENUM(...) GET_ENUM_MACRO(__VA_ARGS__, " + ", ".join(f"ENUM{_}" for _ in range(COUNT - 1, 0, -1)) + ")(__VA_ARGS__)\n"
enum_str += "#define GET_ENUM_NAMES_MACRO(" + ", ".join(f"_{_}" for _ in range(0, COUNT)) + ", NAME, ...) NAME\n"
enum_str += (
    "#define ENUM_NAMES(...) GET_ENUM_NAMES_MACRO(__VA_ARGS__, " + ", ".join(f"ENUM_NAMES{_}" for _ in range(COUNT - 1, 0, -1)) + ")(__VA_ARGS__)\n"
)
enum_str += "#define GET_ENUM_MAPPING_MACRO(" + ", ".join(f"_{_}" for _ in range(0, COUNT)) + ", NAME, ...) NAME\n"
enum_str += (
    "#define ENUM_MAPPING(...) GET_ENUM_MAPPING_MACRO(__VA_ARGS__, "
    + ", ".join(f"ENUM_MAPPING{_}" for _ in range(COUNT - 1, 0, -1))
    + ")(__VA_ARGS__)\n"
)
enum_str += "#define GET_ENUM_MACRO(" + ", ".join(f"_{_}" for _ in range(0, COUNT)) + ", NAME, ...) NAME\n"
enum_str += (
    f"#define PYBIND_ENUM_VALUE(...) GET_ENUM_MACRO(__VA_ARGS__, "
    + ", ".join(f"PYBIND_ENUM_VALUE{_}" for _ in range(COUNT - 1, 0, -1))
    + ")(__VA_ARGS__)\n"
)
print(enum_str)


for _ in range(1, COUNT):
    # lets not be gratuitous
    if _ not in RANGES:
        continue
    enum_str = f"#define ENUM_NAMES{_}(name, " + ", ".join(f'v{i+1}' for i in range(_)) + ")\\\n"
    enum_str += "static const std::vector<str_t> name##_names = {" + ", ".join(f'#v{i+1}' for i in range(_)) + "};\n"

    enum_str += f"#define ENUM_MAPPING{_}(name, " + ", ".join(f'v{i+1}' for i in range(_)) + ")\\\n"
    enum_str += "static std::unordered_map<str_t, name> _##name##_mapping = {" + ", ".join(f'{{#v{i+1}, name::v{i+1}}}' for i in range(_)) + "};\n"

    enum_str += f"#define ENUM{_}(name, " + ", ".join(f'v{i+1}' for i in range(_)) + ")\\\n"
    enum_str += "enum class LIB_EXPORT name { " + ", ".join(f'v{i+1}' for i in range(_)) + "};\\\n"
    enum_str += "ENUM_NAMES(name, " + ", ".join(f'v{i+1}' for i in range(_)) + ")\\\n"
    enum_str += "ENUM_MAPPING(name, " + ", ".join(f'v{i+1}' for i in range(_)) + ")\n"

    enum_str += f"#define PYBIND_ENUM_VALUE{_}(name, " + ", ".join(f'v{i+1}' for i in range(_)) + ")\\\n"
    enum_str += "." + ".".join(f'value(#v{i+1}, name::v{i+1})' for i in range(_)) + "\n"

    print(enum_str)