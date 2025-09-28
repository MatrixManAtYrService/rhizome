"""
SQLModel definition for the app_subscription table.
"""

from __future__ import annotations

import datetime
from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="AppSubscription")


class AppSubscription(RhizomeModel, table=False):
    """
    Base AppSubscription model - defines common fields across all versions.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=13, unique=True)
    developer_app_id: int = Field(foreign_key="developer_app.id")
    label: str = Field(max_length=20)
    plan: bool | None = Field(default=False)
    created_time: datetime.datetime | None = Field(default=None)
    modified_time: datetime.datetime
    deleted_time: datetime.datetime | None = Field(default=None)

    def sanitize(self: T) -> T:
        """Return a sanitized copy of this AppSubscription instance."""
        # This will be overridden by concrete subclasses
        raise NotImplementedError("Subclasses must implement sanitize()")
