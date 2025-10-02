from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiCurrencyAmount")


@_attrs_define
class ApiCurrencyAmount:
    """estimated fee totals by currency

    Attributes:
        currency (Union[Unset, str]): 3-letter currency code Example: USD.
        amount (Union[Unset, float]): the amount that corresponds to the currency
    """

    currency: Union[Unset, str] = UNSET
    amount: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        amount = self.amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency is not UNSET:
            field_dict["currency"] = currency
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency = d.pop("currency", UNSET)

        amount = d.pop("amount", UNSET)

        api_currency_amount = cls(
            currency=currency,
            amount=amount,
        )

        api_currency_amount.additional_properties = d
        return api_currency_amount

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
