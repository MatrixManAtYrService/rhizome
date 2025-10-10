import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_billing_hierarchy_entity_type import ApiBillingHierarchyEntityType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiBillingHierarchy")


@_attrs_define
class ApiBillingHierarchy:
    """
    Attributes:
        id (Union[Unset, int]): Id of the billing hierarchy node
        uuid (Union[Unset, str]): 26-character UUID of the billing hierarchy node
        hierarchy_type (Union[Unset, str]): billing hierarchy type value
        billing_entity_id (Union[Unset, int]): Id of the billing entity associated with this hierarchy node
        billing_entity_uuid (Union[Unset, str]): UUID of the billing entity associated with this hierarchy node
        name (Union[Unset, str]): name of billing entity
        entity_type (Union[Unset, ApiBillingHierarchyEntityType]):
        entity_uuid (Union[Unset, str]): 26-character UUID of the entity
        effective_date (Union[Unset, datetime.date]): date that this billing hierarchy node became effective
        deleted_date (Union[Unset, datetime.date]): date that this billing hierarchy node is no longer effective
        parent_billing_hierarchy_id (Union[Unset, int]): Id of the billing hierarchy that is the parent of this
            hierarchy node
        parent_billing_hierarchy_uuid (Union[Unset, str]): UUID of the billing hierarchy that is the parent of this
            hierarchy node
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the billing hierarchy node was created
            Example: 2020-12-31T23:59:59.123456Z.
        modified_timestamp (Union[Unset, datetime.datetime]): date and time when the billing hierarchy node was last
            modified Example: 2020-12-31T23:59:59.123456Z.
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    hierarchy_type: Union[Unset, str] = UNSET
    billing_entity_id: Union[Unset, int] = UNSET
    billing_entity_uuid: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    entity_type: Union[Unset, ApiBillingHierarchyEntityType] = UNSET
    entity_uuid: Union[Unset, str] = UNSET
    effective_date: Union[Unset, datetime.date] = UNSET
    deleted_date: Union[Unset, datetime.date] = UNSET
    parent_billing_hierarchy_id: Union[Unset, int] = UNSET
    parent_billing_hierarchy_uuid: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        hierarchy_type = self.hierarchy_type

        billing_entity_id = self.billing_entity_id

        billing_entity_uuid = self.billing_entity_uuid

        name = self.name

        entity_type: Union[Unset, str] = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type.value

        entity_uuid = self.entity_uuid

        effective_date: Union[Unset, str] = UNSET
        if not isinstance(self.effective_date, Unset):
            effective_date = self.effective_date.isoformat()

        deleted_date: Union[Unset, str] = UNSET
        if not isinstance(self.deleted_date, Unset):
            deleted_date = self.deleted_date.isoformat()

        parent_billing_hierarchy_id = self.parent_billing_hierarchy_id

        parent_billing_hierarchy_uuid = self.parent_billing_hierarchy_uuid

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
        if hierarchy_type is not UNSET:
            field_dict["hierarchyType"] = hierarchy_type
        if billing_entity_id is not UNSET:
            field_dict["billingEntityId"] = billing_entity_id
        if billing_entity_uuid is not UNSET:
            field_dict["billingEntityUuid"] = billing_entity_uuid
        if name is not UNSET:
            field_dict["name"] = name
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if entity_uuid is not UNSET:
            field_dict["entityUuid"] = entity_uuid
        if effective_date is not UNSET:
            field_dict["effectiveDate"] = effective_date
        if deleted_date is not UNSET:
            field_dict["deletedDate"] = deleted_date
        if parent_billing_hierarchy_id is not UNSET:
            field_dict["parentBillingHierarchyId"] = parent_billing_hierarchy_id
        if parent_billing_hierarchy_uuid is not UNSET:
            field_dict["parentBillingHierarchyUuid"] = parent_billing_hierarchy_uuid
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

        hierarchy_type = d.pop("hierarchyType", UNSET)

        billing_entity_id = d.pop("billingEntityId", UNSET)

        billing_entity_uuid = d.pop("billingEntityUuid", UNSET)

        name = d.pop("name", UNSET)

        _entity_type = d.pop("entityType", UNSET)
        entity_type: Union[Unset, ApiBillingHierarchyEntityType]
        if isinstance(_entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = ApiBillingHierarchyEntityType(_entity_type)

        entity_uuid = d.pop("entityUuid", UNSET)

        _effective_date = d.pop("effectiveDate", UNSET)
        effective_date: Union[Unset, datetime.date]
        if isinstance(_effective_date, Unset) or _effective_date is None:
            effective_date = UNSET
        else:
            effective_date = isoparse(_effective_date).date()

        _deleted_date = d.pop("deletedDate", UNSET)
        deleted_date: Union[Unset, datetime.date]
        if isinstance(_deleted_date, Unset) or _deleted_date is None:
            deleted_date = UNSET
        else:
            deleted_date = isoparse(_deleted_date).date()

        parent_billing_hierarchy_id = d.pop("parentBillingHierarchyId", UNSET)

        parent_billing_hierarchy_uuid = d.pop("parentBillingHierarchyUuid", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_created_timestamp, Unset) or _created_timestamp is None:
            created_timestamp = UNSET
        else:
            created_timestamp = isoparse(_created_timestamp)

        _modified_timestamp = d.pop("modifiedTimestamp", UNSET)
        modified_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_modified_timestamp, Unset) or _modified_timestamp is None:
            modified_timestamp = UNSET
        else:
            modified_timestamp = isoparse(_modified_timestamp)

        api_billing_hierarchy = cls(
            id=id,
            uuid=uuid,
            hierarchy_type=hierarchy_type,
            billing_entity_id=billing_entity_id,
            billing_entity_uuid=billing_entity_uuid,
            name=name,
            entity_type=entity_type,
            entity_uuid=entity_uuid,
            effective_date=effective_date,
            deleted_date=deleted_date,
            parent_billing_hierarchy_id=parent_billing_hierarchy_id,
            parent_billing_hierarchy_uuid=parent_billing_hierarchy_uuid,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
        )

        api_billing_hierarchy.additional_properties = d
        return api_billing_hierarchy

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
