import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiFeeTax")


@_attrs_define
class ApiFeeTax:
    """Array of associated fee_tax entries

    Attributes:
        id (Union[Unset, int]): Id of the fee tax
        uuid (Union[Unset, str]): 26-character UUID of the fee tax
        fee_summary_uuid (Union[Unset, str]): 26-character UUID of the fee summary entity this tax belongs to
        tax1_amount (Union[Unset, float]): Amount of the first tax
        tax2_amount (Union[Unset, float]): Amount of the second tax
        tax3_amount (Union[Unset, float]): Amount of the third tax
        tax4_amount (Union[Unset, float]): Amount of the fourth tax
        tax1_rate (Union[Unset, float]): Rate of the first tax
        tax2_rate (Union[Unset, float]): Rate of the second tax
        tax3_rate (Union[Unset, float]): Rate of the third tax
        tax4_rate (Union[Unset, float]): Rate of the fourth tax
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the fee rate was created Example:
            2020-12-31T23:59:59.123456Z.
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    fee_summary_uuid: Union[Unset, str] = UNSET
    tax1_amount: Union[Unset, float] = UNSET
    tax2_amount: Union[Unset, float] = UNSET
    tax3_amount: Union[Unset, float] = UNSET
    tax4_amount: Union[Unset, float] = UNSET
    tax1_rate: Union[Unset, float] = UNSET
    tax2_rate: Union[Unset, float] = UNSET
    tax3_rate: Union[Unset, float] = UNSET
    tax4_rate: Union[Unset, float] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        fee_summary_uuid = self.fee_summary_uuid

        tax1_amount = self.tax1_amount

        tax2_amount = self.tax2_amount

        tax3_amount = self.tax3_amount

        tax4_amount = self.tax4_amount

        tax1_rate = self.tax1_rate

        tax2_rate = self.tax2_rate

        tax3_rate = self.tax3_rate

        tax4_rate = self.tax4_rate

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
        if fee_summary_uuid is not UNSET:
            field_dict["feeSummaryUuid"] = fee_summary_uuid
        if tax1_amount is not UNSET:
            field_dict["tax1_amount"] = tax1_amount
        if tax2_amount is not UNSET:
            field_dict["tax2_amount"] = tax2_amount
        if tax3_amount is not UNSET:
            field_dict["tax3_amount"] = tax3_amount
        if tax4_amount is not UNSET:
            field_dict["tax4_amount"] = tax4_amount
        if tax1_rate is not UNSET:
            field_dict["tax1_rate"] = tax1_rate
        if tax2_rate is not UNSET:
            field_dict["tax2_rate"] = tax2_rate
        if tax3_rate is not UNSET:
            field_dict["tax3_rate"] = tax3_rate
        if tax4_rate is not UNSET:
            field_dict["tax4_rate"] = tax4_rate
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        fee_summary_uuid = d.pop("feeSummaryUuid", UNSET)

        tax1_amount = d.pop("tax1_amount", UNSET)

        tax2_amount = d.pop("tax2_amount", UNSET)

        tax3_amount = d.pop("tax3_amount", UNSET)

        tax4_amount = d.pop("tax4_amount", UNSET)

        tax1_rate = d.pop("tax1_rate", UNSET)

        tax2_rate = d.pop("tax2_rate", UNSET)

        tax3_rate = d.pop("tax3_rate", UNSET)

        tax4_rate = d.pop("tax4_rate", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if _created_timestamp and not isinstance(_created_timestamp, Unset):
            created_timestamp = isoparse(_created_timestamp)

        else:
            created_timestamp = UNSET

        api_fee_tax = cls(
            id=id,
            uuid=uuid,
            fee_summary_uuid=fee_summary_uuid,
            tax1_amount=tax1_amount,
            tax2_amount=tax2_amount,
            tax3_amount=tax3_amount,
            tax4_amount=tax4_amount,
            tax1_rate=tax1_rate,
            tax2_rate=tax2_rate,
            tax3_rate=tax3_rate,
            tax4_rate=tax4_rate,
            created_timestamp=created_timestamp,
        )

        api_fee_tax.additional_properties = d
        return api_fee_tax

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
