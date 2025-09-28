"""
SQLModel definition for the processor_key table.
"""

from __future__ import annotations

from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="ProcessorKey")


class ProcessorKey(RhizomeModel, table=False):
    """
    Base ProcessorKey model - defines common fields across all versions.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=13, unique=True)
    info: str | None = Field(default=None)

    def sanitize(self: T) -> T:
        """Return a sanitized copy of this ProcessorKey instance."""
        # This will be overridden by concrete subclasses
        raise NotImplementedError("Subclasses must implement sanitize()")
