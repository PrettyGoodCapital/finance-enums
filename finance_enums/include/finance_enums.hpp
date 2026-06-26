// finance_enums C++ header-only wrapper.
// Include this after linking or dlopen-ing the finance_enums shared library.
// Requires C++20 (for std::span).

#ifndef FINANCE_ENUMS_HPP
#define FINANCE_ENUMS_HPP

#include "finance_enums.h"

#include <cstddef>
#include <cstdint>
#include <memory>
#include <optional>
#include <span>
#include <stdexcept>
#include <string>
#include <string_view>
#include <unordered_map>
#include <vector>

#ifdef _WIN32
#include <windows.h>
#else
#include <dlfcn.h>
#endif

namespace fe {

/// Semantic enum-data ABI version. See <finance_enums.h> for the full policy.
struct AbiVersion {
    std::uint32_t major;
    std::uint32_t minor;
    std::uint32_t patch;
};

/// The ABI version baked into the header this translation unit was compiled
/// against. Compare it against a loaded library via EnumLibrary::abi_compatible.
inline constexpr AbiVersion kHeaderAbiVersion{
    FINANCE_ENUMS_ABI_VERSION_MAJOR,
    FINANCE_ENUMS_ABI_VERSION_MINOR,
    FINANCE_ENUMS_ABI_VERSION_PATCH,
};

/// True if a consumer built against `(consumer_major, consumer_minor)` can
/// safely use a library reporting `library`: same major, library minor >=
/// consumer minor.
constexpr bool abi_compatible(std::uint32_t consumer_major,
                              std::uint32_t consumer_minor,
                              const AbiVersion &library) noexcept {
    return consumer_major == library.major && consumer_minor <= library.minor;
}

/// Indexed, read-only view over the enum data export. Groups the flat variant
/// record array by family and offers ordinal/name lookups.
class EnumRegistry {
public:
    struct Family {
        std::string_view name;
        std::span<const EnumVariantRecordRaw> variants;
    };

    explicit EnumRegistry(const EnumDataExportV1 *exp) : exp_(exp) {
        if (!exp_)
            throw std::runtime_error("fe::EnumRegistry: null export pointer");
        if (exp_->abi_version != FINANCE_ENUMS_ENUM_EXPORT_ABI_VERSION)
            throw std::runtime_error("fe::EnumRegistry: ABI version mismatch");
        if (exp_->export_struct_size != sizeof(EnumDataExportV1))
            throw std::runtime_error("fe::EnumRegistry: export struct size mismatch");
        if (exp_->enum_variant_record_size != sizeof(EnumVariantRecordRaw))
            throw std::runtime_error("fe::EnumRegistry: variant record size mismatch");
        build_index();
        // build_index() assumes each family's records are contiguous in the export.
        // If they were not, a family would split into multiple entries and the
        // grouped count would exceed the export's family_count.
        if (families_.size() != exp_->family_count)
            throw std::runtime_error("fe::EnumRegistry: non-contiguous family records");
    }

    size_t family_count() const { return families_.size(); }
    size_t record_count() const { return exp_->records_len; }
    size_t max_ordinal() const { return exp_->max_ordinal; }

    const std::vector<Family> &families() const { return families_; }

    const Family *family(std::string_view name) const {
        auto it = family_index_.find(name);
        return it != family_index_.end() ? &families_[it->second] : nullptr;
    }

    std::optional<size_t> ordinal(std::string_view family_name,
                                  std::string_view variant_name) const {
        auto fam = family(family_name);
        if (!fam) return std::nullopt;
        for (const auto &rec : fam->variants) {
            if (std::string_view(rec.variant) == variant_name)
                return rec.ordinal;
        }
        return std::nullopt;
    }

    std::optional<std::string_view> variant_at(std::string_view family_name,
                                               size_t ord) const {
        auto fam = family(family_name);
        if (!fam || ord >= fam->variants.size()) return std::nullopt;
        return fam->variants[ord].variant;
    }

    std::vector<std::string_view> variant_names(std::string_view family_name) const {
        std::vector<std::string_view> out;
        if (auto fam = family(family_name)) {
            out.reserve(fam->variants.size());
            for (const auto &rec : fam->variants)
                out.emplace_back(rec.variant);
        }
        return out;
    }

private:
    void build_index() {
        const auto *recs = exp_->records;
        size_t i = 0;
        while (i < exp_->records_len) {
            std::string_view name(recs[i].enum_name);
            size_t start = i;
            while (i < exp_->records_len &&
                   std::string_view(recs[i].enum_name) == name)
                ++i;
            families_.push_back({name, {recs + start, i - start}});
            family_index_[name] = families_.size() - 1;
        }
    }

    const EnumDataExportV1 *exp_;
    std::vector<Family> families_;
    std::unordered_map<std::string_view, size_t> family_index_;
};

/// RAII loader for the finance_enums shared library. Resolves the enum export
/// plus the ABI version/compat symbols and exposes the registry.
class EnumLibrary {
public:
    explicit EnumLibrary(const char *path) {
#ifdef _WIN32
        handle_ = LoadLibraryA(path);
        if (!handle_)
            throw std::runtime_error(std::string("LoadLibrary failed: ") + path);
        auto fn = reinterpret_cast<const EnumDataExportV1 *(*)()>(
            reinterpret_cast<void *>(
                GetProcAddress(static_cast<HMODULE>(handle_), "finance_enums_enum_export_v1")));
        if (!fn) {
            FreeLibrary(static_cast<HMODULE>(handle_));
            throw std::runtime_error("GetProcAddress: finance_enums_enum_export_v1 not found");
        }
#else
        handle_ = dlopen(path, RTLD_NOW);
        if (!handle_)
            throw std::runtime_error(std::string("dlopen: ") + dlerror());
        auto fn = reinterpret_cast<const EnumDataExportV1 *(*)()>(
            dlsym(handle_, "finance_enums_enum_export_v1"));
        if (!fn) {
            dlclose(handle_);
            handle_ = nullptr;
            throw std::runtime_error(std::string("dlsym: ") + dlerror());
        }
#endif
        version_fn_ = reinterpret_cast<VersionFn>(resolve("finance_enums_abi_version"));
        compatible_fn_ = reinterpret_cast<CompatibleFn>(resolve("finance_enums_abi_compatible"));
        registry_ = std::make_unique<EnumRegistry>(fn());
    }

    ~EnumLibrary() {
        if (handle_) {
#ifdef _WIN32
            FreeLibrary(static_cast<HMODULE>(handle_));
#else
            dlclose(handle_);
#endif
        }
    }

    EnumLibrary(const EnumLibrary &) = delete;
    EnumLibrary &operator=(const EnumLibrary &) = delete;
    EnumLibrary(EnumLibrary &&o) noexcept
        : handle_(o.handle_), version_fn_(o.version_fn_),
          compatible_fn_(o.compatible_fn_), registry_(std::move(o.registry_)) {
        o.handle_ = nullptr;
        o.version_fn_ = nullptr;
        o.compatible_fn_ = nullptr;
    }
    EnumLibrary &operator=(EnumLibrary &&o) noexcept {
        std::swap(handle_, o.handle_);
        std::swap(version_fn_, o.version_fn_);
        std::swap(compatible_fn_, o.compatible_fn_);
        registry_ = std::move(o.registry_);
        return *this;
    }

    const EnumRegistry &registry() const { return *registry_; }

    /// The semantic enum-data ABI version reported by the loaded library.
    AbiVersion abi_version() const {
        AbiVersion v{0, 0, 0};
        version_fn_(&v.major, &v.minor, &v.patch);
        return v;
    }

    /// True if a consumer built against `(consumer_major, consumer_minor)` is
    /// compatible with the loaded library. Defaults to the header version this
    /// translation unit was compiled against.
    bool abi_compatible(std::uint32_t consumer_major = kHeaderAbiVersion.major,
                        std::uint32_t consumer_minor = kHeaderAbiVersion.minor) const {
        return compatible_fn_(consumer_major, consumer_minor) != 0;
    }

    /// Like abi_compatible(), but throws std::runtime_error on mismatch.
    void assert_abi_compatible(std::uint32_t consumer_major = kHeaderAbiVersion.major,
                               std::uint32_t consumer_minor = kHeaderAbiVersion.minor) const {
        if (!abi_compatible(consumer_major, consumer_minor)) {
            AbiVersion lib = abi_version();
            throw std::runtime_error(
                "finance_enums ABI incompatible: consumer " +
                std::to_string(consumer_major) + "." + std::to_string(consumer_minor) +
                ", library " + std::to_string(lib.major) + "." +
                std::to_string(lib.minor) + "." + std::to_string(lib.patch));
        }
    }

private:
    using VersionFn = void (*)(std::uint32_t *, std::uint32_t *, std::uint32_t *);
    using CompatibleFn = std::int32_t (*)(std::uint32_t, std::uint32_t);

    void *resolve(const char *symbol) const {
#ifdef _WIN32
        auto sym = reinterpret_cast<void *>(
            GetProcAddress(static_cast<HMODULE>(handle_), symbol));
#else
        auto sym = dlsym(handle_, symbol);
#endif
        if (!sym)
            throw std::runtime_error(std::string("symbol not found: ") + symbol);
        return sym;
    }

    void *handle_ = nullptr;
    VersionFn version_fn_ = nullptr;
    CompatibleFn compatible_fn_ = nullptr;
    std::unique_ptr<EnumRegistry> registry_;
};

} // namespace fe

#endif // FINANCE_ENUMS_HPP
