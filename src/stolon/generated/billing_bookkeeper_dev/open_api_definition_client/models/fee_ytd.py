import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="FeeYtd")


@_attrs_define
class FeeYtd:
    """
    Attributes:
        id (Union[Unset, int]):
        uuid (Union[Unset, str]):
        billing_entity_uuid (Union[Unset, str]):
        year (Union[Unset, int]):
        fee_category (Union[Unset, str]):
        fee_code (Union[Unset, str]):
        currency (Union[Unset, str]):
        total_period_units (Union[Unset, float]):
        total_basis_amount (Union[Unset, float]):
        total_fee_amount (Union[Unset, float]):
        created_timestamp (Union[Unset, datetime.datetime]):
        modified_timestamp (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    billing_entity_uuid: Union[Unset, str] = UNSET
    year: Union[Unset, int] = UNSET
    fee_category: Union[Unset, str] = UNSET
    fee_code: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    total_period_units: Union[Unset, float] = UNSET
    total_basis_amount: Union[Unset, float] = UNSET
    total_fee_amount: Union[Unset, float] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        billing_entity_uuid = self.billing_entity_uuid

        year = self.year

        fee_category = self.fee_category

        fee_code = self.fee_code

        currency = self.currency

        total_period_units = self.total_period_units

        total_basis_amount = self.total_basis_amount

        total_fee_amount = self.total_fee_amount

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
        if year is not UNSET:
            field_dict["year"] = year
        if fee_category is not UNSET:
            field_dict["feeCategory"] = fee_category
        if fee_code is not UNSET:
            field_dict["feeCode"] = fee_code
        if currency is not UNSET:
            field_dict["currency"] = currency
        if total_period_units is not UNSET:
            field_dict["totalPeriodUnits"] = total_period_units
        if total_basis_amount is not UNSET:
            field_dict["totalBasisAmount"] = total_basis_amount
        if total_fee_amount is not UNSET:
            field_dict["totalFeeAmount"] = total_fee_amount
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

        year = d.pop("year", UNSET)

        fee_category = d.pop("feeCategory", UNSET)

        fee_code = d.pop("feeCode", UNSET)

        currency = d.pop("currency", UNSET)

        total_period_units = d.pop("totalPeriodUnits", UNSET)

        total_basis_amount = d.pop("totalBasisAmount", UNSET)

        total_fee_amount = d.pop("totalFeeAmount", UNSET)

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

        fee_ytd = cls(
            id=id,
            uuid=uuid,
            billing_entity_uuid=billing_entity_uuid,
            year=year,
            fee_category=fee_category,
            fee_code=fee_code,
            currency=currency,
            total_period_units=total_period_units,
            total_basis_amount=total_basis_amount,
            total_fee_amount=total_fee_amount,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
        )

        fee_ytd.additional_properties = d
        return fee_ytd

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
