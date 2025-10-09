"""
SQLModel definition for the ledger_account_key_purpose table.

This module provides the SQLModel class for the ledger_account_key_purpose table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class LedgerAccountKeyPurpose(RhizomeModel, table=False):
    """
    SQLModel for the `ledger_account_key_purpose` table.

    This model represents ledger account key purpose records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    purpose: str = Field(max_length=25, description="Purpose")
    ledger_account_key: str = Field(max_length=32, description="Ledger Account Key")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    audit_id: str | None = Field(default=None, max_length=26, description="Audit Id")

    def sanitize(self) -> LedgerAccountKeyPurpose:
        """Return a sanitized copy of this LedgerAccountKeyPurpose instance."""
        return LedgerAccountKeyPurpose(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            purpose=self.purpose,
            ledger_account_key=self.ledger_account_key,
            created_timestamp=self.created_timestamp,
            audit_id=sanitize_uuid_field(self.audit_id, 26),
        )
