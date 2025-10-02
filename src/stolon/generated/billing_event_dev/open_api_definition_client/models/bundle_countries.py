from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bundle_country import BundleCountry


T = TypeVar("T", bound="BundleCountries")


@_attrs_define
class BundleCountries:
    """
    Attributes:
        elements (Union[Unset, list['BundleCountry']]):
    """

    elements: Union[Unset, list["BundleCountry"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        elements: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.elements, Unset):
            elements = []
            for elements_item_data in self.elements:
                elements_item = elements_item_data.to_dict()
                elements.append(elements_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if elements is not UNSET:
            field_dict["elements"] = elements

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bundle_country import BundleCountry

        d = dict(src_dict)
        elements = []
        _elements = d.pop("elements", UNSET)
        for elements_item_data in _elements or []:
            elements_item = BundleCountry.from_dict(elements_item_data)

            elements.append(elements_item)

        bundle_countries = cls(
            elements=elements,
        )

        bundle_countries.additional_properties = d
        return bundle_countries

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
