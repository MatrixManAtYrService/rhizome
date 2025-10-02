from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_plan_device_modifier import ApiPlanDeviceModifier


T = TypeVar("T", bound="ApiPlanDevice")


@_attrs_define
class ApiPlanDevice:
    """devices

    Attributes:
        serial_num (Union[Unset, str]): device serial number
        device_mods (Union[Unset, list['ApiPlanDeviceModifier']]): device modifiers
    """

    serial_num: Union[Unset, str] = UNSET
    device_mods: Union[Unset, list["ApiPlanDeviceModifier"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        serial_num = self.serial_num

        device_mods: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.device_mods, Unset):
            device_mods = []
            for device_mods_item_data in self.device_mods:
                device_mods_item = device_mods_item_data.to_dict()
                device_mods.append(device_mods_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if serial_num is not UNSET:
            field_dict["serialNum"] = serial_num
        if device_mods is not UNSET:
            field_dict["deviceMods"] = device_mods

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_plan_device_modifier import ApiPlanDeviceModifier

        d = dict(src_dict)
        serial_num = d.pop("serialNum", UNSET)

        device_mods = []
        _device_mods = d.pop("deviceMods", UNSET)
        for device_mods_item_data in _device_mods or []:
            device_mods_item = ApiPlanDeviceModifier.from_dict(device_mods_item_data)

            device_mods.append(device_mods_item)

        api_plan_device = cls(
            serial_num=serial_num,
            device_mods=device_mods,
        )

        api_plan_device.additional_properties = d
        return api_plan_device

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
