"""
SQLModel definition for the merchant_queue_sensitive table.

This module provides the SQLModel class for the merchant_queue_sensitive table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel


class MerchantQueueSensitive(RhizomeModel, table=False):
    """
    SQLModel for the `merchant_queue_sensitive` table.

    This model represents merchant_queue_sensitive records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    mid: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    name: str | None = Field(default=None, description="name")
    value: str | None = Field(default=None, max_length=255, description="value")
    value_guid: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    created_time: datetime.datetime = Field(description="created_time")

    def sanitize(self) -> MerchantQueueSensitive:
        """Return a sanitized copy of this MerchantQueueSensitive instance."""
        return MerchantQueueSensitive(
            id=self.id,
            mid=self.mid,
            name=self.name,
            value=self.value,
            value_guid=self.value_guid,
            created_time=self.created_time,
        )
