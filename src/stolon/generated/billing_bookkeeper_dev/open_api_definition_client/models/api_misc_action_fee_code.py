import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiMiscActionFeeCode")


@_attrs_define
class ApiMiscActionFeeCode:
    """
    Attributes:
        id (Union[Unset, int]): Id of the miscellaneous-action-to-fee-code mapping
        uuid (Union[Unset, str]): 26-character UUID of the miscellaneous-action-to-fee-code mapping
        misc_specifier (Union[Unset, str]): code that specifies, or qualifies, the miscellaneous action
        misc_action_type (Union[Unset, str]): defined miscellaneous action type value
        effective_date (Union[Unset, datetime.date]): effective date for the miscellaneous-action-to-fee-code mapping
        fee_category (Union[Unset, str]): fee category mapped to by the miscellaneous action
        fee_code (Union[Unset, str]): fee code mapped to by the miscellaneous action
        deleted_date (Union[Unset, datetime.date]): date the miscellaneous-action-to-fee-code mapping is no longer
            effective, or was logically deleted
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the miscellaneous-action-to-fee-code
            mapping was created Example: 2020-12-31T23:59:59.123456Z.
        modified_timestamp (Union[Unset, datetime.datetime]): date and time when the miscellaneous-action-to-fee-code
            mapping was last modified Example: 2020-12-31T23:59:59.123456Z.
        audit_id (Union[Unset, str]): identifier for the user who created or last modified this misc-action-to-fee-code
            mapping
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    misc_specifier: Union[Unset, str] = UNSET
    misc_action_type: Union[Unset, str] = UNSET
    effective_date: Union[Unset, datetime.date] = UNSET
    fee_category: Union[Unset, str] = UNSET
    fee_code: Union[Unset, str] = UNSET
    deleted_date: Union[Unset, datetime.date] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    audit_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        misc_specifier = self.misc_specifier

        misc_action_type = self.misc_action_type

        effective_date: Union[Unset, str] = UNSET
        if not isinstance(self.effective_date, Unset):
            effective_date = self.effective_date.isoformat()

        fee_category = self.fee_category

        fee_code = self.fee_code

        deleted_date: Union[Unset, str] = UNSET
        if not isinstance(self.deleted_date, Unset):
            deleted_date = self.deleted_date.isoformat()

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        modified_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.modified_timestamp, Unset):
            modified_timestamp = self.modified_timestamp.isoformat()

        audit_id = self.audit_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if misc_specifier is not UNSET:
            field_dict["miscSpecifier"] = misc_specifier
        if misc_action_type is not UNSET:
            field_dict["miscActionType"] = misc_action_type
        if effective_date is not UNSET:
            field_dict["effectiveDate"] = effective_date
        if fee_category is not UNSET:
            field_dict["feeCategory"] = fee_category
        if fee_code is not UNSET:
            field_dict["feeCode"] = fee_code
        if deleted_date is not UNSET:
            field_dict["deletedDate"] = deleted_date
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if modified_timestamp is not UNSET:
            field_dict["modifiedTimestamp"] = modified_timestamp
        if audit_id is not UNSET:
            field_dict["auditId"] = audit_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        misc_specifier = d.pop("miscSpecifier", UNSET)

        misc_action_type = d.pop("miscActionType", UNSET)

        _effective_date = d.pop("effectiveDate", UNSET)
        effective_date: Union[Unset, datetime.date]
        if isinstance(_effective_date, Unset):
            effective_date = UNSET
        else:
            effective_date = isoparse(_effective_date).date()

        fee_category = d.pop("feeCategory", UNSET)

        fee_code = d.pop("feeCode", UNSET)

        _deleted_date = d.pop("deletedDate", UNSET)
        deleted_date: Union[Unset, datetime.date]
        if isinstance(_deleted_date, Unset):
            deleted_date = UNSET
        else:
            deleted_date = isoparse(_deleted_date).date()

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

        audit_id = d.pop("auditId", UNSET)

        api_misc_action_fee_code = cls(
            id=id,
            uuid=uuid,
            misc_specifier=misc_specifier,
            misc_action_type=misc_action_type,
            effective_date=effective_date,
            fee_category=fee_category,
            fee_code=fee_code,
            deleted_date=deleted_date,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
            audit_id=audit_id,
        )

        api_misc_action_fee_code.additional_properties = d
        return api_misc_action_fee_code

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
