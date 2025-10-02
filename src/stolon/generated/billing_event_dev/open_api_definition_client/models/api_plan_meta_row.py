import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_plan_meta_row_plan_type import ApiPlanMetaRowPlanType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiPlanMetaRow")


@_attrs_define
class ApiPlanMetaRow:
    """
    Attributes:
        id (Union[Unset, int]): id of the plan meta row
        uuid (Union[Unset, str]): 26-character UUID of the plan meta row
        country (Union[Unset, str]):
        plan_type (Union[Unset, ApiPlanMetaRowPlanType]):
        plan_uuid (Union[Unset, str]):
        name (Union[Unset, str]):
        value (Union[Unset, str]): plan meta row value
        created_timestamp (Union[Unset, datetime.datetime]): created timestamp for plan meta row Example:
            2020-12-31T23:59:59.123456Z.
        modified_timestamp (Union[Unset, datetime.datetime]): modified timestamp for plan meta row Example:
            2020-12-31T23:59:59.123456Z.
        deleted_timestamp (Union[Unset, datetime.datetime]): deleted timestamp for plan meta row Example:
            2020-12-31T23:59:59.123456Z.
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    plan_type: Union[Unset, ApiPlanMetaRowPlanType] = UNSET
    plan_uuid: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    deleted_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        country = self.country

        plan_type: Union[Unset, str] = UNSET
        if not isinstance(self.plan_type, Unset):
            plan_type = self.plan_type.value

        plan_uuid = self.plan_uuid

        name = self.name

        value = self.value

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        modified_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.modified_timestamp, Unset):
            modified_timestamp = self.modified_timestamp.isoformat()

        deleted_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.deleted_timestamp, Unset):
            deleted_timestamp = self.deleted_timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if country is not UNSET:
            field_dict["country"] = country
        if plan_type is not UNSET:
            field_dict["planType"] = plan_type
        if plan_uuid is not UNSET:
            field_dict["planUuid"] = plan_uuid
        if name is not UNSET:
            field_dict["name"] = name
        if value is not UNSET:
            field_dict["value"] = value
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if modified_timestamp is not UNSET:
            field_dict["modifiedTimestamp"] = modified_timestamp
        if deleted_timestamp is not UNSET:
            field_dict["deletedTimestamp"] = deleted_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        country = d.pop("country", UNSET)

        _plan_type = d.pop("planType", UNSET)
        plan_type: Union[Unset, ApiPlanMetaRowPlanType]
        if isinstance(_plan_type, Unset):
            plan_type = UNSET
        else:
            plan_type = ApiPlanMetaRowPlanType(_plan_type)

        plan_uuid = d.pop("planUuid", UNSET)

        name = d.pop("name", UNSET)

        value = d.pop("value", UNSET)

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

        _deleted_timestamp = d.pop("deletedTimestamp", UNSET)
        deleted_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_deleted_timestamp, Unset):
            deleted_timestamp = UNSET
        else:
            deleted_timestamp = isoparse(_deleted_timestamp)

        api_plan_meta_row = cls(
            id=id,
            uuid=uuid,
            country=country,
            plan_type=plan_type,
            plan_uuid=plan_uuid,
            name=name,
            value=value,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
            deleted_timestamp=deleted_timestamp,
        )

        api_plan_meta_row.additional_properties = d
        return api_plan_meta_row

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
