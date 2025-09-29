"""
SQLModel definition for the export_tracker table.

This module provides the SQLModel class for the export_tracker table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class ExportTracker(RhizomeModel, table=False):
    """
    SQLModel for the `export_tracker` table.

    This model represents export_tracker records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    exported_uuid: str | None = Field(default=None, description="UUID field")
    export_type: str | None = Field(default=None, description="export_type")
    system_type: str | None = Field(default=None, description="system_type")
    exported_data: str | None = Field(default=None, description="exported_data")
    created_time: datetime.datetime = Field(description="created_time")
    modified_time: datetime.datetime = Field(description="modified_time")

    def sanitize(self) -> ExportTracker:
        """Return a sanitized copy of this ExportTracker instance."""
        return ExportTracker(
            id=self.id,
            exported_uuid=sanitize_uuid_field(self.exported_uuid, 13),
            export_type=self.export_type,
            system_type=self.system_type,
            exported_data=self.exported_data,
            created_time=self.created_time,
            modified_time=self.modified_time,
        )
