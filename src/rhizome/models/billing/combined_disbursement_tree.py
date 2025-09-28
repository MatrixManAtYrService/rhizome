"""
SQLModel definition for the combined_disbursement_tree table.

This module provides the SQLModel class for the combined_disbursement_tree table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel


class CombinedDisbursementTree(RhizomeModel, table=False):
    """
    SQLModel for the `combined_disbursement_tree` table.

    This model represents combined_disbursement_tree records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    combined_disbursement_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    charge_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    created_time: datetime.datetime = Field(description="created_time")

    def sanitize(self) -> CombinedDisbursementTree:
        """Return a sanitized copy of this CombinedDisbursementTree instance."""
        return CombinedDisbursementTree(
            id=self.id,
            combined_disbursement_id=self.combined_disbursement_id,
            charge_id=self.charge_id,
            created_time=self.created_time,
        )
