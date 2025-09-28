"""
SQLModel definition for the app_metered_event table.
"""

from __future__ import annotations

import datetime
from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="AppMeteredEvent")


class AppMeteredEvent(RhizomeModel, table=False):
    """
    Base AppMeteredEvent model - defines common fields across all versions.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=13, unique=True)
    merchant_app_id: int = Field(foreign_key="merchant_app.id")
    app_metered_id: int = Field(foreign_key="app_metered.id")
    count: int
    charge_id: int | None = Field(default=None, foreign_key="charge.id")
    created_time: datetime.datetime | None = Field(default=None)
    modified_time: datetime.datetime

    def sanitize(self: T) -> T:
        """Return a sanitized copy of this AppMeteredEvent instance."""
        # This will be overridden by concrete subclasses
        raise NotImplementedError("Subclasses must implement sanitize()")
