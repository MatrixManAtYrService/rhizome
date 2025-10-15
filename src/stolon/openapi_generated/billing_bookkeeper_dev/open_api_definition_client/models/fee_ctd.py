import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="FeeCtd")


@_attrs_define
class FeeCtd:
    """
    Attributes:
        id (Union[Unset, int]):
        uuid (Union[Unset, str]):
        billing_entity_uuid (Union[Unset, str]):
        fee_category (Union[Unset, str]):
        fee_code (Union[Unset, str]):
        currency (Union[Unset, str]):
        ctd_num_units (Union[Unset, float]):
        abs_num_units (Union[Unset, float]):
        ctd_basis_amount (Union[Unset, float]):
        abs_basis_amount (Union[Unset, float]):
        num_actions (Union[Unset, int]):
        created_timestamp (Union[Unset, datetime.datetime]):
        modified_timestamp (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    billing_entity_uuid: Union[Unset, str] = UNSET
    fee_category: Union[Unset, str] = UNSET
    fee_code: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    ctd_num_units: Union[Unset, float] = UNSET
    abs_num_units: Union[Unset, float] = UNSET
    ctd_basis_amount: Union[Unset, float] = UNSET
    abs_basis_amount: Union[Unset, float] = UNSET
    num_actions: Union[Unset, int] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        billing_entity_uuid = self.billing_entity_uuid

        fee_category = self.fee_category

        fee_code = self.fee_code

        currency = self.currency

        ctd_num_units = self.ctd_num_units

        abs_num_units = self.abs_num_units

        ctd_basis_amount = self.ctd_basis_amount

        abs_basis_amount = self.abs_basis_amount

        num_actions = self.num_actions

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
        if fee_category is not UNSET:
            field_dict["feeCategory"] = fee_category
        if fee_code is not UNSET:
            field_dict["feeCode"] = fee_code
        if currency is not UNSET:
            field_dict["currency"] = currency
        if ctd_num_units is not UNSET:
            field_dict["ctdNumUnits"] = ctd_num_units
        if abs_num_units is not UNSET:
            field_dict["absNumUnits"] = abs_num_units
        if ctd_basis_amount is not UNSET:
            field_dict["ctdBasisAmount"] = ctd_basis_amount
        if abs_basis_amount is not UNSET:
            field_dict["absBasisAmount"] = abs_basis_amount
        if num_actions is not UNSET:
            field_dict["numActions"] = num_actions
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

        fee_category = d.pop("feeCategory", UNSET)

        fee_code = d.pop("feeCode", UNSET)

        currency = d.pop("currency", UNSET)

        ctd_num_units = d.pop("ctdNumUnits", UNSET)

        abs_num_units = d.pop("absNumUnits", UNSET)

        ctd_basis_amount = d.pop("ctdBasisAmount", UNSET)

        abs_basis_amount = d.pop("absBasisAmount", UNSET)

        num_actions = d.pop("numActions", UNSET)

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

        fee_ctd = cls(
            id=id,
            uuid=uuid,
            billing_entity_uuid=billing_entity_uuid,
            fee_category=fee_category,
            fee_code=fee_code,
            currency=currency,
            ctd_num_units=ctd_num_units,
            abs_num_units=abs_num_units,
            ctd_basis_amount=ctd_basis_amount,
            abs_basis_amount=abs_basis_amount,
            num_actions=num_actions,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
        )

        fee_ctd.additional_properties = d
        return fee_ctd

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
