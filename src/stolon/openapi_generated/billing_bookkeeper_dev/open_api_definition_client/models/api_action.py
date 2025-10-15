import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiAction")


@_attrs_define
class ApiAction:
    """
    Attributes:
        tlement_action_uuid (Union[Unset, ApiAction]):
        id (Union[Unset, int]): Id of action
        action_uuid (Union[Unset, str]): 26-character UUID of action
        action_type (Union[Unset, str]): defined action type value
        action_source (Union[Unset, str]): source of action (action type) ex. PLAN, APP_SUB, APP_METER, CELLULAR, MISC,
            REVENUE
        fee_category (Union[Unset, str]): fee category mapped to by the action
        fee_code (Union[Unset, str]): fee code value
        num_units (Union[Unset, int]): the number of billable units for the action
        units_in_period (Union[Unset, int]): the number of billable units in the billing entity billing period
        basis_amount (Union[Unset, float]): the basis amount for the action
        basis_currency (Union[Unset, str]): 3-letter currency code
        action_date_time (Union[Unset, datetime.datetime]): date and time that the action occurred
        posting_date (Union[Unset, datetime.date]): posting date
        fee_uuid (Union[Unset, str]): 26-character UUID of the fee CTD or fee summary that this action was applied
            towards
        reference (Union[Unset, str]): freeform comment or reference identifier for this action
        merchant_plan_uuid (Union[Unset, str]): current merchant's plan at time of action
        serial_number (Union[Unset, str]): Device of action serial number
        plan_action_type (Union[Unset, str]): Plan action
        plan_action_fee_code_uuid (Union[Unset, str]): Plan action fee code ID
        developer_app_uuid (Union[Unset, str]): App's ID
        app_subscription_uuid (Union[Unset, str]): App subscription's ID
        app_sub_action_type (Union[Unset, str]): App subscription action
        app_sub_action_fee_code_uuid (Union[Unset, str]): App subscriptions fee code ID
        app_metered_uuid (Union[Unset, str]): Metered app ID
        app_meter_action_type (Union[Unset, str]): Metered app type
        app_meter_action_fee_code_uuid (Union[Unset, str]): Metered app fee code ID
        iccid (Union[Unset, str]): Cellular ICCID of SIM
        carrier (Union[Unset, str]): For cellular actions, the carrier for cell service.
        cellular_action_type (Union[Unset, str]): Cellular action type
        cellular_action_fee_code_uuid (Union[Unset, str]): Cellular action fee code ID
        misc_action_type (Union[Unset, str]): Misc action type
        misc_specifier (Union[Unset, str]): Misc specifier
        misc_action_fee_code_uuid (Union[Unset, str]): Misc action fee code ID
        fee_category_group (Union[Unset, str]): Fee category group
        revenue_group (Union[Unset, str]): Revenue group
        developer_uuid (Union[Unset, str]): Developer ID
        revenue_action_type (Union[Unset, str]): Revenue action type
        revenue_action_fee_code_uuid (Union[Unset, str]): Revenue action fee code ID
        source_billing_entity_uuid (Union[Unset, str]): Source billing entity ID
        settlement_action_uuid (Union[Unset, str]): Settlement action ID
    """

    tlement_action_uuid: Union[Unset, "ApiAction"] = UNSET
    id: Union[Unset, int] = UNSET
    action_uuid: Union[Unset, str] = UNSET
    action_type: Union[Unset, str] = UNSET
    action_source: Union[Unset, str] = UNSET
    fee_category: Union[Unset, str] = UNSET
    fee_code: Union[Unset, str] = UNSET
    num_units: Union[Unset, int] = UNSET
    units_in_period: Union[Unset, int] = UNSET
    basis_amount: Union[Unset, float] = UNSET
    basis_currency: Union[Unset, str] = UNSET
    action_date_time: Union[Unset, datetime.datetime] = UNSET
    posting_date: Union[Unset, datetime.date] = UNSET
    fee_uuid: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    merchant_plan_uuid: Union[Unset, str] = UNSET
    serial_number: Union[Unset, str] = UNSET
    plan_action_type: Union[Unset, str] = UNSET
    plan_action_fee_code_uuid: Union[Unset, str] = UNSET
    developer_app_uuid: Union[Unset, str] = UNSET
    app_subscription_uuid: Union[Unset, str] = UNSET
    app_sub_action_type: Union[Unset, str] = UNSET
    app_sub_action_fee_code_uuid: Union[Unset, str] = UNSET
    app_metered_uuid: Union[Unset, str] = UNSET
    app_meter_action_type: Union[Unset, str] = UNSET
    app_meter_action_fee_code_uuid: Union[Unset, str] = UNSET
    iccid: Union[Unset, str] = UNSET
    carrier: Union[Unset, str] = UNSET
    cellular_action_type: Union[Unset, str] = UNSET
    cellular_action_fee_code_uuid: Union[Unset, str] = UNSET
    misc_action_type: Union[Unset, str] = UNSET
    misc_specifier: Union[Unset, str] = UNSET
    misc_action_fee_code_uuid: Union[Unset, str] = UNSET
    fee_category_group: Union[Unset, str] = UNSET
    revenue_group: Union[Unset, str] = UNSET
    developer_uuid: Union[Unset, str] = UNSET
    revenue_action_type: Union[Unset, str] = UNSET
    revenue_action_fee_code_uuid: Union[Unset, str] = UNSET
    source_billing_entity_uuid: Union[Unset, str] = UNSET
    settlement_action_uuid: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tlement_action_uuid: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tlement_action_uuid, Unset):
            tlement_action_uuid = self.tlement_action_uuid.to_dict()

        id = self.id

        action_uuid = self.action_uuid

        action_type = self.action_type

        action_source = self.action_source

        fee_category = self.fee_category

        fee_code = self.fee_code

        num_units = self.num_units

        units_in_period = self.units_in_period

        basis_amount = self.basis_amount

        basis_currency = self.basis_currency

        action_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.action_date_time, Unset):
            action_date_time = self.action_date_time.isoformat()

        posting_date: Union[Unset, str] = UNSET
        if not isinstance(self.posting_date, Unset):
            posting_date = self.posting_date.isoformat()

        fee_uuid = self.fee_uuid

        reference = self.reference

        merchant_plan_uuid = self.merchant_plan_uuid

        serial_number = self.serial_number

        plan_action_type = self.plan_action_type

        plan_action_fee_code_uuid = self.plan_action_fee_code_uuid

        developer_app_uuid = self.developer_app_uuid

        app_subscription_uuid = self.app_subscription_uuid

        app_sub_action_type = self.app_sub_action_type

        app_sub_action_fee_code_uuid = self.app_sub_action_fee_code_uuid

        app_metered_uuid = self.app_metered_uuid

        app_meter_action_type = self.app_meter_action_type

        app_meter_action_fee_code_uuid = self.app_meter_action_fee_code_uuid

        iccid = self.iccid

        carrier = self.carrier

        cellular_action_type = self.cellular_action_type

        cellular_action_fee_code_uuid = self.cellular_action_fee_code_uuid

        misc_action_type = self.misc_action_type

        misc_specifier = self.misc_specifier

        misc_action_fee_code_uuid = self.misc_action_fee_code_uuid

        fee_category_group = self.fee_category_group

        revenue_group = self.revenue_group

        developer_uuid = self.developer_uuid

        revenue_action_type = self.revenue_action_type

        revenue_action_fee_code_uuid = self.revenue_action_fee_code_uuid

        source_billing_entity_uuid = self.source_billing_entity_uuid

        settlement_action_uuid = self.settlement_action_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tlement_action_uuid is not UNSET:
            field_dict["tlementActionUuid"] = tlement_action_uuid
        if id is not UNSET:
            field_dict["id"] = id
        if action_uuid is not UNSET:
            field_dict["actionUuid"] = action_uuid
        if action_type is not UNSET:
            field_dict["actionType"] = action_type
        if action_source is not UNSET:
            field_dict["actionSource"] = action_source
        if fee_category is not UNSET:
            field_dict["feeCategory"] = fee_category
        if fee_code is not UNSET:
            field_dict["feeCode"] = fee_code
        if num_units is not UNSET:
            field_dict["numUnits"] = num_units
        if units_in_period is not UNSET:
            field_dict["unitsInPeriod"] = units_in_period
        if basis_amount is not UNSET:
            field_dict["basisAmount"] = basis_amount
        if basis_currency is not UNSET:
            field_dict["basisCurrency"] = basis_currency
        if action_date_time is not UNSET:
            field_dict["actionDateTime"] = action_date_time
        if posting_date is not UNSET:
            field_dict["postingDate"] = posting_date
        if fee_uuid is not UNSET:
            field_dict["feeUuid"] = fee_uuid
        if reference is not UNSET:
            field_dict["reference"] = reference
        if merchant_plan_uuid is not UNSET:
            field_dict["merchantPlanUuid"] = merchant_plan_uuid
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if plan_action_type is not UNSET:
            field_dict["planActionType"] = plan_action_type
        if plan_action_fee_code_uuid is not UNSET:
            field_dict["planActionFeeCodeUuid"] = plan_action_fee_code_uuid
        if developer_app_uuid is not UNSET:
            field_dict["developerAppUuid"] = developer_app_uuid
        if app_subscription_uuid is not UNSET:
            field_dict["appSubscriptionUuid"] = app_subscription_uuid
        if app_sub_action_type is not UNSET:
            field_dict["appSubActionType"] = app_sub_action_type
        if app_sub_action_fee_code_uuid is not UNSET:
            field_dict["appSubActionFeeCodeUuid"] = app_sub_action_fee_code_uuid
        if app_metered_uuid is not UNSET:
            field_dict["appMeteredUuid"] = app_metered_uuid
        if app_meter_action_type is not UNSET:
            field_dict["appMeterActionType"] = app_meter_action_type
        if app_meter_action_fee_code_uuid is not UNSET:
            field_dict["appMeterActionFeeCodeUuid"] = app_meter_action_fee_code_uuid
        if iccid is not UNSET:
            field_dict["iccid"] = iccid
        if carrier is not UNSET:
            field_dict["carrier"] = carrier
        if cellular_action_type is not UNSET:
            field_dict["cellularActionType"] = cellular_action_type
        if cellular_action_fee_code_uuid is not UNSET:
            field_dict["cellularActionFeeCodeUuid"] = cellular_action_fee_code_uuid
        if misc_action_type is not UNSET:
            field_dict["miscActionType"] = misc_action_type
        if misc_specifier is not UNSET:
            field_dict["miscSpecifier"] = misc_specifier
        if misc_action_fee_code_uuid is not UNSET:
            field_dict["miscActionFeeCodeUuid"] = misc_action_fee_code_uuid
        if fee_category_group is not UNSET:
            field_dict["feeCategoryGroup"] = fee_category_group
        if revenue_group is not UNSET:
            field_dict["revenueGroup"] = revenue_group
        if developer_uuid is not UNSET:
            field_dict["developerUuid"] = developer_uuid
        if revenue_action_type is not UNSET:
            field_dict["revenueActionType"] = revenue_action_type
        if revenue_action_fee_code_uuid is not UNSET:
            field_dict["revenueActionFeeCodeUuid"] = revenue_action_fee_code_uuid
        if source_billing_entity_uuid is not UNSET:
            field_dict["sourceBillingEntityUuid"] = source_billing_entity_uuid
        if settlement_action_uuid is not UNSET:
            field_dict["settlementActionUuid"] = settlement_action_uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _tlement_action_uuid = d.pop("tlementActionUuid", UNSET)
        tlement_action_uuid: Union[Unset, ApiAction]
        if _tlement_action_uuid and not isinstance(_tlement_action_uuid, Unset):
            tlement_action_uuid = ApiAction.from_dict(_tlement_action_uuid)

        else:
            tlement_action_uuid = UNSET

        id = d.pop("id", UNSET)

        action_uuid = d.pop("actionUuid", UNSET)

        action_type = d.pop("actionType", UNSET)

        action_source = d.pop("actionSource", UNSET)

        fee_category = d.pop("feeCategory", UNSET)

        fee_code = d.pop("feeCode", UNSET)

        num_units = d.pop("numUnits", UNSET)

        units_in_period = d.pop("unitsInPeriod", UNSET)

        basis_amount = d.pop("basisAmount", UNSET)

        basis_currency = d.pop("basisCurrency", UNSET)

        _action_date_time = d.pop("actionDateTime", UNSET)
        action_date_time: Union[Unset, datetime.datetime]
        if _action_date_time and not isinstance(_action_date_time, Unset):
            action_date_time = isoparse(_action_date_time)

        else:
            action_date_time = UNSET

        _posting_date = d.pop("postingDate", UNSET)
        posting_date: Union[Unset, datetime.date]
        if _posting_date and not isinstance(_posting_date, Unset):
            posting_date = isoparse(_posting_date).date()

        else:
            posting_date = UNSET

        fee_uuid = d.pop("feeUuid", UNSET)

        reference = d.pop("reference", UNSET)

        merchant_plan_uuid = d.pop("merchantPlanUuid", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        plan_action_type = d.pop("planActionType", UNSET)

        plan_action_fee_code_uuid = d.pop("planActionFeeCodeUuid", UNSET)

        developer_app_uuid = d.pop("developerAppUuid", UNSET)

        app_subscription_uuid = d.pop("appSubscriptionUuid", UNSET)

        app_sub_action_type = d.pop("appSubActionType", UNSET)

        app_sub_action_fee_code_uuid = d.pop("appSubActionFeeCodeUuid", UNSET)

        app_metered_uuid = d.pop("appMeteredUuid", UNSET)

        app_meter_action_type = d.pop("appMeterActionType", UNSET)

        app_meter_action_fee_code_uuid = d.pop("appMeterActionFeeCodeUuid", UNSET)

        iccid = d.pop("iccid", UNSET)

        carrier = d.pop("carrier", UNSET)

        cellular_action_type = d.pop("cellularActionType", UNSET)

        cellular_action_fee_code_uuid = d.pop("cellularActionFeeCodeUuid", UNSET)

        misc_action_type = d.pop("miscActionType", UNSET)

        misc_specifier = d.pop("miscSpecifier", UNSET)

        misc_action_fee_code_uuid = d.pop("miscActionFeeCodeUuid", UNSET)

        fee_category_group = d.pop("feeCategoryGroup", UNSET)

        revenue_group = d.pop("revenueGroup", UNSET)

        developer_uuid = d.pop("developerUuid", UNSET)

        revenue_action_type = d.pop("revenueActionType", UNSET)

        revenue_action_fee_code_uuid = d.pop("revenueActionFeeCodeUuid", UNSET)

        source_billing_entity_uuid = d.pop("sourceBillingEntityUuid", UNSET)

        settlement_action_uuid = d.pop("settlementActionUuid", UNSET)

        api_action = cls(
            tlement_action_uuid=tlement_action_uuid,
            id=id,
            action_uuid=action_uuid,
            action_type=action_type,
            action_source=action_source,
            fee_category=fee_category,
            fee_code=fee_code,
            num_units=num_units,
            units_in_period=units_in_period,
            basis_amount=basis_amount,
            basis_currency=basis_currency,
            action_date_time=action_date_time,
            posting_date=posting_date,
            fee_uuid=fee_uuid,
            reference=reference,
            merchant_plan_uuid=merchant_plan_uuid,
            serial_number=serial_number,
            plan_action_type=plan_action_type,
            plan_action_fee_code_uuid=plan_action_fee_code_uuid,
            developer_app_uuid=developer_app_uuid,
            app_subscription_uuid=app_subscription_uuid,
            app_sub_action_type=app_sub_action_type,
            app_sub_action_fee_code_uuid=app_sub_action_fee_code_uuid,
            app_metered_uuid=app_metered_uuid,
            app_meter_action_type=app_meter_action_type,
            app_meter_action_fee_code_uuid=app_meter_action_fee_code_uuid,
            iccid=iccid,
            carrier=carrier,
            cellular_action_type=cellular_action_type,
            cellular_action_fee_code_uuid=cellular_action_fee_code_uuid,
            misc_action_type=misc_action_type,
            misc_specifier=misc_specifier,
            misc_action_fee_code_uuid=misc_action_fee_code_uuid,
            fee_category_group=fee_category_group,
            revenue_group=revenue_group,
            developer_uuid=developer_uuid,
            revenue_action_type=revenue_action_type,
            revenue_action_fee_code_uuid=revenue_action_fee_code_uuid,
            source_billing_entity_uuid=source_billing_entity_uuid,
            settlement_action_uuid=settlement_action_uuid,
        )

        api_action.additional_properties = d
        return api_action

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
