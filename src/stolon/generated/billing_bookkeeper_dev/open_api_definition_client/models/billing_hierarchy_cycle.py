import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.billing_hierarchy_cycle_frequency import BillingHierarchyCycleFrequency
from ..types import UNSET, Unset

T = TypeVar("T", bound="BillingHierarchyCycle")


@_attrs_define
class BillingHierarchyCycle:
    """
    Attributes:
        id (Union[Unset, int]):
        uuid (Union[Unset, str]):
        processing_group_uuid (Union[Unset, str]):
        billing_hierarchy_uuid (Union[Unset, str]):
        cycle_date (Union[Unset, datetime.date]):
        close_date (Union[Unset, datetime.date]):
        effective_close_date (Union[Unset, datetime.date]):
        billing_entity_uuid (Union[Unset, str]):
        entity_uuid (Union[Unset, str]):
        schedule_parent_billing_entity_uuid (Union[Unset, str]):
        fee_rate_parent_billing_entity_uuid (Union[Unset, str]):
        billing_entity_name (Union[Unset, str]):
        frequency (Union[Unset, BillingHierarchyCycleFrequency]):
        billing_day (Union[Unset, int]):
        next_billing_date (Union[Unset, datetime.date]):
        last_billing_date (Union[Unset, datetime.date]):
        arrears_billing_date (Union[Unset, datetime.date]):
        units_in_next_period (Union[Unset, int]):
        units_in_last_period (Union[Unset, int]):
        units_in_arrears_period (Union[Unset, int]):
        default_currency (Union[Unset, str]):
        post_method (Union[Unset, str]):
        plan_billing_method (Union[Unset, str]):
        invoice_method (Union[Unset, str]):
        invoice_number_format (Union[Unset, str]):
        settlement_method (Union[Unset, str]):
        created_timestamp (Union[Unset, datetime.datetime]):
        modified_timestamp (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    processing_group_uuid: Union[Unset, str] = UNSET
    billing_hierarchy_uuid: Union[Unset, str] = UNSET
    cycle_date: Union[Unset, datetime.date] = UNSET
    close_date: Union[Unset, datetime.date] = UNSET
    effective_close_date: Union[Unset, datetime.date] = UNSET
    billing_entity_uuid: Union[Unset, str] = UNSET
    entity_uuid: Union[Unset, str] = UNSET
    schedule_parent_billing_entity_uuid: Union[Unset, str] = UNSET
    fee_rate_parent_billing_entity_uuid: Union[Unset, str] = UNSET
    billing_entity_name: Union[Unset, str] = UNSET
    frequency: Union[Unset, BillingHierarchyCycleFrequency] = UNSET
    billing_day: Union[Unset, int] = UNSET
    next_billing_date: Union[Unset, datetime.date] = UNSET
    last_billing_date: Union[Unset, datetime.date] = UNSET
    arrears_billing_date: Union[Unset, datetime.date] = UNSET
    units_in_next_period: Union[Unset, int] = UNSET
    units_in_last_period: Union[Unset, int] = UNSET
    units_in_arrears_period: Union[Unset, int] = UNSET
    default_currency: Union[Unset, str] = UNSET
    post_method: Union[Unset, str] = UNSET
    plan_billing_method: Union[Unset, str] = UNSET
    invoice_method: Union[Unset, str] = UNSET
    invoice_number_format: Union[Unset, str] = UNSET
    settlement_method: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        processing_group_uuid = self.processing_group_uuid

        billing_hierarchy_uuid = self.billing_hierarchy_uuid

        cycle_date: Union[Unset, str] = UNSET
        if not isinstance(self.cycle_date, Unset):
            cycle_date = self.cycle_date.isoformat()

        close_date: Union[Unset, str] = UNSET
        if not isinstance(self.close_date, Unset):
            close_date = self.close_date.isoformat()

        effective_close_date: Union[Unset, str] = UNSET
        if not isinstance(self.effective_close_date, Unset):
            effective_close_date = self.effective_close_date.isoformat()

        billing_entity_uuid = self.billing_entity_uuid

        entity_uuid = self.entity_uuid

        schedule_parent_billing_entity_uuid = self.schedule_parent_billing_entity_uuid

        fee_rate_parent_billing_entity_uuid = self.fee_rate_parent_billing_entity_uuid

        billing_entity_name = self.billing_entity_name

        frequency: Union[Unset, str] = UNSET
        if not isinstance(self.frequency, Unset):
            frequency = self.frequency.value

        billing_day = self.billing_day

        next_billing_date: Union[Unset, str] = UNSET
        if not isinstance(self.next_billing_date, Unset):
            next_billing_date = self.next_billing_date.isoformat()

        last_billing_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_billing_date, Unset):
            last_billing_date = self.last_billing_date.isoformat()

        arrears_billing_date: Union[Unset, str] = UNSET
        if not isinstance(self.arrears_billing_date, Unset):
            arrears_billing_date = self.arrears_billing_date.isoformat()

        units_in_next_period = self.units_in_next_period

        units_in_last_period = self.units_in_last_period

        units_in_arrears_period = self.units_in_arrears_period

        default_currency = self.default_currency

        post_method = self.post_method

        plan_billing_method = self.plan_billing_method

        invoice_method = self.invoice_method

        invoice_number_format = self.invoice_number_format

        settlement_method = self.settlement_method

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
        if processing_group_uuid is not UNSET:
            field_dict["processingGroupUuid"] = processing_group_uuid
        if billing_hierarchy_uuid is not UNSET:
            field_dict["billingHierarchyUuid"] = billing_hierarchy_uuid
        if cycle_date is not UNSET:
            field_dict["cycleDate"] = cycle_date
        if close_date is not UNSET:
            field_dict["closeDate"] = close_date
        if effective_close_date is not UNSET:
            field_dict["effectiveCloseDate"] = effective_close_date
        if billing_entity_uuid is not UNSET:
            field_dict["billingEntityUuid"] = billing_entity_uuid
        if entity_uuid is not UNSET:
            field_dict["entityUuid"] = entity_uuid
        if schedule_parent_billing_entity_uuid is not UNSET:
            field_dict["scheduleParentBillingEntityUuid"] = schedule_parent_billing_entity_uuid
        if fee_rate_parent_billing_entity_uuid is not UNSET:
            field_dict["feeRateParentBillingEntityUuid"] = fee_rate_parent_billing_entity_uuid
        if billing_entity_name is not UNSET:
            field_dict["billingEntityName"] = billing_entity_name
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if billing_day is not UNSET:
            field_dict["billingDay"] = billing_day
        if next_billing_date is not UNSET:
            field_dict["nextBillingDate"] = next_billing_date
        if last_billing_date is not UNSET:
            field_dict["lastBillingDate"] = last_billing_date
        if arrears_billing_date is not UNSET:
            field_dict["arrearsBillingDate"] = arrears_billing_date
        if units_in_next_period is not UNSET:
            field_dict["unitsInNextPeriod"] = units_in_next_period
        if units_in_last_period is not UNSET:
            field_dict["unitsInLastPeriod"] = units_in_last_period
        if units_in_arrears_period is not UNSET:
            field_dict["unitsInArrearsPeriod"] = units_in_arrears_period
        if default_currency is not UNSET:
            field_dict["defaultCurrency"] = default_currency
        if post_method is not UNSET:
            field_dict["postMethod"] = post_method
        if plan_billing_method is not UNSET:
            field_dict["planBillingMethod"] = plan_billing_method
        if invoice_method is not UNSET:
            field_dict["invoiceMethod"] = invoice_method
        if invoice_number_format is not UNSET:
            field_dict["invoiceNumberFormat"] = invoice_number_format
        if settlement_method is not UNSET:
            field_dict["settlementMethod"] = settlement_method
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

        processing_group_uuid = d.pop("processingGroupUuid", UNSET)

        billing_hierarchy_uuid = d.pop("billingHierarchyUuid", UNSET)

        _cycle_date = d.pop("cycleDate", UNSET)
        cycle_date: Union[Unset, datetime.date]
        if isinstance(_cycle_date, Unset):
            cycle_date = UNSET
        else:
            cycle_date = isoparse(_cycle_date).date()

        _close_date = d.pop("closeDate", UNSET)
        close_date: Union[Unset, datetime.date]
        if isinstance(_close_date, Unset):
            close_date = UNSET
        else:
            close_date = isoparse(_close_date).date()

        _effective_close_date = d.pop("effectiveCloseDate", UNSET)
        effective_close_date: Union[Unset, datetime.date]
        if isinstance(_effective_close_date, Unset):
            effective_close_date = UNSET
        else:
            effective_close_date = isoparse(_effective_close_date).date()

        billing_entity_uuid = d.pop("billingEntityUuid", UNSET)

        entity_uuid = d.pop("entityUuid", UNSET)

        schedule_parent_billing_entity_uuid = d.pop("scheduleParentBillingEntityUuid", UNSET)

        fee_rate_parent_billing_entity_uuid = d.pop("feeRateParentBillingEntityUuid", UNSET)

        billing_entity_name = d.pop("billingEntityName", UNSET)

        _frequency = d.pop("frequency", UNSET)
        frequency: Union[Unset, BillingHierarchyCycleFrequency]
        if isinstance(_frequency, Unset):
            frequency = UNSET
        else:
            frequency = BillingHierarchyCycleFrequency(_frequency)

        billing_day = d.pop("billingDay", UNSET)

        _next_billing_date = d.pop("nextBillingDate", UNSET)
        next_billing_date: Union[Unset, datetime.date]
        if isinstance(_next_billing_date, Unset):
            next_billing_date = UNSET
        else:
            next_billing_date = isoparse(_next_billing_date).date()

        _last_billing_date = d.pop("lastBillingDate", UNSET)
        last_billing_date: Union[Unset, datetime.date]
        if isinstance(_last_billing_date, Unset):
            last_billing_date = UNSET
        else:
            last_billing_date = isoparse(_last_billing_date).date()

        _arrears_billing_date = d.pop("arrearsBillingDate", UNSET)
        arrears_billing_date: Union[Unset, datetime.date]
        if isinstance(_arrears_billing_date, Unset):
            arrears_billing_date = UNSET
        else:
            arrears_billing_date = isoparse(_arrears_billing_date).date()

        units_in_next_period = d.pop("unitsInNextPeriod", UNSET)

        units_in_last_period = d.pop("unitsInLastPeriod", UNSET)

        units_in_arrears_period = d.pop("unitsInArrearsPeriod", UNSET)

        default_currency = d.pop("defaultCurrency", UNSET)

        post_method = d.pop("postMethod", UNSET)

        plan_billing_method = d.pop("planBillingMethod", UNSET)

        invoice_method = d.pop("invoiceMethod", UNSET)

        invoice_number_format = d.pop("invoiceNumberFormat", UNSET)

        settlement_method = d.pop("settlementMethod", UNSET)

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

        billing_hierarchy_cycle = cls(
            id=id,
            uuid=uuid,
            processing_group_uuid=processing_group_uuid,
            billing_hierarchy_uuid=billing_hierarchy_uuid,
            cycle_date=cycle_date,
            close_date=close_date,
            effective_close_date=effective_close_date,
            billing_entity_uuid=billing_entity_uuid,
            entity_uuid=entity_uuid,
            schedule_parent_billing_entity_uuid=schedule_parent_billing_entity_uuid,
            fee_rate_parent_billing_entity_uuid=fee_rate_parent_billing_entity_uuid,
            billing_entity_name=billing_entity_name,
            frequency=frequency,
            billing_day=billing_day,
            next_billing_date=next_billing_date,
            last_billing_date=last_billing_date,
            arrears_billing_date=arrears_billing_date,
            units_in_next_period=units_in_next_period,
            units_in_last_period=units_in_last_period,
            units_in_arrears_period=units_in_arrears_period,
            default_currency=default_currency,
            post_method=post_method,
            plan_billing_method=plan_billing_method,
            invoice_method=invoice_method,
            invoice_number_format=invoice_number_format,
            settlement_method=settlement_method,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
        )

        billing_hierarchy_cycle.additional_properties = d
        return billing_hierarchy_cycle

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
