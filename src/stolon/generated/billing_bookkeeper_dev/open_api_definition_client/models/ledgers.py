from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ledger_account import LedgerAccount
    from ..models.ledger_account_balance import LedgerAccountBalance
    from ..models.ledger_journal import LedgerJournal


T = TypeVar("T", bound="Ledgers")


@_attrs_define
class Ledgers:
    """
    Attributes:
        ledger_accounts (Union[Unset, list['LedgerAccount']]):
        ledger_account_balances (Union[Unset, list['LedgerAccountBalance']]):
        ledger_journals (Union[Unset, list['LedgerJournal']]):
    """

    ledger_accounts: Union[Unset, list["LedgerAccount"]] = UNSET
    ledger_account_balances: Union[Unset, list["LedgerAccountBalance"]] = UNSET
    ledger_journals: Union[Unset, list["LedgerJournal"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ledger_accounts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ledger_accounts, Unset):
            ledger_accounts = []
            for ledger_accounts_item_data in self.ledger_accounts:
                ledger_accounts_item = ledger_accounts_item_data.to_dict()
                ledger_accounts.append(ledger_accounts_item)

        ledger_account_balances: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ledger_account_balances, Unset):
            ledger_account_balances = []
            for ledger_account_balances_item_data in self.ledger_account_balances:
                ledger_account_balances_item = ledger_account_balances_item_data.to_dict()
                ledger_account_balances.append(ledger_account_balances_item)

        ledger_journals: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ledger_journals, Unset):
            ledger_journals = []
            for ledger_journals_item_data in self.ledger_journals:
                ledger_journals_item = ledger_journals_item_data.to_dict()
                ledger_journals.append(ledger_journals_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ledger_accounts is not UNSET:
            field_dict["ledgerAccounts"] = ledger_accounts
        if ledger_account_balances is not UNSET:
            field_dict["ledgerAccountBalances"] = ledger_account_balances
        if ledger_journals is not UNSET:
            field_dict["ledgerJournals"] = ledger_journals

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ledger_account import LedgerAccount
        from ..models.ledger_account_balance import LedgerAccountBalance
        from ..models.ledger_journal import LedgerJournal

        d = dict(src_dict)
        ledger_accounts = []
        _ledger_accounts = d.pop("ledgerAccounts", UNSET)
        for ledger_accounts_item_data in _ledger_accounts or []:
            ledger_accounts_item = LedgerAccount.from_dict(ledger_accounts_item_data)

            ledger_accounts.append(ledger_accounts_item)

        ledger_account_balances = []
        _ledger_account_balances = d.pop("ledgerAccountBalances", UNSET)
        for ledger_account_balances_item_data in _ledger_account_balances or []:
            ledger_account_balances_item = LedgerAccountBalance.from_dict(ledger_account_balances_item_data)

            ledger_account_balances.append(ledger_account_balances_item)

        ledger_journals = []
        _ledger_journals = d.pop("ledgerJournals", UNSET)
        for ledger_journals_item_data in _ledger_journals or []:
            ledger_journals_item = LedgerJournal.from_dict(ledger_journals_item_data)

            ledger_journals.append(ledger_journals_item)

        ledgers = cls(
            ledger_accounts=ledger_accounts,
            ledger_account_balances=ledger_account_balances,
            ledger_journals=ledger_journals,
        )

        ledgers.additional_properties = d
        return ledgers

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
