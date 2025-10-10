import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.billing_hierarchy_entity_type import BillingHierarchyEntityType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BillingHierarchy")


@_attrs_define
class BillingHierarchy:
    """
    Attributes:
        id (Union[Unset, int]):
        uuid (Union[Unset, str]):
        hierarchy_type (Union[Unset, str]):
        billing_entity_uuid (Union[Unset, str]):
        billing_entity_id (Union[Unset, int]):
        name (Union[Unset, str]):
        entity_type (Union[Unset, BillingHierarchyEntityType]):
        entity_uuid (Union[Unset, str]):
        effective_date (Union[Unset, datetime.date]):
        deleted_date (Union[Unset, datetime.date]):
        parent_billing_hierarchy_uuid (Union[Unset, str]):
        parent_billing_hierarchy_id (Union[Unset, int]):
        created_timestamp (Union[Unset, datetime.datetime]):
        modified_timestamp (Union[Unset, datetime.datetime]):
        root_node (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    hierarchy_type: Union[Unset, str] = UNSET
    billing_entity_uuid: Union[Unset, str] = UNSET
    billing_entity_id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    entity_type: Union[Unset, BillingHierarchyEntityType] = UNSET
    entity_uuid: Union[Unset, str] = UNSET
    effective_date: Union[Unset, datetime.date] = UNSET
    deleted_date: Union[Unset, datetime.date] = UNSET
    parent_billing_hierarchy_uuid: Union[Unset, str] = UNSET
    parent_billing_hierarchy_id: Union[Unset, int] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    root_node: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        hierarchy_type = self.hierarchy_type

        billing_entity_uuid = self.billing_entity_uuid

        billing_entity_id = self.billing_entity_id

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

        parent_billing_hierarchy_uuid = self.parent_billing_hierarchy_uuid

        parent_billing_hierarchy_id = self.parent_billing_hierarchy_id

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        modified_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.modified_timestamp, Unset):
            modified_timestamp = self.modified_timestamp.isoformat()

        root_node = self.root_node

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if hierarchy_type is not UNSET:
            field_dict["hierarchyType"] = hierarchy_type
        if billing_entity_uuid is not UNSET:
            field_dict["billingEntityUuid"] = billing_entity_uuid
        if billing_entity_id is not UNSET:
            field_dict["billingEntityId"] = billing_entity_id
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
        if parent_billing_hierarchy_uuid is not UNSET:
            field_dict["parentBillingHierarchyUuid"] = parent_billing_hierarchy_uuid
        if parent_billing_hierarchy_id is not UNSET:
            field_dict["parentBillingHierarchyId"] = parent_billing_hierarchy_id
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if modified_timestamp is not UNSET:
            field_dict["modifiedTimestamp"] = modified_timestamp
        if root_node is not UNSET:
            field_dict["rootNode"] = root_node

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        hierarchy_type = d.pop("hierarchyType", UNSET)

        billing_entity_uuid = d.pop("billingEntityUuid", UNSET)

        billing_entity_id = d.pop("billingEntityId", UNSET)

        name = d.pop("name", UNSET)

        _entity_type = d.pop("entityType", UNSET)
        entity_type: Union[Unset, BillingHierarchyEntityType]
        if _entity_type and not isinstance(_entity_type, Unset):
            entity_type = BillingHierarchyEntityType(_entity_type)

        else:
            entity_type = UNSET

        entity_uuid = d.pop("entityUuid", UNSET)

        _effective_date = d.pop("effectiveDate", UNSET)
        effective_date: Union[Unset, datetime.date]
        if _effective_date and not isinstance(_effective_date, Unset):
            effective_date = isoparse(_effective_date).date()

        else:
            effective_date = UNSET

        _deleted_date = d.pop("deletedDate", UNSET)
        deleted_date: Union[Unset, datetime.date]
        if _deleted_date and not isinstance(_deleted_date, Unset):
            deleted_date = isoparse(_deleted_date).date()

        else:
            deleted_date = UNSET

        parent_billing_hierarchy_uuid = d.pop("parentBillingHierarchyUuid", UNSET)

        parent_billing_hierarchy_id = d.pop("parentBillingHierarchyId", UNSET)

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

        root_node = d.pop("rootNode", UNSET)

        billing_hierarchy = cls(
            id=id,
            uuid=uuid,
            hierarchy_type=hierarchy_type,
            billing_entity_uuid=billing_entity_uuid,
            billing_entity_id=billing_entity_id,
            name=name,
            entity_type=entity_type,
            entity_uuid=entity_uuid,
            effective_date=effective_date,
            deleted_date=deleted_date,
            parent_billing_hierarchy_uuid=parent_billing_hierarchy_uuid,
            parent_billing_hierarchy_id=parent_billing_hierarchy_id,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
            root_node=root_node,
        )

        billing_hierarchy.additional_properties = d
        return billing_hierarchy

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
