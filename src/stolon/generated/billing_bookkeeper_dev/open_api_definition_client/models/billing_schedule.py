import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.billing_schedule_frequency import BillingScheduleFrequency
from ..types import UNSET, Unset

T = TypeVar("T", bound="BillingSchedule")


@_attrs_define
class BillingSchedule:
    """
    Attributes:
        id (Union[Unset, int]):
        uuid (Union[Unset, str]):
        billing_entity_uuid (Union[Unset, str]):
        effective_date (Union[Unset, datetime.date]):
        frequency (Union[Unset, BillingScheduleFrequency]):
        billing_day (Union[Unset, int]):
        next_billing_date (Union[Unset, datetime.date]):
        last_billing_date (Union[Unset, datetime.date]):
        units_in_next_period (Union[Unset, int]):
        units_in_last_period (Union[Unset, int]):
        default_currency (Union[Unset, str]):
        created_timestamp (Union[Unset, datetime.datetime]):
        modified_timestamp (Union[Unset, datetime.datetime]):
        close_date (Union[Unset, datetime.date]):
        effective_close_date (Union[Unset, datetime.date]):
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    billing_entity_uuid: Union[Unset, str] = UNSET
    effective_date: Union[Unset, datetime.date] = UNSET
    frequency: Union[Unset, BillingScheduleFrequency] = UNSET
    billing_day: Union[Unset, int] = UNSET
    next_billing_date: Union[Unset, datetime.date] = UNSET
    last_billing_date: Union[Unset, datetime.date] = UNSET
    units_in_next_period: Union[Unset, int] = UNSET
    units_in_last_period: Union[Unset, int] = UNSET
    default_currency: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    close_date: Union[Unset, datetime.date] = UNSET
    effective_close_date: Union[Unset, datetime.date] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        billing_entity_uuid = self.billing_entity_uuid

        effective_date: Union[Unset, str] = UNSET
        if not isinstance(self.effective_date, Unset):
            effective_date = self.effective_date.isoformat()

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

        units_in_next_period = self.units_in_next_period

        units_in_last_period = self.units_in_last_period

        default_currency = self.default_currency

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        modified_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.modified_timestamp, Unset):
            modified_timestamp = self.modified_timestamp.isoformat()

        close_date: Union[Unset, str] = UNSET
        if not isinstance(self.close_date, Unset):
            close_date = self.close_date.isoformat()

        effective_close_date: Union[Unset, str] = UNSET
        if not isinstance(self.effective_close_date, Unset):
            effective_close_date = self.effective_close_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if billing_entity_uuid is not UNSET:
            field_dict["billingEntityUuid"] = billing_entity_uuid
        if effective_date is not UNSET:
            field_dict["effectiveDate"] = effective_date
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if billing_day is not UNSET:
            field_dict["billingDay"] = billing_day
        if next_billing_date is not UNSET:
            field_dict["nextBillingDate"] = next_billing_date
        if last_billing_date is not UNSET:
            field_dict["lastBillingDate"] = last_billing_date
        if units_in_next_period is not UNSET:
            field_dict["unitsInNextPeriod"] = units_in_next_period
        if units_in_last_period is not UNSET:
            field_dict["unitsInLastPeriod"] = units_in_last_period
        if default_currency is not UNSET:
            field_dict["defaultCurrency"] = default_currency
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if modified_timestamp is not UNSET:
            field_dict["modifiedTimestamp"] = modified_timestamp
        if close_date is not UNSET:
            field_dict["closeDate"] = close_date
        if effective_close_date is not UNSET:
            field_dict["effectiveCloseDate"] = effective_close_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        billing_entity_uuid = d.pop("billingEntityUuid", UNSET)

        _effective_date = d.pop("effectiveDate", UNSET)
        effective_date: Union[Unset, datetime.date]
        if _effective_date and not isinstance(_effective_date, Unset):
            effective_date = isoparse(_effective_date).date()

        else:
            effective_date = UNSET

        _frequency = d.pop("frequency", UNSET)
        frequency: Union[Unset, BillingScheduleFrequency]
        if _frequency and not isinstance(_frequency, Unset):
            frequency = BillingScheduleFrequency(_frequency)

        else:
            frequency = UNSET

        billing_day = d.pop("billingDay", UNSET)

        _next_billing_date = d.pop("nextBillingDate", UNSET)
        next_billing_date: Union[Unset, datetime.date]
        if _next_billing_date and not isinstance(_next_billing_date, Unset):
            next_billing_date = isoparse(_next_billing_date).date()

        else:
            next_billing_date = UNSET

        _last_billing_date = d.pop("lastBillingDate", UNSET)
        last_billing_date: Union[Unset, datetime.date]
        if _last_billing_date and not isinstance(_last_billing_date, Unset):
            last_billing_date = isoparse(_last_billing_date).date()

        else:
            last_billing_date = UNSET

        units_in_next_period = d.pop("unitsInNextPeriod", UNSET)

        units_in_last_period = d.pop("unitsInLastPeriod", UNSET)

        default_currency = d.pop("defaultCurrency", UNSET)

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

        _close_date = d.pop("closeDate", UNSET)
        close_date: Union[Unset, datetime.date]
        if _close_date and not isinstance(_close_date, Unset):
            close_date = isoparse(_close_date).date()

        else:
            close_date = UNSET

        _effective_close_date = d.pop("effectiveCloseDate", UNSET)
        effective_close_date: Union[Unset, datetime.date]
        if _effective_close_date and not isinstance(_effective_close_date, Unset):
            effective_close_date = isoparse(_effective_close_date).date()

        else:
            effective_close_date = UNSET

        billing_schedule = cls(
            id=id,
            uuid=uuid,
            billing_entity_uuid=billing_entity_uuid,
            effective_date=effective_date,
            frequency=frequency,
            billing_day=billing_day,
            next_billing_date=next_billing_date,
            last_billing_date=last_billing_date,
            units_in_next_period=units_in_next_period,
            units_in_last_period=units_in_last_period,
            default_currency=default_currency,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
            close_date=close_date,
            effective_close_date=effective_close_date,
        )

        billing_schedule.additional_properties = d
        return billing_schedule

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
