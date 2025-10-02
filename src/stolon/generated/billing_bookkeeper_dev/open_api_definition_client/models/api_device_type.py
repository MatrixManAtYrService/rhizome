from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiDeviceType")


@_attrs_define
class ApiDeviceType:
    """
    Attributes:
        device_type (Union[Unset, str]): the device type, which is either the name of a device or a device group
        message_bundle_name (Union[Unset, str]): name or key used to lookup description or label in an internationalized
            message bundle
        clover_name (Union[Unset, str]): for devices, the internal Clover name assigned to the device
        serial_number_regex (Union[Unset, str]): for devices, the regular expression for matching against a device
            serial number
        equipment_code (Union[Unset, str]): for devices, the equipment code assigned to the device for boarding
        is_group (Union[Unset, bool]): indicates whether the device type is a device (false) or a device group (true)
        belongs_to_groups (Union[Unset, list[str]]): for devices, a list of device groups that the device belongs to
        devices_in_group (Union[Unset, list[str]]): for device groups, a list of devices that belong to the group
    """

    device_type: Union[Unset, str] = UNSET
    message_bundle_name: Union[Unset, str] = UNSET
    clover_name: Union[Unset, str] = UNSET
    serial_number_regex: Union[Unset, str] = UNSET
    equipment_code: Union[Unset, str] = UNSET
    is_group: Union[Unset, bool] = UNSET
    belongs_to_groups: Union[Unset, list[str]] = UNSET
    devices_in_group: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_type = self.device_type

        message_bundle_name = self.message_bundle_name

        clover_name = self.clover_name

        serial_number_regex = self.serial_number_regex

        equipment_code = self.equipment_code

        is_group = self.is_group

        belongs_to_groups: Union[Unset, list[str]] = UNSET
        if not isinstance(self.belongs_to_groups, Unset):
            belongs_to_groups = self.belongs_to_groups

        devices_in_group: Union[Unset, list[str]] = UNSET
        if not isinstance(self.devices_in_group, Unset):
            devices_in_group = self.devices_in_group

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if message_bundle_name is not UNSET:
            field_dict["messageBundleName"] = message_bundle_name
        if clover_name is not UNSET:
            field_dict["cloverName"] = clover_name
        if serial_number_regex is not UNSET:
            field_dict["serialNumberRegex"] = serial_number_regex
        if equipment_code is not UNSET:
            field_dict["equipmentCode"] = equipment_code
        if is_group is not UNSET:
            field_dict["isGroup"] = is_group
        if belongs_to_groups is not UNSET:
            field_dict["belongsToGroups"] = belongs_to_groups
        if devices_in_group is not UNSET:
            field_dict["devicesInGroup"] = devices_in_group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        device_type = d.pop("deviceType", UNSET)

        message_bundle_name = d.pop("messageBundleName", UNSET)

        clover_name = d.pop("cloverName", UNSET)

        serial_number_regex = d.pop("serialNumberRegex", UNSET)

        equipment_code = d.pop("equipmentCode", UNSET)

        is_group = d.pop("isGroup", UNSET)

        belongs_to_groups = cast(list[str], d.pop("belongsToGroups", UNSET))

        devices_in_group = cast(list[str], d.pop("devicesInGroup", UNSET))

        api_device_type = cls(
            device_type=device_type,
            message_bundle_name=message_bundle_name,
            clover_name=clover_name,
            serial_number_regex=serial_number_regex,
            equipment_code=equipment_code,
            is_group=is_group,
            belongs_to_groups=belongs_to_groups,
            devices_in_group=devices_in_group,
        )

        api_device_type.additional_properties = d
        return api_device_type

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
