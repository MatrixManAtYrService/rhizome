import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiRevenueShareGroup")


@_attrs_define
class ApiRevenueShareGroup:
    """
    Attributes:
        id (Union[Unset, int]): Id of the revenue share group instance
        uuid (Union[Unset, str]): 26-character UUID of the revenue share group instance
        revenue_share_group (Union[Unset, str]): group that the partners belong to for revenue share splits
        short_desc (Union[Unset, str]): short description of revenue share group
        description (Union[Unset, str]): description of the revenue share group
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the revenue share group was created
            Example: 2020-12-31T23:59:59.123456Z.
        modified_timestamp (Union[Unset, datetime.datetime]): date and time when the revenue share group was last
            modified Example: 2020-12-31T23:59:59.123456Z.
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    revenue_share_group: Union[Unset, str] = UNSET
    short_desc: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        revenue_share_group = self.revenue_share_group

        short_desc = self.short_desc

        description = self.description

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
        if revenue_share_group is not UNSET:
            field_dict["revenueShareGroup"] = revenue_share_group
        if short_desc is not UNSET:
            field_dict["shortDesc"] = short_desc
        if description is not UNSET:
            field_dict["description"] = description
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

        revenue_share_group = d.pop("revenueShareGroup", UNSET)

        short_desc = d.pop("shortDesc", UNSET)

        description = d.pop("description", UNSET)

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

        api_revenue_share_group = cls(
            id=id,
            uuid=uuid,
            revenue_share_group=revenue_share_group,
            short_desc=short_desc,
            description=description,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
        )

        api_revenue_share_group.additional_properties = d
        return api_revenue_share_group

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
