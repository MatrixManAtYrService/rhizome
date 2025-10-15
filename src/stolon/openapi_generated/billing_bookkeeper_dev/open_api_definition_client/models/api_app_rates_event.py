import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_app_rates_event_party import ApiAppRatesEventParty
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_metered_rate import ApiMeteredRate
    from ..models.api_subscription_rate import ApiSubscriptionRate


T = TypeVar("T", bound="ApiAppRatesEvent")


@_attrs_define
class ApiAppRatesEvent:
    """app rates events

    Attributes:
        code (Union[Unset, str]): app subscription event code
        effective_date_time (Union[Unset, datetime.datetime]): date and time that the event is effective Example:
            2020-12-31T23:59:59.123456Z.
        developer_uuid (Union[Unset, str]): 13-character UUID assigned to the developer
        developer_name (Union[Unset, str]): the name of the developer
        vendor_code (Union[Unset, str]): the vendor code of the developer
        gl_code (Union[Unset, str]): the GL code of the developer
        dev_app_uuid (Union[Unset, str]): 13-character UUID assigned to the developer app
        app_name (Union[Unset, str]): the name of the app
        party (Union[Unset, ApiAppRatesEventParty]):
        subscription_rates (Union[Unset, list['ApiSubscriptionRate']]): subscription rates for the app
        metered_rates (Union[Unset, list['ApiMeteredRate']]): metered rates for the app
    """

    code: Union[Unset, str] = UNSET
    effective_date_time: Union[Unset, datetime.datetime] = UNSET
    developer_uuid: Union[Unset, str] = UNSET
    developer_name: Union[Unset, str] = UNSET
    vendor_code: Union[Unset, str] = UNSET
    gl_code: Union[Unset, str] = UNSET
    dev_app_uuid: Union[Unset, str] = UNSET
    app_name: Union[Unset, str] = UNSET
    party: Union[Unset, ApiAppRatesEventParty] = UNSET
    subscription_rates: Union[Unset, list["ApiSubscriptionRate"]] = UNSET
    metered_rates: Union[Unset, list["ApiMeteredRate"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        effective_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.effective_date_time, Unset):
            effective_date_time = self.effective_date_time.isoformat()

        developer_uuid = self.developer_uuid

        developer_name = self.developer_name

        vendor_code = self.vendor_code

        gl_code = self.gl_code

        dev_app_uuid = self.dev_app_uuid

        app_name = self.app_name

        party: Union[Unset, str] = UNSET
        if not isinstance(self.party, Unset):
            party = self.party.value

        subscription_rates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.subscription_rates, Unset):
            subscription_rates = []
            for subscription_rates_item_data in self.subscription_rates:
                subscription_rates_item = subscription_rates_item_data.to_dict()
                subscription_rates.append(subscription_rates_item)

        metered_rates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.metered_rates, Unset):
            metered_rates = []
            for metered_rates_item_data in self.metered_rates:
                metered_rates_item = metered_rates_item_data.to_dict()
                metered_rates.append(metered_rates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if effective_date_time is not UNSET:
            field_dict["effectiveDateTime"] = effective_date_time
        if developer_uuid is not UNSET:
            field_dict["developerUuid"] = developer_uuid
        if developer_name is not UNSET:
            field_dict["developerName"] = developer_name
        if vendor_code is not UNSET:
            field_dict["vendorCode"] = vendor_code
        if gl_code is not UNSET:
            field_dict["glCode"] = gl_code
        if dev_app_uuid is not UNSET:
            field_dict["devAppUuid"] = dev_app_uuid
        if app_name is not UNSET:
            field_dict["appName"] = app_name
        if party is not UNSET:
            field_dict["party"] = party
        if subscription_rates is not UNSET:
            field_dict["subscriptionRates"] = subscription_rates
        if metered_rates is not UNSET:
            field_dict["meteredRates"] = metered_rates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_metered_rate import ApiMeteredRate
        from ..models.api_subscription_rate import ApiSubscriptionRate

        d = dict(src_dict)
        code = d.pop("code", UNSET)

        _effective_date_time = d.pop("effectiveDateTime", UNSET)
        effective_date_time: Union[Unset, datetime.datetime]
        if _effective_date_time and not isinstance(_effective_date_time, Unset):
            effective_date_time = isoparse(_effective_date_time)

        else:
            effective_date_time = UNSET

        developer_uuid = d.pop("developerUuid", UNSET)

        developer_name = d.pop("developerName", UNSET)

        vendor_code = d.pop("vendorCode", UNSET)

        gl_code = d.pop("glCode", UNSET)

        dev_app_uuid = d.pop("devAppUuid", UNSET)

        app_name = d.pop("appName", UNSET)

        _party = d.pop("party", UNSET)
        party: Union[Unset, ApiAppRatesEventParty]
        if _party and not isinstance(_party, Unset):
            party = ApiAppRatesEventParty(_party)

        else:
            party = UNSET

        subscription_rates = []
        _subscription_rates = d.pop("subscriptionRates", UNSET)
        for subscription_rates_item_data in _subscription_rates or []:
            subscription_rates_item = ApiSubscriptionRate.from_dict(subscription_rates_item_data)

            subscription_rates.append(subscription_rates_item)

        metered_rates = []
        _metered_rates = d.pop("meteredRates", UNSET)
        for metered_rates_item_data in _metered_rates or []:
            metered_rates_item = ApiMeteredRate.from_dict(metered_rates_item_data)

            metered_rates.append(metered_rates_item)

        api_app_rates_event = cls(
            code=code,
            effective_date_time=effective_date_time,
            developer_uuid=developer_uuid,
            developer_name=developer_name,
            vendor_code=vendor_code,
            gl_code=gl_code,
            dev_app_uuid=dev_app_uuid,
            app_name=app_name,
            party=party,
            subscription_rates=subscription_rates,
            metered_rates=metered_rates,
        )

        api_app_rates_event.additional_properties = d
        return api_app_rates_event

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
