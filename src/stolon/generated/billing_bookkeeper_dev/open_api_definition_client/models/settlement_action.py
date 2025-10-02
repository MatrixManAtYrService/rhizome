import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SettlementAction")


@_attrs_define
class SettlementAction:
    """
    Attributes:
        settlement_uuid (Union[Unset, str]):
        action_date (Union[Unset, datetime.date]):
        action (Union[Unset, str]):
        currency (Union[Unset, str]):
        total_amount (Union[Unset, float]):
        fee_amount (Union[Unset, float]):
        tax_1_amount (Union[Unset, float]):
        tax_2_amount (Union[Unset, float]):
        tax_3_amount (Union[Unset, float]):
        tax_4_amount (Union[Unset, float]):
        reject_code (Union[Unset, str]):
        id (Union[Unset, int]):
        uuid (Union[Unset, str]):
        message (Union[Unset, str]):
        ledger_account_transition_uuid (Union[Unset, str]):
        credit_ledger_account_uuid (Union[Unset, str]):
        debit_ledger_account_uuid (Union[Unset, str]):
        created_timestamp (Union[Unset, datetime.datetime]):
        total_tax_amount (Union[Unset, float]):
    """

    settlement_uuid: Union[Unset, str] = UNSET
    action_date: Union[Unset, datetime.date] = UNSET
    action: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    total_amount: Union[Unset, float] = UNSET
    fee_amount: Union[Unset, float] = UNSET
    tax_1_amount: Union[Unset, float] = UNSET
    tax_2_amount: Union[Unset, float] = UNSET
    tax_3_amount: Union[Unset, float] = UNSET
    tax_4_amount: Union[Unset, float] = UNSET
    reject_code: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    ledger_account_transition_uuid: Union[Unset, str] = UNSET
    credit_ledger_account_uuid: Union[Unset, str] = UNSET
    debit_ledger_account_uuid: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    total_tax_amount: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        settlement_uuid = self.settlement_uuid

        action_date: Union[Unset, str] = UNSET
        if not isinstance(self.action_date, Unset):
            action_date = self.action_date.isoformat()

        action = self.action

        currency = self.currency

        total_amount = self.total_amount

        fee_amount = self.fee_amount

        tax_1_amount = self.tax_1_amount

        tax_2_amount = self.tax_2_amount

        tax_3_amount = self.tax_3_amount

        tax_4_amount = self.tax_4_amount

        reject_code = self.reject_code

        id = self.id

        uuid = self.uuid

        message = self.message

        ledger_account_transition_uuid = self.ledger_account_transition_uuid

        credit_ledger_account_uuid = self.credit_ledger_account_uuid

        debit_ledger_account_uuid = self.debit_ledger_account_uuid

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        total_tax_amount = self.total_tax_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if settlement_uuid is not UNSET:
            field_dict["settlementUuid"] = settlement_uuid
        if action_date is not UNSET:
            field_dict["actionDate"] = action_date
        if action is not UNSET:
            field_dict["action"] = action
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
        if reject_code is not UNSET:
            field_dict["rejectCode"] = reject_code
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if message is not UNSET:
            field_dict["message"] = message
        if ledger_account_transition_uuid is not UNSET:
            field_dict["ledgerAccountTransitionUuid"] = ledger_account_transition_uuid
        if credit_ledger_account_uuid is not UNSET:
            field_dict["creditLedgerAccountUuid"] = credit_ledger_account_uuid
        if debit_ledger_account_uuid is not UNSET:
            field_dict["debitLedgerAccountUuid"] = debit_ledger_account_uuid
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if total_tax_amount is not UNSET:
            field_dict["totalTaxAmount"] = total_tax_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        settlement_uuid = d.pop("settlementUuid", UNSET)

        _action_date = d.pop("actionDate", UNSET)
        action_date: Union[Unset, datetime.date]
        if isinstance(_action_date, Unset):
            action_date = UNSET
        else:
            action_date = isoparse(_action_date).date()

        action = d.pop("action", UNSET)

        currency = d.pop("currency", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        fee_amount = d.pop("feeAmount", UNSET)

        tax_1_amount = d.pop("tax1Amount", UNSET)

        tax_2_amount = d.pop("tax2Amount", UNSET)

        tax_3_amount = d.pop("tax3Amount", UNSET)

        tax_4_amount = d.pop("tax4Amount", UNSET)

        reject_code = d.pop("rejectCode", UNSET)

        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        message = d.pop("message", UNSET)

        ledger_account_transition_uuid = d.pop("ledgerAccountTransitionUuid", UNSET)

        credit_ledger_account_uuid = d.pop("creditLedgerAccountUuid", UNSET)

        debit_ledger_account_uuid = d.pop("debitLedgerAccountUuid", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_created_timestamp, Unset):
            created_timestamp = UNSET
        else:
            created_timestamp = isoparse(_created_timestamp)

        total_tax_amount = d.pop("totalTaxAmount", UNSET)

        settlement_action = cls(
            settlement_uuid=settlement_uuid,
            action_date=action_date,
            action=action,
            currency=currency,
            total_amount=total_amount,
            fee_amount=fee_amount,
            tax_1_amount=tax_1_amount,
            tax_2_amount=tax_2_amount,
            tax_3_amount=tax_3_amount,
            tax_4_amount=tax_4_amount,
            reject_code=reject_code,
            id=id,
            uuid=uuid,
            message=message,
            ledger_account_transition_uuid=ledger_account_transition_uuid,
            credit_ledger_account_uuid=credit_ledger_account_uuid,
            debit_ledger_account_uuid=debit_ledger_account_uuid,
            created_timestamp=created_timestamp,
            total_tax_amount=total_tax_amount,
        )

        settlement_action.additional_properties = d
        return settlement_action

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
