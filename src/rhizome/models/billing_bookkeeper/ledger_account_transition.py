"""
SQLModel definition for the ledger_account_transition table.

This module provides the SQLModel class for the ledger_account_transition table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class LedgerAccountTransition(RhizomeModel, table=False):
    """
    SQLModel for the `ledger_account_transition` table.

    This model represents ledger account transition records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    action: str = Field(max_length=25, description="Action")
    effective_date: datetime.date = Field(description="Effective Date")
    lookup_ledger_account_key: str = Field(max_length=32, description="Lookup Ledger Account Key")
    credit_ledger_account_key: str = Field(max_length=32, description="Credit Ledger Account Key")
    credit_billing_entity_uuid_source: str = Field(description="Credit Billing Entity Uuid Source")
    debit_ledger_account_key: str = Field(max_length=32, description="Debit Ledger Account Key")
    debit_billing_entity_uuid_source: str = Field(description="Debit Billing Entity Uuid Source")
    deleted_date: datetime.date | None = Field(default=None, description="Deleted Date")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")
    audit_id: str | None = Field(default=None, max_length=26, description="Audit Id")

    def sanitize(self) -> LedgerAccountTransition:
        """Return a sanitized copy of this LedgerAccountTransition instance."""
        return LedgerAccountTransition(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            action=self.action,
            effective_date=self.effective_date,
            lookup_ledger_account_key=self.lookup_ledger_account_key,
            credit_ledger_account_key=self.credit_ledger_account_key,
            credit_billing_entity_uuid_source=self.credit_billing_entity_uuid_source,
            debit_ledger_account_key=self.debit_ledger_account_key,
            debit_billing_entity_uuid_source=self.debit_billing_entity_uuid_source,
            deleted_date=self.deleted_date,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
            audit_id=sanitize_uuid_field(self.audit_id, 26),
        )
