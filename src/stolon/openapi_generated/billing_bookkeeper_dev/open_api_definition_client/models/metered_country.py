from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.developer_app_current_subscription import DeveloperAppCurrentSubscription


T = TypeVar("T", bound="MeteredCountry")


@_attrs_define
class MeteredCountry:
    """
    Attributes:
        id (Union[Unset, str]):
        amount (Union[Unset, int]):
        country (Union[Unset, str]):
        active (Union[Unset, bool]):
        app_metered (Union[Unset, DeveloperAppCurrentSubscription]):
    """

    id: Union[Unset, str] = UNSET
    amount: Union[Unset, int] = UNSET
    country: Union[Unset, str] = UNSET
    active: Union[Unset, bool] = UNSET
    app_metered: Union[Unset, "DeveloperAppCurrentSubscription"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        amount = self.amount

        country = self.country

        active = self.active

        app_metered: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.app_metered, Unset):
            app_metered = self.app_metered.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if country is not UNSET:
            field_dict["country"] = country
        if active is not UNSET:
            field_dict["active"] = active
        if app_metered is not UNSET:
            field_dict["appMetered"] = app_metered

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.developer_app_current_subscription import DeveloperAppCurrentSubscription

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        amount = d.pop("amount", UNSET)

        country = d.pop("country", UNSET)

        active = d.pop("active", UNSET)

        _app_metered = d.pop("appMetered", UNSET)
        app_metered: Union[Unset, DeveloperAppCurrentSubscription]
        if _app_metered and not isinstance(_app_metered, Unset):
            app_metered = DeveloperAppCurrentSubscription.from_dict(_app_metered)

        else:
            app_metered = UNSET

        metered_country = cls(
            id=id,
            amount=amount,
            country=country,
            active=active,
            app_metered=app_metered,
        )

        metered_country.additional_properties = d
        return metered_country

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
