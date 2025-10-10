import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiAsOfMerchantPlan")


@_attrs_define
class ApiAsOfMerchantPlan:
    """
    Attributes:
        id (Union[Unset, int]): ID of the merchant's plan data associated with an as-of date break
        uuid (Union[Unset, str]): 26-character UUID for the merchant's plan data associated with an as-of date break
        as_of_merchant_uuid (Union[Unset, str]): 26-character UUID for the merchant's as-of date break
        merchant_plan_uuid (Union[Unset, str]): 13-character COS UUID for the merchant plan selected for the date break
        trial_start_date (Union[Unset, datetime.date]): the date when the merchant trial period started
        trial_days (Union[Unset, int]): the number of days for the merchant's trial period
        modifier (Union[Unset, str]): billing modifier assigned to the plan for the date break
        created_timestamp (Union[Unset, datetime.datetime]): timestamp for when the merchant's plan data associated with
            an as-of date break was first created Example: 2020-12-31T23:59:59.123456Z.
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    as_of_merchant_uuid: Union[Unset, str] = UNSET
    merchant_plan_uuid: Union[Unset, str] = UNSET
    trial_start_date: Union[Unset, datetime.date] = UNSET
    trial_days: Union[Unset, int] = UNSET
    modifier: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        as_of_merchant_uuid = self.as_of_merchant_uuid

        merchant_plan_uuid = self.merchant_plan_uuid

        trial_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.trial_start_date, Unset):
            trial_start_date = self.trial_start_date.isoformat()

        trial_days = self.trial_days

        modifier = self.modifier

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
        if as_of_merchant_uuid is not UNSET:
            field_dict["asOfMerchantUuid"] = as_of_merchant_uuid
        if merchant_plan_uuid is not UNSET:
            field_dict["merchantPlanUuid"] = merchant_plan_uuid
        if trial_start_date is not UNSET:
            field_dict["trialStartDate"] = trial_start_date
        if trial_days is not UNSET:
            field_dict["trialDays"] = trial_days
        if modifier is not UNSET:
            field_dict["modifier"] = modifier
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        as_of_merchant_uuid = d.pop("asOfMerchantUuid", UNSET)

        merchant_plan_uuid = d.pop("merchantPlanUuid", UNSET)

        _trial_start_date = d.pop("trialStartDate", UNSET)
        trial_start_date: Union[Unset, datetime.date]
        if _trial_start_date and not isinstance(_trial_start_date, Unset):
            trial_start_date = isoparse(_trial_start_date).date()

        else:
            trial_start_date = UNSET

        trial_days = d.pop("trialDays", UNSET)

        modifier = d.pop("modifier", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if _created_timestamp and not isinstance(_created_timestamp, Unset):
            created_timestamp = isoparse(_created_timestamp)

        else:
            created_timestamp = UNSET

        api_as_of_merchant_plan = cls(
            id=id,
            uuid=uuid,
            as_of_merchant_uuid=as_of_merchant_uuid,
            merchant_plan_uuid=merchant_plan_uuid,
            trial_start_date=trial_start_date,
            trial_days=trial_days,
            modifier=modifier,
            created_timestamp=created_timestamp,
        )

        api_as_of_merchant_plan.additional_properties = d
        return api_as_of_merchant_plan

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
