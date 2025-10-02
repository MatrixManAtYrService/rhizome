import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiFeeYtdExtended")


@_attrs_define
class ApiFeeYtdExtended:
    """
    Attributes:
        id (Union[Unset, int]): Id of the year-to-date fee
        uuid (Union[Unset, str]): 26-character UUID of the year-to-date fee
        billing_entity_uuid (Union[Unset, str]): 26-character UUID of the billing entity this year-to-date fee belongs
            to
        year (Union[Unset, int]): the year that the year-to-date fee total is for
        fee_category_group (Union[Unset, str]): defined fee category grouping
        fee_category (Union[Unset, str]): the fee category of the year-to-date fee
        fee_code (Union[Unset, str]): the fee code of the year-to-date fee
        short_desc (Union[Unset, str]): short description of fee code
        full_desc (Union[Unset, str]): long description for fee code
        currency (Union[Unset, str]): the currency of the year-to-date fee Example: USD.
        total_period_units (Union[Unset, float]): the year-to-date total number of billed units
        total_basis_amount (Union[Unset, float]): the year-to-date total basis amount
        total_fee_amount (Union[Unset, float]): the year-to-date total fee amount
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the year-to-date fee was created
            Example: 2020-12-31T23:59:59.123456Z.
        modified_timestamp (Union[Unset, datetime.datetime]): date and time when the year-to-date fee was last modified
            Example: 2020-12-31T23:59:59.123456Z.
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    billing_entity_uuid: Union[Unset, str] = UNSET
    year: Union[Unset, int] = UNSET
    fee_category_group: Union[Unset, str] = UNSET
    fee_category: Union[Unset, str] = UNSET
    fee_code: Union[Unset, str] = UNSET
    short_desc: Union[Unset, str] = UNSET
    full_desc: Union[Unset, str] = UNSET
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

        fee_category_group = self.fee_category_group

        fee_category = self.fee_category

        fee_code = self.fee_code

        short_desc = self.short_desc

        full_desc = self.full_desc

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
        if fee_category_group is not UNSET:
            field_dict["feeCategoryGroup"] = fee_category_group
        if fee_category is not UNSET:
            field_dict["feeCategory"] = fee_category
        if fee_code is not UNSET:
            field_dict["feeCode"] = fee_code
        if short_desc is not UNSET:
            field_dict["shortDesc"] = short_desc
        if full_desc is not UNSET:
            field_dict["fullDesc"] = full_desc
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

        fee_category_group = d.pop("feeCategoryGroup", UNSET)

        fee_category = d.pop("feeCategory", UNSET)

        fee_code = d.pop("feeCode", UNSET)

        short_desc = d.pop("shortDesc", UNSET)

        full_desc = d.pop("fullDesc", UNSET)

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

        api_fee_ytd_extended = cls(
            id=id,
            uuid=uuid,
            billing_entity_uuid=billing_entity_uuid,
            year=year,
            fee_category_group=fee_category_group,
            fee_category=fee_category,
            fee_code=fee_code,
            short_desc=short_desc,
            full_desc=full_desc,
            currency=currency,
            total_period_units=total_period_units,
            total_basis_amount=total_basis_amount,
            total_fee_amount=total_fee_amount,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
        )

        api_fee_ytd_extended.additional_properties = d
        return api_fee_ytd_extended

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
