import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiLedgerAccountKeyPurpose")


@_attrs_define
class ApiLedgerAccountKeyPurpose:
    """
    Attributes:
        id (Union[Unset, int]): Id of the ledger account key-purpose association
        uuid (Union[Unset, str]): 26-character UUID of the ledger account key-purpose association
        purpose (Union[Unset, str]): the purpose or usage for the ledger account key-purpose association
        ledger_account_key (Union[Unset, str]): the key value for this ledger account key-purpose association
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the ledger account key-purpose
            association was created Example: 2020-12-31T23:59:59.123456Z.
        audit_id (Union[Unset, str]): identifier for the user who created or last modified this ledger account key-
            purpose association
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    purpose: Union[Unset, str] = UNSET
    ledger_account_key: Union[Unset, str] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    audit_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        purpose = self.purpose

        ledger_account_key = self.ledger_account_key

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        audit_id = self.audit_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if ledger_account_key is not UNSET:
            field_dict["ledgerAccountKey"] = ledger_account_key
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if audit_id is not UNSET:
            field_dict["auditId"] = audit_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        purpose = d.pop("purpose", UNSET)

        ledger_account_key = d.pop("ledgerAccountKey", UNSET)

        _created_timestamp = d.pop("createdTimestamp", UNSET)
        created_timestamp: Union[Unset, datetime.datetime]
        if _created_timestamp and not isinstance(_created_timestamp, Unset):
            created_timestamp = isoparse(_created_timestamp)

        else:
            created_timestamp = UNSET

        audit_id = d.pop("auditId", UNSET)

        api_ledger_account_key_purpose = cls(
            id=id,
            uuid=uuid,
            purpose=purpose,
            ledger_account_key=ledger_account_key,
            created_timestamp=created_timestamp,
            audit_id=audit_id,
        )

        api_ledger_account_key_purpose.additional_properties = d
        return api_ledger_account_key_purpose

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
