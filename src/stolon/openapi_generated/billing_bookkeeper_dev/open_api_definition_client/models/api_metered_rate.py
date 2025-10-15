from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_metered_currency_rate import ApiMeteredCurrencyRate


T = TypeVar("T", bound="ApiMeteredRate")


@_attrs_define
class ApiMeteredRate:
    """metered rates for the app

    Attributes:
        app_metered_uuid (Union[Unset, str]): 13-character UUID of the app metered activity
        app_metered_name (Union[Unset, str]): name of the metered event
        rates (Union[Unset, list['ApiMeteredCurrencyRate']]): rates for the metered event broken down by currency
    """

    app_metered_uuid: Union[Unset, str] = UNSET
    app_metered_name: Union[Unset, str] = UNSET
    rates: Union[Unset, list["ApiMeteredCurrencyRate"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_metered_uuid = self.app_metered_uuid

        app_metered_name = self.app_metered_name

        rates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.rates, Unset):
            rates = []
            for rates_item_data in self.rates:
                rates_item = rates_item_data.to_dict()
                rates.append(rates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_metered_uuid is not UNSET:
            field_dict["appMeteredUuid"] = app_metered_uuid
        if app_metered_name is not UNSET:
            field_dict["appMeteredName"] = app_metered_name
        if rates is not UNSET:
            field_dict["rates"] = rates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_metered_currency_rate import ApiMeteredCurrencyRate

        d = dict(src_dict)
        app_metered_uuid = d.pop("appMeteredUuid", UNSET)

        app_metered_name = d.pop("appMeteredName", UNSET)

        rates = []
        _rates = d.pop("rates", UNSET)
        for rates_item_data in _rates or []:
            rates_item = ApiMeteredCurrencyRate.from_dict(rates_item_data)

            rates.append(rates_item)

        api_metered_rate = cls(
            app_metered_uuid=app_metered_uuid,
            app_metered_name=app_metered_name,
            rates=rates,
        )

        api_metered_rate.additional_properties = d
        return api_metered_rate

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
