import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_billing_archetype_archetype_type import ApiBillingArchetypeArchetypeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiBillingArchetype")


@_attrs_define
class ApiBillingArchetype:
    """
    Attributes:
        id (Union[Unset, int]): Id of the billing archetype
        uuid (Union[Unset, str]): 13-character UUID of the billing archetype
        archetype_type (Union[Unset, ApiBillingArchetypeArchetypeType]):
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the billing archetype was created
            Example: 2020-12-31T23:59:59.123456Z.
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    archetype_type: Union[Unset, ApiBillingArchetypeArchetypeType] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        archetype_type: Union[Unset, str] = UNSET
        if not isinstance(self.archetype_type, Unset):
            archetype_type = self.archetype_type.value

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
        if archetype_type is not UNSET:
            field_dict["archetypeType"] = archetype_type
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        _archetype_type = d.pop("archetypeType", UNSET)
        archetype_type: Union[Unset, ApiBillingArchetypeArchetypeType]
        if isinstance(_archetype_type, Unset):
            archetype_type = UNSET
        else:
            archetype_type = ApiBillingArchetypeArchetypeType(_archetype_type)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_created_timestamp, Unset):
            created_timestamp = UNSET
        else:
            created_timestamp = isoparse(_created_timestamp)

        api_billing_archetype = cls(
            id=id,
            uuid=uuid,
            archetype_type=archetype_type,
            created_timestamp=created_timestamp,
        )

        api_billing_archetype.additional_properties = d
        return api_billing_archetype

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
