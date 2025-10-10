from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiCellularActionFeeRateSummary")


@_attrs_define
class ApiCellularActionFeeRateSummary:
    """Summary list

    Attributes:
        carrier (Union[Unset, str]): defined cellular carrier value
        fee_category (Union[Unset, str]): fee category value that cellular fee rate applies to
        fee_code (Union[Unset, str]): fee code value that cellular fee rate applies to
        currency (Union[Unset, str]): the currency of the fee rate Example: USD.
        short_desc (Union[Unset, str]): short description of fee code
        full_desc (Union[Unset, str]): full description of fee code
        per_item_amount (Union[Unset, float]): the per-item rate
        total_tax_amount (Union[Unset, float]): the total tax amount applied to the per-item amount
        tax_1_amount (Union[Unset, float]): the portion of the total tax amount that is for tax 1, typically Federal
            tax, GST, or VAT
        tax_2_amount (Union[Unset, float]): the portion of the total tax amount that is for tax 2, typically state or
            province tax
        tax_3_amount (Union[Unset, float]): the portion of the total tax amount that is for tax 3, typically county tax
        tax_4_amount (Union[Unset, float]): the portion of the total tax amount that is for tax 4, typically city or
            local tax
        total_tax_rate (Union[Unset, float]): The total of the tax rates applied.
        tax_1_rate (Union[Unset, float]): The portion of the total tax rate that is for tax 1, typically Federal tax,
            GST, or VAT.
        tax_2_rate (Union[Unset, float]): The portion of the total tax rate that is for tax 2, typically state or
            province tax.
        tax_3_rate (Union[Unset, float]): The portion of the total tax rate that is for tax 3, typically county tax.
        tax_4_rate (Union[Unset, float]): The portion of the total tax rate that is for tax 4, typically city or local
            tax.
        total_amount (Union[Unset, float]): the total amount including the fee amount (per-item amount) and taxes
    """

    carrier: Union[Unset, str] = UNSET
    fee_category: Union[Unset, str] = UNSET
    fee_code: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    short_desc: Union[Unset, str] = UNSET
    full_desc: Union[Unset, str] = UNSET
    per_item_amount: Union[Unset, float] = UNSET
    total_tax_amount: Union[Unset, float] = UNSET
    tax_1_amount: Union[Unset, float] = UNSET
    tax_2_amount: Union[Unset, float] = UNSET
    tax_3_amount: Union[Unset, float] = UNSET
    tax_4_amount: Union[Unset, float] = UNSET
    total_tax_rate: Union[Unset, float] = UNSET
    tax_1_rate: Union[Unset, float] = UNSET
    tax_2_rate: Union[Unset, float] = UNSET
    tax_3_rate: Union[Unset, float] = UNSET
    tax_4_rate: Union[Unset, float] = UNSET
    total_amount: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        carrier = self.carrier

        fee_category = self.fee_category

        fee_code = self.fee_code

        currency = self.currency

        short_desc = self.short_desc

        full_desc = self.full_desc

        per_item_amount = self.per_item_amount

        total_tax_amount = self.total_tax_amount

        tax_1_amount = self.tax_1_amount

        tax_2_amount = self.tax_2_amount

        tax_3_amount = self.tax_3_amount

        tax_4_amount = self.tax_4_amount

        total_tax_rate = self.total_tax_rate

        tax_1_rate = self.tax_1_rate

        tax_2_rate = self.tax_2_rate

        tax_3_rate = self.tax_3_rate

        tax_4_rate = self.tax_4_rate

        total_amount = self.total_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if carrier is not UNSET:
            field_dict["carrier"] = carrier
        if fee_category is not UNSET:
            field_dict["feeCategory"] = fee_category
        if fee_code is not UNSET:
            field_dict["feeCode"] = fee_code
        if currency is not UNSET:
            field_dict["currency"] = currency
        if short_desc is not UNSET:
            field_dict["shortDesc"] = short_desc
        if full_desc is not UNSET:
            field_dict["fullDesc"] = full_desc
        if per_item_amount is not UNSET:
            field_dict["perItemAmount"] = per_item_amount
        if total_tax_amount is not UNSET:
            field_dict["totalTaxAmount"] = total_tax_amount
        if tax_1_amount is not UNSET:
            field_dict["tax1Amount"] = tax_1_amount
        if tax_2_amount is not UNSET:
            field_dict["tax2Amount"] = tax_2_amount
        if tax_3_amount is not UNSET:
            field_dict["tax3Amount"] = tax_3_amount
        if tax_4_amount is not UNSET:
            field_dict["tax4Amount"] = tax_4_amount
        if total_tax_rate is not UNSET:
            field_dict["totalTaxRate"] = total_tax_rate
        if tax_1_rate is not UNSET:
            field_dict["tax1Rate"] = tax_1_rate
        if tax_2_rate is not UNSET:
            field_dict["tax2Rate"] = tax_2_rate
        if tax_3_rate is not UNSET:
            field_dict["tax3Rate"] = tax_3_rate
        if tax_4_rate is not UNSET:
            field_dict["tax4Rate"] = tax_4_rate
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        carrier = d.pop("carrier", UNSET)

        fee_category = d.pop("feeCategory", UNSET)

        fee_code = d.pop("feeCode", UNSET)

        currency = d.pop("currency", UNSET)

        short_desc = d.pop("shortDesc", UNSET)

        full_desc = d.pop("fullDesc", UNSET)

        per_item_amount = d.pop("perItemAmount", UNSET)

        total_tax_amount = d.pop("totalTaxAmount", UNSET)

        tax_1_amount = d.pop("tax1Amount", UNSET)

        tax_2_amount = d.pop("tax2Amount", UNSET)

        tax_3_amount = d.pop("tax3Amount", UNSET)

        tax_4_amount = d.pop("tax4Amount", UNSET)

        total_tax_rate = d.pop("totalTaxRate", UNSET)

        tax_1_rate = d.pop("tax1Rate", UNSET)

        tax_2_rate = d.pop("tax2Rate", UNSET)

        tax_3_rate = d.pop("tax3Rate", UNSET)

        tax_4_rate = d.pop("tax4Rate", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        api_cellular_action_fee_rate_summary = cls(
            carrier=carrier,
            fee_category=fee_category,
            fee_code=fee_code,
            currency=currency,
            short_desc=short_desc,
            full_desc=full_desc,
            per_item_amount=per_item_amount,
            total_tax_amount=total_tax_amount,
            tax_1_amount=tax_1_amount,
            tax_2_amount=tax_2_amount,
            tax_3_amount=tax_3_amount,
            tax_4_amount=tax_4_amount,
            total_tax_rate=total_tax_rate,
            tax_1_rate=tax_1_rate,
            tax_2_rate=tax_2_rate,
            tax_3_rate=tax_3_rate,
            tax_4_rate=tax_4_rate,
            total_amount=total_amount,
        )

        api_cellular_action_fee_rate_summary.additional_properties = d
        return api_cellular_action_fee_rate_summary

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
