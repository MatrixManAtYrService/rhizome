from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_fee_summary_total_by_fee_category_group_currency_totals import (
        ApiFeeSummaryTotalByFeeCategoryGroupCurrencyTotals,
    )


T = TypeVar("T", bound="ApiFeeSummaryTotalByFeeCategoryGroup")


@_attrs_define
class ApiFeeSummaryTotalByFeeCategoryGroup:
    """the fee details belonging to the fee category grouping

    Attributes:
        fee_category_group (Union[Unset, str]): defined fee category grouping value
        currency_totals (Union[Unset, list['ApiFeeSummaryTotalByFeeCategoryGroupCurrencyTotals']]): the total fee amount
            for the fee category grouping
    """

    fee_category_group: Union[Unset, str] = UNSET
    currency_totals: Union[Unset, list["ApiFeeSummaryTotalByFeeCategoryGroupCurrencyTotals"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fee_category_group = self.fee_category_group

        currency_totals: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.currency_totals, Unset):
            currency_totals = []
            for currency_totals_item_data in self.currency_totals:
                currency_totals_item = currency_totals_item_data.to_dict()
                currency_totals.append(currency_totals_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fee_category_group is not UNSET:
            field_dict["feeCategoryGroup"] = fee_category_group
        if currency_totals is not UNSET:
            field_dict["currencyTotals"] = currency_totals

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_fee_summary_total_by_fee_category_group_currency_totals import (
            ApiFeeSummaryTotalByFeeCategoryGroupCurrencyTotals,
        )

        d = dict(src_dict)
        fee_category_group = d.pop("feeCategoryGroup", UNSET)

        currency_totals = []
        _currency_totals = d.pop("currencyTotals", UNSET)
        for currency_totals_item_data in _currency_totals or []:
            currency_totals_item = ApiFeeSummaryTotalByFeeCategoryGroupCurrencyTotals.from_dict(
                currency_totals_item_data
            )

            currency_totals.append(currency_totals_item)

        api_fee_summary_total_by_fee_category_group = cls(
            fee_category_group=fee_category_group,
            currency_totals=currency_totals,
        )

        api_fee_summary_total_by_fee_category_group.additional_properties = d
        return api_fee_summary_total_by_fee_category_group

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
