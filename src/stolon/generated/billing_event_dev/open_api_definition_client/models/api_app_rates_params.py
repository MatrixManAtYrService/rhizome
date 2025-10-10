import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiAppRatesParams")


@_attrs_define
class ApiAppRatesParams:
    """
    Attributes:
        developer_uuids (Union[Unset, list[str]]): An array of developer uuids from COS to generate app rates events for
        app_uuids (Union[Unset, list[str]]): An array of developer app uuids from COS to generate app rates events for
        effective_date_time_override (Union[Unset, datetime.datetime]): An optional date/time that can be used to
            override the effective date/time used in the billing event.  The default effectiveDateTime is the createdTime of
            the app. Example: 2020-12-31T23:59:59.123456Z.
    """

    developer_uuids: Union[Unset, list[str]] = UNSET
    app_uuids: Union[Unset, list[str]] = UNSET
    effective_date_time_override: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        developer_uuids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.developer_uuids, Unset):
            developer_uuids = self.developer_uuids

        app_uuids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.app_uuids, Unset):
            app_uuids = self.app_uuids

        effective_date_time_override: Union[Unset, str] = UNSET
        if not isinstance(self.effective_date_time_override, Unset):
            effective_date_time_override = self.effective_date_time_override.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if developer_uuids is not UNSET:
            field_dict["developerUuids"] = developer_uuids
        if app_uuids is not UNSET:
            field_dict["appUuids"] = app_uuids
        if effective_date_time_override is not UNSET:
            field_dict["effectiveDateTimeOverride"] = effective_date_time_override

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        developer_uuids = cast(list[str], d.pop("developerUuids", UNSET))

        app_uuids = cast(list[str], d.pop("appUuids", UNSET))

        _effective_date_time_override = d.pop("effectiveDateTimeOverride", UNSET)
        effective_date_time_override: Union[Unset, datetime.datetime]
        if _effective_date_time_override and not isinstance(_effective_date_time_override, Unset):
            effective_date_time_override = isoparse(_effective_date_time_override)

        else:
            effective_date_time_override = UNSET

        api_app_rates_params = cls(
            developer_uuids=developer_uuids,
            app_uuids=app_uuids,
            effective_date_time_override=effective_date_time_override,
        )

        api_app_rates_params.additional_properties = d
        return api_app_rates_params

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
