"""
SQLModel definition for the device_type table.
"""

from __future__ import annotations

import datetime
from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="DeviceType")


class DeviceType(RhizomeModel, table=False):
    """
    Base DeviceType model - defines common fields across all versions.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=13, unique=True)
    name: str = Field(max_length=255, unique=True)
    models: str | None = Field(default=None, max_length=255)
    skus: str | None = Field(default=None, max_length=255)
    sdk_version: int | None = Field(default=None)
    prioritized_kernel_types: str | None = Field(default=None, max_length=255)
    modified_time: datetime.datetime
    deleted_time: datetime.datetime | None = Field(default=None)

    def sanitize(self: T) -> T:
        """Return a sanitized copy of this DeviceType instance."""
        # This will be overridden by concrete subclasses
        raise NotImplementedError("Subclasses must implement sanitize()")
