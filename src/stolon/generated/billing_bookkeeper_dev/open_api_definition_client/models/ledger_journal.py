import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.ledger_journal_credit_debit_ind import LedgerJournalCreditDebitInd
from ..models.ledger_journal_ref_uuid_type import LedgerJournalRefUuidType
from ..types import UNSET, Unset

T = TypeVar("T", bound="LedgerJournal")


@_attrs_define
class LedgerJournal:
    """
    Attributes:
        id (Union[Unset, int]):
        uuid (Union[Unset, str]):
        ledger_account_uuid (Union[Unset, str]):
        journal_date (Union[Unset, datetime.date]):
        ref_uuid_type (Union[Unset, LedgerJournalRefUuidType]):
        ref_uuid (Union[Unset, str]):
        credit_debit_ind (Union[Unset, LedgerJournalCreditDebitInd]):
        currency (Union[Unset, str]):
        amount (Union[Unset, float]):
        created_timestamp (Union[Unset, datetime.datetime]):
        credit_entry (Union[Unset, bool]):
        debit_entry (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    ledger_account_uuid: Union[Unset, str] = UNSET
    journal_date: Union[Unset, datetime.date] = UNSET
    ref_uuid_type: Union[Unset, LedgerJournalRefUuidType] = UNSET
    ref_uuid: Union[Unset, str] = UNSET
    credit_debit_ind: Union[Unset, LedgerJournalCreditDebitInd] = UNSET
    currency: Union[Unset, str] = UNSET
    amount: Union[Unset, float] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    credit_entry: Union[Unset, bool] = UNSET
    debit_entry: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        ledger_account_uuid = self.ledger_account_uuid

        journal_date: Union[Unset, str] = UNSET
        if not isinstance(self.journal_date, Unset):
            journal_date = self.journal_date.isoformat()

        ref_uuid_type: Union[Unset, str] = UNSET
        if not isinstance(self.ref_uuid_type, Unset):
            ref_uuid_type = self.ref_uuid_type.value

        ref_uuid = self.ref_uuid

        credit_debit_ind: Union[Unset, str] = UNSET
        if not isinstance(self.credit_debit_ind, Unset):
            credit_debit_ind = self.credit_debit_ind.value

        currency = self.currency

        amount = self.amount

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        credit_entry = self.credit_entry

        debit_entry = self.debit_entry

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if ledger_account_uuid is not UNSET:
            field_dict["ledgerAccountUuid"] = ledger_account_uuid
        if journal_date is not UNSET:
            field_dict["journalDate"] = journal_date
        if ref_uuid_type is not UNSET:
            field_dict["refUuidType"] = ref_uuid_type
        if ref_uuid is not UNSET:
            field_dict["refUuid"] = ref_uuid
        if credit_debit_ind is not UNSET:
            field_dict["creditDebitInd"] = credit_debit_ind
        if currency is not UNSET:
            field_dict["currency"] = currency
        if amount is not UNSET:
            field_dict["amount"] = amount
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if credit_entry is not UNSET:
            field_dict["creditEntry"] = credit_entry
        if debit_entry is not UNSET:
            field_dict["debitEntry"] = debit_entry

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        ledger_account_uuid = d.pop("ledgerAccountUuid", UNSET)

        _journal_date = d.pop("journalDate", UNSET)
        journal_date: Union[Unset, datetime.date]
        if isinstance(_journal_date, Unset):
            journal_date = UNSET
        else:
            journal_date = isoparse(_journal_date).date()

        _ref_uuid_type = d.pop("refUuidType", UNSET)
        ref_uuid_type: Union[Unset, LedgerJournalRefUuidType]
        if isinstance(_ref_uuid_type, Unset):
            ref_uuid_type = UNSET
        else:
            ref_uuid_type = LedgerJournalRefUuidType(_ref_uuid_type)

        ref_uuid = d.pop("refUuid", UNSET)

        _credit_debit_ind = d.pop("creditDebitInd", UNSET)
        credit_debit_ind: Union[Unset, LedgerJournalCreditDebitInd]
        if isinstance(_credit_debit_ind, Unset):
            credit_debit_ind = UNSET
        else:
            credit_debit_ind = LedgerJournalCreditDebitInd(_credit_debit_ind)

        currency = d.pop("currency", UNSET)

        amount = d.pop("amount", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_created_timestamp, Unset):
            created_timestamp = UNSET
        else:
            created_timestamp = isoparse(_created_timestamp)

        credit_entry = d.pop("creditEntry", UNSET)

        debit_entry = d.pop("debitEntry", UNSET)

        ledger_journal = cls(
            id=id,
            uuid=uuid,
            ledger_account_uuid=ledger_account_uuid,
            journal_date=journal_date,
            ref_uuid_type=ref_uuid_type,
            ref_uuid=ref_uuid,
            credit_debit_ind=credit_debit_ind,
            currency=currency,
            amount=amount,
            created_timestamp=created_timestamp,
            credit_entry=credit_entry,
            debit_entry=debit_entry,
        )

        ledger_journal.additional_properties = d
        return ledger_journal

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
