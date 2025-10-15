from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EbbDeviceEvent")


@_attrs_define
class EbbDeviceEvent:
    """
    Attributes:
        database_id (Union[Unset, int]):
        event (Union[Unset, str]):
        timestamp (Union[Unset, int]):
    """

    database_id: Union[Unset, int] = UNSET
    event: Union[Unset, str] = UNSET
    timestamp: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        database_id = self.database_id

        event = self.event

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if database_id is not UNSET:
            field_dict["databaseId"] = database_id
        if event is not UNSET:
            field_dict["event"] = event
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        database_id = d.pop("databaseId", UNSET)

        event = d.pop("event", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        ebb_device_event = cls(
            database_id=database_id,
            event=event,
            timestamp=timestamp,
        )

        ebb_device_event.additional_properties = d
        return ebb_device_event

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
