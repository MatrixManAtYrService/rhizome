import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiAdjustActionType")


@_attrs_define
class ApiAdjustActionType:
    """
    Attributes:
        id (Union[Unset, int]): Id of the adjustment action type
        uuid (Union[Unset, str]): 26-character UUID of the adjustment action type
        adjust_action_type (Union[Unset, str]): defined adjustment action type value
        fee_category_group (Union[Unset, str]): the fee category grouping to which the adjustment action applies
        revenue_group (Union[Unset, str]): the revenue group used to sub-categorize fee category
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the adjustment action type was created
            Example: 2020-12-31T23:59:59.123456Z.
        modified_timestamp (Union[Unset, datetime.datetime]): date and time when the adjustment action type was last
            modified Example: 2020-12-31T23:59:59.123456Z.
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    adjust_action_type: Union[Unset, str] = UNSET
    fee_category_group: Union[Unset, str] = UNSET
    revenue_group: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        adjust_action_type = self.adjust_action_type

        fee_category_group = self.fee_category_group

        revenue_group = self.revenue_group

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
        if adjust_action_type is not UNSET:
            field_dict["adjustActionType"] = adjust_action_type
        if fee_category_group is not UNSET:
            field_dict["feeCategoryGroup"] = fee_category_group
        if revenue_group is not UNSET:
            field_dict["revenueGroup"] = revenue_group
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

        adjust_action_type = d.pop("adjustActionType", UNSET)

        fee_category_group = d.pop("feeCategoryGroup", UNSET)

        revenue_group = d.pop("revenueGroup", UNSET)

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

        api_adjust_action_type = cls(
            id=id,
            uuid=uuid,
            adjust_action_type=adjust_action_type,
            fee_category_group=fee_category_group,
            revenue_group=revenue_group,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
        )

        api_adjust_action_type.additional_properties = d
        return api_adjust_action_type

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
