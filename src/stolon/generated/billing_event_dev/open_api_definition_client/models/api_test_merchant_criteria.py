import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_test_merchant_criteria_type import ApiTestMerchantCriteriaType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiTestMerchantCriteria")


@_attrs_define
class ApiTestMerchantCriteria:
    """
    Attributes:
        id (Union[Unset, int]): Id of the test merchant criteria
        uuid (Union[Unset, str]): 26-character UUID of the test merchant criteria
        type_ (Union[Unset, ApiTestMerchantCriteriaType]):
        value (Union[Unset, str]): criteria value
        created_timestamp (Union[Unset, datetime.datetime]): created timestamp Example: 2020-12-31T23:59:59.123456Z.
        modified_timestamp (Union[Unset, datetime.datetime]): modified timestamp Example: 2020-12-31T23:59:59.123456Z.
        deleted_timestamp (Union[Unset, datetime.datetime]): deleted timestamp Example: 2020-12-31T23:59:59.123456Z.
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    type_: Union[Unset, ApiTestMerchantCriteriaType] = UNSET
    value: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    deleted_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

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
        if type_ is not UNSET:
            field_dict["type"] = type_
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

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ApiTestMerchantCriteriaType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ApiTestMerchantCriteriaType(_type_)

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

        api_test_merchant_criteria = cls(
            id=id,
            uuid=uuid,
            type_=type_,
            value=value,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
            deleted_timestamp=deleted_timestamp,
        )

        api_test_merchant_criteria.additional_properties = d
        return api_test_merchant_criteria

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
