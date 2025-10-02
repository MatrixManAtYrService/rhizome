import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LedgerAccountBalance")


@_attrs_define
class LedgerAccountBalance:
    """
    Attributes:
        id (Union[Unset, int]):
        uuid (Union[Unset, str]):
        ledger_account_uuid (Union[Unset, str]):
        currency (Union[Unset, str]):
        balance (Union[Unset, float]):
        created_timestamp (Union[Unset, datetime.datetime]):
        modified_timestamp (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    ledger_account_uuid: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    balance: Union[Unset, float] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        ledger_account_uuid = self.ledger_account_uuid

        currency = self.currency

        balance = self.balance

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        modified_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.modified_timestamp, Unset):
            modified_timestamp = self.modified_timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if ledger_account_uuid is not UNSET:
            field_dict["ledgerAccountUuid"] = ledger_account_uuid
        if currency is not UNSET:
            field_dict["currency"] = currency
        if balance is not UNSET:
            field_dict["balance"] = balance
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if modified_timestamp is not UNSET:
            field_dict["modifiedTimestamp"] = modified_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        ledger_account_uuid = d.pop("ledgerAccountUuid", UNSET)

        currency = d.pop("currency", UNSET)

        balance = d.pop("balance", UNSET)

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

        ledger_account_balance = cls(
            id=id,
            uuid=uuid,
            ledger_account_uuid=ledger_account_uuid,
            currency=currency,
            balance=balance,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
        )

        ledger_account_balance.additional_properties = d
        return ledger_account_balance

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
