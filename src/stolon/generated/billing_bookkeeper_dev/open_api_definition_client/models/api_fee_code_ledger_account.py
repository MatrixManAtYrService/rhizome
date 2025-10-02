import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_fee_code_ledger_account_credit_billing_entity_uuid_source import (
    ApiFeeCodeLedgerAccountCreditBillingEntityUuidSource,
)
from ..models.api_fee_code_ledger_account_debit_billing_entity_uuid_source import (
    ApiFeeCodeLedgerAccountDebitBillingEntityUuidSource,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiFeeCodeLedgerAccount")


@_attrs_define
class ApiFeeCodeLedgerAccount:
    """
    Attributes:
        id (Union[Unset, int]): Id of the fee-code-to-ledger-account mapping
        uuid (Union[Unset, str]): 26-character UUID of the fee-code-to-ledger-account mapping
        fee_category (Union[Unset, str]): the fee category that maps to the ledger account key
        fee_code (Union[Unset, str]): the fee code that maps to the ledger account key
        effective_date (Union[Unset, datetime.date]): effective date for the fee-code-to-ledger-account mapping
        credit_ledger_account_key (Union[Unset, str]): the credit ledger account key that the fee category and fee code
            combination maps to
        credit_billing_entity_uuid_source (Union[Unset, ApiFeeCodeLedgerAccountCreditBillingEntityUuidSource]):
        debit_ledger_account_key (Union[Unset, str]): the debit ledger account key that the fee category and fee code
            combination maps to
        debit_billing_entity_uuid_source (Union[Unset, ApiFeeCodeLedgerAccountDebitBillingEntityUuidSource]):
        deleted_date (Union[Unset, datetime.date]): date the fee-code-to-ledger-account mapping is no longer effective,
            or was logically deleted
        created_timestamp (Union[Unset, datetime.datetime]): date and time when the ledger account was created Example:
            2020-12-31T23:59:59.123456Z.
        modified_timestamp (Union[Unset, datetime.datetime]): date and time when the ledger account was last modified
            Example: 2020-12-31T23:59:59.123456Z.
        audit_id (Union[Unset, str]): identifier for the user who created or last modified this fee-code-to-ledger-
            account mapping
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    fee_category: Union[Unset, str] = UNSET
    fee_code: Union[Unset, str] = UNSET
    effective_date: Union[Unset, datetime.date] = UNSET
    credit_ledger_account_key: Union[Unset, str] = UNSET
    credit_billing_entity_uuid_source: Union[Unset, ApiFeeCodeLedgerAccountCreditBillingEntityUuidSource] = UNSET
    debit_ledger_account_key: Union[Unset, str] = UNSET
    debit_billing_entity_uuid_source: Union[Unset, ApiFeeCodeLedgerAccountDebitBillingEntityUuidSource] = UNSET
    deleted_date: Union[Unset, datetime.date] = UNSET
    created_timestamp: Union[Unset, datetime.datetime] = UNSET
    modified_timestamp: Union[Unset, datetime.datetime] = UNSET
    audit_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        fee_category = self.fee_category

        fee_code = self.fee_code

        effective_date: Union[Unset, str] = UNSET
        if not isinstance(self.effective_date, Unset):
            effective_date = self.effective_date.isoformat()

        credit_ledger_account_key = self.credit_ledger_account_key

        credit_billing_entity_uuid_source: Union[Unset, str] = UNSET
        if not isinstance(self.credit_billing_entity_uuid_source, Unset):
            credit_billing_entity_uuid_source = self.credit_billing_entity_uuid_source.value

        debit_ledger_account_key = self.debit_ledger_account_key

        debit_billing_entity_uuid_source: Union[Unset, str] = UNSET
        if not isinstance(self.debit_billing_entity_uuid_source, Unset):
            debit_billing_entity_uuid_source = self.debit_billing_entity_uuid_source.value

        deleted_date: Union[Unset, str] = UNSET
        if not isinstance(self.deleted_date, Unset):
            deleted_date = self.deleted_date.isoformat()

        created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.created_timestamp, Unset):
            created_timestamp = self.created_timestamp.isoformat()

        modified_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.modified_timestamp, Unset):
            modified_timestamp = self.modified_timestamp.isoformat()

        audit_id = self.audit_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if fee_category is not UNSET:
            field_dict["feeCategory"] = fee_category
        if fee_code is not UNSET:
            field_dict["feeCode"] = fee_code
        if effective_date is not UNSET:
            field_dict["effectiveDate"] = effective_date
        if credit_ledger_account_key is not UNSET:
            field_dict["creditLedgerAccountKey"] = credit_ledger_account_key
        if credit_billing_entity_uuid_source is not UNSET:
            field_dict["creditBillingEntityUuidSource"] = credit_billing_entity_uuid_source
        if debit_ledger_account_key is not UNSET:
            field_dict["debitLedgerAccountKey"] = debit_ledger_account_key
        if debit_billing_entity_uuid_source is not UNSET:
            field_dict["debitBillingEntityUuidSource"] = debit_billing_entity_uuid_source
        if deleted_date is not UNSET:
            field_dict["deletedDate"] = deleted_date
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if modified_timestamp is not UNSET:
            field_dict["modifiedTimestamp"] = modified_timestamp
        if audit_id is not UNSET:
            field_dict["auditId"] = audit_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        fee_category = d.pop("feeCategory", UNSET)

        fee_code = d.pop("feeCode", UNSET)

        _effective_date = d.pop("effectiveDate", UNSET)
        effective_date: Union[Unset, datetime.date]
        if isinstance(_effective_date, Unset):
            effective_date = UNSET
        else:
            effective_date = isoparse(_effective_date).date()

        credit_ledger_account_key = d.pop("creditLedgerAccountKey", UNSET)

        _credit_billing_entity_uuid_source = d.pop("creditBillingEntityUuidSource", UNSET)
        credit_billing_entity_uuid_source: Union[Unset, ApiFeeCodeLedgerAccountCreditBillingEntityUuidSource]
        if isinstance(_credit_billing_entity_uuid_source, Unset):
            credit_billing_entity_uuid_source = UNSET
        else:
            credit_billing_entity_uuid_source = ApiFeeCodeLedgerAccountCreditBillingEntityUuidSource(
                _credit_billing_entity_uuid_source
            )

        debit_ledger_account_key = d.pop("debitLedgerAccountKey", UNSET)

        _debit_billing_entity_uuid_source = d.pop("debitBillingEntityUuidSource", UNSET)
        debit_billing_entity_uuid_source: Union[Unset, ApiFeeCodeLedgerAccountDebitBillingEntityUuidSource]
        if isinstance(_debit_billing_entity_uuid_source, Unset):
            debit_billing_entity_uuid_source = UNSET
        else:
            debit_billing_entity_uuid_source = ApiFeeCodeLedgerAccountDebitBillingEntityUuidSource(
                _debit_billing_entity_uuid_source
            )

        _deleted_date = d.pop("deletedDate", UNSET)
        deleted_date: Union[Unset, datetime.date]
        if isinstance(_deleted_date, Unset):
            deleted_date = UNSET
        else:
            deleted_date = isoparse(_deleted_date).date()

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

        audit_id = d.pop("auditId", UNSET)

        api_fee_code_ledger_account = cls(
            id=id,
            uuid=uuid,
            fee_category=fee_category,
            fee_code=fee_code,
            effective_date=effective_date,
            credit_ledger_account_key=credit_ledger_account_key,
            credit_billing_entity_uuid_source=credit_billing_entity_uuid_source,
            debit_ledger_account_key=debit_ledger_account_key,
            debit_billing_entity_uuid_source=debit_billing_entity_uuid_source,
            deleted_date=deleted_date,
            created_timestamp=created_timestamp,
            modified_timestamp=modified_timestamp,
            audit_id=audit_id,
        )

        api_fee_code_ledger_account.additional_properties = d
        return api_fee_code_ledger_account

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
