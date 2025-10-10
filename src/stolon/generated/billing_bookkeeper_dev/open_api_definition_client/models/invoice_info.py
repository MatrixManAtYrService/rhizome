import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceInfo")


@_attrs_define
class InvoiceInfo:
    """
    Attributes:
        id (Union[Unset, int]):
        uuid (Union[Unset, str]):
        billing_entity_uuid (Union[Unset, str]):
        entity_uuid (Union[Unset, str]):
        alternate_id (Union[Unset, str]):
        billing_date (Union[Unset, datetime.date]):
        invoice_num (Union[Unset, str]):
        currency (Union[Unset, str]):
        total_amount (Union[Unset, float]):
        document_uuid (Union[Unset, str]):
        request_uuid (Union[Unset, str]):
        created_timestamp (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    billing_entity_uuid: Union[Unset, str] = UNSET
    entity_uuid: Union[Unset, str] = UNSET
    alternate_id: Union[Unset, str] = UNSET
    billing_date: Union[Unset, datetime.date] = UNSET
    invoice_num: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    total_amount: Union[Unset, float] = UNSET
    document_uuid: Union[Unset, str] = UNSET
    request_uuid: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        billing_entity_uuid = self.billing_entity_uuid

        entity_uuid = self.entity_uuid

        alternate_id = self.alternate_id

        billing_date: Union[Unset, str] = UNSET
        if not isinstance(self.billing_date, Unset):
            billing_date = self.billing_date.isoformat()

        invoice_num = self.invoice_num

        currency = self.currency

        total_amount = self.total_amount

        document_uuid = self.document_uuid

        request_uuid = self.request_uuid

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
        if billing_entity_uuid is not UNSET:
            field_dict["billingEntityUuid"] = billing_entity_uuid
        if entity_uuid is not UNSET:
            field_dict["entityUuid"] = entity_uuid
        if alternate_id is not UNSET:
            field_dict["alternateId"] = alternate_id
        if billing_date is not UNSET:
            field_dict["billingDate"] = billing_date
        if invoice_num is not UNSET:
            field_dict["invoiceNum"] = invoice_num
        if currency is not UNSET:
            field_dict["currency"] = currency
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if document_uuid is not UNSET:
            field_dict["documentUuid"] = document_uuid
        if request_uuid is not UNSET:
            field_dict["requestUuid"] = request_uuid
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        billing_entity_uuid = d.pop("billingEntityUuid", UNSET)

        entity_uuid = d.pop("entityUuid", UNSET)

        alternate_id = d.pop("alternateId", UNSET)

        _billing_date = d.pop("billingDate", UNSET)
        billing_date: Union[Unset, datetime.date]
        if _billing_date and not isinstance(_billing_date, Unset):
            billing_date = isoparse(_billing_date).date()

        else:
            billing_date = UNSET

        invoice_num = d.pop("invoiceNum", UNSET)

        currency = d.pop("currency", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        document_uuid = d.pop("documentUuid", UNSET)

        request_uuid = d.pop("requestUuid", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if _created_timestamp and not isinstance(_created_timestamp, Unset):
            created_timestamp = isoparse(_created_timestamp)

        else:
            created_timestamp = UNSET

        invoice_info = cls(
            id=id,
            uuid=uuid,
            billing_entity_uuid=billing_entity_uuid,
            entity_uuid=entity_uuid,
            alternate_id=alternate_id,
            billing_date=billing_date,
            invoice_num=invoice_num,
            currency=currency,
            total_amount=total_amount,
            document_uuid=document_uuid,
            request_uuid=request_uuid,
            created_timestamp=created_timestamp,
        )

        invoice_info.additional_properties = d
        return invoice_info

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
