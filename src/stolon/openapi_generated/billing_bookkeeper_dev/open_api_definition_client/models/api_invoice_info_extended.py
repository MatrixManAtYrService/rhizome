import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_invoice_info_extended_entity_type import ApiInvoiceInfoExtendedEntityType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_fee_tax import ApiFeeTax
    from ..models.api_invoice_info_amount import ApiInvoiceInfoAmount


T = TypeVar("T", bound="ApiInvoiceInfoExtended")


@_attrs_define
class ApiInvoiceInfoExtended:
    """
    Attributes:
        id (Union[Unset, int]): Id of the invoice info
        uuid (Union[Unset, str]): 26-character UUID of the invoice document
        billing_entity_uuid (Union[Unset, str]): 26-character UUID of the billing entity that the invoice belongs to
        entity_uuid (Union[Unset, str]): 13-character UUID of the entity that the invoice belongs to
        alternate_id (Union[Unset, str]): alternate identifier (such as a MID) for the entity that the invoice belongs
            to
        name (Union[Unset, str]): name of billing entity
        entity_type (Union[Unset, ApiInvoiceInfoExtendedEntityType]):
        billing_date (Union[Unset, datetime.date]): billing date when the invoice was created
        invoice_num (Union[Unset, str]): invoice number assigned to the invoice
        currency (Union[Unset, str]): the currency of the invoice total amount Example: USD.
        total_amount (Union[Unset, float]): the total amount of the invoice
        document_uuid (Union[Unset, str]): 26-character UUID of the invoice document
        request_uuid (Union[Unset, str]): 26-character UUID of the billing request that produced this settlement request
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the ledger account transition was
            created Example: 2020-12-31T23:59:59.123456Z.
        invoice_info_amounts (Union[Unset, list['ApiInvoiceInfoAmount']]): Array of associated invoice_info_amount
            entries
        fee_taxes (Union[Unset, list['ApiFeeTax']]): Array of associated fee_tax entries
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    billing_entity_uuid: Union[Unset, str] = UNSET
    entity_uuid: Union[Unset, str] = UNSET
    alternate_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    entity_type: Union[Unset, ApiInvoiceInfoExtendedEntityType] = UNSET
    billing_date: Union[Unset, datetime.date] = UNSET
    invoice_num: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    total_amount: Union[Unset, float] = UNSET
    document_uuid: Union[Unset, str] = UNSET
    request_uuid: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    invoice_info_amounts: Union[Unset, list["ApiInvoiceInfoAmount"]] = UNSET
    fee_taxes: Union[Unset, list["ApiFeeTax"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        billing_entity_uuid = self.billing_entity_uuid

        entity_uuid = self.entity_uuid

        alternate_id = self.alternate_id

        name = self.name

        entity_type: Union[Unset, str] = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type.value

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

        invoice_info_amounts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.invoice_info_amounts, Unset):
            invoice_info_amounts = []
            for invoice_info_amounts_item_data in self.invoice_info_amounts:
                invoice_info_amounts_item = invoice_info_amounts_item_data.to_dict()
                invoice_info_amounts.append(invoice_info_amounts_item)

        fee_taxes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fee_taxes, Unset):
            fee_taxes = []
            for fee_taxes_item_data in self.fee_taxes:
                fee_taxes_item = fee_taxes_item_data.to_dict()
                fee_taxes.append(fee_taxes_item)

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
        if name is not UNSET:
            field_dict["name"] = name
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
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
        if invoice_info_amounts is not UNSET:
            field_dict["invoiceInfoAmounts"] = invoice_info_amounts
        if fee_taxes is not UNSET:
            field_dict["feeTaxes"] = fee_taxes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_fee_tax import ApiFeeTax
        from ..models.api_invoice_info_amount import ApiInvoiceInfoAmount

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        billing_entity_uuid = d.pop("billingEntityUuid", UNSET)

        entity_uuid = d.pop("entityUuid", UNSET)

        alternate_id = d.pop("alternateId", UNSET)

        name = d.pop("name", UNSET)

        _entity_type = d.pop("entityType", UNSET)
        entity_type: Union[Unset, ApiInvoiceInfoExtendedEntityType]
        if _entity_type and not isinstance(_entity_type, Unset):
            entity_type = ApiInvoiceInfoExtendedEntityType(_entity_type)

        else:
            entity_type = UNSET

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

        invoice_info_amounts = []
        _invoice_info_amounts = d.pop("invoiceInfoAmounts", UNSET)
        for invoice_info_amounts_item_data in _invoice_info_amounts or []:
            invoice_info_amounts_item = ApiInvoiceInfoAmount.from_dict(invoice_info_amounts_item_data)

            invoice_info_amounts.append(invoice_info_amounts_item)

        fee_taxes = []
        _fee_taxes = d.pop("feeTaxes", UNSET)
        for fee_taxes_item_data in _fee_taxes or []:
            fee_taxes_item = ApiFeeTax.from_dict(fee_taxes_item_data)

            fee_taxes.append(fee_taxes_item)

        api_invoice_info_extended = cls(
            id=id,
            uuid=uuid,
            billing_entity_uuid=billing_entity_uuid,
            entity_uuid=entity_uuid,
            alternate_id=alternate_id,
            name=name,
            entity_type=entity_type,
            billing_date=billing_date,
            invoice_num=invoice_num,
            currency=currency,
            total_amount=total_amount,
            document_uuid=document_uuid,
            request_uuid=request_uuid,
            created_timestamp=created_timestamp,
            invoice_info_amounts=invoice_info_amounts,
            fee_taxes=fee_taxes,
        )

        api_invoice_info_extended.additional_properties = d
        return api_invoice_info_extended

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
