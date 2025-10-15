import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_billing_hierarchy_level_node_entity_type import ApiBillingHierarchyLevelNodeEntityType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiBillingHierarchyLevelNode")


@_attrs_define
class ApiBillingHierarchyLevelNode:
    """
    Attributes:
        id (Union[Unset, int]): Id of the billing hierarchy node
        uuid (Union[Unset, str]): 26-character UUID of the billing hierarchy node
        hierarchy_type (Union[Unset, str]): billing hierarchy type value
        billing_entity_id (Union[Unset, int]): Id of the billing entity associated with this hierarchy node
        billing_entity_uuid (Union[Unset, str]): UUID of the billing entity associated with this hierarchy node
        name (Union[Unset, str]): name of billing entity
        entity_type (Union[Unset, ApiBillingHierarchyLevelNodeEntityType]):
        entity_uuid (Union[Unset, str]): 26-character UUID of the entity
        effective_date (Union[Unset, datetime.date]): date that this billing hierarchy node became effective
        deleted_date (Union[Unset, datetime.date]): date that this billing hierarchy node is no longer effective
        parent_billing_hierarchy_id (Union[Unset, int]): Id of the billing hierarchy that is the parent of this
            hierarchy node
        parent_billing_hierarchy_uuid (Union[Unset, str]): UUID of the billing hierarchy that is the parent of this
            hierarchy node
        parent_billing_entity_uuid (Union[Unset, str]): UUID of the billing entity that is associated with the parent
            hierarchy node
        level (Union[Unset, int]): the level within the hierarchy represented by this instance
        children (Union[Unset, list['ApiBillingHierarchyLevelNode']]):
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    hierarchy_type: Union[Unset, str] = UNSET
    billing_entity_id: Union[Unset, int] = UNSET
    billing_entity_uuid: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    entity_type: Union[Unset, ApiBillingHierarchyLevelNodeEntityType] = UNSET
    entity_uuid: Union[Unset, str] = UNSET
    effective_date: Union[Unset, datetime.date] = UNSET
    deleted_date: Union[Unset, datetime.date] = UNSET
    parent_billing_hierarchy_id: Union[Unset, int] = UNSET
    parent_billing_hierarchy_uuid: Union[Unset, str] = UNSET
    parent_billing_entity_uuid: Union[Unset, str] = UNSET
    level: Union[Unset, int] = UNSET
    children: Union[Unset, list["ApiBillingHierarchyLevelNode"]] = UNSET
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

        parent_billing_entity_uuid = self.parent_billing_entity_uuid

        level = self.level

        children: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

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
        if parent_billing_entity_uuid is not UNSET:
            field_dict["parentBillingEntityUuid"] = parent_billing_entity_uuid
        if level is not UNSET:
            field_dict["level"] = level
        if children is not UNSET:
            field_dict["children"] = children

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
        entity_type: Union[Unset, ApiBillingHierarchyLevelNodeEntityType]
        if _entity_type and not isinstance(_entity_type, Unset):
            entity_type = ApiBillingHierarchyLevelNodeEntityType(_entity_type)

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

        parent_billing_hierarchy_id = d.pop("parentBillingHierarchyId", UNSET)

        parent_billing_hierarchy_uuid = d.pop("parentBillingHierarchyUuid", UNSET)

        parent_billing_entity_uuid = d.pop("parentBillingEntityUuid", UNSET)

        level = d.pop("level", UNSET)

        children = []
        _children = d.pop("children", UNSET)
        for children_item_data in _children or []:
            children_item = ApiBillingHierarchyLevelNode.from_dict(children_item_data)

            children.append(children_item)

        api_billing_hierarchy_level_node = cls(
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
            parent_billing_entity_uuid=parent_billing_entity_uuid,
            level=level,
            children=children,
        )

        api_billing_hierarchy_level_node.additional_properties = d
        return api_billing_hierarchy_level_node

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
