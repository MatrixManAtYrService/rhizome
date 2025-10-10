from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bundle_countries import BundleCountries


T = TypeVar("T", bound="AppBundle")


@_attrs_define
class AppBundle:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        price (Union[Unset, int]):
        price_per_device (Union[Unset, int]):
        bundle_countries (Union[Unset, BundleCountries]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    price: Union[Unset, int] = UNSET
    price_per_device: Union[Unset, int] = UNSET
    bundle_countries: Union[Unset, "BundleCountries"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        price = self.price

        price_per_device = self.price_per_device

        bundle_countries: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bundle_countries, Unset):
            bundle_countries = self.bundle_countries.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if price is not UNSET:
            field_dict["price"] = price
        if price_per_device is not UNSET:
            field_dict["pricePerDevice"] = price_per_device
        if bundle_countries is not UNSET:
            field_dict["bundleCountries"] = bundle_countries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bundle_countries import BundleCountries

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        price = d.pop("price", UNSET)

        price_per_device = d.pop("pricePerDevice", UNSET)

        _bundle_countries = d.pop("bundleCountries", UNSET)
        bundle_countries: Union[Unset, BundleCountries]
        if _bundle_countries and not isinstance(_bundle_countries, Unset):
            bundle_countries = BundleCountries.from_dict(_bundle_countries)

        else:
            bundle_countries = UNSET

        app_bundle = cls(
            id=id,
            name=name,
            price=price,
            price_per_device=price_per_device,
            bundle_countries=bundle_countries,
        )

        app_bundle.additional_properties = d
        return app_bundle

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
