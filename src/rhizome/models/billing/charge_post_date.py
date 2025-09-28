"""
SQLModel definition for the charge_post_date table.

This module provides the SQLModel class for the charge_post_date table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel


class ChargePostDate(RhizomeModel, table=False):
    """
    SQLModel for the `charge_post_date` table.

    This model represents charge_post_date records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    charge_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    post_date: datetime.date | None = Field(default=None, description="post_date")
    created_time: datetime.datetime = Field(description="created_time")
    modified_time: datetime.datetime = Field(description="modified_time")

    def sanitize(self) -> ChargePostDate:
        """Return a sanitized copy of this ChargePostDate instance."""
        return ChargePostDate(
            id=self.id,
            charge_id=self.charge_id,
            post_date=self.post_date,
            created_time=self.created_time,
            modified_time=self.modified_time,
        )
