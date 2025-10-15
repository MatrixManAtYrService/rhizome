from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ebb_device_event import EbbDeviceEvent


T = TypeVar("T", bound="EbbDeviceProvision")


@_attrs_define
class EbbDeviceProvision:
    """
    Attributes:
        serial_number (Union[Unset, str]):
        bundle_indicator (Union[Unset, str]):
        activated_time (Union[Unset, int]):
        provisioned_time (Union[Unset, int]):
        deleted_time (Union[Unset, int]):
        device_events (Union[Unset, list['EbbDeviceEvent']]):
    """

    serial_number: Union[Unset, str] = UNSET
    bundle_indicator: Union[Unset, str] = UNSET
    activated_time: Union[Unset, int] = UNSET
    provisioned_time: Union[Unset, int] = UNSET
    deleted_time: Union[Unset, int] = UNSET
    device_events: Union[Unset, list["EbbDeviceEvent"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        serial_number = self.serial_number

        bundle_indicator = self.bundle_indicator

        activated_time = self.activated_time

        provisioned_time = self.provisioned_time

        deleted_time = self.deleted_time

        device_events: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.device_events, Unset):
            device_events = []
            for device_events_item_data in self.device_events:
                device_events_item = device_events_item_data.to_dict()
                device_events.append(device_events_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if bundle_indicator is not UNSET:
            field_dict["bundleIndicator"] = bundle_indicator
        if activated_time is not UNSET:
            field_dict["activatedTime"] = activated_time
        if provisioned_time is not UNSET:
            field_dict["provisionedTime"] = provisioned_time
        if deleted_time is not UNSET:
            field_dict["deletedTime"] = deleted_time
        if device_events is not UNSET:
            field_dict["deviceEvents"] = device_events

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ebb_device_event import EbbDeviceEvent

        d = dict(src_dict)
        serial_number = d.pop("serialNumber", UNSET)

        bundle_indicator = d.pop("bundleIndicator", UNSET)

        activated_time = d.pop("activatedTime", UNSET)

        provisioned_time = d.pop("provisionedTime", UNSET)

        deleted_time = d.pop("deletedTime", UNSET)

        device_events = []
        _device_events = d.pop("deviceEvents", UNSET)
        for device_events_item_data in _device_events or []:
            device_events_item = EbbDeviceEvent.from_dict(device_events_item_data)

            device_events.append(device_events_item)

        ebb_device_provision = cls(
            serial_number=serial_number,
            bundle_indicator=bundle_indicator,
            activated_time=activated_time,
            provisioned_time=provisioned_time,
            deleted_time=deleted_time,
            device_events=device_events,
        )

        ebb_device_provision.additional_properties = d
        return ebb_device_provision

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
