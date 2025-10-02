import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_ledger_account_key_ledger_account_type import ApiLedgerAccountKeyLedgerAccountType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiLedgerAccountKey")


@_attrs_define
class ApiLedgerAccountKey:
    """
    Attributes:
        id (Union[Unset, int]): Id of the ledger account key
        uuid (Union[Unset, str]): 26-character UUID of the ledger account key
        ledger_account_key (Union[Unset, str]): the key value for this ledger account key
        ledger_account_type (Union[Unset, ApiLedgerAccountKeyLedgerAccountType]):
        default_gl_code (Union[Unset, str]): the default external general ledger (GL) code (or account number) for
            ledger accounts assigned this ledger account key
        short_desc (Union[Unset, str]): a short description of the ledger account key
        full_desc (Union[Unset, str]): a full description of the ledger account key
        purposes (Union[Unset, list[str]]): the purposes or usages for the ledger account key
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the ledger account key was created
            Example: 2020-12-31T23:59:59.123456Z.
        modified_timestamp (Union[Unset, datetime.datetime]): date and time when the ledger account key was last
            modified Example: 2020-12-31T23:59:59.123456Z.
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    ledger_account_key: Union[Unset, str] = UNSET
    ledger_account_type: Union[Unset, ApiLedgerAccountKeyLedgerAccountType] = UNSET
    default_gl_code: Union[Unset, str] = UNSET
    short_desc: Union[Unset, str] = UNSET
    full_desc: Union[Unset, str] = UNSET
    purposes: Union[Unset, list[str]] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        ledger_account_key = self.ledger_account_key

        ledger_account_type: Union[Unset, str] = UNSET
        if not isinstance(self.ledger_account_type, Unset):
            ledger_account_type = self.ledger_account_type.value

        default_gl_code = self.default_gl_code

        short_desc = self.short_desc

        full_desc = self.full_desc

        purposes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.purposes, Unset):
            purposes = self.purposes

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
        if ledger_account_key is not UNSET:
            field_dict["ledgerAccountKey"] = ledger_account_key
        if ledger_account_type is not UNSET:
            field_dict["ledgerAccountType"] = ledger_account_type
        if default_gl_code is not UNSET:
            field_dict["defaultGlCode"] = default_gl_code
        if short_desc is not UNSET:
            field_dict["shortDesc"] = short_desc
        if full_desc is not UNSET:
            field_dict["fullDesc"] = full_desc
        if purposes is not UNSET:
            field_dict["purposes"] = purposes
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

        ledger_account_key = d.pop("ledgerAccountKey", UNSET)

        _ledger_account_type = d.pop("ledgerAccountType", UNSET)
        ledger_account_type: Union[Unset, ApiLedgerAccountKeyLedgerAccountType]
        if isinstance(_ledger_account_type, Unset):
            ledger_account_type = UNSET
        else:
            ledger_account_type = ApiLedgerAccountKeyLedgerAccountType(_ledger_account_type)

        default_gl_code = d.pop("defaultGlCode", UNSET)

        short_desc = d.pop("shortDesc", UNSET)

        full_desc = d.pop("fullDesc", UNSET)

        purposes = cast(list[str], d.pop("purposes", UNSET))

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

        api_ledger_account_key = cls(
            id=id,
            uuid=uuid,
            ledger_account_key=ledger_account_key,
            ledger_account_type=ledger_account_type,
            default_gl_code=default_gl_code,
            short_desc=short_desc,
            full_desc=full_desc,
            purposes=purposes,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
        )

        api_ledger_account_key.additional_properties = d
        return api_ledger_account_key

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
