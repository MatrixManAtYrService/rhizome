"""
SQLModel definition for the as_of_merchant table.

This module provides the SQLModel class for the as_of_merchant table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="AsOfMerchant")


class AsOfMerchant(RhizomeModel, table=False):
    """
    SQLModel for the `as_of_merchant` table.

    This model represents merchant state snapshots at specific points in time,
    tracking when merchant events occurred and associated billing events.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=26, unique=True, description="Unique identifier for the as-of-merchant record")
    merchant_uuid: str = Field(max_length=13, description="UUID of the merchant")
    as_of_timestamp: datetime.datetime = Field(description="Timestamp for this snapshot")
    event_datetime: datetime.datetime | None = Field(default=None, description="Datetime when the event occurred")
    billing_event_uuid: str | None = Field(default=None, max_length=26, description="UUID of the associated billing event")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")

    def sanitize(self: T) -> T:
        """Return a sanitized copy of this AsOfMerchant instance."""
        # This will be overridden by concrete subclasses
        raise NotImplementedError("Subclasses must implement sanitize()")