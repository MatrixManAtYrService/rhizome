"""
SQLModel definition for the locale table.
"""

from __future__ import annotations

from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="Locale")


class Locale(RhizomeModel, table=True):
    """
    SQLModel for the `locale` table.
    """

    id: int | None = Field(default=None, primary_key=True)
    language: str = Field(max_length=2)
    country: str | None = Field(default=None, max_length=2)

    def sanitize(self: T) -> T:
        """Return a sanitized copy of this Locale instance."""
        # This will be overridden by concrete subclasses
        raise NotImplementedError("Subclasses must implement sanitize()")
