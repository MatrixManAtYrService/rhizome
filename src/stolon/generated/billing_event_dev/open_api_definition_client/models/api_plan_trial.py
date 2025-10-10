import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiPlanTrial")


@_attrs_define
class ApiPlanTrial:
    """
    Attributes:
        id (Union[Unset, int]): Id of the plan trial
        uuid (Union[Unset, str]): 26-character UUID of the plan trial
        merchant_uuid (Union[Unset, str]): 13-character merchant UUID of plan trial
        environment (Union[Unset, str]): plan trial environment
        effective_datetime (Union[Unset, datetime.datetime]): date and time when the plan trial settings became
            effective Example: 2020-12-31T23:59:59.123456Z.
        merchant_plan_uuid (Union[Unset, str]): merchant plan UUID
        trial_start_date (Union[Unset, datetime.date]): plan trial start date
        trial_days (Union[Unset, int]):
        is_active (Union[Unset, bool]):
        billing_event_uuid (Union[Unset, str]): billing event UUID
        created_timestamp (Union[Unset, datetime.datetime]): plan trial created timestamp Example:
            2020-12-31T23:59:59.123456Z.
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    merchant_uuid: Union[Unset, str] = UNSET
    environment: Union[Unset, str] = UNSET
    effective_datetime: Union[Unset, datetime.datetime] = UNSET
    merchant_plan_uuid: Union[Unset, str] = UNSET
    trial_start_date: Union[Unset, datetime.date] = UNSET
    trial_days: Union[Unset, int] = UNSET
    is_active: Union[Unset, bool] = UNSET
    billing_event_uuid: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        merchant_uuid = self.merchant_uuid

        environment = self.environment

        effective_datetime: Union[Unset, str] = UNSET
        if not isinstance(self.effective_datetime, Unset):
            effective_datetime = self.effective_datetime.isoformat()

        merchant_plan_uuid = self.merchant_plan_uuid

        trial_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.trial_start_date, Unset):
            trial_start_date = self.trial_start_date.isoformat()

        trial_days = self.trial_days

        is_active = self.is_active

        billing_event_uuid = self.billing_event_uuid

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if merchant_uuid is not UNSET:
            field_dict["merchantUuid"] = merchant_uuid
        if environment is not UNSET:
            field_dict["environment"] = environment
        if effective_datetime is not UNSET:
            field_dict["effectiveDatetime"] = effective_datetime
        if merchant_plan_uuid is not UNSET:
            field_dict["merchantPlanUuid"] = merchant_plan_uuid
        if trial_start_date is not UNSET:
            field_dict["trialStartDate"] = trial_start_date
        if trial_days is not UNSET:
            field_dict["trialDays"] = trial_days
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if billing_event_uuid is not UNSET:
            field_dict["billingEventUuid"] = billing_event_uuid
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        merchant_uuid = d.pop("merchantUuid", UNSET)

        environment = d.pop("environment", UNSET)

        _effective_datetime = d.pop("effectiveDatetime", UNSET)
        effective_datetime: Union[Unset, datetime.datetime]
        if _effective_datetime and not isinstance(_effective_datetime, Unset):
            effective_datetime = isoparse(_effective_datetime)

        else:
            effective_datetime = UNSET

        merchant_plan_uuid = d.pop("merchantPlanUuid", UNSET)

        _trial_start_date = d.pop("trialStartDate", UNSET)
        trial_start_date: Union[Unset, datetime.date]
        if _trial_start_date and not isinstance(_trial_start_date, Unset):
            trial_start_date = isoparse(_trial_start_date).date()

        else:
            trial_start_date = UNSET

        trial_days = d.pop("trialDays", UNSET)

        is_active = d.pop("isActive", UNSET)

        billing_event_uuid = d.pop("billingEventUuid", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if _created_timestamp and not isinstance(_created_timestamp, Unset):
            created_timestamp = isoparse(_created_timestamp)

        else:
            created_timestamp = UNSET

        api_plan_trial = cls(
            id=id,
            uuid=uuid,
            merchant_uuid=merchant_uuid,
            environment=environment,
            effective_datetime=effective_datetime,
            merchant_plan_uuid=merchant_plan_uuid,
            trial_start_date=trial_start_date,
            trial_days=trial_days,
            is_active=is_active,
            billing_event_uuid=billing_event_uuid,
            created_timestamp=created_timestamp,
        )

        api_plan_trial.additional_properties = d
        return api_plan_trial

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
