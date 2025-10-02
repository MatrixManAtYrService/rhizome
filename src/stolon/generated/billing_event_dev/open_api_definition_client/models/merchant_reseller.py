from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MerchantReseller")


@_attrs_define
class MerchantReseller:
    """
    Attributes:
        id (Union[Unset, str]):
        support_phone (Union[Unset, str]):
        support_email (Union[Unset, str]):
        force_phone (Union[Unset, bool]):
    """

    id: Union[Unset, str] = UNSET
    support_phone: Union[Unset, str] = UNSET
    support_email: Union[Unset, str] = UNSET
    force_phone: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        support_phone = self.support_phone

        support_email = self.support_email

        force_phone = self.force_phone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if support_phone is not UNSET:
            field_dict["supportPhone"] = support_phone
        if support_email is not UNSET:
            field_dict["supportEmail"] = support_email
        if force_phone is not UNSET:
            field_dict["forcePhone"] = force_phone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        support_phone = d.pop("supportPhone", UNSET)

        support_email = d.pop("supportEmail", UNSET)

        force_phone = d.pop("forcePhone", UNSET)

        merchant_reseller = cls(
            id=id,
            support_phone=support_phone,
            support_email=support_email,
            force_phone=force_phone,
        )

        merchant_reseller.additional_properties = d
        return merchant_reseller

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
