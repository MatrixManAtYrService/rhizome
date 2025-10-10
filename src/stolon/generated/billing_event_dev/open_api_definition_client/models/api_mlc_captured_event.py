import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiMlcCapturedEvent")


@_attrs_define
class ApiMlcCapturedEvent:
    """
    Attributes:
        uuid (Union[Unset, str]): 26-character UUID of the captured event record
        environment (Union[Unset, str]): environment of the captured mlc event
        merchant_uuid (Union[Unset, str]):
        reseller_uuid (Union[Unset, str]):
        event_timestamp (Union[Unset, datetime.datetime]): timestamp of the event Example: 2020-12-31T23:59:59.123456Z.
        mlc_event_uuid (Union[Unset, str]): the uuid of the mlc event
        event_json (Union[Unset, str]): the json of the mlc event
        event_context_json (Union[Unset, str]): the json of the context needed to process the event later
        processed_timestamp (Union[Unset, datetime.datetime]): timestamp of when the event is played Example:
            2020-12-31T23:59:59.123456Z.
        processed_billing_event_uuid (Union[Unset, str]): 26-character UUID of the billing event that is generated when
            the event is played
        created_timestamp (Union[Unset, datetime.datetime]): created timestamp Example: 2020-12-31T23:59:59.123456Z.
        modified_timestamp (Union[Unset, datetime.datetime]): modified timestamp Example: 2020-12-31T23:59:59.123456Z.
    """

    uuid: Union[Unset, str] = UNSET
    environment: Union[Unset, str] = UNSET
    merchant_uuid: Union[Unset, str] = UNSET
    reseller_uuid: Union[Unset, str] = UNSET
    event_timestamp: Union[Unset, datetime.datetime] = UNSET
    mlc_event_uuid: Union[Unset, str] = UNSET
    event_json: Union[Unset, str] = UNSET
    event_context_json: Union[Unset, str] = UNSET
    processed_timestamp: Union[Unset, datetime.datetime] = UNSET
    processed_billing_event_uuid: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        environment = self.environment

        merchant_uuid = self.merchant_uuid

        reseller_uuid = self.reseller_uuid

        event_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.event_timestamp, Unset):
            event_timestamp = self.event_timestamp.isoformat()

        mlc_event_uuid = self.mlc_event_uuid

        event_json = self.event_json

        event_context_json = self.event_context_json

        processed_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.processed_timestamp, Unset):
            processed_timestamp = self.processed_timestamp.isoformat()

        processed_billing_event_uuid = self.processed_billing_event_uuid

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        modified_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.modified_timestamp, Unset):
            modified_timestamp = self.modified_timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if environment is not UNSET:
            field_dict["environment"] = environment
        if merchant_uuid is not UNSET:
            field_dict["merchantUuid"] = merchant_uuid
        if reseller_uuid is not UNSET:
            field_dict["resellerUuid"] = reseller_uuid
        if event_timestamp is not UNSET:
            field_dict["eventTimestamp"] = event_timestamp
        if mlc_event_uuid is not UNSET:
            field_dict["mlcEventUuid"] = mlc_event_uuid
        if event_json is not UNSET:
            field_dict["eventJson"] = event_json
        if event_context_json is not UNSET:
            field_dict["eventContextJson"] = event_context_json
        if processed_timestamp is not UNSET:
            field_dict["processedTimestamp"] = processed_timestamp
        if processed_billing_event_uuid is not UNSET:
            field_dict["processedBillingEventUuid"] = processed_billing_event_uuid
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if modified_timestamp is not UNSET:
            field_dict["modifiedTimestamp"] = modified_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = d.pop("uuid", UNSET)

        environment = d.pop("environment", UNSET)

        merchant_uuid = d.pop("merchantUuid", UNSET)

        reseller_uuid = d.pop("resellerUuid", UNSET)

        _event_timestamp = d.pop("eventTimestamp", UNSET)
        event_timestamp: Union[Unset, datetime.datetime]
        if _event_timestamp and not isinstance(_event_timestamp, Unset):
            event_timestamp = isoparse(_event_timestamp)

        else:
            event_timestamp = UNSET

        mlc_event_uuid = d.pop("mlcEventUuid", UNSET)

        event_json = d.pop("eventJson", UNSET)

        event_context_json = d.pop("eventContextJson", UNSET)

        _processed_timestamp = d.pop("processedTimestamp", UNSET)
        processed_timestamp: Union[Unset, datetime.datetime]
        if _processed_timestamp and not isinstance(_processed_timestamp, Unset):
            processed_timestamp = isoparse(_processed_timestamp)

        else:
            processed_timestamp = UNSET

        processed_billing_event_uuid = d.pop("processedBillingEventUuid", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if _created_timestamp and not isinstance(_created_timestamp, Unset):
            created_timestamp = isoparse(_created_timestamp)

        else:
            created_timestamp = UNSET

        _modified_timestamp = d.pop("modifiedTimestamp", UNSET)
        modified_timestamp: Union[Unset, datetime.datetime]
        if _modified_timestamp and not isinstance(_modified_timestamp, Unset):
            modified_timestamp = isoparse(_modified_timestamp)

        else:
            modified_timestamp = UNSET

        api_mlc_captured_event = cls(
            uuid=uuid,
            environment=environment,
            merchant_uuid=merchant_uuid,
            reseller_uuid=reseller_uuid,
            event_timestamp=event_timestamp,
            mlc_event_uuid=mlc_event_uuid,
            event_json=event_json,
            event_context_json=event_context_json,
            processed_timestamp=processed_timestamp,
            processed_billing_event_uuid=processed_billing_event_uuid,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
        )

        api_mlc_captured_event.additional_properties = d
        return api_mlc_captured_event

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
