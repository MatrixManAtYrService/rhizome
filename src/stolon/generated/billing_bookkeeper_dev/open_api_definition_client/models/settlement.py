import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.settlement_entity_type import SettlementEntityType
from ..models.settlement_payable_receivable import SettlementPayableReceivable
from ..types import UNSET, Unset

T = TypeVar("T", bound="Settlement")


@_attrs_define
class Settlement:
    """
    Attributes:
        id (Union[Unset, int]):
        uuid (Union[Unset, str]):
        settlement_date (Union[Unset, datetime.date]):
        billing_entity_name (Union[Unset, str]):
        billing_entity_uuid (Union[Unset, str]):
        entity_uuid (Union[Unset, str]):
        alternate_id (Union[Unset, str]):
        entity_type (Union[Unset, SettlementEntityType]):
        payable_receivable (Union[Unset, SettlementPayableReceivable]):
        currency (Union[Unset, str]):
        total_amount (Union[Unset, float]):
        fee_amount (Union[Unset, float]):
        tax_1_amount (Union[Unset, float]):
        tax_2_amount (Union[Unset, float]):
        tax_3_amount (Union[Unset, float]):
        tax_4_amount (Union[Unset, float]):
        lookup_ledger_account_key (Union[Unset, str]):
        gl_code (Union[Unset, str]):
        item_code (Union[Unset, str]):
        description (Union[Unset, str]):
        last_invoice_num (Union[Unset, str]):
        request_uuid (Union[Unset, str]):
        created_timestamp (Union[Unset, datetime.datetime]):
        modified_timestamp (Union[Unset, datetime.datetime]):
        total_tax_amount (Union[Unset, float]):
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    settlement_date: Union[Unset, datetime.date] = UNSET
    billing_entity_name: Union[Unset, str] = UNSET
    billing_entity_uuid: Union[Unset, str] = UNSET
    entity_uuid: Union[Unset, str] = UNSET
    alternate_id: Union[Unset, str] = UNSET
    entity_type: Union[Unset, SettlementEntityType] = UNSET
    payable_receivable: Union[Unset, SettlementPayableReceivable] = UNSET
    currency: Union[Unset, str] = UNSET
    total_amount: Union[Unset, float] = UNSET
    fee_amount: Union[Unset, float] = UNSET
    tax_1_amount: Union[Unset, float] = UNSET
    tax_2_amount: Union[Unset, float] = UNSET
    tax_3_amount: Union[Unset, float] = UNSET
    tax_4_amount: Union[Unset, float] = UNSET
    lookup_ledger_account_key: Union[Unset, str] = UNSET
    gl_code: Union[Unset, str] = UNSET
    item_code: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    last_invoice_num: Union[Unset, str] = UNSET
    request_uuid: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    total_tax_amount: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        settlement_date: Union[Unset, str] = UNSET
        if not isinstance(self.settlement_date, Unset):
            settlement_date = self.settlement_date.isoformat()

        billing_entity_name = self.billing_entity_name

        billing_entity_uuid = self.billing_entity_uuid

        entity_uuid = self.entity_uuid

        alternate_id = self.alternate_id

        entity_type: Union[Unset, str] = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type.value

        payable_receivable: Union[Unset, str] = UNSET
        if not isinstance(self.payable_receivable, Unset):
            payable_receivable = self.payable_receivable.value

        currency = self.currency

        total_amount = self.total_amount

        fee_amount = self.fee_amount

        tax_1_amount = self.tax_1_amount

        tax_2_amount = self.tax_2_amount

        tax_3_amount = self.tax_3_amount

        tax_4_amount = self.tax_4_amount

        lookup_ledger_account_key = self.lookup_ledger_account_key

        gl_code = self.gl_code

        item_code = self.item_code

        description = self.description

        last_invoice_num = self.last_invoice_num

        request_uuid = self.request_uuid

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        modified_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.modified_timestamp, Unset):
            modified_timestamp = self.modified_timestamp.isoformat()

        total_tax_amount = self.total_tax_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if settlement_date is not UNSET:
            field_dict["settlementDate"] = settlement_date
        if billing_entity_name is not UNSET:
            field_dict["billingEntityName"] = billing_entity_name
        if billing_entity_uuid is not UNSET:
            field_dict["billingEntityUuid"] = billing_entity_uuid
        if entity_uuid is not UNSET:
            field_dict["entityUuid"] = entity_uuid
        if alternate_id is not UNSET:
            field_dict["alternateId"] = alternate_id
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if payable_receivable is not UNSET:
            field_dict["payableReceivable"] = payable_receivable
        if currency is not UNSET:
            field_dict["currency"] = currency
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if fee_amount is not UNSET:
            field_dict["feeAmount"] = fee_amount
        if tax_1_amount is not UNSET:
            field_dict["tax1Amount"] = tax_1_amount
        if tax_2_amount is not UNSET:
            field_dict["tax2Amount"] = tax_2_amount
        if tax_3_amount is not UNSET:
            field_dict["tax3Amount"] = tax_3_amount
        if tax_4_amount is not UNSET:
            field_dict["tax4Amount"] = tax_4_amount
        if lookup_ledger_account_key is not UNSET:
            field_dict["lookupLedgerAccountKey"] = lookup_ledger_account_key
        if gl_code is not UNSET:
            field_dict["glCode"] = gl_code
        if item_code is not UNSET:
            field_dict["itemCode"] = item_code
        if description is not UNSET:
            field_dict["description"] = description
        if last_invoice_num is not UNSET:
            field_dict["lastInvoiceNum"] = last_invoice_num
        if request_uuid is not UNSET:
            field_dict["requestUuid"] = request_uuid
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if modified_timestamp is not UNSET:
            field_dict["modifiedTimestamp"] = modified_timestamp
        if total_tax_amount is not UNSET:
            field_dict["totalTaxAmount"] = total_tax_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        _settlement_date = d.pop("settlementDate", UNSET)
        settlement_date: Union[Unset, datetime.date]
        if isinstance(_settlement_date, Unset):
            settlement_date = UNSET
        else:
            settlement_date = isoparse(_settlement_date).date()

        billing_entity_name = d.pop("billingEntityName", UNSET)

        billing_entity_uuid = d.pop("billingEntityUuid", UNSET)

        entity_uuid = d.pop("entityUuid", UNSET)

        alternate_id = d.pop("alternateId", UNSET)

        _entity_type = d.pop("entityType", UNSET)
        entity_type: Union[Unset, SettlementEntityType]
        if isinstance(_entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = SettlementEntityType(_entity_type)

        _payable_receivable = d.pop("payableReceivable", UNSET)
        payable_receivable: Union[Unset, SettlementPayableReceivable]
        if isinstance(_payable_receivable, Unset):
            payable_receivable = UNSET
        else:
            payable_receivable = SettlementPayableReceivable(_payable_receivable)

        currency = d.pop("currency", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        fee_amount = d.pop("feeAmount", UNSET)

        tax_1_amount = d.pop("tax1Amount", UNSET)

        tax_2_amount = d.pop("tax2Amount", UNSET)

        tax_3_amount = d.pop("tax3Amount", UNSET)

        tax_4_amount = d.pop("tax4Amount", UNSET)

        lookup_ledger_account_key = d.pop("lookupLedgerAccountKey", UNSET)

        gl_code = d.pop("glCode", UNSET)

        item_code = d.pop("itemCode", UNSET)

        description = d.pop("description", UNSET)

        last_invoice_num = d.pop("lastInvoiceNum", UNSET)

        request_uuid = d.pop("requestUuid", UNSET)

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

        total_tax_amount = d.pop("totalTaxAmount", UNSET)

        settlement = cls(
            id=id,
            uuid=uuid,
            settlement_date=settlement_date,
            billing_entity_name=billing_entity_name,
            billing_entity_uuid=billing_entity_uuid,
            entity_uuid=entity_uuid,
            alternate_id=alternate_id,
            entity_type=entity_type,
            payable_receivable=payable_receivable,
            currency=currency,
            total_amount=total_amount,
            fee_amount=fee_amount,
            tax_1_amount=tax_1_amount,
            tax_2_amount=tax_2_amount,
            tax_3_amount=tax_3_amount,
            tax_4_amount=tax_4_amount,
            lookup_ledger_account_key=lookup_ledger_account_key,
            gl_code=gl_code,
            item_code=item_code,
            description=description,
            last_invoice_num=last_invoice_num,
            request_uuid=request_uuid,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
            total_tax_amount=total_tax_amount,
        )

        settlement.additional_properties = d
        return settlement

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
