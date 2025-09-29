"""
SQLModel definition for the stage_vendor_disbursement_error table.

This module provides the SQLModel class for the stage_vendor_disbursement_error table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class StageVendorDisbursementError(RhizomeModel, table=False):
    """
    SQLModel for the `stage_vendor_disbursement_error` table.

    This model represents stage_vendor_disbursement_error records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    charge_uuid: str | None = Field(default=None, description="UUID field")
    vendor_code: str = Field(max_length=30, description="vendor_code")
    file_instance_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    request_uuid: str | None = Field(default=None, description="UUID field")
    state: str | None = Field(default=None, description="state")
    created_time: datetime.datetime = Field(description="created_time")
    promoted_time: datetime.datetime | None = Field(default=None, description="promoted_time")
    promoted_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")

    def sanitize(self) -> StageVendorDisbursementError:
        """Return a sanitized copy of this StageVendorDisbursementError instance."""
        return StageVendorDisbursementError(
            id=self.id,
            charge_uuid=sanitize_uuid_field(self.charge_uuid, 13),
            vendor_code=self.vendor_code,
            file_instance_id=self.file_instance_id,
            request_uuid=sanitize_uuid_field(self.request_uuid, 13),
            state=self.state,
            created_time=self.created_time,
            promoted_time=self.promoted_time,
            promoted_id=self.promoted_id,
        )
