"""
SQLModel definition for the app_metered_country table.
"""

from __future__ import annotations

import datetime
from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="AppMeteredCountry")


class AppMeteredCountry(RhizomeModel, table=True):
    """
    SQLModel for the `app_metered_country` table.
    """

    id: int | None = Field(default=None, primary_key=True)
    uuid: str = Field(max_length=13, unique=True)
    amount: int
    country: str = Field(max_length=2)
    action: str = Field(max_length=40)
    app_metered_id: int = Field(foreign_key="app_metered.id")
    active: bool
    created_time: datetime.datetime | None = Field(default=None)
    modified_time: datetime.datetime
    deleted_time: datetime.datetime | None = Field(default=None)

    def sanitize(self: T) -> T:
        """Return a sanitized copy of this AppMeteredCountry instance."""
        # This will be overridden by concrete subclasses
        raise NotImplementedError("Subclasses must implement sanitize()")
