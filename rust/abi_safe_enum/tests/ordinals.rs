use std::mem::size_of;

use abi_safe_enum::{abi_safe_enum, AbiSafeEnum, UnknownName, UnknownOrdinal};

#[abi_safe_enum]
pub enum Dense {
    Invalid = 0,
    Buy,
    Sell,
}

#[abi_safe_enum]
pub enum Sparse {
    /// Doc comments on variants are kept.
    Unknown = 0,
    First = 1,
    Tenth = 10,
    Eleventh,
}

#[abi_safe_enum]
pub enum Wide {
    Invalid = 0,
    Large = 300,
}

#[abi_safe_enum(repr = u16)]
pub enum Pinned {
    Invalid = 0,
    A,
}

#[abi_safe_enum]
pub enum Reordered {
    Second = 2,
    Zero = 0,
    One,
}

#[test]
fn implicit_ordinals_follow_the_previous_variant() {
    assert_eq!(Dense::ORDINALS, &[0, 1, 2]);
    assert_eq!(Sparse::ORDINALS, &[0, 1, 10, 11]);
    assert_eq!(Reordered::ORDINALS, &[2, 0, 1]);
    assert_eq!(Sparse::Eleventh as u8, 11);
}

#[test]
fn width_is_the_smallest_that_fits_unless_pinned() {
    assert_eq!(size_of::<Dense>(), 1);
    assert_eq!(size_of::<Sparse>(), 1);
    assert_eq!(size_of::<Wide>(), 2);
    assert_eq!(size_of::<Pinned>(), 2);
    assert_eq!(Dense::ORDINAL_SIZE, 1);
    assert_eq!(Wide::ORDINAL_SIZE, 2);
    assert_eq!(Pinned::ORDINAL_SIZE, 2);
}

#[test]
fn lookups_use_declared_ordinals() {
    assert_eq!(Sparse::from_ordinal(10), Some(Sparse::Tenth));
    assert_eq!(Sparse::from_ordinal(2), None);
    assert_eq!(Sparse::Tenth.ordinal(), 10);
    assert_eq!(Wide::from_ordinal(300), Some(Wide::Large));
    assert_eq!(Sparse::try_from(11), Ok(Sparse::Eleventh));
    assert_eq!(Sparse::try_from(3), Err(UnknownOrdinal(3)));
    assert_eq!(u32::from(Sparse::Tenth), 10);
}

#[test]
fn names_round_trip() {
    assert_eq!(Sparse::NAME, "Sparse");
    assert_eq!(Sparse::VARIANTS, &["Unknown", "First", "Tenth", "Eleventh"]);
    assert_eq!(Sparse::COUNT, 4);
    assert_eq!(Sparse::Tenth.name(), "Tenth");
    assert_eq!(Sparse::Tenth.to_string(), "Tenth");
    assert_eq!("Tenth".parse::<Sparse>(), Ok(Sparse::Tenth));
    assert_eq!("Nope".parse::<Sparse>(), Err(UnknownName));
}

fn describe<E: AbiSafeEnum>() -> (&'static str, &'static [u32], usize) {
    (E::NAME, E::ORDINALS, E::ORDINAL_SIZE)
}

#[test]
fn trait_exposes_the_same_tables() {
    assert_eq!(describe::<Sparse>(), ("Sparse", Sparse::ORDINALS, 1));
    assert_eq!(
        <Sparse as AbiSafeEnum>::from_ordinal(1),
        Some(Sparse::First)
    );
    assert_eq!(
        <Sparse as AbiSafeEnum>::from_name("First"),
        Some(Sparse::First)
    );
}
