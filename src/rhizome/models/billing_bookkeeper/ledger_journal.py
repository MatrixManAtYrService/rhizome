"""
SQLModel definition for the ledger_journal table.

This module provides the SQLModel class for the ledger_journal table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from decimal import Decimal

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class LedgerJournal(RhizomeModel, table=False):
    """
    SQLModel for the `ledger_journal` table.

    This model represents ledger journal records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    ledger_account_uuid: str = Field(max_length=26, description="Ledger Account Uuid")
    journal_date: datetime.date = Field(description="Journal Date")
    ref_uuid_type: str = Field(description="Ref Uuid Type")
    ref_uuid: str = Field(max_length=26, description="Ref Uuid")
    cr_db: str = Field(description="Cr Db")
    currency: str = Field(max_length=3, description="Currency")
    amount: Decimal = Field(max_digits=12, decimal_places=3, description="Amount")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")

    def sanitize(self) -> LedgerJournal:
        """Return a sanitized copy of this LedgerJournal instance."""
        return LedgerJournal(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            ledger_account_uuid=sanitize_uuid_field(self.ledger_account_uuid, 26),  # type: ignore
            journal_date=self.journal_date,
            ref_uuid_type=self.ref_uuid_type,
            ref_uuid=sanitize_uuid_field(self.ref_uuid, 26),  # type: ignore
            cr_db=self.cr_db,
            currency=self.currency,
            amount=self.amount,
            created_timestamp=self.created_timestamp,
        )
