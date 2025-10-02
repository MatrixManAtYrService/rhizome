from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiFeeSummaryTotalByFeeCategoryGroupCurrencyTotals")


@_attrs_define
class ApiFeeSummaryTotalByFeeCategoryGroupCurrencyTotals:
    """the total fee amount for the fee category grouping

    Attributes:
        fee_amount (Union[Unset, float]): the total fee amount billed
        currency (Union[Unset, str]): the currency of the fee summary Example: USD.
    """

    fee_amount: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fee_amount = self.fee_amount

        currency = self.currency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fee_amount is not UNSET:
            field_dict["feeAmount"] = fee_amount
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fee_amount = d.pop("feeAmount", UNSET)

        currency = d.pop("currency", UNSET)

        api_fee_summary_total_by_fee_category_group_currency_totals = cls(
            fee_amount=fee_amount,
            currency=currency,
        )

        api_fee_summary_total_by_fee_category_group_currency_totals.additional_properties = d
        return api_fee_summary_total_by_fee_category_group_currency_totals

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
