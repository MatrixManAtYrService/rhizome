from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiDeviceInfo")


@_attrs_define
class ApiDeviceInfo:
    """details for devices for which this device pricing data applies

    Attributes:
        device_type (Union[Unset, str]): the device type
        clover_name (Union[Unset, str]): for devices, the internal Clover name assigned to the device
        message_bundle_name (Union[Unset, str]): name or key used to lookup description or label in an internationalized
            message bundle
        serial_number_regex (Union[Unset, str]): the regular expression for matching against a device serial number
        equipment_code (Union[Unset, str]): the equipment code assigned to the device for boarding
    """

    device_type: Union[Unset, str] = UNSET
    clover_name: Union[Unset, str] = UNSET
    message_bundle_name: Union[Unset, str] = UNSET
    serial_number_regex: Union[Unset, str] = UNSET
    equipment_code: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_type = self.device_type

        clover_name = self.clover_name

        message_bundle_name = self.message_bundle_name

        serial_number_regex = self.serial_number_regex

        equipment_code = self.equipment_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if clover_name is not UNSET:
            field_dict["cloverName"] = clover_name
        if message_bundle_name is not UNSET:
            field_dict["messageBundleName"] = message_bundle_name
        if serial_number_regex is not UNSET:
            field_dict["serialNumberRegex"] = serial_number_regex
        if equipment_code is not UNSET:
            field_dict["equipmentCode"] = equipment_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        device_type = d.pop("deviceType", UNSET)

        clover_name = d.pop("cloverName", UNSET)

        message_bundle_name = d.pop("messageBundleName", UNSET)

        serial_number_regex = d.pop("serialNumberRegex", UNSET)

        equipment_code = d.pop("equipmentCode", UNSET)

        api_device_info = cls(
            device_type=device_type,
            clover_name=clover_name,
            message_bundle_name=message_bundle_name,
            serial_number_regex=serial_number_regex,
            equipment_code=equipment_code,
        )

        api_device_info.additional_properties = d
        return api_device_info

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
