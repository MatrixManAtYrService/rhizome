"""
SQLModel definition for the corollary_data table.

This module provides the SQLModel class for the corollary_data table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class CorollaryData(RhizomeModel, table=False):
    """
    SQLModel for the `corollary_data` table.

    This model represents corollary_data records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    request_uuid: str | None = Field(default=None, description="UUID field")
    calling_class: str = Field(max_length=127, description="calling_class")
    path: str = Field(max_length=511, description="path")
    output: str | None = Field(default=None, max_length=4095, description="output")
    created_time: datetime.datetime = Field(description="created_time")

    def sanitize(self) -> CorollaryData:
        """Return a sanitized copy of this CorollaryData instance."""
        return CorollaryData(
            id=self.id,
            request_uuid=sanitize_uuid_field(self.request_uuid, 13),
            calling_class=self.calling_class,
            path=self.path,
            output=self.output,
            created_time=self.created_time,
        )
