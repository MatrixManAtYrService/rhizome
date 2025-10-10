import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiRevenueActionFeeCode")


@_attrs_define
class ApiRevenueActionFeeCode:
    """All revenue action fee code records used by this revenue share abstraction.

    Attributes:
        id (Union[Unset, int]): Id of the revenue-action-to-fee-code mapping
        uuid (Union[Unset, str]): 26-character UUID of the revenue-action-to-fee-code mapping
        fee_category_group (Union[Unset, str]): defined fee category grouping
        revenue_group (Union[Unset, str]): defined revenue group, or fee category sub-grouping
        revenue_share_group (Union[Unset, str]): group that the partners belong to for revenue share splits
        developer_uuid (Union[Unset, str]): 13-character UUID of the developer that the revenue-action-to-fee-code
            mapping applies to
        developer_app_uuid (Union[Unset, str]): 13-character UUID of the developer app that the revenue-action-to-fee-
            code mapping applies to
        app_subscription_uuid (Union[Unset, str]): 13-character UUID of the app subscription level that the revenue-
            action-to-fee-code mapping applies to
        app_metered_uuid (Union[Unset, str]): 13-character UUID of the app metered activity that the revenue-action-to-
            fee-code mapping applies to
        merchant_plan_uuid (Union[Unset, str]): 13-character UUID of the merchant plan that the revenue-action-to-fee-
            code mapping applies to
        revenue_action_type (Union[Unset, str]): defined revenue action type value
        effective_date (Union[Unset, datetime.date]): effective date for the revenue-action-to-fee-code mapping
        fee_category (Union[Unset, str]): fee category mapped to by revenue action
        fee_code (Union[Unset, str]): fee code mapped to by revenue action
        deleted_date (Union[Unset, datetime.date]): date the revenue-action-to-fee-code mapping is no longer effective,
            or was logically deleted
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the revenue action was created Example:
            2020-12-31T23:59:59.123456Z.
        modified_timestamp (Union[Unset, datetime.datetime]): date and time when the revenue action was last modified
            Example: 2020-12-31T23:59:59.123456Z.
        audit_id (Union[Unset, str]): identifier for the user who created or last modified this revenue-action-to-fee-
            code mapping
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    fee_category_group: Union[Unset, str] = UNSET
    revenue_group: Union[Unset, str] = UNSET
    revenue_share_group: Union[Unset, str] = UNSET
    developer_uuid: Union[Unset, str] = UNSET
    developer_app_uuid: Union[Unset, str] = UNSET
    app_subscription_uuid: Union[Unset, str] = UNSET
    app_metered_uuid: Union[Unset, str] = UNSET
    merchant_plan_uuid: Union[Unset, str] = UNSET
    revenue_action_type: Union[Unset, str] = UNSET
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

        fee_category_group = self.fee_category_group

        revenue_group = self.revenue_group

        revenue_share_group = self.revenue_share_group

        developer_uuid = self.developer_uuid

        developer_app_uuid = self.developer_app_uuid

        app_subscription_uuid = self.app_subscription_uuid

        app_metered_uuid = self.app_metered_uuid

        merchant_plan_uuid = self.merchant_plan_uuid

        revenue_action_type = self.revenue_action_type

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
        if fee_category_group is not UNSET:
            field_dict["feeCategoryGroup"] = fee_category_group
        if revenue_group is not UNSET:
            field_dict["revenueGroup"] = revenue_group
        if revenue_share_group is not UNSET:
            field_dict["revenueShareGroup"] = revenue_share_group
        if developer_uuid is not UNSET:
            field_dict["developerUuid"] = developer_uuid
        if developer_app_uuid is not UNSET:
            field_dict["developerAppUuid"] = developer_app_uuid
        if app_subscription_uuid is not UNSET:
            field_dict["appSubscriptionUuid"] = app_subscription_uuid
        if app_metered_uuid is not UNSET:
            field_dict["appMeteredUuid"] = app_metered_uuid
        if merchant_plan_uuid is not UNSET:
            field_dict["merchantPlanUuid"] = merchant_plan_uuid
        if revenue_action_type is not UNSET:
            field_dict["revenueActionType"] = revenue_action_type
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

        fee_category_group = d.pop("feeCategoryGroup", UNSET)

        revenue_group = d.pop("revenueGroup", UNSET)

        revenue_share_group = d.pop("revenueShareGroup", UNSET)

        developer_uuid = d.pop("developerUuid", UNSET)

        developer_app_uuid = d.pop("developerAppUuid", UNSET)

        app_subscription_uuid = d.pop("appSubscriptionUuid", UNSET)

        app_metered_uuid = d.pop("appMeteredUuid", UNSET)

        merchant_plan_uuid = d.pop("merchantPlanUuid", UNSET)

        revenue_action_type = d.pop("revenueActionType", UNSET)

        _effective_date = d.pop("effectiveDate", UNSET)
        effective_date: Union[Unset, datetime.date]
        if _effective_date and not isinstance(_effective_date, Unset):
            effective_date = isoparse(_effective_date).date()

        else:
            effective_date = UNSET

        fee_category = d.pop("feeCategory", UNSET)

        fee_code = d.pop("feeCode", UNSET)

        _deleted_date = d.pop("deletedDate", UNSET)
        deleted_date: Union[Unset, datetime.date]
        if _deleted_date and not isinstance(_deleted_date, Unset):
            deleted_date = isoparse(_deleted_date).date()

        else:
            deleted_date = UNSET

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if _created_timestamp and not isinstance(_created_timestamp, Unset):
            created_timestamp = isoparse(_created_timestamp)

        else:
            created_timestamp = UNSET

        _modified_timestamp = d.pop("modifiedTimestamp", UNSET)
        modified_timestamp: Union[Unset, datetime.datetime]
        if _modified_timestamp and not isinstance(_modified_timestamp, Unset):
            modified_timestamp = isoparse(_modified_timestamp)

        else:
            modified_timestamp = UNSET

        audit_id = d.pop("auditId", UNSET)

        api_revenue_action_fee_code = cls(
            id=id,
            uuid=uuid,
            fee_category_group=fee_category_group,
            revenue_group=revenue_group,
            revenue_share_group=revenue_share_group,
            developer_uuid=developer_uuid,
            developer_app_uuid=developer_app_uuid,
            app_subscription_uuid=app_subscription_uuid,
            app_metered_uuid=app_metered_uuid,
            merchant_plan_uuid=merchant_plan_uuid,
            revenue_action_type=revenue_action_type,
            effective_date=effective_date,
            fee_category=fee_category,
            fee_code=fee_code,
            deleted_date=deleted_date,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
            audit_id=audit_id,
        )

        api_revenue_action_fee_code.additional_properties = d
        return api_revenue_action_fee_code

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
