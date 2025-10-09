"""
SQLModel definition for the ledger_journal_mutation table.

This module provides the SQLModel class for the ledger_journal_mutation table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from decimal import Decimal

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class LedgerJournalMutation(RhizomeModel, table=False):
    """
    SQLModel for the `ledger_journal_mutation` table.

    This model represents ledger journal mutation records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    mutation_action: str = Field(description="Mutation Action")
    mutation_timestamp: datetime.datetime = Field(description="Mutation Timestamp")
    ledger_journal_id: int = Field(description="Ledger Journal Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    ledger_account_uuid: str | None = Field(default=None, max_length=26, description="Ledger Account Uuid")
    journal_date: datetime.date | None = Field(default=None, description="Journal Date")
    ref_uuid_type: str | None = Field(default=None, description="Ref Uuid Type")
    ref_uuid: str | None = Field(default=None, max_length=26, description="Ref Uuid")
    cr_db: str | None = Field(default=None, description="Cr Db")
    currency: str | None = Field(default=None, max_length=3, description="Currency")
    amount: Decimal | None = Field(default=None, max_digits=12, decimal_places=3, description="Amount")
    created_timestamp: datetime.datetime | None = Field(default=None, description="Created Timestamp")

    def sanitize(self) -> LedgerJournalMutation:
        """Return a sanitized copy of this LedgerJournalMutation instance."""
        return LedgerJournalMutation(
            id=self.id,
            mutation_action=self.mutation_action,
            mutation_timestamp=self.mutation_timestamp,
            ledger_journal_id=self.ledger_journal_id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            ledger_account_uuid=sanitize_uuid_field(self.ledger_account_uuid, 26),
            journal_date=self.journal_date,
            ref_uuid_type=self.ref_uuid_type,
            ref_uuid=sanitize_uuid_field(self.ref_uuid, 26),
            cr_db=self.cr_db,
            currency=self.currency,
            amount=self.amount,
            created_timestamp=self.created_timestamp,
        )
