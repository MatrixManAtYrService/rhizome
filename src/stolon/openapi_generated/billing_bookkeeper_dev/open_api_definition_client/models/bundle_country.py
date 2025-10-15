from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BundleCountry")


@_attrs_define
class BundleCountry:
    """
    Attributes:
        id (Union[Unset, str]):
        country (Union[Unset, str]):
        price (Union[Unset, int]):
        price_per_device (Union[Unset, int]):
    """

    id: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    price: Union[Unset, int] = UNSET
    price_per_device: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        country = self.country

        price = self.price

        price_per_device = self.price_per_device

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if country is not UNSET:
            field_dict["country"] = country
        if price is not UNSET:
            field_dict["price"] = price
        if price_per_device is not UNSET:
            field_dict["pricePerDevice"] = price_per_device

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        country = d.pop("country", UNSET)

        price = d.pop("price", UNSET)

        price_per_device = d.pop("pricePerDevice", UNSET)

        bundle_country = cls(
            id=id,
            country=country,
            price=price,
            price_per_device=price_per_device,
        )

        bundle_country.additional_properties = d
        return bundle_country

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
