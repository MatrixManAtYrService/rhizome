import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AcceptanceQuery")


@_attrs_define
class AcceptanceQuery:
    """
    Attributes:
        include_deleted (Union[Unset, bool]):
        include_template (Union[Unset, bool]):
        modified_before (Union[Unset, datetime.datetime]):
        modified_after (Union[Unset, datetime.datetime]):
        created_before (Union[Unset, datetime.datetime]):
        created_after (Union[Unset, datetime.datetime]):
        type_ (Union[Unset, str]):
        action (Union[Unset, str]):
    """

    include_deleted: Union[Unset, bool] = UNSET
    include_template: Union[Unset, bool] = UNSET
    modified_before: Union[Unset, datetime.datetime] = UNSET
    modified_after: Union[Unset, datetime.datetime] = UNSET
    created_before: Union[Unset, datetime.datetime] = UNSET
    created_after: Union[Unset, datetime.datetime] = UNSET
    type_: Union[Unset, str] = UNSET
    action: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        include_deleted = self.include_deleted

        include_template = self.include_template

        modified_before: Union[Unset, str] = UNSET
        if not isinstance(self.modified_before, Unset):
            modified_before = self.modified_before.isoformat()

        modified_after: Union[Unset, str] = UNSET
        if not isinstance(self.modified_after, Unset):
            modified_after = self.modified_after.isoformat()

        created_before: Union[Unset, str] = UNSET
        if not isinstance(self.created_before, Unset):
            created_before = self.created_before.isoformat()

        created_after: Union[Unset, str] = UNSET
        if not isinstance(self.created_after, Unset):
            created_after = self.created_after.isoformat()

        type_ = self.type_

        action = self.action

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if include_deleted is not UNSET:
            field_dict["includeDeleted"] = include_deleted
        if include_template is not UNSET:
            field_dict["includeTemplate"] = include_template
        if modified_before is not UNSET:
            field_dict["modifiedBefore"] = modified_before
        if modified_after is not UNSET:
            field_dict["modifiedAfter"] = modified_after
        if created_before is not UNSET:
            field_dict["createdBefore"] = created_before
        if created_after is not UNSET:
            field_dict["createdAfter"] = created_after
        if type_ is not UNSET:
            field_dict["type"] = type_
        if action is not UNSET:
            field_dict["action"] = action

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        include_deleted = d.pop("includeDeleted", UNSET)

        include_template = d.pop("includeTemplate", UNSET)

        _modified_before = d.pop("modifiedBefore", UNSET)
        modified_before: Union[Unset, datetime.datetime]
        if _modified_before and not isinstance(_modified_before, Unset):
            modified_before = isoparse(_modified_before)

        else:
            modified_before = UNSET

        _modified_after = d.pop("modifiedAfter", UNSET)
        modified_after: Union[Unset, datetime.datetime]
        if _modified_after and not isinstance(_modified_after, Unset):
            modified_after = isoparse(_modified_after)

        else:
            modified_after = UNSET

        _created_before = d.pop("createdBefore", UNSET)
        created_before: Union[Unset, datetime.datetime]
        if _created_before and not isinstance(_created_before, Unset):
            created_before = isoparse(_created_before)

        else:
            created_before = UNSET

        _created_after = d.pop("createdAfter", UNSET)
        created_after: Union[Unset, datetime.datetime]
        if _created_after and not isinstance(_created_after, Unset):
            created_after = isoparse(_created_after)

        else:
            created_after = UNSET

        type_ = d.pop("type", UNSET)

        action = d.pop("action", UNSET)

        acceptance_query = cls(
            include_deleted=include_deleted,
            include_template=include_template,
            modified_before=modified_before,
            modified_after=modified_after,
            created_before=created_before,
            created_after=created_after,
            type_=type_,
            action=action,
        )

        acceptance_query.additional_properties = d
        return acceptance_query

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
