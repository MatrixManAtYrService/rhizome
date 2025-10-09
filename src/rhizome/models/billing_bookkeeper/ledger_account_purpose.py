"""
SQLModel definition for the ledger_account_purpose table.

This module provides the SQLModel class for the ledger_account_purpose table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class LedgerAccountPurpose(RhizomeModel, table=False):
    """
    SQLModel for the `ledger_account_purpose` table.

    This model represents ledger account purpose records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    purpose: str = Field(max_length=25, description="Purpose")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")

    def sanitize(self) -> LedgerAccountPurpose:
        """Return a sanitized copy of this LedgerAccountPurpose instance."""
        return LedgerAccountPurpose(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            purpose=self.purpose,
            created_timestamp=self.created_timestamp,
        )
