import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiInvoiceInfoAmount")


@_attrs_define
class ApiInvoiceInfoAmount:
    """Array of associated invoice_info_amount entries

    Attributes:
        id (Union[Unset, int]): Id of the invoice info
        uuid (Union[Unset, str]): 26-character UUID of the invoice document
        invoice_info_uuid (Union[Unset, str]): 26-character invoice-info UUID
        currency (Union[Unset, str]): the currency of the invoice total amount Example: USD.
        amount (Union[Unset, float]): the amount of the invoice
        fee_category_group (Union[Unset, str]): are used to group and organize fee codes
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the ledger account transition was
            created Example: 2020-12-31T23:59:59.123456Z.
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    invoice_info_uuid: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    amount: Union[Unset, float] = UNSET
    fee_category_group: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        invoice_info_uuid = self.invoice_info_uuid

        currency = self.currency

        amount = self.amount

        fee_category_group = self.fee_category_group

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
        if invoice_info_uuid is not UNSET:
            field_dict["invoice_info_uuid"] = invoice_info_uuid
        if currency is not UNSET:
            field_dict["currency"] = currency
        if amount is not UNSET:
            field_dict["amount"] = amount
        if fee_category_group is not UNSET:
            field_dict["feeCategoryGroup"] = fee_category_group
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        invoice_info_uuid = d.pop("invoice_info_uuid", UNSET)

        currency = d.pop("currency", UNSET)

        amount = d.pop("amount", UNSET)

        fee_category_group = d.pop("feeCategoryGroup", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if _created_timestamp and not isinstance(_created_timestamp, Unset):
            created_timestamp = isoparse(_created_timestamp)

        else:
            created_timestamp = UNSET

        api_invoice_info_amount = cls(
            id=id,
            uuid=uuid,
            invoice_info_uuid=invoice_info_uuid,
            currency=currency,
            amount=amount,
            fee_category_group=fee_category_group,
            created_timestamp=created_timestamp,
        )

        api_invoice_info_amount.additional_properties = d
        return api_invoice_info_amount

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
