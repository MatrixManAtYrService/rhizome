from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_backfill_acceptance_type import ApiBackfillAcceptanceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiBackfillAcceptance")


@_attrs_define
class ApiBackfillAcceptance:
    """
    Attributes:
        id (Union[Unset, int]): ID of the backfill acceptance record in Billing Event
        acceptance_id (Union[Unset, str]): ID of acceptance created by Agreement Service
        merchant_id (Union[Unset, str]): 13-character UUID from COS of the merchant
        account_id (Union[Unset, str]): 13-character UUID from COS of the account of merchant
        type_ (Union[Unset, ApiBackfillAcceptanceType]):
        comment (Union[Unset, str]): Comment for reason this backfill acceptance was created
        agreement_id (Union[Unset, str]):
        locale (Union[Unset, str]): If providing only agreement type then must supply locale as well
        serial_number (Union[Unset, str]): Serial number of Clover device this agreement was accepted for
        iccid (Union[Unset, str]): For cellular acceptance, the ICCID of the device SIM
    """

    id: Union[Unset, int] = UNSET
    acceptance_id: Union[Unset, str] = UNSET
    merchant_id: Union[Unset, str] = UNSET
    account_id: Union[Unset, str] = UNSET
    type_: Union[Unset, ApiBackfillAcceptanceType] = UNSET
    comment: Union[Unset, str] = UNSET
    agreement_id: Union[Unset, str] = UNSET
    locale: Union[Unset, str] = UNSET
    serial_number: Union[Unset, str] = UNSET
    iccid: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        acceptance_id = self.acceptance_id

        merchant_id = self.merchant_id

        account_id = self.account_id

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        comment = self.comment

        agreement_id = self.agreement_id

        locale = self.locale

        serial_number = self.serial_number

        iccid = self.iccid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if acceptance_id is not UNSET:
            field_dict["acceptanceId"] = acceptance_id
        if merchant_id is not UNSET:
            field_dict["merchantId"] = merchant_id
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if comment is not UNSET:
            field_dict["comment"] = comment
        if agreement_id is not UNSET:
            field_dict["agreementId"] = agreement_id
        if locale is not UNSET:
            field_dict["locale"] = locale
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if iccid is not UNSET:
            field_dict["iccid"] = iccid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        acceptance_id = d.pop("acceptanceId", UNSET)

        merchant_id = d.pop("merchantId", UNSET)

        account_id = d.pop("accountId", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ApiBackfillAcceptanceType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ApiBackfillAcceptanceType(_type_)

        comment = d.pop("comment", UNSET)

        agreement_id = d.pop("agreementId", UNSET)

        locale = d.pop("locale", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        iccid = d.pop("iccid", UNSET)

        api_backfill_acceptance = cls(
            id=id,
            acceptance_id=acceptance_id,
            merchant_id=merchant_id,
            account_id=account_id,
            type_=type_,
            comment=comment,
            agreement_id=agreement_id,
            locale=locale,
            serial_number=serial_number,
            iccid=iccid,
        )

        api_backfill_acceptance.additional_properties = d
        return api_backfill_acceptance

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
