import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="BaseRule")


@_attrs_define
class BaseRule:
    """
    Attributes:
        uuid (Union[Unset, str]):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        lexicon (Union[Unset, str]):
        priority (Union[Unset, int]):
        rule_type (Union[Unset, str]):
        created_timestamp (Union[Unset, datetime.datetime]):
        deleted_timestamp (Union[Unset, datetime.datetime]):
    """

    uuid: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    lexicon: Union[Unset, str] = UNSET
    priority: Union[Unset, int] = UNSET
    rule_type: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    deleted_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        name = self.name

        description = self.description

        lexicon = self.lexicon

        priority = self.priority

        rule_type = self.rule_type

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        deleted_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.deleted_timestamp, Unset):
            deleted_timestamp = self.deleted_timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if lexicon is not UNSET:
            field_dict["lexicon"] = lexicon
        if priority is not UNSET:
            field_dict["priority"] = priority
        if rule_type is not UNSET:
            field_dict["ruleType"] = rule_type
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if deleted_timestamp is not UNSET:
            field_dict["deletedTimestamp"] = deleted_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = d.pop("uuid", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        lexicon = d.pop("lexicon", UNSET)

        priority = d.pop("priority", UNSET)

        rule_type = d.pop("ruleType", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if _created_timestamp and not isinstance(_created_timestamp, Unset):
            created_timestamp = isoparse(_created_timestamp)

        else:
            created_timestamp = UNSET

        _deleted_timestamp = d.pop("deletedTimestamp", UNSET)
        deleted_timestamp: Union[Unset, datetime.datetime]
        if _deleted_timestamp and not isinstance(_deleted_timestamp, Unset):
            deleted_timestamp = isoparse(_deleted_timestamp)

        else:
            deleted_timestamp = UNSET

        base_rule = cls(
            uuid=uuid,
            name=name,
            description=description,
            lexicon=lexicon,
            priority=priority,
            rule_type=rule_type,
            created_timestamp=created_timestamp,
            deleted_timestamp=deleted_timestamp,
        )

        base_rule.additional_properties = d
        return base_rule

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
