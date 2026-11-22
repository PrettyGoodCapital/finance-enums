//! Accounts, books, positions, and fund share classes.

use abi_safe_enum::abi_safe_enum;

#[abi_safe_enum]
pub enum AccountType {
    Invalid = 0,
    Cash,
    Margin,
    PrimeBrokerage,
    Custody,
    Settlement,
    Omnibus,
}

#[abi_safe_enum]
pub enum BookType {
    Invalid = 0,
    Trading,
    Hedging,
    Treasury,
    Financing,
    Inventory,
    Custody,
}

#[abi_safe_enum]
pub enum PositionType {
    Invalid = 0,
    Long,
    Short,
    Flat,
    Net,
    Gross,
}

#[abi_safe_enum]
pub enum InventoryType {
    Invalid = 0,
    Available,
    Reserved,
    Borrowed,
    Lent,
    Encumbered,
    PendingSettlement,
}

#[abi_safe_enum]
pub enum StrategyType {
    Invalid = 0,
    MarketMaking,
    Arbitrage,
    Hedging,
    Directional,
    Execution,
    RelativeValue,
}

#[abi_safe_enum]
pub enum NettingType {
    Invalid = 0,
    None,
    Bilateral,
    Multilateral,
    Portfolio,
    CrossProduct,
}

#[abi_safe_enum]
pub enum DistributionPolicy {
    Invalid = 0,
    Accumulating,
    Distributing,
    Income,
    Growth,
    Mixed,
}

#[abi_safe_enum]
pub enum ShareClassHedging {
    Invalid = 0,
    Unhedged,
    CurrencyHedged,
    DurationHedged,
    CommodityHedged,
    PartialHedged,
}
