from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiSubscriptionCurrencyRate")


@_attrs_define
class ApiSubscriptionCurrencyRate:
    """rates for the subscription level broken down by currency

    Attributes:
        currency (Union[Unset, str]): 3-letter currency code Example: USD.
        cost (Union[Unset, float]): the per item (usually monthly) cost of the subscription.
    """

    currency: Union[Unset, str] = UNSET
    cost: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        cost = self.cost

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency is not UNSET:
            field_dict["currency"] = currency
        if cost is not UNSET:
            field_dict["cost"] = cost

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency = d.pop("currency", UNSET)

        cost = d.pop("cost", UNSET)

        api_subscription_currency_rate = cls(
            currency=currency,
            cost=cost,
        )

        api_subscription_currency_rate.additional_properties = d
        return api_subscription_currency_rate

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
