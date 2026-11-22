//! Enum families declared with `#[abi_safe_enum]`, one directory per domain and one
//! file per topic. Everything is re-exported flat from [`crate::data`].
//!
//! Ordinals are part of the C ABI and are persisted by consumers, so treat
//! them as append-only: never reorder, remove, or renumber a variant. Add new
//! variants at the end of a family, or give them an explicit `= N` that is not
//! already used. Ordinal 0 is always the invalid/unknown sentinel.
#![allow(non_upper_case_globals)]

mod benchmarks;
mod credit;
mod factors;
mod financing;
mod fixed_income;
mod foreign_exchange;
mod instruments;
mod lifecycle;
mod market_structure;
mod portfolio;
mod post_trade;
mod reference;
mod trading;

pub use benchmarks::*;
pub use credit::*;
pub use factors::*;
pub use financing::*;
pub use fixed_income::*;
pub use foreign_exchange::*;
pub use instruments::*;
pub use lifecycle::*;
pub use market_structure::*;
pub use portfolio::*;
pub use post_trade::*;
pub use reference::*;
pub use trading::*;
