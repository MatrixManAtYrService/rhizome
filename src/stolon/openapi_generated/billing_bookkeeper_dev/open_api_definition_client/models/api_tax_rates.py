from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiTaxRates")


@_attrs_define
class ApiTaxRates:
    """
    Attributes:
        total_tax_rate (Union[Unset, float]): The total of the tax rates applied.
        tax_1_rate (Union[Unset, float]): The portion of the total tax rate that is for tax 1, typically Federal tax,
            GST, or VAT.
        tax_2_rate (Union[Unset, float]): The portion of the total tax rate that is for tax 2, typically state or
            province tax.
        tax_3_rate (Union[Unset, float]): The portion of the total tax rate that is for tax 3, typically county tax.
        tax_4_rate (Union[Unset, float]): The portion of the total tax rate that is for tax 4, typically city or local
            tax.
    """

    total_tax_rate: Union[Unset, float] = UNSET
    tax_1_rate: Union[Unset, float] = UNSET
    tax_2_rate: Union[Unset, float] = UNSET
    tax_3_rate: Union[Unset, float] = UNSET
    tax_4_rate: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_tax_rate = self.total_tax_rate

        tax_1_rate = self.tax_1_rate

        tax_2_rate = self.tax_2_rate

        tax_3_rate = self.tax_3_rate

        tax_4_rate = self.tax_4_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_tax_rate = d.pop("totalTaxRate", UNSET)

        tax_1_rate = d.pop("tax1Rate", UNSET)

        tax_2_rate = d.pop("tax2Rate", UNSET)

        tax_3_rate = d.pop("tax3Rate", UNSET)

        tax_4_rate = d.pop("tax4Rate", UNSET)

        api_tax_rates = cls(
            total_tax_rate=total_tax_rate,
            tax_1_rate=tax_1_rate,
            tax_2_rate=tax_2_rate,
            tax_3_rate=tax_3_rate,
            tax_4_rate=tax_4_rate,
        )

        api_tax_rates.additional_properties = d
        return api_tax_rates

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
