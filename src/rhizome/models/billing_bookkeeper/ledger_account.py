"""
SQLModel definition for the ledger_account table.

This module provides the SQLModel class for the ledger_account table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class LedgerAccount(RhizomeModel, table=False):
    """
    SQLModel for the `ledger_account` table.

    This model represents ledger account records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    ledger_account_key: str = Field(max_length=32, description="Ledger Account Key")
    billing_entity_uuid: str = Field(max_length=26, description="Billing Entity Uuid")
    gl_code: str | None = Field(default=None, max_length=40, description="Gl Code")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")

    def sanitize(self) -> LedgerAccount:
        """Return a sanitized copy of this LedgerAccount instance."""
        return LedgerAccount(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            ledger_account_key=self.ledger_account_key,
            billing_entity_uuid=sanitize_uuid_field(self.billing_entity_uuid, 26),  # type: ignore
            gl_code=self.gl_code,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
        )
