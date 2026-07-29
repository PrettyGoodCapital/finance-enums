"""CFI (ISO 10962) classification helpers.

Parse and build six-character CFI codes and map them to/from the
strongly-typed enum families exposed by :mod:`finance_enums`.
"""

from __future__ import annotations

from dataclasses import dataclass, replace

from .finance_enums import int_enums as _int_enums

__all__ = [
    "CFIClassification",
    "build_cfi",
    "build_cfi_from_classification",
    "parse_cfi",
    "validate_cfi_classification",
]

SecurityType = _int_enums.SecurityType
InstrumentType = _int_enums.InstrumentType
EquityType = _int_enums.EquityType
OptionType = _int_enums.OptionType
OptionExerciseType = _int_enums.OptionExerciseType
BondType = _int_enums.BondType
FundType = _int_enums.FundType
MutualFundEndedness = _int_enums.MutualFundEndedness
FutureAssetClass = _int_enums.FutureAssetClass
SettlementType = _int_enums.SettlementType
DeliveryType = _int_enums.DeliveryType
UnderlyingAssetClass = _int_enums.UnderlyingAssetClass
ContractStyle = _int_enums.ContractStyle
SwapType = _int_enums.SwapType
FinancingType = _int_enums.FinancingType
CommodityType = _int_enums.CommodityType


@dataclass(frozen=True)
class CFIClassification:
    code: str
    category: str
    group: str
    attributes: tuple[str, str, str, str]
    security_type: SecurityType | None
    instrument_type: InstrumentType | None
    equity_type: EquityType | None = None
    option_type: OptionType | None = None
    option_exercise_type: OptionExerciseType | None = None
    bond_type: BondType | None = None
    fund_type: FundType | None = None
    mutual_fund_endedness: MutualFundEndedness | None = None
    future_asset_class: FutureAssetClass | None = None
    settlement_type: SettlementType | None = None
    delivery_type: DeliveryType | None = None
    underlying_asset_class: UnderlyingAssetClass | None = None
    contract_style: ContractStyle | None = None
    swap_type: SwapType | None = None
    financing_type: FinancingType | None = None
    commodity_type: CommodityType | None = None
    underlying_security_type: SecurityType | None = None


_EQUITY_GROUP_TO_TYPE = {
    "S": EquityType.Shares,
    "P": EquityType.PreferredShares,
    "R": EquityType.PreferredShares,
    "C": EquityType.ConvertibleShares,
    "F": EquityType.PreferredConvertibleShares,
    "V": EquityType.PreferredConvertibleShares,
    "D": EquityType.DepositoryReceipt,
}
_EQUITY_TYPE_TO_GROUP = {
    EquityType.Shares: "S",
    EquityType.PreferredShares: "P",
    EquityType.ConvertibleShares: "C",
    EquityType.PreferredConvertibleShares: "F",
    EquityType.DepositoryReceipt: "D",
}
_OPTION_GROUP_TO_TYPE = {"C": OptionType.Call, "P": OptionType.Put}
_OPTION_TYPE_TO_GROUP = {value: key for key, value in _OPTION_GROUP_TO_TYPE.items()}
_OPTION_EXERCISE_TO_ATTR = {
    OptionExerciseType.American: "A",
    OptionExerciseType.European: "E",
    OptionExerciseType.Bermudan: "B",
}
_OPTION_ATTR_TO_EXERCISE = {value: key for key, value in _OPTION_EXERCISE_TO_ATTR.items()}
_SETTLEMENT_TYPE_TO_DELIVERY_TYPE = {
    SettlementType.Physical: DeliveryType.Physical,
    SettlementType.Cash: DeliveryType.Cash,
    SettlementType.NonDeliverable: DeliveryType.NonDeliverable,
    SettlementType.ElectAtExercise: DeliveryType.ElectAtExercise,
    SettlementType.DeliveryVersusPayment: DeliveryType.DeliveryVersusPayment,
    SettlementType.FreeOfPayment: DeliveryType.FreeOfPayment,
}
_DELIVERY_TYPE_TO_SETTLEMENT_TYPE = {value: key for key, value in _SETTLEMENT_TYPE_TO_DELIVERY_TYPE.items()}
_DERIVATIVE_DELIVERY_ATTR_TO_TYPE = {
    "P": DeliveryType.Physical,
    "C": DeliveryType.Cash,
    "N": DeliveryType.NonDeliverable,
    "E": DeliveryType.ElectAtExercise,
}
_DERIVATIVE_DELIVERY_TYPE_TO_ATTR = {value: key for key, value in _DERIVATIVE_DELIVERY_ATTR_TO_TYPE.items()}
_FINANCING_DELIVERY_ATTR_TO_TYPE = {
    "P": DeliveryType.Physical,
    "C": DeliveryType.Cash,
    "N": DeliveryType.NonDeliverable,
    "D": DeliveryType.DeliveryVersusPayment,
    "F": DeliveryType.FreeOfPayment,
    "H": DeliveryType.HoldInCustody,
    "T": DeliveryType.TriParty,
}
_FINANCING_DELIVERY_TYPE_TO_ATTR = {value: key for key, value in _FINANCING_DELIVERY_ATTR_TO_TYPE.items()}
_CONTRACT_STYLE_TO_ATTR = {
    ContractStyle.Standardized: "S",
    ContractStyle.NonStandardized: "N",
}
_CONTRACT_STYLE_ATTR_TO_STYLE = {value: key for key, value in _CONTRACT_STYLE_TO_ATTR.items()}
_OPTION_ASSET_ATTR_TO_CLASS = {
    "B": UnderlyingAssetClass.Basket,
    "S": UnderlyingAssetClass.Equity,
    "D": UnderlyingAssetClass.Debt,
    "T": UnderlyingAssetClass.Commodity,
    "C": UnderlyingAssetClass.Currency,
    "I": UnderlyingAssetClass.Index,
    "O": UnderlyingAssetClass.Option,
    "F": UnderlyingAssetClass.Future,
    "W": UnderlyingAssetClass.Swap,
    "N": UnderlyingAssetClass.InterestRate,
    "M": UnderlyingAssetClass.Other,
}
_OPTION_CLASS_TO_ASSET_ATTR = {value: key for key, value in _OPTION_ASSET_ATTR_TO_CLASS.items()}
_FUND_GROUP_TO_TYPE = {
    "E": FundType.ExchangeTradedFund,
    "B": FundType.RealEstateInvestmentTrust,
    "I": FundType.MutualFund,
}
_FUTURE_GROUP_TO_ASSET_CLASS = {"F": FutureAssetClass.Financial, "C": FutureAssetClass.Commodity}
_FUTURE_ASSET_CLASS_TO_GROUP = {value: key for key, value in _FUTURE_GROUP_TO_ASSET_CLASS.items()}
_FINANCIAL_FUTURE_ATTR_TO_CLASS = {
    "B": UnderlyingAssetClass.Basket,
    "S": UnderlyingAssetClass.Equity,
    "D": UnderlyingAssetClass.Debt,
    "C": UnderlyingAssetClass.Currency,
    "I": UnderlyingAssetClass.Index,
    "O": UnderlyingAssetClass.Option,
    "F": UnderlyingAssetClass.Future,
    "W": UnderlyingAssetClass.Swap,
    "N": UnderlyingAssetClass.InterestRate,
    "V": UnderlyingAssetClass.StockDividend,
    "M": UnderlyingAssetClass.Other,
}
_FINANCIAL_FUTURE_CLASS_TO_ATTR = {value: key for key, value in _FINANCIAL_FUTURE_ATTR_TO_CLASS.items()}
_COMMODITY_FUTURE_ATTR_TO_CLASS = {
    "E": UnderlyingAssetClass.ExtractionResources,
    "A": UnderlyingAssetClass.Agriculture,
    "I": UnderlyingAssetClass.IndustrialProducts,
    "S": UnderlyingAssetClass.Services,
    "N": UnderlyingAssetClass.Environmental,
    "P": UnderlyingAssetClass.PolypropyleneProducts,
    "H": UnderlyingAssetClass.GeneratedResources,
    "M": UnderlyingAssetClass.Other,
}
_COMMODITY_FUTURE_CLASS_TO_ATTR = {value: key for key, value in _COMMODITY_FUTURE_ATTR_TO_CLASS.items()}
_COMMODITY_FUTURE_CLASS_TO_TYPE = {
    UnderlyingAssetClass.Agriculture: CommodityType.Agriculture,
}
_SWAP_GROUP_TO_TYPE = {
    "R": SwapType.Rates,
    "T": SwapType.Commodities,
    "E": SwapType.Equity,
    "C": SwapType.Credit,
    "F": SwapType.ForeignExchange,
    "M": SwapType.Other,
}
_SWAP_TYPE_TO_GROUP = {value: key for key, value in _SWAP_GROUP_TO_TYPE.items()}
_SPOT_COMMODITY_ATTR_TO_TYPE = {
    "A": CommodityType.Agriculture,
    "J": CommodityType.Energy,
    "K": CommodityType.Metals,
}
_COMMODITY_TYPE_TO_SPOT_ATTR = {value: key for key, value in _SPOT_COMMODITY_ATTR_TO_TYPE.items()}
_FINANCING_GROUP_TO_TYPE = {
    "L": FinancingType.LoanLease,
    "R": FinancingType.RepurchaseAgreement,
    "S": FinancingType.SecuritiesLending,
}
_FINANCING_TYPE_TO_GROUP = {value: key for key, value in _FINANCING_GROUP_TO_TYPE.items()}
_COMPLEX_OPTION_GROUP_TO_ASSET_CLASS = {
    "R": UnderlyingAssetClass.InterestRate,
    "T": UnderlyingAssetClass.Commodity,
    "E": UnderlyingAssetClass.Equity,
    "C": UnderlyingAssetClass.Credit,
    "F": UnderlyingAssetClass.Currency,
    "M": UnderlyingAssetClass.Other,
}
_ASSET_CLASS_TO_COMPLEX_OPTION_GROUP = {value: key for key, value in _COMPLEX_OPTION_GROUP_TO_ASSET_CLASS.items()}
_FORWARD_GROUP_TO_ASSET_CLASS = {
    "E": UnderlyingAssetClass.Equity,
    "F": UnderlyingAssetClass.Currency,
    "C": UnderlyingAssetClass.Credit,
    "R": UnderlyingAssetClass.InterestRate,
    "T": UnderlyingAssetClass.Commodity,
}
_ASSET_CLASS_TO_FORWARD_GROUP = {value: key for key, value in _FORWARD_GROUP_TO_ASSET_CLASS.items()}
_STRATEGY_GROUP_TO_ASSET_CLASS = {
    "R": UnderlyingAssetClass.InterestRate,
    "T": UnderlyingAssetClass.Commodity,
    "E": UnderlyingAssetClass.Equity,
    "C": UnderlyingAssetClass.Credit,
    "F": UnderlyingAssetClass.Currency,
    "Y": UnderlyingAssetClass.MixedAssets,
    "M": UnderlyingAssetClass.Other,
}
_ASSET_CLASS_TO_STRATEGY_GROUP = {value: key for key, value in _STRATEGY_GROUP_TO_ASSET_CLASS.items()}
_ASSET_CLASS_TO_SECURITY_TYPE = {
    UnderlyingAssetClass.Equity: SecurityType.Equity,
    UnderlyingAssetClass.Currency: SecurityType.Currency,
    UnderlyingAssetClass.Commodity: SecurityType.Commodity,
    UnderlyingAssetClass.Debt: SecurityType.Bond,
    UnderlyingAssetClass.Index: SecurityType.Index,
    UnderlyingAssetClass.Option: SecurityType.Option,
    UnderlyingAssetClass.Future: SecurityType.Future,
    UnderlyingAssetClass.Swap: SecurityType.Swap,
}
_SECURITY_TYPE_TO_ASSET_CLASS = {value: key for key, value in _ASSET_CLASS_TO_SECURITY_TYPE.items()}


def _coerce_enum(enum_type, value, field_name: str):  # type: ignore[no-untyped-def]
    if value is None or isinstance(value, enum_type):
        return value
    try:
        return enum_type(value)
    except ValueError as exc:
        raise ValueError(f"invalid {field_name}: {value!r}") from exc


def _normalize_cfi_attributes(attributes: str | tuple[str, str, str, str] | None) -> tuple[str, str, str, str]:
    if attributes is None:
        return ("X", "X", "X", "X")
    if isinstance(attributes, str):
        normalized = attributes.strip().upper()
        if len(normalized) != 4:
            raise ValueError("CFI attributes must be exactly 4 characters")
        return tuple(normalized)  # type: ignore[return-value]
    if len(attributes) != 4:
        raise ValueError("CFI attributes must contain exactly 4 characters")
    return tuple(str(value).strip().upper() for value in attributes)


def _resolve_underlying_asset_class(
    underlying_asset_class: UnderlyingAssetClass | None,
    underlying_security_type: SecurityType | None,
) -> UnderlyingAssetClass | None:
    if underlying_security_type is None:
        return underlying_asset_class

    mapped_asset_class = _SECURITY_TYPE_TO_ASSET_CLASS.get(underlying_security_type)
    if mapped_asset_class is None:
        raise NotImplementedError(
            f"derivative underlying asset-class resolution is not implemented for security type {underlying_security_type.name}"
        )
    if underlying_asset_class is not None and underlying_asset_class != mapped_asset_class:
        raise ValueError("underlying_asset_class and underlying_security_type refer to different underliers")
    return mapped_asset_class


def _resolve_delivery_fields(
    settlement_type: SettlementType | None,
    delivery_type: DeliveryType | None,
) -> tuple[SettlementType | None, DeliveryType | None]:
    resolved_delivery_type = delivery_type

    if settlement_type is not None:
        settlement_delivery_type = _SETTLEMENT_TYPE_TO_DELIVERY_TYPE.get(settlement_type)
        if settlement_delivery_type is None:
            raise ValueError(f"settlement_type {settlement_type.name} is not supported by CFI delivery attributes")
        if resolved_delivery_type is not None and resolved_delivery_type != settlement_delivery_type:
            raise ValueError("settlement_type and delivery_type refer to different delivery semantics")
        resolved_delivery_type = settlement_delivery_type

    if resolved_delivery_type is None:
        return settlement_type, None

    return (
        _DELIVERY_TYPE_TO_SETTLEMENT_TYPE.get(resolved_delivery_type),
        resolved_delivery_type,
    )


def parse_cfi(code: str) -> CFIClassification:
    normalized = code.strip().upper()
    if len(normalized) != 6:
        raise ValueError("CFI codes must be exactly 6 characters")

    category = normalized[0]
    group = normalized[1]
    attributes = (normalized[2], normalized[3], normalized[4], normalized[5])

    security_type = None
    instrument_type = None
    equity_type = None
    option_type = None
    option_exercise_type = None
    bond_type = None
    fund_type = None
    mutual_fund_endedness = None
    future_asset_class = None
    settlement_type = None
    delivery_type = None
    underlying_asset_class = None
    contract_style = None
    swap_type = None
    financing_type = None
    commodity_type = None
    underlying_security_type = None

    if category == "E":
        security_type = SecurityType.Equity
        instrument_type = InstrumentType.Spot
        equity_type = _EQUITY_GROUP_TO_TYPE.get(group)
    elif category == "D":
        security_type = SecurityType.Bond
        instrument_type = InstrumentType.Spot
        if group == "N":
            bond_type = BondType.Municipal
        elif group in {"B", "C", "W", "T", "S", "E", "G", "A", "H"}:
            bond_type = BondType.Government if attributes[1] == "T" else BondType.Corporate
    elif category == "C":
        security_type = SecurityType.Fund
        instrument_type = InstrumentType.Spot
        fund_type = _FUND_GROUP_TO_TYPE.get(group)
        if group == "I":
            if attributes[0] == "O":
                mutual_fund_endedness = MutualFundEndedness.OpenEnded
            elif attributes[0] == "C":
                mutual_fund_endedness = MutualFundEndedness.ClosedEnded
    elif category == "O":
        security_type = SecurityType.Option
        instrument_type = InstrumentType.Option
        option_type = _OPTION_GROUP_TO_TYPE.get(group)
        option_exercise_type = _OPTION_ATTR_TO_EXERCISE.get(attributes[0])
        underlying_asset_class = _OPTION_ASSET_ATTR_TO_CLASS.get(attributes[1])
        delivery_type = _DERIVATIVE_DELIVERY_ATTR_TO_TYPE.get(attributes[2])
        settlement_type = _DELIVERY_TYPE_TO_SETTLEMENT_TYPE.get(delivery_type)
        contract_style = _CONTRACT_STYLE_ATTR_TO_STYLE.get(attributes[3])
        underlying_security_type = _ASSET_CLASS_TO_SECURITY_TYPE.get(underlying_asset_class)
    elif category == "F":
        security_type = SecurityType.Future
        instrument_type = InstrumentType.Future
        future_asset_class = _FUTURE_GROUP_TO_ASSET_CLASS.get(group)
        if group == "F":
            underlying_asset_class = _FINANCIAL_FUTURE_ATTR_TO_CLASS.get(attributes[0])
        elif group == "C":
            underlying_asset_class = _COMMODITY_FUTURE_ATTR_TO_CLASS.get(attributes[0])
            commodity_type = _COMMODITY_FUTURE_CLASS_TO_TYPE.get(underlying_asset_class)
        delivery_type = _DERIVATIVE_DELIVERY_ATTR_TO_TYPE.get(attributes[1])
        settlement_type = _DELIVERY_TYPE_TO_SETTLEMENT_TYPE.get(delivery_type)
        contract_style = _CONTRACT_STYLE_ATTR_TO_STYLE.get(attributes[2])
        underlying_security_type = _ASSET_CLASS_TO_SECURITY_TYPE.get(underlying_asset_class)
    elif category == "S":
        security_type = SecurityType.Swap
        instrument_type = InstrumentType.Swap
        swap_type = _SWAP_GROUP_TO_TYPE.get(group)
    elif category == "H":
        security_type = SecurityType.Option
        instrument_type = InstrumentType.Option
        underlying_asset_class = _COMPLEX_OPTION_GROUP_TO_ASSET_CLASS.get(group)
        underlying_security_type = _ASSET_CLASS_TO_SECURITY_TYPE.get(underlying_asset_class)
    elif category == "I":
        instrument_type = InstrumentType.Spot
        if group == "F":
            security_type = SecurityType.Currency
        elif group == "T":
            security_type = SecurityType.Commodity
            commodity_type = _SPOT_COMMODITY_ATTR_TO_TYPE.get(attributes[0])
    elif category == "J":
        security_type = SecurityType.Forward
        instrument_type = InstrumentType.Forward
        underlying_asset_class = _FORWARD_GROUP_TO_ASSET_CLASS.get(group)
        underlying_security_type = _ASSET_CLASS_TO_SECURITY_TYPE.get(underlying_asset_class)
    elif category == "L":
        security_type = SecurityType.Financing
        instrument_type = InstrumentType.Financing
        financing_type = _FINANCING_GROUP_TO_TYPE.get(group)
        delivery_type = _FINANCING_DELIVERY_ATTR_TO_TYPE.get(attributes[3])
        settlement_type = _DELIVERY_TYPE_TO_SETTLEMENT_TYPE.get(delivery_type)
    elif category == "K":
        security_type = SecurityType.Spread
        instrument_type = InstrumentType.Spread
        underlying_asset_class = _STRATEGY_GROUP_TO_ASSET_CLASS.get(group)
        underlying_security_type = _ASSET_CLASS_TO_SECURITY_TYPE.get(underlying_asset_class)
    elif category == "R":
        instrument_type = InstrumentType.Right
    elif category == "T":
        if group == "C":
            security_type = SecurityType.Currency
            instrument_type = InstrumentType.Spot
        elif group == "T":
            security_type = SecurityType.Commodity
            instrument_type = InstrumentType.Spot
        elif group == "I":
            security_type = SecurityType.Index
            instrument_type = InstrumentType.Spot
        elif group == "B":
            instrument_type = InstrumentType.Basket
        elif group == "D":
            security_type = SecurityType.Equity
            instrument_type = InstrumentType.Spot

    return CFIClassification(
        code=normalized,
        category=category,
        group=group,
        attributes=attributes,
        security_type=security_type,
        instrument_type=instrument_type,
        equity_type=equity_type,
        option_type=option_type,
        option_exercise_type=option_exercise_type,
        bond_type=bond_type,
        fund_type=fund_type,
        mutual_fund_endedness=mutual_fund_endedness,
        future_asset_class=future_asset_class,
        settlement_type=settlement_type,
        delivery_type=delivery_type,
        underlying_asset_class=underlying_asset_class,
        contract_style=contract_style,
        swap_type=swap_type,
        financing_type=financing_type,
        commodity_type=commodity_type,
        underlying_security_type=underlying_security_type,
    )


def build_cfi(
    *,
    security_type: SecurityType | str | None = None,
    equity_type: EquityType | str | None = None,
    option_type: OptionType | str | None = None,
    option_exercise_type: OptionExerciseType | str | None = None,
    bond_type: BondType | str | None = None,
    commodity_type: CommodityType | str | None = None,
    fund_type: FundType | str | None = None,
    financing_type: FinancingType | str | None = None,
    mutual_fund_endedness: MutualFundEndedness | str | None = None,
    future_asset_class: FutureAssetClass | str | None = None,
    settlement_type: SettlementType | str | None = None,
    delivery_type: DeliveryType | str | None = None,
    underlying_asset_class: UnderlyingAssetClass | str | None = None,
    contract_style: ContractStyle | str | None = None,
    swap_type: SwapType | str | None = None,
    underlying_security_type: SecurityType | str | None = None,
    category: str | None = None,
    group: str | None = None,
    attributes: str | tuple[str, str, str, str] | None = None,
) -> str:
    security_type = _coerce_enum(SecurityType, security_type, "security_type")
    equity_type = _coerce_enum(EquityType, equity_type, "equity_type")
    option_type = _coerce_enum(OptionType, option_type, "option_type")
    option_exercise_type = _coerce_enum(OptionExerciseType, option_exercise_type, "option_exercise_type")
    bond_type = _coerce_enum(BondType, bond_type, "bond_type")
    commodity_type = _coerce_enum(CommodityType, commodity_type, "commodity_type")
    fund_type = _coerce_enum(FundType, fund_type, "fund_type")
    financing_type = _coerce_enum(FinancingType, financing_type, "financing_type")
    mutual_fund_endedness = _coerce_enum(MutualFundEndedness, mutual_fund_endedness, "mutual_fund_endedness")
    future_asset_class = _coerce_enum(FutureAssetClass, future_asset_class, "future_asset_class")
    settlement_type = _coerce_enum(SettlementType, settlement_type, "settlement_type")
    delivery_type = _coerce_enum(DeliveryType, delivery_type, "delivery_type")
    underlying_asset_class = _coerce_enum(UnderlyingAssetClass, underlying_asset_class, "underlying_asset_class")
    contract_style = _coerce_enum(ContractStyle, contract_style, "contract_style")
    swap_type = _coerce_enum(SwapType, swap_type, "swap_type")
    underlying_security_type = _coerce_enum(SecurityType, underlying_security_type, "underlying_security_type")

    underlying_asset_class = _resolve_underlying_asset_class(underlying_asset_class, underlying_security_type)
    settlement_type, delivery_type = _resolve_delivery_fields(
        settlement_type,
        delivery_type,
    )

    if category is not None or group is not None or attributes is not None:
        if category is None or group is None:
            raise ValueError("category and group are required when building a raw CFI code")
        return f"{category.strip().upper()}{group.strip().upper()}{''.join(_normalize_cfi_attributes(attributes))}"

    if security_type is None:
        raise ValueError("security_type is required when category and group are not provided")

    if security_type == SecurityType.Equity:
        resolved_equity_type = equity_type if equity_type is not None else EquityType.Shares
        return f"E{_EQUITY_TYPE_TO_GROUP[resolved_equity_type]}XXXX"

    if security_type == SecurityType.Bond:
        resolved_bond_type = bond_type if bond_type is not None else BondType.Corporate
        if resolved_bond_type == BondType.Municipal:
            return "DNXXXX"
        if resolved_bond_type == BondType.Government:
            return "DBXTXX"
        return "DBXXXX"

    if security_type == SecurityType.Currency:
        return "IFXXXP"

    if security_type == SecurityType.Commodity:
        commodity_attr = _COMMODITY_TYPE_TO_SPOT_ATTR.get(commodity_type, "X")
        return f"IT{commodity_attr}XXX"

    if security_type == SecurityType.Fund:
        resolved_fund_type = fund_type if fund_type is not None else FundType.MutualFund
        if resolved_fund_type == FundType.ExchangeTradedFund:
            return "CEXXXX"
        if resolved_fund_type == FundType.RealEstateInvestmentTrust:
            return "CBXXXX"
        endedness_attr = "X"
        if mutual_fund_endedness == MutualFundEndedness.OpenEnded:
            endedness_attr = "O"
        elif mutual_fund_endedness == MutualFundEndedness.ClosedEnded:
            endedness_attr = "C"
        return f"CI{endedness_attr}XXX"

    if security_type == SecurityType.Option:
        if option_type is None:
            if underlying_asset_class is None:
                raise ValueError("option_type is required when building a listed option CFI")
            complex_group = _ASSET_CLASS_TO_COMPLEX_OPTION_GROUP.get(underlying_asset_class)
            if complex_group is None:
                raise NotImplementedError(
                    f"CFI complex option generation is not implemented for underlying asset class {underlying_asset_class.name}"
                )
            return f"H{complex_group}XXXX"
        exercise_attr = _OPTION_EXERCISE_TO_ATTR.get(option_exercise_type, "X")
        underlying_attr = _OPTION_CLASS_TO_ASSET_ATTR.get(underlying_asset_class, "X")
        delivery_attr = _DERIVATIVE_DELIVERY_TYPE_TO_ATTR.get(delivery_type, "X")
        style_attr = _CONTRACT_STYLE_TO_ATTR.get(contract_style, "X")
        return f"O{_OPTION_TYPE_TO_GROUP[option_type]}{exercise_attr}{underlying_attr}{delivery_attr}{style_attr}"

    # Perpetual futures share the ISO 10962 'F' (future) encoding with standard
    # futures; CFI does not distinguish the two.
    if security_type in (SecurityType.Future, SecurityType.PerpetualFuture):
        resolved_future_asset_class = future_asset_class if future_asset_class is not None else FutureAssetClass.Financial
        resolved_underlying_asset_class = underlying_asset_class
        if resolved_future_asset_class == FutureAssetClass.Commodity and resolved_underlying_asset_class is None:
            resolved_underlying_asset_class = {
                CommodityType.Agriculture: UnderlyingAssetClass.Agriculture,
            }.get(commodity_type)
        if resolved_future_asset_class == FutureAssetClass.Financial:
            underlying_attr = _FINANCIAL_FUTURE_CLASS_TO_ATTR.get(resolved_underlying_asset_class, "X")
        else:
            underlying_attr = _COMMODITY_FUTURE_CLASS_TO_ATTR.get(resolved_underlying_asset_class, "X")
        delivery_attr = _DERIVATIVE_DELIVERY_TYPE_TO_ATTR.get(delivery_type, "X")
        style_attr = _CONTRACT_STYLE_TO_ATTR.get(contract_style, "X")
        return f"F{_FUTURE_ASSET_CLASS_TO_GROUP[resolved_future_asset_class]}{underlying_attr}{delivery_attr}{style_attr}X"

    if security_type == SecurityType.Swap:
        if swap_type is None:
            raise ValueError("swap_type is required when building a swap CFI")
        return f"S{_SWAP_TYPE_TO_GROUP[swap_type]}XXXX"

    if security_type == SecurityType.Financing:
        if financing_type is None:
            raise ValueError("financing_type is required when building a financing CFI")
        delivery_attr = _FINANCING_DELIVERY_TYPE_TO_ATTR.get(delivery_type, "X")
        return f"L{_FINANCING_TYPE_TO_GROUP[financing_type]}XXX{delivery_attr}"

    if security_type == SecurityType.Forward:
        if underlying_asset_class is None:
            raise ValueError("underlying_asset_class or underlying_security_type is required when building a forward CFI")
        forward_group = _ASSET_CLASS_TO_FORWARD_GROUP.get(underlying_asset_class)
        if forward_group is None:
            raise NotImplementedError(f"CFI forward generation is not implemented for underlying asset class {underlying_asset_class.name}")
        return f"J{forward_group}XXXX"

    if security_type == SecurityType.Spread:
        if underlying_asset_class is None:
            raise ValueError("underlying_asset_class or underlying_security_type is required when building a spread CFI")
        strategy_group = _ASSET_CLASS_TO_STRATEGY_GROUP.get(underlying_asset_class)
        if strategy_group is None:
            raise NotImplementedError(f"CFI spread generation is not implemented for underlying asset class {underlying_asset_class.name}")
        return f"K{strategy_group}XXXX"

    if security_type == SecurityType.Index:
        return "TIXXXX"

    raise NotImplementedError(f"CFI generation is not implemented for security type {security_type.name}")


def build_cfi_from_classification(classification: CFIClassification) -> str:
    if not isinstance(classification, CFIClassification):
        raise TypeError("classification must be a CFIClassification")

    try:
        if classification.security_type is not None:
            return build_cfi(
                security_type=classification.security_type,
                equity_type=classification.equity_type,
                option_type=classification.option_type,
                option_exercise_type=classification.option_exercise_type,
                bond_type=classification.bond_type,
                commodity_type=classification.commodity_type,
                fund_type=classification.fund_type,
                financing_type=classification.financing_type,
                mutual_fund_endedness=classification.mutual_fund_endedness,
                future_asset_class=classification.future_asset_class,
                settlement_type=classification.settlement_type,
                delivery_type=classification.delivery_type,
                underlying_asset_class=classification.underlying_asset_class,
                contract_style=classification.contract_style,
                swap_type=classification.swap_type,
                underlying_security_type=classification.underlying_security_type,
            )
    except NotImplementedError:
        pass

    return build_cfi(
        category=classification.category,
        group=classification.group,
        attributes=classification.attributes,
    )


def validate_cfi_classification(classification: CFIClassification) -> CFIClassification:
    if not isinstance(classification, CFIClassification):
        raise TypeError("classification must be a CFIClassification")

    raw_code = build_cfi(
        category=classification.category,
        group=classification.group,
        attributes=classification.attributes,
    )
    structured_code = build_cfi_from_classification(classification)
    normalized_code = classification.code.strip().upper()

    if normalized_code != raw_code:
        raise ValueError(f"CFI classification code does not match derived code {raw_code}")
    if structured_code != raw_code:
        raise ValueError("CFI classification typed fields do not match category/group/attributes")

    return replace(
        classification,
        code=raw_code,
        category=raw_code[0],
        group=raw_code[1],
        attributes=tuple(raw_code[2:]),
    )


def _cfi_classification_to_code(self):
    return build_cfi_from_classification(self)


def _cfi_classification_validate(self):
    return validate_cfi_classification(self)


CFIClassification.to_code = _cfi_classification_to_code  # type: ignore[attr-defined]
CFIClassification.validate = _cfi_classification_validate  # type: ignore[attr-defined]
