import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LexiAttributeDTO")


@_attrs_define
class LexiAttributeDTO:
    """
    Attributes:
        id (Union[Unset, int]):
        uuid (Union[Unset, str]):
        word (Union[Unset, str]):
        lexicon (Union[Unset, str]):
        attr_name (Union[Unset, str]):
        created_timestamp (Union[Unset, datetime.datetime]):
        deleted_timestamp (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    word: Union[Unset, str] = UNSET
    lexicon: Union[Unset, str] = UNSET
    attr_name: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    deleted_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        word = self.word

        lexicon = self.lexicon

        attr_name = self.attr_name

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

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
        if word is not UNSET:
            field_dict["word"] = word
        if lexicon is not UNSET:
            field_dict["lexicon"] = lexicon
        if attr_name is not UNSET:
            field_dict["attrName"] = attr_name
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if deleted_timestamp is not UNSET:
            field_dict["deletedTimestamp"] = deleted_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        word = d.pop("word", UNSET)

        lexicon = d.pop("lexicon", UNSET)

        attr_name = d.pop("attrName", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_created_timestamp, Unset):
            created_timestamp = UNSET
        else:
            created_timestamp = isoparse(_created_timestamp)

        _deleted_timestamp = d.pop("deletedTimestamp", UNSET)
        deleted_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_deleted_timestamp, Unset):
            deleted_timestamp = UNSET
        else:
            deleted_timestamp = isoparse(_deleted_timestamp)

        lexi_attribute_dto = cls(
            id=id,
            uuid=uuid,
            word=word,
            lexicon=lexicon,
            attr_name=attr_name,
            created_timestamp=created_timestamp,
            deleted_timestamp=deleted_timestamp,
        )

        lexi_attribute_dto.additional_properties = d
        return lexi_attribute_dto

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
