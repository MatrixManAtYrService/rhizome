from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VaultedCard")


@_attrs_define
class VaultedCard:
    """Vaulted card which can be used for subsequent transactions

    Attributes:
        first6 (Union[Unset, str]): First six digits of the card number
        last4 (Union[Unset, str]): Last four digits of the card number
        cardholder_name (Union[Unset, str]): Name of cardholder
        expiration_date (Union[Unset, str]): Card expiration date
        token (Union[Unset, str]): Token for vaulted card
    """

    first6: Union[Unset, str] = UNSET
    last4: Union[Unset, str] = UNSET
    cardholder_name: Union[Unset, str] = UNSET
    expiration_date: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first6 = self.first6

        last4 = self.last4

        cardholder_name = self.cardholder_name

        expiration_date = self.expiration_date

        token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first6 is not UNSET:
            field_dict["first6"] = first6
        if last4 is not UNSET:
            field_dict["last4"] = last4
        if cardholder_name is not UNSET:
            field_dict["cardholderName"] = cardholder_name
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        first6 = d.pop("first6", UNSET)

        last4 = d.pop("last4", UNSET)

        cardholder_name = d.pop("cardholderName", UNSET)

        expiration_date = d.pop("expirationDate", UNSET)

        token = d.pop("token", UNSET)

        vaulted_card = cls(
            first6=first6,
            last4=last4,
            cardholder_name=cardholder_name,
            expiration_date=expiration_date,
            token=token,
        )

        vaulted_card.additional_properties = d
        return vaulted_card

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
