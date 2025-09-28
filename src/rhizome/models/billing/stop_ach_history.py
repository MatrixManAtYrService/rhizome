"""
SQLModel definition for the stop_ach_history table.

This module provides the SQLModel class for the stop_ach_history table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel


class StopAchHistory(RhizomeModel, table=False):
    """
    SQLModel for the `stop_ach_history` table.

    This model represents stop_ach_history records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    merchant_odessa_mapping_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    old_stop_ach: bool = Field(description="old_stop_ach")
    old_modified_time: datetime.datetime | None = Field(default=None, description="old_modified_time")
    created_time: datetime.datetime = Field(description="created_time")

    def sanitize(self) -> StopAchHistory:
        """Return a sanitized copy of this StopAchHistory instance."""
        return StopAchHistory(
            id=self.id,
            merchant_odessa_mapping_id=self.merchant_odessa_mapping_id,
            old_stop_ach=self.old_stop_ach,
            old_modified_time=self.old_modified_time,
            created_time=self.created_time,
        )
