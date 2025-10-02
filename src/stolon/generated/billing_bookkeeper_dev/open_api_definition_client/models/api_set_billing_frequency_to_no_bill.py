import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiSetBillingFrequencyToNoBill")


@_attrs_define
class ApiSetBillingFrequencyToNoBill:
    """
    Attributes:
        billing_entity_uuid (Union[Unset, str]): UUID of the billing entity that this schedule belongs to
        effective_date (Union[Unset, datetime.date]): Date that this billing schedule will take effective
        reference (Union[Unset, str]): freeform comment or reference identifier for this schedule change
    """

    billing_entity_uuid: Union[Unset, str] = UNSET
    effective_date: Union[Unset, datetime.date] = UNSET
    reference: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        billing_entity_uuid = self.billing_entity_uuid

        effective_date: Union[Unset, str] = UNSET
        if not isinstance(self.effective_date, Unset):
            effective_date = self.effective_date.isoformat()

        reference = self.reference

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if billing_entity_uuid is not UNSET:
            field_dict["billingEntityUuid"] = billing_entity_uuid
        if effective_date is not UNSET:
            field_dict["effectiveDate"] = effective_date
        if reference is not UNSET:
            field_dict["reference"] = reference

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        billing_entity_uuid = d.pop("billingEntityUuid", UNSET)

        _effective_date = d.pop("effectiveDate", UNSET)
        effective_date: Union[Unset, datetime.date]
        if isinstance(_effective_date, Unset):
            effective_date = UNSET
        else:
            effective_date = isoparse(_effective_date).date()

        reference = d.pop("reference", UNSET)

        api_set_billing_frequency_to_no_bill = cls(
            billing_entity_uuid=billing_entity_uuid,
            effective_date=effective_date,
            reference=reference,
        )

        api_set_billing_frequency_to_no_bill.additional_properties = d
        return api_set_billing_frequency_to_no_bill

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
