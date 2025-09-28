"""
SQLModel definition for the vendor_disbursement_state_attempt table.

This module provides the SQLModel class for the vendor_disbursement_state_attempt table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel


class VendorDisbursementStateAttempt(RhizomeModel, table=False):
    """
    SQLModel for the `vendor_disbursement_state_attempt` table.

    This model represents vendor_disbursement_state_attempt records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    charge_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    state: str | None = Field(default=None, description="state")
    created_time: datetime.datetime = Field(description="created_time")
    modified_time: datetime.datetime = Field(description="modified_time")

    def sanitize(self) -> VendorDisbursementStateAttempt:
        """Return a sanitized copy of this VendorDisbursementStateAttempt instance."""
        return VendorDisbursementStateAttempt(
            id=self.id,
            charge_id=self.charge_id,
            state=self.state,
            created_time=self.created_time,
            modified_time=self.modified_time,
        )
