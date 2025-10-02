import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiInvoiceAllianceCode")


@_attrs_define
class ApiInvoiceAllianceCode:
    """
    Attributes:
        id (Union[Unset, int]): Id of the invoice alliance code definition
        uuid (Union[Unset, str]): 26-character UUID of the invoice alliance code definition
        billing_entity_uuid (Union[Unset, str]): 26-character UUID of the billing entity this invoice alliance code
            belongs to
        name (Union[Unset, str]): name of billing entity
        alliance_code (Union[Unset, str]): 3-character code embedded into generated invoice numbers for the alliance (or
            billing entity that the alliance code belongs to) Example: 001.
        invoice_count (Union[Unset, int]): the last sequential number assigned to an invoice for the alliance code
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the invoice alliance code definition was
            created Example: 2020-12-31T23:59:59.123456Z.
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    billing_entity_uuid: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    alliance_code: Union[Unset, str] = UNSET
    invoice_count: Union[Unset, int] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        billing_entity_uuid = self.billing_entity_uuid

        name = self.name

        alliance_code = self.alliance_code

        invoice_count = self.invoice_count

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
        if name is not UNSET:
            field_dict["name"] = name
        if alliance_code is not UNSET:
            field_dict["allianceCode"] = alliance_code
        if invoice_count is not UNSET:
            field_dict["invoiceCount"] = invoice_count
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        billing_entity_uuid = d.pop("billingEntityUuid", UNSET)

        name = d.pop("name", UNSET)

        alliance_code = d.pop("allianceCode", UNSET)

        invoice_count = d.pop("invoiceCount", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_created_timestamp, Unset):
            created_timestamp = UNSET
        else:
            created_timestamp = isoparse(_created_timestamp)

        api_invoice_alliance_code = cls(
            id=id,
            uuid=uuid,
            billing_entity_uuid=billing_entity_uuid,
            name=name,
            alliance_code=alliance_code,
            invoice_count=invoice_count,
            created_timestamp=created_timestamp,
        )

        api_invoice_alliance_code.additional_properties = d
        return api_invoice_alliance_code

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
