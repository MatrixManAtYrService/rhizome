from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_subscription_currency_rate import ApiSubscriptionCurrencyRate


T = TypeVar("T", bound="ApiSubscriptionRate")


@_attrs_define
class ApiSubscriptionRate:
    """subscription rates for the app

    Attributes:
        app_sub_uuid (Union[Unset, str]): 13-character UUID assigned to the app subscription level
        app_sub_name (Union[Unset, str]): name of the subscription level
        has_trial (Union[Unset, bool]): does the subscription level have a trial
        rates (Union[Unset, list['ApiSubscriptionCurrencyRate']]): rates for the subscription level broken down by
            currency
    """

    app_sub_uuid: Union[Unset, str] = UNSET
    app_sub_name: Union[Unset, str] = UNSET
    has_trial: Union[Unset, bool] = UNSET
    rates: Union[Unset, list["ApiSubscriptionCurrencyRate"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_sub_uuid = self.app_sub_uuid

        app_sub_name = self.app_sub_name

        has_trial = self.has_trial

        rates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.rates, Unset):
            rates = []
            for rates_item_data in self.rates:
                rates_item = rates_item_data.to_dict()
                rates.append(rates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_sub_uuid is not UNSET:
            field_dict["appSubUuid"] = app_sub_uuid
        if app_sub_name is not UNSET:
            field_dict["appSubName"] = app_sub_name
        if has_trial is not UNSET:
            field_dict["hasTrial"] = has_trial
        if rates is not UNSET:
            field_dict["rates"] = rates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_subscription_currency_rate import ApiSubscriptionCurrencyRate

        d = dict(src_dict)
        app_sub_uuid = d.pop("appSubUuid", UNSET)

        app_sub_name = d.pop("appSubName", UNSET)

        has_trial = d.pop("hasTrial", UNSET)

        rates = []
        _rates = d.pop("rates", UNSET)
        for rates_item_data in _rates or []:
            rates_item = ApiSubscriptionCurrencyRate.from_dict(rates_item_data)

            rates.append(rates_item)

        api_subscription_rate = cls(
            app_sub_uuid=app_sub_uuid,
            app_sub_name=app_sub_name,
            has_trial=has_trial,
            rates=rates,
        )

        api_subscription_rate.additional_properties = d
        return api_subscription_rate

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
