"""
SQLModel definition for the charge_capture_error table.

This module provides the SQLModel class for the charge_capture_error table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class ChargeCaptureError(RhizomeModel, table=False):
    """
    SQLModel for the `charge_capture_error` table.

    This model represents charge_capture_error records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    charge_uuid: str | None = Field(default=None, description="UUID field")
    mid: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    file_instance_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    request_uuid: str | None = Field(default=None, description="UUID field")
    created_time: datetime.datetime = Field(description="created_time")

    def sanitize(self) -> ChargeCaptureError:
        """Return a sanitized copy of this ChargeCaptureError instance."""
        return ChargeCaptureError(
            id=self.id,
            charge_uuid=sanitize_uuid_field(self.charge_uuid, 13),
            mid=self.mid,
            file_instance_id=self.file_instance_id,
            request_uuid=sanitize_uuid_field(self.request_uuid, 13),
            created_time=self.created_time,
        )
