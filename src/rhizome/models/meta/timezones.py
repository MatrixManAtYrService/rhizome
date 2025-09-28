"""
SQLModel definition for the timezones table.
"""

from __future__ import annotations

from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="Timezones")


class Timezones(RhizomeModel, table=True):
    """
    SQLModel for the `timezones` table.
    """

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=255, unique=True)
    display_name: str | None = Field(default=None, max_length=255)
    visible: bool | None = Field(default=False)
    offset: int | None = Field(default=None)
    offset_dst: int | None = Field(default=None)

    def sanitize(self) -> Timezones:
        """Return a sanitized copy of this Timezones instance."""
        return Timezones(
            id=self.id,
            name=self.name,
            display_name=self.display_name,
            visible=self.visible,
            offset=self.offset,
            offset_dst=self.offset_dst,
        )
