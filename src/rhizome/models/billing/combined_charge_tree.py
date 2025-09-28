"""
SQLModel definition for the combined_charge_tree table.

This module provides the SQLModel class for the combined_charge_tree table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel


class CombinedChargeTree(RhizomeModel, table=False):
    """
    SQLModel for the `combined_charge_tree` table.

    This model represents combined_charge_tree records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    combined_charge_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    charge_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    created_time: datetime.datetime = Field(description="created_time")

    def sanitize(self) -> CombinedChargeTree:
        """Return a sanitized copy of this CombinedChargeTree instance."""
        return CombinedChargeTree(
            id=self.id,
            combined_charge_id=self.combined_charge_id,
            charge_id=self.charge_id,
            created_time=self.created_time,
        )
