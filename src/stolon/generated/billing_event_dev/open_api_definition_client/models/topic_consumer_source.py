from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopicConsumerSource")


@_attrs_define
class TopicConsumerSource:
    """
    Attributes:
        topic_names (Union[Unset, list[str]]):
        channels (Union[Unset, list[str]]):
    """

    topic_names: Union[Unset, list[str]] = UNSET
    channels: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        topic_names: Union[Unset, list[str]] = UNSET
        if not isinstance(self.topic_names, Unset):
            topic_names = self.topic_names

        channels: Union[Unset, list[str]] = UNSET
        if not isinstance(self.channels, Unset):
            channels = self.channels

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if topic_names is not UNSET:
            field_dict["topicNames"] = topic_names
        if channels is not UNSET:
            field_dict["channels"] = channels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        topic_names = cast(list[str], d.pop("topicNames", UNSET))

        channels = cast(list[str], d.pop("channels", UNSET))

        topic_consumer_source = cls(
            topic_names=topic_names,
            channels=channels,
        )

        topic_consumer_source.additional_properties = d
        return topic_consumer_source

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
