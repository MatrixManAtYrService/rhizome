"""
SQLModel definition for the server_feature table.
"""

from __future__ import annotations

import datetime
from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="ServerFeature")


class ServerFeature(RhizomeModel, table=False):
    """
    Base ServerFeature model - defines common fields across all versions.
    """

    id: int | None = Field(default=None, primary_key=True)
    uuid: str = Field(max_length=13, unique=True)
    name: str = Field(max_length=127, unique=True)
    config: str | None = Field(default=None)
    enabled: bool
    modified_time: datetime.datetime
    deleted_time: datetime.datetime | None = Field(default=None)

    def sanitize(self: T) -> T:
        """Return a sanitized copy of this ServerFeature instance."""
        # This will be overridden by concrete subclasses
        raise NotImplementedError("Subclasses must implement sanitize()")
