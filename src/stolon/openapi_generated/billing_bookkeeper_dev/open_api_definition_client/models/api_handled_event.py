from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiHandledEvent")


@_attrs_define
class ApiHandledEvent:
    """
    Attributes:
        events_handled (Union[Unset, int]): number of events handled successfully
        events_no_action_performed (Union[Unset, int]): number of events handled but no action was performed
        events_excluded (Union[Unset, int]): number of events excluded due to conditional event processing
        messages (Union[Unset, list[str]]): error messages, if any
    """

    events_handled: Union[Unset, int] = UNSET
    events_no_action_performed: Union[Unset, int] = UNSET
    events_excluded: Union[Unset, int] = UNSET
    messages: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        events_handled = self.events_handled

        events_no_action_performed = self.events_no_action_performed

        events_excluded = self.events_excluded

        messages: Union[Unset, list[str]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = self.messages

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if events_handled is not UNSET:
            field_dict["eventsHandled"] = events_handled
        if events_no_action_performed is not UNSET:
            field_dict["eventsNoActionPerformed"] = events_no_action_performed
        if events_excluded is not UNSET:
            field_dict["eventsExcluded"] = events_excluded
        if messages is not UNSET:
            field_dict["messages"] = messages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        events_handled = d.pop("eventsHandled", UNSET)

        events_no_action_performed = d.pop("eventsNoActionPerformed", UNSET)

        events_excluded = d.pop("eventsExcluded", UNSET)

        messages = cast(list[str], d.pop("messages", UNSET))

        api_handled_event = cls(
            events_handled=events_handled,
            events_no_action_performed=events_no_action_performed,
            events_excluded=events_excluded,
            messages=messages,
        )

        api_handled_event.additional_properties = d
        return api_handled_event

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
