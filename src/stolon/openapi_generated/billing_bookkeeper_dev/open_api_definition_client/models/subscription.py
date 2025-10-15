from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subscription_countries import SubscriptionCountries


T = TypeVar("T", bound="Subscription")


@_attrs_define
class Subscription:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        plan (Union[Unset, bool]): True if special zero cost app pricing for default app in custom service plans
        label (Union[Unset, str]): App subscription label
        subscription_countries (Union[Unset, SubscriptionCountries]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    plan: Union[Unset, bool] = UNSET
    label: Union[Unset, str] = UNSET
    subscription_countries: Union[Unset, "SubscriptionCountries"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        plan = self.plan

        label = self.label

        subscription_countries: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.subscription_countries, Unset):
            subscription_countries = self.subscription_countries.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if plan is not UNSET:
            field_dict["plan"] = plan
        if label is not UNSET:
            field_dict["label"] = label
        if subscription_countries is not UNSET:
            field_dict["subscriptionCountries"] = subscription_countries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subscription_countries import SubscriptionCountries

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        plan = d.pop("plan", UNSET)

        label = d.pop("label", UNSET)

        _subscription_countries = d.pop("subscriptionCountries", UNSET)
        subscription_countries: Union[Unset, SubscriptionCountries]
        if _subscription_countries and not isinstance(_subscription_countries, Unset):
            subscription_countries = SubscriptionCountries.from_dict(_subscription_countries)

        else:
            subscription_countries = UNSET

        subscription = cls(
            id=id,
            name=name,
            plan=plan,
            label=label,
            subscription_countries=subscription_countries,
        )

        subscription.additional_properties = d
        return subscription

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
