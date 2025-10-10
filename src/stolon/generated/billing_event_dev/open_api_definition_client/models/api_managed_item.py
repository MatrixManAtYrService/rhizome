import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_managed_item_criteria import ApiManagedItemCriteria
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiManagedItem")


@_attrs_define
class ApiManagedItem:
    """
    Attributes:
        id (Union[Unset, int]): Id of the managed item
        uuid (Union[Unset, str]): 26-character UUID of the managed item
        criteria (Union[Unset, ApiManagedItemCriteria]):
        item (Union[Unset, str]): managed item
        created_timestamp (Union[Unset, datetime.datetime]): managed item created timestamp Example:
            2020-12-31T23:59:59.123456Z.
        begin_timestamp (Union[Unset, datetime.datetime]): managed item begin filtering timestamp Example:
            2020-12-31T23:59:59.123456Z.
        end_timestamp (Union[Unset, datetime.datetime]): managed item end filtering timestamp Example:
            2020-12-31T23:59:59.123456Z.
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    criteria: Union[Unset, ApiManagedItemCriteria] = UNSET
    item: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    begin_timestamp: Union[Unset, datetime.datetime] = UNSET
    end_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        criteria: Union[Unset, str] = UNSET
        if not isinstance(self.criteria, Unset):
            criteria = self.criteria.value

        item = self.item

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        begin_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.begin_timestamp, Unset):
            begin_timestamp = self.begin_timestamp.isoformat()

        end_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.end_timestamp, Unset):
            end_timestamp = self.end_timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if criteria is not UNSET:
            field_dict["criteria"] = criteria
        if item is not UNSET:
            field_dict["item"] = item
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if begin_timestamp is not UNSET:
            field_dict["beginTimestamp"] = begin_timestamp
        if end_timestamp is not UNSET:
            field_dict["endTimestamp"] = end_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        _criteria = d.pop("criteria", UNSET)
        criteria: Union[Unset, ApiManagedItemCriteria]
        if _criteria and not isinstance(_criteria, Unset):
            criteria = ApiManagedItemCriteria(_criteria)

        else:
            criteria = UNSET

        item = d.pop("item", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if _created_timestamp and not isinstance(_created_timestamp, Unset):
            created_timestamp = isoparse(_created_timestamp)

        else:
            created_timestamp = UNSET

        _begin_timestamp = d.pop("beginTimestamp", UNSET)
        begin_timestamp: Union[Unset, datetime.datetime]
        if _begin_timestamp and not isinstance(_begin_timestamp, Unset):
            begin_timestamp = isoparse(_begin_timestamp)

        else:
            begin_timestamp = UNSET

        _end_timestamp = d.pop("endTimestamp", UNSET)
        end_timestamp: Union[Unset, datetime.datetime]
        if _end_timestamp and not isinstance(_end_timestamp, Unset):
            end_timestamp = isoparse(_end_timestamp)

        else:
            end_timestamp = UNSET

        api_managed_item = cls(
            id=id,
            uuid=uuid,
            criteria=criteria,
            item=item,
            created_timestamp=created_timestamp,
            begin_timestamp=begin_timestamp,
            end_timestamp=end_timestamp,
        )

        api_managed_item.additional_properties = d
        return api_managed_item

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
