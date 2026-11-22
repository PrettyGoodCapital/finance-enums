//! Enum families declared with `#[abi_safe_enum]`.
//!
//! Ordinals are part of the C ABI and are persisted by consumers, so treat
//! them as append-only: never reorder, remove, or renumber a variant. Add new
//! variants at the end of a family, or give them an explicit `= N` that is not
//! already used. Ordinal 0 is always the invalid/unknown sentinel.
#![allow(non_upper_case_globals)]

mod benchmarks;
mod commodities;
mod country;
mod factors;
mod financing;
mod fixed_income;
mod foreign_exchange;
mod gics;
mod identifiers;
mod instruments;
mod lifecycle;
mod market_structure;
mod portfolio;
mod post_trade;
mod trading;

pub use benchmarks::*;
pub use commodities::*;
pub use country::*;
pub use factors::*;
pub use financing::*;
pub use fixed_income::*;
pub use foreign_exchange::*;
pub use gics::*;
pub use identifiers::*;
pub use instruments::*;
pub use lifecycle::*;
pub use market_structure::*;
pub use portfolio::*;
pub use post_trade::*;
pub use trading::*;
