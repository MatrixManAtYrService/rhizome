"""
SQLModel definition for the biie_file_instance table.

This module provides the SQLModel class for the biie_file_instance table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class BiieFileInstance(RhizomeModel, table=False):
    """
    SQLModel for the `biie_file_instance` table.

    This model represents biie_file_instance records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str | None = Field(default=None, description="UUID field")
    biie_file_def_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    file_name: str = Field(max_length=512, description="file_name")
    file_size: int = Field(description="file_size")
    net_file_size: int = Field(description="net_file_size")
    num_records: int = Field(description="num_records")
    net_num_records: int = Field(description="net_num_records")
    dry_run: bool | None = Field(default=None, description="dry_run")
    file_status: str | None = Field(default=None, description="file_status")
    created_time: datetime.datetime = Field(description="created_time")
    modified_time: datetime.datetime = Field(description="modified_time")

    def sanitize(self) -> BiieFileInstance:
        """Return a sanitized copy of this BiieFileInstance instance."""
        return BiieFileInstance(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),
            biie_file_def_id=self.biie_file_def_id,
            file_name=self.file_name,
            file_size=self.file_size,
            net_file_size=self.net_file_size,
            num_records=self.num_records,
            net_num_records=self.net_num_records,
            dry_run=self.dry_run,
            file_status=self.file_status,
            created_time=self.created_time,
            modified_time=self.modified_time,
        )
