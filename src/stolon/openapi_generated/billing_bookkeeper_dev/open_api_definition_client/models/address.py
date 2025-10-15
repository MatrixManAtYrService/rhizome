from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Address")


@_attrs_define
class Address:
    """
    Attributes:
        address1 (Union[Unset, str]):
        address2 (Union[Unset, str]):
        address3 (Union[Unset, str]):
        city (Union[Unset, str]):
        country (Union[Unset, str]):
        phone_number (Union[Unset, str]):
        state (Union[Unset, str]):
        zip_ (Union[Unset, str]):
    """

    address1: Union[Unset, str] = UNSET
    address2: Union[Unset, str] = UNSET
    address3: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    zip_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address1 = self.address1

        address2 = self.address2

        address3 = self.address3

        city = self.city

        country = self.country

        phone_number = self.phone_number

        state = self.state

        zip_ = self.zip_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address1 is not UNSET:
            field_dict["address1"] = address1
        if address2 is not UNSET:
            field_dict["address2"] = address2
        if address3 is not UNSET:
            field_dict["address3"] = address3
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if state is not UNSET:
            field_dict["state"] = state
        if zip_ is not UNSET:
            field_dict["zip"] = zip_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address1 = d.pop("address1", UNSET)

        address2 = d.pop("address2", UNSET)

        address3 = d.pop("address3", UNSET)

        city = d.pop("city", UNSET)

        country = d.pop("country", UNSET)

        phone_number = d.pop("phoneNumber", UNSET)

        state = d.pop("state", UNSET)

        zip_ = d.pop("zip", UNSET)

        address = cls(
            address1=address1,
            address2=address2,
            address3=address3,
            city=city,
            country=country,
            phone_number=phone_number,
            state=state,
            zip_=zip_,
        )

        address.additional_properties = d
        return address

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
