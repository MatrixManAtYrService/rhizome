import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiPlanAction")


@_attrs_define
class ApiPlanAction:
    """
    Attributes:
        id (Union[Unset, int]): Id of the plan action
        uuid (Union[Unset, str]): 26-character UUID of the plan action
        billing_entity_uuid (Union[Unset, str]): 26-character UUID of the billing entity this plan action belongs to
        billing_entity_name (Union[Unset, str]): name of the billing entity
        entity_uuid (Union[Unset, str]): 13-character UUID of the actual entity that this billing entity represents
        merchant_plan_uuid (Union[Unset, str]): 13-character UUID of the merchant plan that the action applies to
        serial_number (Union[Unset, str]): device serial number, or n/a when the plan action does not apply to a
            specific device
        plan_action_type (Union[Unset, str]): defined plan action type value
        fee_category (Union[Unset, str]): defined fee category value
        fee_code (Union[Unset, str]): defined fee code value
        action_date_time (Union[Unset, datetime.datetime]): date and time that the plan action occurred Example:
            2020-12-31T23:59:59.123456Z.
        num_units (Union[Unset, int]): the number of billable units for the plan action
        units_in_period (Union[Unset, int]): the number of billable units in the billing entity billing period
        basis_amount (Union[Unset, float]): the basis amount for the plan action
        basis_currency (Union[Unset, str]): 3-letter currency code Example: USD.
        reference (Union[Unset, str]): freeform comment or reference identifier for this plan action
        plan_action_fee_code_uuid (Union[Unset, str]): 26-character UUID of the plan-action-to-fee-code mapping used to
            create this action
        fee_uuid (Union[Unset, str]): 26-character UUID of the fee CTD or fee summary that this plan action was applied
            towards
        event_uuid (Union[Unset, str]): 26-character UUID of the billing event that triggered this plan action
        request_uuid (Union[Unset, str]): 26-character UUID of the billing request that posted this plan action to the
            current-to-date totals
        posting_date (Union[Unset, datetime.date]): posting date
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the plan action was created Example:
            2020-12-31T23:59:59.123456Z.
        modified_timestamp (Union[Unset, datetime.datetime]): date and time when the plan action was last modified
            Example: 2020-12-31T23:59:59.123456Z.
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    billing_entity_uuid: Union[Unset, str] = UNSET
    billing_entity_name: Union[Unset, str] = UNSET
    entity_uuid: Union[Unset, str] = UNSET
    merchant_plan_uuid: Union[Unset, str] = UNSET
    serial_number: Union[Unset, str] = UNSET
    plan_action_type: Union[Unset, str] = UNSET
    fee_category: Union[Unset, str] = UNSET
    fee_code: Union[Unset, str] = UNSET
    action_date_time: Union[Unset, datetime.datetime] = UNSET
    num_units: Union[Unset, int] = UNSET
    units_in_period: Union[Unset, int] = UNSET
    basis_amount: Union[Unset, float] = UNSET
    basis_currency: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    plan_action_fee_code_uuid: Union[Unset, str] = UNSET
    fee_uuid: Union[Unset, str] = UNSET
    event_uuid: Union[Unset, str] = UNSET
    request_uuid: Union[Unset, str] = UNSET
    posting_date: Union[Unset, datetime.date] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        billing_entity_uuid = self.billing_entity_uuid

        billing_entity_name = self.billing_entity_name

        entity_uuid = self.entity_uuid

        merchant_plan_uuid = self.merchant_plan_uuid

        serial_number = self.serial_number

        plan_action_type = self.plan_action_type

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

        plan_action_fee_code_uuid = self.plan_action_fee_code_uuid

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
        if merchant_plan_uuid is not UNSET:
            field_dict["merchantPlanUuid"] = merchant_plan_uuid
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if plan_action_type is not UNSET:
            field_dict["planActionType"] = plan_action_type
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
        if plan_action_fee_code_uuid is not UNSET:
            field_dict["planActionFeeCodeUuid"] = plan_action_fee_code_uuid
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
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        billing_entity_uuid = d.pop("billingEntityUuid", UNSET)

        billing_entity_name = d.pop("billingEntityName", UNSET)

        entity_uuid = d.pop("entityUuid", UNSET)

        merchant_plan_uuid = d.pop("merchantPlanUuid", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        plan_action_type = d.pop("planActionType", UNSET)

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

        plan_action_fee_code_uuid = d.pop("planActionFeeCodeUuid", UNSET)

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

        api_plan_action = cls(
            id=id,
            uuid=uuid,
            billing_entity_uuid=billing_entity_uuid,
            billing_entity_name=billing_entity_name,
            entity_uuid=entity_uuid,
            merchant_plan_uuid=merchant_plan_uuid,
            serial_number=serial_number,
            plan_action_type=plan_action_type,
            fee_category=fee_category,
            fee_code=fee_code,
            action_date_time=action_date_time,
            num_units=num_units,
            units_in_period=units_in_period,
            basis_amount=basis_amount,
            basis_currency=basis_currency,
            reference=reference,
            plan_action_fee_code_uuid=plan_action_fee_code_uuid,
            fee_uuid=fee_uuid,
            event_uuid=event_uuid,
            request_uuid=request_uuid,
            posting_date=posting_date,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
        )

        api_plan_action.additional_properties = d
        return api_plan_action

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
