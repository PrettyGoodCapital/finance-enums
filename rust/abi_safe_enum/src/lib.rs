//! Fieldless enums with stable ordinals, for values that cross a C ABI or are
//! stored as integers.
//!
//! `#[abi_safe_enum]` goes on a plain Rust enum:
//!
//! ```
//! use abi_safe_enum::abi_safe_enum;
//!
//! #[abi_safe_enum]
//! pub enum OrderStatus {
//!     Invalid = 0,
//!     New,
//!     Filled = 10,
//!     Canceled,
//! }
//!
//! assert_eq!(OrderStatus::Canceled.ordinal(), 11);
//! assert_eq!(OrderStatus::from_ordinal(10), Some(OrderStatus::Filled));
//! assert_eq!(OrderStatus::from_ordinal(2), None);
//! assert_eq!("New".parse::<OrderStatus>(), Ok(OrderStatus::New));
//! assert_eq!(OrderStatus::ORDINALS, &[0, 1, 10, 11]);
//! assert_eq!(std::mem::size_of::<OrderStatus>(), 1);
//! ```
//!
//! The contract:
//!
//! - Ordinals follow Rust's rules: an explicit `= N` (an integer literal), or
//!   one more than the previous variant, starting at 0.
//! - Some variant must have ordinal 0. It is the invalid/unknown sentinel, so a
//!   zero-initialized value never reads as a real variant.
//! - Ordinals must be unique.
//! - The macro picks the smallest `#[repr]` (`u8`, `u16`, or `u32`) that holds
//!   the largest ordinal. The width is part of the ABI, so an enum close to a
//!   boundary can pin a wider one to leave room to grow:
//!   `#[abi_safe_enum(repr = u16)]`.
//! - The macro adds `#[repr]` and derives `Debug`, `Clone`, `Copy`,
//!   `PartialEq`, `Eq`, `Hash`, `PartialOrd`, and `Ord`; don't add them yourself.
//!
//! Each enum gets `NAME`, `VARIANTS`, `ORDINALS`, `COUNT`, `ORDINAL_SIZE`,
//! `ordinal()`, `from_ordinal()`, `name()`, `from_name()`, the [`AbiSafeEnum`]
//! trait, `Display`, `FromStr`, `From<E> for u32`, and `TryFrom<u32>`.
//!
//! Invalid declarations fail to compile:
//!
//! ```compile_fail
//! # use abi_safe_enum::abi_safe_enum;
//! #[abi_safe_enum]
//! enum NoSentinel { A = 1, B }
//! ```
//!
//! ```compile_fail
//! # use abi_safe_enum::abi_safe_enum;
//! #[abi_safe_enum]
//! enum Duplicate { Invalid = 0, A = 3, B = 3 }
//! ```
//!
//! ```compile_fail
//! # use abi_safe_enum::abi_safe_enum;
//! #[abi_safe_enum(repr = u8)]
//! enum TooWide { Invalid = 0, A = 256 }
//! ```
//!
//! ```compile_fail
//! # use abi_safe_enum::abi_safe_enum;
//! #[abi_safe_enum]
//! #[repr(u16)]
//! enum HandwrittenRepr { Invalid = 0, A }
//! ```
//!
//! ```compile_fail
//! # use abi_safe_enum::abi_safe_enum;
//! const TEN: u8 = 10;
//! #[abi_safe_enum]
//! enum NonLiteral { Invalid = 0, A = TEN }
//! ```

use std::fmt;

pub use abi_safe_enum_macros::abi_safe_enum;

/// Implemented by every `#[abi_safe_enum]` enum.
pub trait AbiSafeEnum: Copy + Eq + Sized + 'static {
    /// The enum's name.
    const NAME: &'static str;
    /// Variant names in declaration order.
    const VARIANTS: &'static [&'static str];
    /// Ordinal of each variant, parallel to `VARIANTS`.
    const ORDINALS: &'static [u32];
    /// Size in bytes of the enum's representation.
    const ORDINAL_SIZE: usize;

    /// The variant's ordinal.
    fn ordinal(self) -> u32;
    /// The variant with `ordinal`, or `None` if no variant uses it.
    fn from_ordinal(ordinal: u32) -> Option<Self>;
    /// The variant's name.
    fn name(self) -> &'static str;
    /// The variant named `name`, or `None` if no variant has that name.
    fn from_name(name: &str) -> Option<Self>;
}

/// No variant uses this ordinal.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct UnknownOrdinal(pub u32);

impl fmt::Display for UnknownOrdinal {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "no variant has ordinal {}", self.0)
    }
}

impl std::error::Error for UnknownOrdinal {}

/// No variant has this name.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct UnknownName;

impl fmt::Display for UnknownName {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.write_str("no variant has that name")
    }
}

impl std::error::Error for UnknownName {}
