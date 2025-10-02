import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiFeeCode")


@_attrs_define
class ApiFeeCode:
    """
    Attributes:
        id (Union[Unset, int]): Id of the fee code
        uuid (Union[Unset, str]): 26-character UUID of the fee code
        fee_category (Union[Unset, str]): defined fee category value
        fee_code (Union[Unset, str]): defined fee code value
        short_desc (Union[Unset, str]): short description of fee code
        full_desc (Union[Unset, str]): full description of fee code
        sort_order (Union[Unset, int]): sort order relative to other fee codes
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the fee code was created Example:
            2020-12-31T23:59:59.123456Z.
        modified_timestamp (Union[Unset, datetime.datetime]): date and time when the fee code was last modified Example:
            2020-12-31T23:59:59.123456Z.
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    fee_category: Union[Unset, str] = UNSET
    fee_code: Union[Unset, str] = UNSET
    short_desc: Union[Unset, str] = UNSET
    full_desc: Union[Unset, str] = UNSET
    sort_order: Union[Unset, int] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        fee_category = self.fee_category

        fee_code = self.fee_code

        short_desc = self.short_desc

        full_desc = self.full_desc

        sort_order = self.sort_order

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
        if fee_category is not UNSET:
            field_dict["feeCategory"] = fee_category
        if fee_code is not UNSET:
            field_dict["feeCode"] = fee_code
        if short_desc is not UNSET:
            field_dict["shortDesc"] = short_desc
        if full_desc is not UNSET:
            field_dict["fullDesc"] = full_desc
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
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

        fee_category = d.pop("feeCategory", UNSET)

        fee_code = d.pop("feeCode", UNSET)

        short_desc = d.pop("shortDesc", UNSET)

        full_desc = d.pop("fullDesc", UNSET)

        sort_order = d.pop("sortOrder", UNSET)

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

        api_fee_code = cls(
            id=id,
            uuid=uuid,
            fee_category=fee_category,
            fee_code=fee_code,
            short_desc=short_desc,
            full_desc=full_desc,
            sort_order=sort_order,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
        )

        api_fee_code.additional_properties = d
        return api_fee_code

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
