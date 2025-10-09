"""
SQLModel definition for the ledger_account_key table.

This module provides the SQLModel class for the ledger_account_key table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class LedgerAccountKey(RhizomeModel, table=False):
    """
    SQLModel for the `ledger_account_key` table.

    This model represents ledger account key records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    ledger_account_key: str = Field(max_length=32, description="Ledger Account Key")
    ledger_account_type: str = Field(description="Ledger Account Type")
    default_gl_code: str | None = Field(default=None, max_length=40, description="Default Gl Code")
    short_desc: str = Field(max_length=40, description="Short Desc")
    full_desc: str | None = Field(default=None, max_length=255, description="Full Desc")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")

    def sanitize(self) -> LedgerAccountKey:
        """Return a sanitized copy of this LedgerAccountKey instance."""
        return LedgerAccountKey(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            ledger_account_key=self.ledger_account_key,
            ledger_account_type=self.ledger_account_type,
            default_gl_code=self.default_gl_code,
            short_desc=self.short_desc,
            full_desc=self.full_desc,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
        )
