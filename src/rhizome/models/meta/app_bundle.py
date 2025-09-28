"""
SQLModel definition for the app_bundle table.
"""

from __future__ import annotations

from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="AppBundle")


class AppBundle(RhizomeModel, table=False):
    """
    Base AppBundle model - defines common fields across all versions.
    """
    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=13)
    name: str = Field(max_length=127)

    def sanitize(self: T) -> T:
        """Return a sanitized copy of this AppBundle instance."""
        # This will be overridden by concrete subclasses
        raise NotImplementedError("Subclasses must implement sanitize()")
