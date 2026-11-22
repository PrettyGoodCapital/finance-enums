//! Commodity sectors and products.

use abi_safe_enum::abi_safe_enum;

#[abi_safe_enum]
pub enum CommodityType {
    Invalid = 0,
    Energy,
    Metals,
    Agriculture,
    Livestock,
    Softs,
    Lumber,
    Freight,
    Carbon,
}

#[abi_safe_enum]
pub enum EnergyType {
    Invalid = 0,
    Crude,
    NaturalGas,
    HeatingOil,
    Gasoline,
    Electricity,
    LiquefiedNaturalGas,
    Propane,
    Uranium,
}

#[abi_safe_enum]
pub enum MetalType {
    Invalid = 0,
    Gold,
    Silver,
    Copper,
    Platinum,
    Palladium,
    Aluminum,
    Zinc,
    Nickel,
    Lead,
    Tin,
    Steel,
    Cobalt,
    Iron,
}

#[abi_safe_enum]
pub enum AgricultureType {
    Invalid = 0,
    Corn,
    Wheat,
    Oats,
    Soybean,
    Cocoa,
    Coffee,
    Sugar,
    Cotton,
    OrangeJuice,
    Cattle,
    Hogs,
}

#[abi_safe_enum]
pub enum LivestockType {
    Invalid = 0,
    Cattle,
    Feeder,
    Hogs,
}
