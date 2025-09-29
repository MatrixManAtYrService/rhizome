"""
SQLModel definition for the biie_file_def table.

This module provides the SQLModel class for the biie_file_def table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class BiieFileDef(RhizomeModel, table=False):
    """
    SQLModel for the `biie_file_def` table.

    This model represents biie_file_def records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str | None = Field(default=None, description="UUID field")
    file_type: str = Field(max_length=50, description="file_type")
    file_format: str | None = Field(default=None, description="file_format")
    num_headers: int = Field(description="num_headers")
    num_footers: int = Field(description="num_footers")
    key1_field: int = Field(description="key1_field")
    key2_field: int = Field(description="key2_field")
    error_threshold_method: str | None = Field(default=None, description="error_threshold_method")
    error_threshold: int = Field(description="error_threshold")
    created_time: datetime.datetime = Field(description="created_time")
    modified_time: datetime.datetime = Field(description="modified_time")

    def sanitize(self) -> BiieFileDef:
        """Return a sanitized copy of this BiieFileDef instance."""
        return BiieFileDef(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),
            file_type=self.file_type,
            file_format=self.file_format,
            num_headers=self.num_headers,
            num_footers=self.num_footers,
            key1_field=self.key1_field,
            key2_field=self.key2_field,
            error_threshold_method=self.error_threshold_method,
            error_threshold=self.error_threshold,
            created_time=self.created_time,
            modified_time=self.modified_time,
        )
