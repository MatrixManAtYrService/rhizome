import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiRevenueAction")


@_attrs_define
class ApiRevenueAction:
    """
    Attributes:
        tlement_action_uuid (Union[Unset, ApiRevenueAction]):
        id (Union[Unset, int]): Id of the revenue action
        uuid (Union[Unset, str]): 26-character UUID of the revenue action
        billing_entity_uuid (Union[Unset, str]): 26-character UUID of the billing entity this revenue action belongs to
        billing_entity_name (Union[Unset, str]): name of the billing entity
        entity_uuid (Union[Unset, str]): 13-character UUID of the actual entity that this billing entity represents
        fee_category_group (Union[Unset, str]): defined fee category grouping
        revenue_group (Union[Unset, str]): defined revenue group
        developer_uuid (Union[Unset, str]): 13-character UUID of the developer that the action applies to
        developer_app_uuid (Union[Unset, str]): 13-character UUID of the developer app that the action applies to
        app_subscription_uuid (Union[Unset, str]): 13-character UUID of the app subscription level that the action
            applies to
        app_metered_uuid (Union[Unset, str]): 13-character UUID of the app metered activity that the action applies to
        merchant_plan_uuid (Union[Unset, str]): 13-character UUID of the merchant plan that the action applies to
        revenue_action_type (Union[Unset, str]): defined revenue action type value
        fee_category (Union[Unset, str]): defined fee category value
        fee_code (Union[Unset, str]): defined fee code value
        action_date_time (Union[Unset, datetime.datetime]): date and time that the revenue action occurred Example:
            2020-12-31T23:59:59.123456Z.
        num_units (Union[Unset, int]): the number of billable units for the revenue action
        units_in_period (Union[Unset, int]): the number of billable units in the billing entity billing period
        basis_amount (Union[Unset, float]): the basis amount for the revenue action
        basis_currency (Union[Unset, str]): 3-letter currency code Example: USD.
        reference (Union[Unset, str]): freeform comment or reference identifier for this revenue action
        source_billing_entity_uuid (Union[Unset, str]): 26-character UUID of the billing entity that was the source of
            the revenue
        settlement_action_uuid (Union[Unset, str]): 26-character UUID of the settlement action that was the source of
            this revenue
        revenue_action_fee_code_uuid (Union[Unset, str]): 26-character UUID of the revenue-action-to-fee-code mapping
            used to create this action
        fee_uuid (Union[Unset, str]): 26-character UUID of the fee CTD or fee summary that this revenue action was
            applied towards
        event_uuid (Union[Unset, str]): 26-character UUID of the billing event that triggered this revenue action
        request_uuid (Union[Unset, str]): 26-character UUID of the billing request that posted this revenue action to
            the current-to-date totals
        posting_date (Union[Unset, datetime.date]): posting date
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the revenue action was created Example:
            2020-12-31T23:59:59.123456Z.
        modified_timestamp (Union[Unset, datetime.datetime]): date and time when the revenue action was last modified
            Example: 2020-12-31T23:59:59.123456Z.
    """

    tlement_action_uuid: Union[Unset, "ApiRevenueAction"] = UNSET
    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    billing_entity_uuid: Union[Unset, str] = UNSET
    billing_entity_name: Union[Unset, str] = UNSET
    entity_uuid: Union[Unset, str] = UNSET
    fee_category_group: Union[Unset, str] = UNSET
    revenue_group: Union[Unset, str] = UNSET
    developer_uuid: Union[Unset, str] = UNSET
    developer_app_uuid: Union[Unset, str] = UNSET
    app_subscription_uuid: Union[Unset, str] = UNSET
    app_metered_uuid: Union[Unset, str] = UNSET
    merchant_plan_uuid: Union[Unset, str] = UNSET
    revenue_action_type: Union[Unset, str] = UNSET
    fee_category: Union[Unset, str] = UNSET
    fee_code: Union[Unset, str] = UNSET
    action_date_time: Union[Unset, datetime.datetime] = UNSET
    num_units: Union[Unset, int] = UNSET
    units_in_period: Union[Unset, int] = UNSET
    basis_amount: Union[Unset, float] = UNSET
    basis_currency: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    source_billing_entity_uuid: Union[Unset, str] = UNSET
    settlement_action_uuid: Union[Unset, str] = UNSET
    revenue_action_fee_code_uuid: Union[Unset, str] = UNSET
    fee_uuid: Union[Unset, str] = UNSET
    event_uuid: Union[Unset, str] = UNSET
    request_uuid: Union[Unset, str] = UNSET
    posting_date: Union[Unset, datetime.date] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tlement_action_uuid: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tlement_action_uuid, Unset):
            tlement_action_uuid = self.tlement_action_uuid.to_dict()

        id = self.id

        uuid = self.uuid

        billing_entity_uuid = self.billing_entity_uuid

        billing_entity_name = self.billing_entity_name

        entity_uuid = self.entity_uuid

        fee_category_group = self.fee_category_group

        revenue_group = self.revenue_group

        developer_uuid = self.developer_uuid

        developer_app_uuid = self.developer_app_uuid

        app_subscription_uuid = self.app_subscription_uuid

        app_metered_uuid = self.app_metered_uuid

        merchant_plan_uuid = self.merchant_plan_uuid

        revenue_action_type = self.revenue_action_type

        fee_category = self.fee_category

        fee_code = self.fee_code

        action_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.action_date_time, Unset):
            action_date_time = self.action_date_time.isoformat()

        num_units = self.num_units

        units_in_period = self.units_in_period

        basis_amount = self.basis_amount

        basis_currency = self.basis_currency

        reference = self.reference

        source_billing_entity_uuid = self.source_billing_entity_uuid

        settlement_action_uuid = self.settlement_action_uuid

        revenue_action_fee_code_uuid = self.revenue_action_fee_code_uuid

        fee_uuid = self.fee_uuid

        event_uuid = self.event_uuid

        request_uuid = self.request_uuid

        posting_date: Union[Unset, str] = UNSET
        if not isinstance(self.posting_date, Unset):
            posting_date = self.posting_date.isoformat()

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        modified_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.modified_timestamp, Unset):
            modified_timestamp = self.modified_timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tlement_action_uuid is not UNSET:
            field_dict["tlementActionUuid"] = tlement_action_uuid
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if billing_entity_uuid is not UNSET:
            field_dict["billingEntityUuid"] = billing_entity_uuid
        if billing_entity_name is not UNSET:
            field_dict["billingEntityName"] = billing_entity_name
        if entity_uuid is not UNSET:
            field_dict["entityUuid"] = entity_uuid
        if fee_category_group is not UNSET:
            field_dict["feeCategoryGroup"] = fee_category_group
        if revenue_group is not UNSET:
            field_dict["revenueGroup"] = revenue_group
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
        if fee_category is not UNSET:
            field_dict["feeCategory"] = fee_category
        if fee_code is not UNSET:
            field_dict["feeCode"] = fee_code
        if action_date_time is not UNSET:
            field_dict["actionDateTime"] = action_date_time
        if num_units is not UNSET:
            field_dict["numUnits"] = num_units
        if units_in_period is not UNSET:
            field_dict["unitsInPeriod"] = units_in_period
        if basis_amount is not UNSET:
            field_dict["basisAmount"] = basis_amount
        if basis_currency is not UNSET:
            field_dict["basisCurrency"] = basis_currency
        if reference is not UNSET:
            field_dict["reference"] = reference
        if source_billing_entity_uuid is not UNSET:
            field_dict["sourceBillingEntityUuid"] = source_billing_entity_uuid
        if settlement_action_uuid is not UNSET:
            field_dict["settlementActionUuid"] = settlement_action_uuid
        if revenue_action_fee_code_uuid is not UNSET:
            field_dict["revenueActionFeeCodeUuid"] = revenue_action_fee_code_uuid
        if fee_uuid is not UNSET:
            field_dict["feeUuid"] = fee_uuid
        if event_uuid is not UNSET:
            field_dict["eventUuid"] = event_uuid
        if request_uuid is not UNSET:
            field_dict["requestUuid"] = request_uuid
        if posting_date is not UNSET:
            field_dict["postingDate"] = posting_date
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if modified_timestamp is not UNSET:
            field_dict["modifiedTimestamp"] = modified_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _tlement_action_uuid = d.pop("tlementActionUuid", UNSET)
        tlement_action_uuid: Union[Unset, ApiRevenueAction]
        if isinstance(_tlement_action_uuid, Unset):
            tlement_action_uuid = UNSET
        else:
            tlement_action_uuid = ApiRevenueAction.from_dict(_tlement_action_uuid)

        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        billing_entity_uuid = d.pop("billingEntityUuid", UNSET)

        billing_entity_name = d.pop("billingEntityName", UNSET)

        entity_uuid = d.pop("entityUuid", UNSET)

        fee_category_group = d.pop("feeCategoryGroup", UNSET)

        revenue_group = d.pop("revenueGroup", UNSET)

        developer_uuid = d.pop("developerUuid", UNSET)

        developer_app_uuid = d.pop("developerAppUuid", UNSET)

        app_subscription_uuid = d.pop("appSubscriptionUuid", UNSET)

        app_metered_uuid = d.pop("appMeteredUuid", UNSET)

        merchant_plan_uuid = d.pop("merchantPlanUuid", UNSET)

        revenue_action_type = d.pop("revenueActionType", UNSET)

        fee_category = d.pop("feeCategory", UNSET)

        fee_code = d.pop("feeCode", UNSET)

        _action_date_time = d.pop("actionDateTime", UNSET)
        action_date_time: Union[Unset, datetime.datetime]
        if isinstance(_action_date_time, Unset):
            action_date_time = UNSET
        else:
            action_date_time = isoparse(_action_date_time)

        num_units = d.pop("numUnits", UNSET)

        units_in_period = d.pop("unitsInPeriod", UNSET)

        basis_amount = d.pop("basisAmount", UNSET)

        basis_currency = d.pop("basisCurrency", UNSET)

        reference = d.pop("reference", UNSET)

        source_billing_entity_uuid = d.pop("sourceBillingEntityUuid", UNSET)

        settlement_action_uuid = d.pop("settlementActionUuid", UNSET)

        revenue_action_fee_code_uuid = d.pop("revenueActionFeeCodeUuid", UNSET)

        fee_uuid = d.pop("feeUuid", UNSET)

        event_uuid = d.pop("eventUuid", UNSET)

        request_uuid = d.pop("requestUuid", UNSET)

        _posting_date = d.pop("postingDate", UNSET)
        posting_date: Union[Unset, datetime.date]
        if isinstance(_posting_date, Unset):
            posting_date = UNSET
        else:
            posting_date = isoparse(_posting_date).date()

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

        api_revenue_action = cls(
            tlement_action_uuid=tlement_action_uuid,
            id=id,
            uuid=uuid,
            billing_entity_uuid=billing_entity_uuid,
            billing_entity_name=billing_entity_name,
            entity_uuid=entity_uuid,
            fee_category_group=fee_category_group,
            revenue_group=revenue_group,
            developer_uuid=developer_uuid,
            developer_app_uuid=developer_app_uuid,
            app_subscription_uuid=app_subscription_uuid,
            app_metered_uuid=app_metered_uuid,
            merchant_plan_uuid=merchant_plan_uuid,
            revenue_action_type=revenue_action_type,
            fee_category=fee_category,
            fee_code=fee_code,
            action_date_time=action_date_time,
            num_units=num_units,
            units_in_period=units_in_period,
            basis_amount=basis_amount,
            basis_currency=basis_currency,
            reference=reference,
            source_billing_entity_uuid=source_billing_entity_uuid,
            settlement_action_uuid=settlement_action_uuid,
            revenue_action_fee_code_uuid=revenue_action_fee_code_uuid,
            fee_uuid=fee_uuid,
            event_uuid=event_uuid,
            request_uuid=request_uuid,
            posting_date=posting_date,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
        )

        api_revenue_action.additional_properties = d
        return api_revenue_action

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
