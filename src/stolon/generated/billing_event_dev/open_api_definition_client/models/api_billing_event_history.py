import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_billing_event_history_event_source import ApiBillingEventHistoryEventSource
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiBillingEventHistory")


@_attrs_define
class ApiBillingEventHistory:
    """
    Attributes:
        id (Union[Unset, int]): Id of the billing event history
        environment (Union[Unset, str]): merchant billing history environment
        merchant_id (Union[Unset, str]):
        event_source (Union[Unset, ApiBillingEventHistoryEventSource]):
        event_context_json (Union[Unset, str]): json context used to process the event
        billing_event_uuid (Union[Unset, str]): 26-character UUID of the billing event
        event_uuid (Union[Unset, str]): 26-character UUID of the billing event - This is deprecated, using
            billingEventUuid instead - BILLNA-3409
        input_event_uuid (Union[Unset, str]):
        input_ (Union[Unset, str]):
        output (Union[Unset, str]):
        created_timestamp (Union[Unset, datetime.datetime]): billing event history created timestamp Example:
            2020-12-31T23:59:59.123456Z.
    """

    id: Union[Unset, int] = UNSET
    environment: Union[Unset, str] = UNSET
    merchant_id: Union[Unset, str] = UNSET
    event_source: Union[Unset, ApiBillingEventHistoryEventSource] = UNSET
    event_context_json: Union[Unset, str] = UNSET
    billing_event_uuid: Union[Unset, str] = UNSET
    event_uuid: Union[Unset, str] = UNSET
    input_event_uuid: Union[Unset, str] = UNSET
    input_: Union[Unset, str] = UNSET
    output: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        environment = self.environment

        merchant_id = self.merchant_id

        event_source: Union[Unset, str] = UNSET
        if not isinstance(self.event_source, Unset):
            event_source = self.event_source.value

        event_context_json = self.event_context_json

        billing_event_uuid = self.billing_event_uuid

        event_uuid = self.event_uuid

        input_event_uuid = self.input_event_uuid

        input_ = self.input_

        output = self.output

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if environment is not UNSET:
            field_dict["environment"] = environment
        if merchant_id is not UNSET:
            field_dict["merchantId"] = merchant_id
        if event_source is not UNSET:
            field_dict["eventSource"] = event_source
        if event_context_json is not UNSET:
            field_dict["eventContextJson"] = event_context_json
        if billing_event_uuid is not UNSET:
            field_dict["billingEventUuid"] = billing_event_uuid
        if event_uuid is not UNSET:
            field_dict["eventUuid"] = event_uuid
        if input_event_uuid is not UNSET:
            field_dict["inputEventUuid"] = input_event_uuid
        if input_ is not UNSET:
            field_dict["input"] = input_
        if output is not UNSET:
            field_dict["output"] = output
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        environment = d.pop("environment", UNSET)

        merchant_id = d.pop("merchantId", UNSET)

        _event_source = d.pop("eventSource", UNSET)
        event_source: Union[Unset, ApiBillingEventHistoryEventSource]
        if _event_source and not isinstance(_event_source, Unset):
            event_source = ApiBillingEventHistoryEventSource(_event_source)

        else:
            event_source = UNSET

        event_context_json = d.pop("eventContextJson", UNSET)

        billing_event_uuid = d.pop("billingEventUuid", UNSET)

        event_uuid = d.pop("eventUuid", UNSET)

        input_event_uuid = d.pop("inputEventUuid", UNSET)

        input_ = d.pop("input", UNSET)

        output = d.pop("output", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if _created_timestamp and not isinstance(_created_timestamp, Unset):
            created_timestamp = isoparse(_created_timestamp)

        else:
            created_timestamp = UNSET

        api_billing_event_history = cls(
            id=id,
            environment=environment,
            merchant_id=merchant_id,
            event_source=event_source,
            event_context_json=event_context_json,
            billing_event_uuid=billing_event_uuid,
            event_uuid=event_uuid,
            input_event_uuid=input_event_uuid,
            input_=input_,
            output=output,
            created_timestamp=created_timestamp,
        )

        api_billing_event_history.additional_properties = d
        return api_billing_event_history

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
