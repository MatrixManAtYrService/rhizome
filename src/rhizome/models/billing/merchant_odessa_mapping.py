"""
SQLModel definition for the merchant_odessa_mapping table.

This module provides the SQLModel class for the merchant_odessa_mapping table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel


class MerchantOdessaMapping(RhizomeModel, table=False):
    """
    SQLModel for the `merchant_odessa_mapping` table.

    This model represents merchant_odessa_mapping records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    mid: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    odessa_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    created_time: datetime.datetime = Field(description="created_time")
    modified_time: datetime.datetime = Field(description="modified_time")
    stop_ach: bool = Field(description="stop_ach")
    stop_ach_date: datetime.datetime | None = Field(default=None, description="stop_ach_date")

    def sanitize(self) -> MerchantOdessaMapping:
        """Return a sanitized copy of this MerchantOdessaMapping instance."""
        return MerchantOdessaMapping(
            id=self.id,
            mid=self.mid,
            odessa_id=self.odessa_id,
            created_time=self.created_time,
            modified_time=self.modified_time,
            stop_ach=self.stop_ach,
            stop_ach_date=self.stop_ach_date,
        )
