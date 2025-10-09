"""
SQLModel definition for the ledger_account_balance table.

This module provides the SQLModel class for the ledger_account_balance table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from decimal import Decimal

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class LedgerAccountBalance(RhizomeModel, table=False):
    """
    SQLModel for the `ledger_account_balance` table.

    This model represents ledger account balance records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    ledger_account_uuid: str = Field(max_length=26, description="Ledger Account Uuid")
    currency: str = Field(max_length=3, description="Currency")
    balance: Decimal = Field(max_digits=12, decimal_places=3, description="Balance")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")

    def sanitize(self) -> LedgerAccountBalance:
        """Return a sanitized copy of this LedgerAccountBalance instance."""
        return LedgerAccountBalance(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            ledger_account_uuid=sanitize_uuid_field(self.ledger_account_uuid, 26),  # type: ignore
            currency=self.currency,
            balance=self.balance,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
        )
