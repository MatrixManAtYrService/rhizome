"""
SQLModel definition for the device_events table.
"""

from __future__ import annotations

import datetime
from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="DeviceEvents")


class DeviceEvents(RhizomeModel, table=False):
    """
    Base DeviceEvents model - defines common fields across all versions.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    device_event: str | None = Field(default=None, max_length=13)
    serial_number: str | None = Field(default=None, max_length=32)
    device_type_id: int | None = Field(default=None)
    merchant_id: int | None = Field(default=None)
    account_id: int | None = Field(default=None)
    internal_account_id: int | None = Field(default=None)
    timestamp: datetime.datetime

    def sanitize(self: T) -> T:
        """Return a sanitized copy of this DeviceEvents instance."""
        # This will be overridden by concrete subclasses
        raise NotImplementedError("Subclasses must implement sanitize()")
