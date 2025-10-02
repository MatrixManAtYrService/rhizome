import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiPlanActionFeeCode")


@_attrs_define
class ApiPlanActionFeeCode:
    """All plan action fee code records used by this plan pricing abstraction

    Attributes:
        id (Union[Unset, int]): Id of the plan-action-to-fee-code mapping
        uuid (Union[Unset, str]): 26-character UUID of the plan-action-to-fee-code mapping
        merchant_plan_uuid (Union[Unset, str]): 13-character UUID of the merchant plan that the plan-action-to-fee-code
            mapping applies to
        device_type (Union[Unset, str]): type of device that this plan-action-to-fee-code mapping applies to
        plan_action_type (Union[Unset, str]): defined plan action type value
        effective_date (Union[Unset, datetime.date]): effective date for the plan-action-to-fee-code mapping
        fee_category (Union[Unset, str]): fee category mapped to by the plan action
        fee_code (Union[Unset, str]): fee code mapped to by the plan action
        deleted_date (Union[Unset, datetime.date]): date the plan-action-to-fee-code mapping is no longer effective, or
            was logically deleted
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the plan-action-to-fee-code mapping was
            created Example: 2020-12-31T23:59:59.123456Z.
        modified_timestamp (Union[Unset, datetime.datetime]): date and time when the plan-action-to-fee-code mapping was
            last modified Example: 2020-12-31T23:59:59.123456Z.
        audit_id (Union[Unset, str]): identifier for the user who created or last modified this plan-action-to-fee-code
            mapping
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    merchant_plan_uuid: Union[Unset, str] = UNSET
    device_type: Union[Unset, str] = UNSET
    plan_action_type: Union[Unset, str] = UNSET
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

        merchant_plan_uuid = self.merchant_plan_uuid

        device_type = self.device_type

        plan_action_type = self.plan_action_type

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
        if merchant_plan_uuid is not UNSET:
            field_dict["merchantPlanUuid"] = merchant_plan_uuid
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if plan_action_type is not UNSET:
            field_dict["planActionType"] = plan_action_type
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

        merchant_plan_uuid = d.pop("merchantPlanUuid", UNSET)

        device_type = d.pop("deviceType", UNSET)

        plan_action_type = d.pop("planActionType", UNSET)

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

        api_plan_action_fee_code = cls(
            id=id,
            uuid=uuid,
            merchant_plan_uuid=merchant_plan_uuid,
            device_type=device_type,
            plan_action_type=plan_action_type,
            effective_date=effective_date,
            fee_category=fee_category,
            fee_code=fee_code,
            deleted_date=deleted_date,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
            audit_id=audit_id,
        )

        api_plan_action_fee_code.additional_properties = d
        return api_plan_action_fee_code

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
