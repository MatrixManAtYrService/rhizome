import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiAutoAdjustAdvice")


@_attrs_define
class ApiAutoAdjustAdvice:
    """
    Attributes:
        id (Union[Unset, int]): ID of the auto-adjust advice
        uuid (Union[Unset, str]): 26-character UUID of the auto-adjust advice
        billing_entity_uuid (Union[Unset, str]): UUID of the billing entity associated with this auto-adjust advice
        auto_adjust_rule_uuid (Union[Unset, str]): 26-character UUID of the auto-adjust rule that this advice applies to
        start_date (Union[Unset, datetime.date]): date that this auto-adjust advice begins to apply
        deleted_date (Union[Unset, datetime.date]): date that this auto-adjust advice is no longer applicable
        total_periods (Union[Unset, int]): the total number of billing periods that this auto-adjust advice and
            associated rule should be evaluated
        evaluated_periods (Union[Unset, int]): the total number of billing periods that this auto-adjust advice and
            associated rule have been evaluated
        applied_periods (Union[Unset, int]): the total number of billing periods where this auto-adjust advice and
            associated rule applied an adjustment
        max_units (Union[Unset, float]): the maximum total number of units from qualified fee summaries that can be used
            to create an auto-adjustment
        max_amount (Union[Unset, float]): the maximum total of fee amount from qualified fee summaries that can be used
            to create an auto-adjustment
        currency (Union[Unset, str]): 3-letter currency code Example: USD.
        reference (Union[Unset, str]): free-form comment or reference identifier for this auto-adjust advice
        request_uuid (Union[Unset, str]): 26-character UUID for the execution request that created the monetary
            adjustment
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the auto-adjust advice was created
            Example: 2020-12-31T23:59:59.123456Z.
        modified_timestamp (Union[Unset, datetime.datetime]): date and time when the auto-adjust advice was last
            modified Example: 2020-12-31T23:59:59.123456Z.
        audit_id (Union[Unset, str]): identifier for the user who created or last modified this auto-adjust advice
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    billing_entity_uuid: Union[Unset, str] = UNSET
    auto_adjust_rule_uuid: Union[Unset, str] = UNSET
    start_date: Union[Unset, datetime.date] = UNSET
    deleted_date: Union[Unset, datetime.date] = UNSET
    total_periods: Union[Unset, int] = UNSET
    evaluated_periods: Union[Unset, int] = UNSET
    applied_periods: Union[Unset, int] = UNSET
    max_units: Union[Unset, float] = UNSET
    max_amount: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    request_uuid: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    audit_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        billing_entity_uuid = self.billing_entity_uuid

        auto_adjust_rule_uuid = self.auto_adjust_rule_uuid

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        deleted_date: Union[Unset, str] = UNSET
        if not isinstance(self.deleted_date, Unset):
            deleted_date = self.deleted_date.isoformat()

        total_periods = self.total_periods

        evaluated_periods = self.evaluated_periods

        applied_periods = self.applied_periods

        max_units = self.max_units

        max_amount = self.max_amount

        currency = self.currency

        reference = self.reference

        request_uuid = self.request_uuid

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
        if billing_entity_uuid is not UNSET:
            field_dict["billingEntityUuid"] = billing_entity_uuid
        if auto_adjust_rule_uuid is not UNSET:
            field_dict["autoAdjustRuleUuid"] = auto_adjust_rule_uuid
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if deleted_date is not UNSET:
            field_dict["deletedDate"] = deleted_date
        if total_periods is not UNSET:
            field_dict["totalPeriods"] = total_periods
        if evaluated_periods is not UNSET:
            field_dict["evaluatedPeriods"] = evaluated_periods
        if applied_periods is not UNSET:
            field_dict["appliedPeriods"] = applied_periods
        if max_units is not UNSET:
            field_dict["maxUnits"] = max_units
        if max_amount is not UNSET:
            field_dict["maxAmount"] = max_amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if reference is not UNSET:
            field_dict["reference"] = reference
        if request_uuid is not UNSET:
            field_dict["requestUuid"] = request_uuid
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

        billing_entity_uuid = d.pop("billingEntityUuid", UNSET)

        auto_adjust_rule_uuid = d.pop("autoAdjustRuleUuid", UNSET)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.date]
        if _start_date and not isinstance(_start_date, Unset):
            start_date = isoparse(_start_date).date()

        else:
            start_date = UNSET

        _deleted_date = d.pop("deletedDate", UNSET)
        deleted_date: Union[Unset, datetime.date]
        if _deleted_date and not isinstance(_deleted_date, Unset):
            deleted_date = isoparse(_deleted_date).date()

        else:
            deleted_date = UNSET

        total_periods = d.pop("totalPeriods", UNSET)

        evaluated_periods = d.pop("evaluatedPeriods", UNSET)

        applied_periods = d.pop("appliedPeriods", UNSET)

        max_units = d.pop("maxUnits", UNSET)

        max_amount = d.pop("maxAmount", UNSET)

        currency = d.pop("currency", UNSET)

        reference = d.pop("reference", UNSET)

        request_uuid = d.pop("requestUuid", UNSET)

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

        api_auto_adjust_advice = cls(
            id=id,
            uuid=uuid,
            billing_entity_uuid=billing_entity_uuid,
            auto_adjust_rule_uuid=auto_adjust_rule_uuid,
            start_date=start_date,
            deleted_date=deleted_date,
            total_periods=total_periods,
            evaluated_periods=evaluated_periods,
            applied_periods=applied_periods,
            max_units=max_units,
            max_amount=max_amount,
            currency=currency,
            reference=reference,
            request_uuid=request_uuid,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
            audit_id=audit_id,
        )

        api_auto_adjust_advice.additional_properties = d
        return api_auto_adjust_advice

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
