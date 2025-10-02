import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_plan_device import ApiPlanDevice
    from ..models.api_plan_modifier import ApiPlanModifier


T = TypeVar("T", bound="ApiPlanEvent")


@_attrs_define
class ApiPlanEvent:
    """plan events

    Attributes:
        code (Union[Unset, str]): plan event code
        effective_date_time (Union[Unset, datetime.datetime]): date and time that the event is effective Example:
            2020-12-31T23:59:59.123456Z.
        merch_uuid (Union[Unset, str]): 13-character UUID assigned to the merchant
        merch_plan_uuid (Union[Unset, str]): 13-character UUID assigned to the merchant plan
        plan_mods (Union[Unset, list['ApiPlanModifier']]): plan event modifiers
        devices (Union[Unset, list['ApiPlanDevice']]): devices
    """

    code: Union[Unset, str] = UNSET
    effective_date_time: Union[Unset, datetime.datetime] = UNSET
    merch_uuid: Union[Unset, str] = UNSET
    merch_plan_uuid: Union[Unset, str] = UNSET
    plan_mods: Union[Unset, list["ApiPlanModifier"]] = UNSET
    devices: Union[Unset, list["ApiPlanDevice"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        effective_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.effective_date_time, Unset):
            effective_date_time = self.effective_date_time.isoformat()

        merch_uuid = self.merch_uuid

        merch_plan_uuid = self.merch_plan_uuid

        plan_mods: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.plan_mods, Unset):
            plan_mods = []
            for plan_mods_item_data in self.plan_mods:
                plan_mods_item = plan_mods_item_data.to_dict()
                plan_mods.append(plan_mods_item)

        devices: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.devices, Unset):
            devices = []
            for devices_item_data in self.devices:
                devices_item = devices_item_data.to_dict()
                devices.append(devices_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if effective_date_time is not UNSET:
            field_dict["effectiveDateTime"] = effective_date_time
        if merch_uuid is not UNSET:
            field_dict["merchUuid"] = merch_uuid
        if merch_plan_uuid is not UNSET:
            field_dict["merchPlanUuid"] = merch_plan_uuid
        if plan_mods is not UNSET:
            field_dict["planMods"] = plan_mods
        if devices is not UNSET:
            field_dict["devices"] = devices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_plan_device import ApiPlanDevice
        from ..models.api_plan_modifier import ApiPlanModifier

        d = dict(src_dict)
        code = d.pop("code", UNSET)

        _effective_date_time = d.pop("effectiveDateTime", UNSET)
        effective_date_time: Union[Unset, datetime.datetime]
        if isinstance(_effective_date_time, Unset):
            effective_date_time = UNSET
        else:
            effective_date_time = isoparse(_effective_date_time)

        merch_uuid = d.pop("merchUuid", UNSET)

        merch_plan_uuid = d.pop("merchPlanUuid", UNSET)

        plan_mods = []
        _plan_mods = d.pop("planMods", UNSET)
        for plan_mods_item_data in _plan_mods or []:
            plan_mods_item = ApiPlanModifier.from_dict(plan_mods_item_data)

            plan_mods.append(plan_mods_item)

        devices = []
        _devices = d.pop("devices", UNSET)
        for devices_item_data in _devices or []:
            devices_item = ApiPlanDevice.from_dict(devices_item_data)

            devices.append(devices_item)

        api_plan_event = cls(
            code=code,
            effective_date_time=effective_date_time,
            merch_uuid=merch_uuid,
            merch_plan_uuid=merch_plan_uuid,
            plan_mods=plan_mods,
            devices=devices,
        )

        api_plan_event.additional_properties = d
        return api_plan_event

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
