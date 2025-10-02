from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiCellularModifier")


@_attrs_define
class ApiCellularModifier:
    """cellular event modifiers

    Attributes:
        mod_type (Union[Unset, str]): type of cellular modifier
        ref (Union[Unset, str]): reference
        num_units (Union[Unset, int]): the number of billable units
        basis_units (Union[Unset, int]): the number of basis units
        basis_amt (Union[Unset, float]): the basis amount
        basis_currency (Union[Unset, str]): 3-letter currency code Example: USD.
    """

    mod_type: Union[Unset, str] = UNSET
    ref: Union[Unset, str] = UNSET
    num_units: Union[Unset, int] = UNSET
    basis_units: Union[Unset, int] = UNSET
    basis_amt: Union[Unset, float] = UNSET
    basis_currency: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mod_type = self.mod_type

        ref = self.ref

        num_units = self.num_units

        basis_units = self.basis_units

        basis_amt = self.basis_amt

        basis_currency = self.basis_currency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mod_type is not UNSET:
            field_dict["modType"] = mod_type
        if ref is not UNSET:
            field_dict["ref"] = ref
        if num_units is not UNSET:
            field_dict["numUnits"] = num_units
        if basis_units is not UNSET:
            field_dict["basisUnits"] = basis_units
        if basis_amt is not UNSET:
            field_dict["basisAmt"] = basis_amt
        if basis_currency is not UNSET:
            field_dict["basisCurrency"] = basis_currency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mod_type = d.pop("modType", UNSET)

        ref = d.pop("ref", UNSET)

        num_units = d.pop("numUnits", UNSET)

        basis_units = d.pop("basisUnits", UNSET)

        basis_amt = d.pop("basisAmt", UNSET)

        basis_currency = d.pop("basisCurrency", UNSET)

        api_cellular_modifier = cls(
            mod_type=mod_type,
            ref=ref,
            num_units=num_units,
            basis_units=basis_units,
            basis_amt=basis_amt,
            basis_currency=basis_currency,
        )

        api_cellular_modifier.additional_properties = d
        return api_cellular_modifier

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
