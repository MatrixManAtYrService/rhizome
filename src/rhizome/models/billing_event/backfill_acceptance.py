"""
SQLModel definition for the backfill_acceptance table.

This module provides the SQLModel class for the backfill_acceptance table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from enum import StrEnum

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class BackfillAcceptanceType(StrEnum):
    """Enum for backfill acceptance types."""

    BILLING = "BILLING"
    CELLULAR_ARREARS = "CELLULAR_ARREARS"
    CELLULAR_ADVANCE = "CELLULAR_ADVANCE"


class BackfillAcceptance(RhizomeModel, table=False):
    """
    SQLModel for the `backfill_acceptance` table.

    This model represents backfill acceptance records for various billing-related
    processes, tracking acceptance data for billing, cellular arrears, and advances.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    acceptance_id: str = Field(max_length=36, description="Unique identifier for the acceptance")
    merchant_id: str = Field(max_length=13, description="ID of the merchant")
    account_id: str = Field(max_length=13, description="ID of the account")
    type: BackfillAcceptanceType = Field(description="Type of backfill acceptance")
    comment: str = Field(max_length=500, description="Comment for the acceptance")
    serial_number: str | None = Field(default=None, max_length=32, description="Serial number of associated device")
    iccid: str | None = Field(default=None, max_length=22, description="ICCID of associated cellular device")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")

    def sanitize(self) -> BackfillAcceptance:
        """Return a sanitized copy of this BackfillAcceptance instance."""
        return BackfillAcceptance(
            id=self.id,
            acceptance_id=sanitize_uuid_field(self.acceptance_id, 36),  # type: ignore
            merchant_id=sanitize_uuid_field(self.merchant_id, 13),  # type: ignore
            account_id=sanitize_uuid_field(self.account_id, 13),  # type: ignore
            type=self.type,
            comment=self.comment,
            serial_number=self.serial_number,
            iccid=self.iccid,
            created_timestamp=self.created_timestamp,
        )
