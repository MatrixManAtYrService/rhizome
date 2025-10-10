import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_consumer_failure_consumer_source import ApiConsumerFailureConsumerSource
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiConsumerFailure")


@_attrs_define
class ApiConsumerFailure:
    """
    Attributes:
        id (Union[Unset, int]): Id of the consumer failure
        uuid (Union[Unset, str]): 26-character UUID of the consumer failure
        environment (Union[Unset, str]): The environment the event was from that resulted in the consumer failure
        reference_id (Union[Unset, str]): 13-character UUID from COS or the billing entity this failure is for
        consumer_source (Union[Unset, ApiConsumerFailureConsumerSource]):
        payload (Union[Unset, str]): The full text of the billing event that resulted in the consumer failure
        channel (Union[Unset, str]): The source of the billing event that resulted in the consumer failure
        topic (Union[Unset, str]): The topic of the billing event that resulted in the consumer failure
        cause (Union[Unset, str]): The cause from the exception that resulted in the consumer failure
        message (Union[Unset, str]): The message from the exception that resulted in the consumer failure
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the consumer failure was created
            Example: 2020-12-31T23:59:59.123456Z.
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    environment: Union[Unset, str] = UNSET
    reference_id: Union[Unset, str] = UNSET
    consumer_source: Union[Unset, ApiConsumerFailureConsumerSource] = UNSET
    payload: Union[Unset, str] = UNSET
    channel: Union[Unset, str] = UNSET
    topic: Union[Unset, str] = UNSET
    cause: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        environment = self.environment

        reference_id = self.reference_id

        consumer_source: Union[Unset, str] = UNSET
        if not isinstance(self.consumer_source, Unset):
            consumer_source = self.consumer_source.value

        payload = self.payload

        channel = self.channel

        topic = self.topic

        cause = self.cause

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
        if environment is not UNSET:
            field_dict["environment"] = environment
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
        if cause is not UNSET:
            field_dict["cause"] = cause
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

        environment = d.pop("environment", UNSET)

        reference_id = d.pop("referenceId", UNSET)

        _consumer_source = d.pop("consumerSource", UNSET)
        consumer_source: Union[Unset, ApiConsumerFailureConsumerSource]
        if _consumer_source and not isinstance(_consumer_source, Unset):
            consumer_source = ApiConsumerFailureConsumerSource(_consumer_source)

        else:
            consumer_source = UNSET

        payload = d.pop("payload", UNSET)

        channel = d.pop("channel", UNSET)

        topic = d.pop("topic", UNSET)

        cause = d.pop("cause", UNSET)

        message = d.pop("message", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if _created_timestamp and not isinstance(_created_timestamp, Unset):
            created_timestamp = isoparse(_created_timestamp)

        else:
            created_timestamp = UNSET

        api_consumer_failure = cls(
            id=id,
            uuid=uuid,
            environment=environment,
            reference_id=reference_id,
            consumer_source=consumer_source,
            payload=payload,
            channel=channel,
            topic=topic,
            cause=cause,
            message=message,
            created_timestamp=created_timestamp,
        )

        api_consumer_failure.additional_properties = d
        return api_consumer_failure

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
