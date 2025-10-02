import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.billing_entity_entity_type import BillingEntityEntityType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BillingEntity")


@_attrs_define
class BillingEntity:
    """
    Attributes:
        id (Union[Unset, int]):
        uuid (Union[Unset, str]):
        entity_uuid (Union[Unset, str]):
        entity_type (Union[Unset, BillingEntityEntityType]):
        name (Union[Unset, str]):
        created_timestamp (Union[Unset, datetime.datetime]):
        modified_timestamp (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    entity_uuid: Union[Unset, str] = UNSET
    entity_type: Union[Unset, BillingEntityEntityType] = UNSET
    name: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        entity_uuid = self.entity_uuid

        entity_type: Union[Unset, str] = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type.value

        name = self.name

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        modified_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.modified_timestamp, Unset):
            modified_timestamp = self.modified_timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if entity_uuid is not UNSET:
            field_dict["entityUuid"] = entity_uuid
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if name is not UNSET:
            field_dict["name"] = name
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if modified_timestamp is not UNSET:
            field_dict["modifiedTimestamp"] = modified_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        entity_uuid = d.pop("entityUuid", UNSET)

        _entity_type = d.pop("entityType", UNSET)
        entity_type: Union[Unset, BillingEntityEntityType]
        if isinstance(_entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = BillingEntityEntityType(_entity_type)

        name = d.pop("name", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_created_timestamp, Unset):
            created_timestamp = UNSET
        else:
            created_timestamp = isoparse(_created_timestamp)

        _modified_timestamp = d.pop("modifiedTimestamp", UNSET)
        modified_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_modified_timestamp, Unset):
            modified_timestamp = UNSET
        else:
            modified_timestamp = isoparse(_modified_timestamp)

        billing_entity = cls(
            id=id,
            uuid=uuid,
            entity_uuid=entity_uuid,
            entity_type=entity_type,
            name=name,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
        )

        billing_entity.additional_properties = d
        return billing_entity

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
