from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.developer_app_current_subscription import DeveloperAppCurrentSubscription


T = TypeVar("T", bound="SubscriptionCountry")


@_attrs_define
class SubscriptionCountry:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        amount (Union[Unset, int]):
        country (Union[Unset, str]):
        description (Union[Unset, str]):
        active (Union[Unset, bool]):
        app_subscription (Union[Unset, DeveloperAppCurrentSubscription]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    amount: Union[Unset, int] = UNSET
    country: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    active: Union[Unset, bool] = UNSET
    app_subscription: Union[Unset, "DeveloperAppCurrentSubscription"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        amount = self.amount

        country = self.country

        description = self.description

        active = self.active

        app_subscription: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.app_subscription, Unset):
            app_subscription = self.app_subscription.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if amount is not UNSET:
            field_dict["amount"] = amount
        if country is not UNSET:
            field_dict["country"] = country
        if description is not UNSET:
            field_dict["description"] = description
        if active is not UNSET:
            field_dict["active"] = active
        if app_subscription is not UNSET:
            field_dict["appSubscription"] = app_subscription

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.developer_app_current_subscription import DeveloperAppCurrentSubscription

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        amount = d.pop("amount", UNSET)

        country = d.pop("country", UNSET)

        description = d.pop("description", UNSET)

        active = d.pop("active", UNSET)

        _app_subscription = d.pop("appSubscription", UNSET)
        app_subscription: Union[Unset, DeveloperAppCurrentSubscription]
        if _app_subscription and not isinstance(_app_subscription, Unset):
            app_subscription = DeveloperAppCurrentSubscription.from_dict(_app_subscription)

        else:
            app_subscription = UNSET

        subscription_country = cls(
            id=id,
            name=name,
            amount=amount,
            country=country,
            description=description,
            active=active,
            app_subscription=app_subscription,
        )

        subscription_country.additional_properties = d
        return subscription_country

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
