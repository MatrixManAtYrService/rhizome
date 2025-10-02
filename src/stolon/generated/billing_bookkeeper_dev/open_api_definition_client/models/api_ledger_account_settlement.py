import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiLedgerAccountSettlement")


@_attrs_define
class ApiLedgerAccountSettlement:
    """
    Attributes:
        tlement_item_code (Union[Unset, ApiLedgerAccountSettlement]):
        tlement_desc (Union[Unset, ApiLedgerAccountSettlement]):
        id (Union[Unset, int]): Id of the ledger-account-settlement data
        uuid (Union[Unset, str]): 26-character UUID of the ledger-account-settlement data
        ledger_account_key (Union[Unset, str]): the ledger account key that this ledger-account-settlement data is for
        effective_date (Union[Unset, datetime.date]): effective date for the ledger-account-settlement data
        settlement_item_code (Union[Unset, str]): item identifier used to itemize settlement transactions with external
            parties
        settlement_desc (Union[Unset, str]): a description of the settlement items associated with the ledger account
            key
        fee_category_group (Union[Unset, str]): the fee category grouping that should be used for settlement items
        revenue_group (Union[Unset, str]): the revenue group that should be used to sub-categorize settled revenue
        merchant_plan_uuid (Union[Unset, str]): 13-character UUID of the merchant plan that identifies settlement items
            associated with the ledger account key
        developer_uuid (Union[Unset, str]): 13-character UUID of the developer or vendor that identifies settlement
            items associated with the ledger account key
        developer_app_uuid (Union[Unset, str]): 13-character UUID of the developer app that identifies settlement items
            associated with the ledger account key
        app_subscription_uuid (Union[Unset, str]): 13-character UUID of the app subscription level that identifies
            settlement items associated with the ledger account key
        app_metered_uuid (Union[Unset, str]): 13-character UUID of the app metered activity type that identifies
            settlement items associated with the ledger account key
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the ledger account settlement was
            created Example: 2020-12-31T23:59:59.123456Z.
        modified_timestamp (Union[Unset, datetime.datetime]): date and time when the ledger account settlement was last
            modified Example: 2020-12-31T23:59:59.123456Z.
        audit_id (Union[Unset, str]): identifier for the user who created or last modified this ledger-account-
            settlement data
    """

    tlement_item_code: Union[Unset, "ApiLedgerAccountSettlement"] = UNSET
    tlement_desc: Union[Unset, "ApiLedgerAccountSettlement"] = UNSET
    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    ledger_account_key: Union[Unset, str] = UNSET
    effective_date: Union[Unset, datetime.date] = UNSET
    settlement_item_code: Union[Unset, str] = UNSET
    settlement_desc: Union[Unset, str] = UNSET
    fee_category_group: Union[Unset, str] = UNSET
    revenue_group: Union[Unset, str] = UNSET
    merchant_plan_uuid: Union[Unset, str] = UNSET
    developer_uuid: Union[Unset, str] = UNSET
    developer_app_uuid: Union[Unset, str] = UNSET
    app_subscription_uuid: Union[Unset, str] = UNSET
    app_metered_uuid: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    audit_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tlement_item_code: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tlement_item_code, Unset):
            tlement_item_code = self.tlement_item_code.to_dict()

        tlement_desc: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tlement_desc, Unset):
            tlement_desc = self.tlement_desc.to_dict()

        id = self.id

        uuid = self.uuid

        ledger_account_key = self.ledger_account_key

        effective_date: Union[Unset, str] = UNSET
        if not isinstance(self.effective_date, Unset):
            effective_date = self.effective_date.isoformat()

        settlement_item_code = self.settlement_item_code

        settlement_desc = self.settlement_desc

        fee_category_group = self.fee_category_group

        revenue_group = self.revenue_group

        merchant_plan_uuid = self.merchant_plan_uuid

        developer_uuid = self.developer_uuid

        developer_app_uuid = self.developer_app_uuid

        app_subscription_uuid = self.app_subscription_uuid

        app_metered_uuid = self.app_metered_uuid

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
        if tlement_item_code is not UNSET:
            field_dict["tlementItemCode"] = tlement_item_code
        if tlement_desc is not UNSET:
            field_dict["tlementDesc"] = tlement_desc
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if ledger_account_key is not UNSET:
            field_dict["ledgerAccountKey"] = ledger_account_key
        if effective_date is not UNSET:
            field_dict["effectiveDate"] = effective_date
        if settlement_item_code is not UNSET:
            field_dict["settlementItemCode"] = settlement_item_code
        if settlement_desc is not UNSET:
            field_dict["settlementDesc"] = settlement_desc
        if fee_category_group is not UNSET:
            field_dict["feeCategoryGroup"] = fee_category_group
        if revenue_group is not UNSET:
            field_dict["revenueGroup"] = revenue_group
        if merchant_plan_uuid is not UNSET:
            field_dict["merchantPlanUuid"] = merchant_plan_uuid
        if developer_uuid is not UNSET:
            field_dict["developerUuid"] = developer_uuid
        if developer_app_uuid is not UNSET:
            field_dict["developerAppUuid"] = developer_app_uuid
        if app_subscription_uuid is not UNSET:
            field_dict["appSubscriptionUuid"] = app_subscription_uuid
        if app_metered_uuid is not UNSET:
            field_dict["appMeteredUuid"] = app_metered_uuid
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
        _tlement_item_code = d.pop("tlementItemCode", UNSET)
        tlement_item_code: Union[Unset, ApiLedgerAccountSettlement]
        if isinstance(_tlement_item_code, Unset):
            tlement_item_code = UNSET
        else:
            tlement_item_code = ApiLedgerAccountSettlement.from_dict(_tlement_item_code)

        _tlement_desc = d.pop("tlementDesc", UNSET)
        tlement_desc: Union[Unset, ApiLedgerAccountSettlement]
        if isinstance(_tlement_desc, Unset):
            tlement_desc = UNSET
        else:
            tlement_desc = ApiLedgerAccountSettlement.from_dict(_tlement_desc)

        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        ledger_account_key = d.pop("ledgerAccountKey", UNSET)

        _effective_date = d.pop("effectiveDate", UNSET)
        effective_date: Union[Unset, datetime.date]
        if isinstance(_effective_date, Unset):
            effective_date = UNSET
        else:
            effective_date = isoparse(_effective_date).date()

        settlement_item_code = d.pop("settlementItemCode", UNSET)

        settlement_desc = d.pop("settlementDesc", UNSET)

        fee_category_group = d.pop("feeCategoryGroup", UNSET)

        revenue_group = d.pop("revenueGroup", UNSET)

        merchant_plan_uuid = d.pop("merchantPlanUuid", UNSET)

        developer_uuid = d.pop("developerUuid", UNSET)

        developer_app_uuid = d.pop("developerAppUuid", UNSET)

        app_subscription_uuid = d.pop("appSubscriptionUuid", UNSET)

        app_metered_uuid = d.pop("appMeteredUuid", UNSET)

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

        api_ledger_account_settlement = cls(
            tlement_item_code=tlement_item_code,
            tlement_desc=tlement_desc,
            id=id,
            uuid=uuid,
            ledger_account_key=ledger_account_key,
            effective_date=effective_date,
            settlement_item_code=settlement_item_code,
            settlement_desc=settlement_desc,
            fee_category_group=fee_category_group,
            revenue_group=revenue_group,
            merchant_plan_uuid=merchant_plan_uuid,
            developer_uuid=developer_uuid,
            developer_app_uuid=developer_app_uuid,
            app_subscription_uuid=app_subscription_uuid,
            app_metered_uuid=app_metered_uuid,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
            audit_id=audit_id,
        )

        api_ledger_account_settlement.additional_properties = d
        return api_ledger_account_settlement

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
