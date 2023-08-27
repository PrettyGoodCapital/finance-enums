#[derive(
    Copy, Clone, Debug, Eq, PartialEq
)]
#[repr(C)]
pub struct SecurityType {
    name: &'static str,
    value: u8,
}
//     Equity,
//     Option,
//     Bond,
//     Forward,
//     Future,
//     PerpetualFuture,
//     Spread,
//     Fund,
//     Commodity,
//     Currency,
//     Pair,
//     Index,
