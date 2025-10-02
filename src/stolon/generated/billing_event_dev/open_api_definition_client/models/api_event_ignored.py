import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_event_ignored_consumer_source import ApiEventIgnoredConsumerSource
from ..models.api_event_ignored_ignore_reason import ApiEventIgnoredIgnoreReason
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiEventIgnored")


@_attrs_define
class ApiEventIgnored:
    """
    Attributes:
        id (Union[Unset, int]): Id of the ignored event
        uuid (Union[Unset, str]): 26-character UUID of the ignored event
        reference_id (Union[Unset, str]): 13-character UUID from COS or the billing entity this ignored event is for
        consumer_source (Union[Unset, ApiEventIgnoredConsumerSource]):
        payload (Union[Unset, str]): The full text or body of the ignored event
        channel (Union[Unset, str]): The source of the ignored event
        topic (Union[Unset, str]): The topic of the ignored event
        ignore_reason (Union[Unset, ApiEventIgnoredIgnoreReason]):
        message (Union[Unset, str]): Any message from the event handler determined to ignore the event
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the ignored event was created Example:
            2020-12-31T23:59:59.123456Z.
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    reference_id: Union[Unset, str] = UNSET
    consumer_source: Union[Unset, ApiEventIgnoredConsumerSource] = UNSET
    payload: Union[Unset, str] = UNSET
    channel: Union[Unset, str] = UNSET
    topic: Union[Unset, str] = UNSET
    ignore_reason: Union[Unset, ApiEventIgnoredIgnoreReason] = UNSET
    message: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        reference_id = self.reference_id

        consumer_source: Union[Unset, str] = UNSET
        if not isinstance(self.consumer_source, Unset):
            consumer_source = self.consumer_source.value

        payload = self.payload

        channel = self.channel

        topic = self.topic

        ignore_reason: Union[Unset, str] = UNSET
        if not isinstance(self.ignore_reason, Unset):
            ignore_reason = self.ignore_reason.value

        message = self.message

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if reference_id is not UNSET:
            field_dict["referenceId"] = reference_id
        if consumer_source is not UNSET:
            field_dict["consumerSource"] = consumer_source
        if payload is not UNSET:
            field_dict["payload"] = payload
        if channel is not UNSET:
            field_dict["channel"] = channel
        if topic is not UNSET:
            field_dict["topic"] = topic
        if ignore_reason is not UNSET:
            field_dict["ignoreReason"] = ignore_reason
        if message is not UNSET:
            field_dict["message"] = message
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        reference_id = d.pop("referenceId", UNSET)

        _consumer_source = d.pop("consumerSource", UNSET)
        consumer_source: Union[Unset, ApiEventIgnoredConsumerSource]
        if isinstance(_consumer_source, Unset):
            consumer_source = UNSET
        else:
            consumer_source = ApiEventIgnoredConsumerSource(_consumer_source)

        payload = d.pop("payload", UNSET)

        channel = d.pop("channel", UNSET)

        topic = d.pop("topic", UNSET)

        _ignore_reason = d.pop("ignoreReason", UNSET)
        ignore_reason: Union[Unset, ApiEventIgnoredIgnoreReason]
        if isinstance(_ignore_reason, Unset):
            ignore_reason = UNSET
        else:
            ignore_reason = ApiEventIgnoredIgnoreReason(_ignore_reason)

        message = d.pop("message", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_created_timestamp, Unset):
            created_timestamp = UNSET
        else:
            created_timestamp = isoparse(_created_timestamp)

        api_event_ignored = cls(
            id=id,
            uuid=uuid,
            reference_id=reference_id,
            consumer_source=consumer_source,
            payload=payload,
            channel=channel,
            topic=topic,
            ignore_reason=ignore_reason,
            message=message,
            created_timestamp=created_timestamp,
        )

        api_event_ignored.additional_properties = d
        return api_event_ignored

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
