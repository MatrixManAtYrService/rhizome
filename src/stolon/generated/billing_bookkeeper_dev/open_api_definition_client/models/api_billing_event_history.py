import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_billing_event_history_entity_type import ApiBillingEventHistoryEntityType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiBillingEventHistory")


@_attrs_define
class ApiBillingEventHistory:
    """
    Attributes:
        id (Union[Unset, int]): Id of the merchant event history
        environment (Union[Unset, str]): merchant event history environment
        entity_uuid (Union[Unset, str]): 13-character UUID of the actual entity that this billing entity represents
        entity_type (Union[Unset, ApiBillingEventHistoryEntityType]):
        event_uuid (Union[Unset, str]): 26-character UUID of the billing event
        input_ (Union[Unset, str]):
        message (Union[Unset, str]): any captured processing message resulting from processing the billing event
        created_timestamp (Union[Unset, datetime.datetime]): merchant event history created timestamp Example:
            2020-12-31T23:59:59.123456Z.
    """

    id: Union[Unset, int] = UNSET
    environment: Union[Unset, str] = UNSET
    entity_uuid: Union[Unset, str] = UNSET
    entity_type: Union[Unset, ApiBillingEventHistoryEntityType] = UNSET
    event_uuid: Union[Unset, str] = UNSET
    input_: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        environment = self.environment

        entity_uuid = self.entity_uuid

        entity_type: Union[Unset, str] = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type.value

        event_uuid = self.event_uuid

        input_ = self.input_

        message = self.message

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
        if entity_uuid is not UNSET:
            field_dict["entityUuid"] = entity_uuid
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if event_uuid is not UNSET:
            field_dict["eventUuid"] = event_uuid
        if input_ is not UNSET:
            field_dict["input"] = input_
        if message is not UNSET:
            field_dict["message"] = message
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        environment = d.pop("environment", UNSET)

        entity_uuid = d.pop("entityUuid", UNSET)

        _entity_type = d.pop("entityType", UNSET)
        entity_type: Union[Unset, ApiBillingEventHistoryEntityType]
        if isinstance(_entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = ApiBillingEventHistoryEntityType(_entity_type)

        event_uuid = d.pop("eventUuid", UNSET)

        input_ = d.pop("input", UNSET)

        message = d.pop("message", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_created_timestamp, Unset):
            created_timestamp = UNSET
        else:
            created_timestamp = isoparse(_created_timestamp)

        api_billing_event_history = cls(
            id=id,
            environment=environment,
            entity_uuid=entity_uuid,
            entity_type=entity_type,
            event_uuid=event_uuid,
            input_=input_,
            message=message,
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
