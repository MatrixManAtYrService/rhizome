"""
SQLModel definition for the biie_file_instance_request table.

This module provides the SQLModel class for the biie_file_instance_request table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class BiieFileInstanceRequest(RhizomeModel, table=False):
    """
    SQLModel for the `biie_file_instance_request` table.

    This model represents biie_file_instance_request records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    biie_file_instance_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    request_uuid: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    process_name: str = Field(max_length=127, description="process_name")
    num_attempted: int = Field(description="num_attempted")
    num_success: int = Field(description="num_success")
    num_errors: int = Field(description="num_errors")
    num_warnings: int = Field(description="num_warnings")
    num_skipped: int = Field(description="num_skipped")
    reason_code: str | None = Field(default=None, description="reason_code")
    reason_detail: str | None = Field(default=None, max_length=2000, description="reason_detail")
    created_time: datetime.datetime = Field(description="created_time")
    modified_time: datetime.datetime = Field(description="modified_time")

    def sanitize(self) -> BiieFileInstanceRequest:
        """Return a sanitized copy of this BiieFileInstanceRequest instance."""
        return BiieFileInstanceRequest(
            id=self.id,
            biie_file_instance_id=self.biie_file_instance_id,
            request_uuid=sanitize_uuid_field(self.request_uuid, 13),
            process_name=self.process_name,
            num_attempted=self.num_attempted,
            num_success=self.num_success,
            num_errors=self.num_errors,
            num_warnings=self.num_warnings,
            num_skipped=self.num_skipped,
            reason_code=self.reason_code,
            reason_detail=self.reason_detail,
            created_time=self.created_time,
            modified_time=self.modified_time,
        )
