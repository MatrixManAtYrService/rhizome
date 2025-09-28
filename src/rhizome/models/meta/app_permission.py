"""
SQLModel definition for the app_permission table.
"""

from __future__ import annotations

import datetime
from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="AppPermission")


class AppPermission(RhizomeModel, table=True):
    """
    SQLModel for the `app_permission` table.
    """

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=100, unique=True)
    created_time: datetime.datetime | None = Field(default=None)
    modified_time: datetime.datetime

    def sanitize(self: T) -> T:
        """Return a sanitized copy of this AppPermission instance."""
        # This will be overridden by concrete subclasses
        raise NotImplementedError("Subclasses must implement sanitize()")
