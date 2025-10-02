import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_producer_failure_history_event_source import ApiProducerFailureHistoryEventSource
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiProducerFailureHistory")


@_attrs_define
class ApiProducerFailureHistory:
    """
    Attributes:
        id (Union[Unset, int]): Id of the producer failure
        uuid (Union[Unset, str]): 26-character UUID of the producer failure
        environment (Union[Unset, str]): The environment the event was from that resulted in the producer failure
        reference_id (Union[Unset, str]): 13-character UUID from COS of the billing entity this failure is for
        event_source (Union[Unset, ApiProducerFailureHistoryEventSource]):
        event_context_json (Union[Unset, str]): json context used to process the event
        input_event_uuid (Union[Unset, str]):
        input_ (Union[Unset, str]): The full text of the billing event that resulted in the producer failure
        output (Union[Unset, str]): The full text of the billing event that resulted in the producer failure
        channel (Union[Unset, str]): The source of the billing event that resulted in the producer failure
        topic (Union[Unset, str]): The topic of the billing event that resulted in the producer failure
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the producer failure was created
            Example: 2020-12-31T23:59:59.123456Z.
        comment (Union[Unset, str]): A comment for why the consumer failure was acknowledged
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    environment: Union[Unset, str] = UNSET
    reference_id: Union[Unset, str] = UNSET
    event_source: Union[Unset, ApiProducerFailureHistoryEventSource] = UNSET
    event_context_json: Union[Unset, str] = UNSET
    input_event_uuid: Union[Unset, str] = UNSET
    input_: Union[Unset, str] = UNSET
    output: Union[Unset, str] = UNSET
    channel: Union[Unset, str] = UNSET
    topic: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    comment: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        environment = self.environment

        reference_id = self.reference_id

        event_source: Union[Unset, str] = UNSET
        if not isinstance(self.event_source, Unset):
            event_source = self.event_source.value

        event_context_json = self.event_context_json

        input_event_uuid = self.input_event_uuid

        input_ = self.input_

        output = self.output

        channel = self.channel

        topic = self.topic

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        comment = self.comment

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
        if event_source is not UNSET:
            field_dict["eventSource"] = event_source
        if event_context_json is not UNSET:
            field_dict["eventContextJson"] = event_context_json
        if input_event_uuid is not UNSET:
            field_dict["inputEventUuid"] = input_event_uuid
        if input_ is not UNSET:
            field_dict["input"] = input_
        if output is not UNSET:
            field_dict["output"] = output
        if channel is not UNSET:
            field_dict["channel"] = channel
        if topic is not UNSET:
            field_dict["topic"] = topic
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        environment = d.pop("environment", UNSET)

        reference_id = d.pop("referenceId", UNSET)

        _event_source = d.pop("eventSource", UNSET)
        event_source: Union[Unset, ApiProducerFailureHistoryEventSource]
        if isinstance(_event_source, Unset):
            event_source = UNSET
        else:
            event_source = ApiProducerFailureHistoryEventSource(_event_source)

        event_context_json = d.pop("eventContextJson", UNSET)

        input_event_uuid = d.pop("inputEventUuid", UNSET)

        input_ = d.pop("input", UNSET)

        output = d.pop("output", UNSET)

        channel = d.pop("channel", UNSET)

        topic = d.pop("topic", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_created_timestamp, Unset):
            created_timestamp = UNSET
        else:
            created_timestamp = isoparse(_created_timestamp)

        comment = d.pop("comment", UNSET)

        api_producer_failure_history = cls(
            id=id,
            uuid=uuid,
            environment=environment,
            reference_id=reference_id,
            event_source=event_source,
            event_context_json=event_context_json,
            input_event_uuid=input_event_uuid,
            input_=input_,
            output=output,
            channel=channel,
            topic=topic,
            created_timestamp=created_timestamp,
            comment=comment,
        )

        api_producer_failure_history.additional_properties = d
        return api_producer_failure_history

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
