"""
SQLModel definition for the offboarding table.

This module provides the SQLModel class for the offboarding table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class Offboarding(RhizomeModel, table=False):
    """
    SQLModel for the `offboarding` table.

    This model represents offboarding records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    request_uuid: str | None = Field(default=None, description="UUID field")
    merchant_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    step: str | None = Field(default=None, description="step")
    dry_run: bool | None = Field(default=None, description="dry_run")
    due_time: datetime.datetime | None = Field(default=None, description="due_time")
    created_time: datetime.datetime = Field(description="created_time")
    deleted_time: datetime.datetime | None = Field(default=None, description="deleted_time")

    def sanitize(self) -> Offboarding:
        """Return a sanitized copy of this Offboarding instance."""
        return Offboarding(
            id=self.id,
            request_uuid=sanitize_uuid_field(self.request_uuid, 13),
            merchant_id=self.merchant_id,
            step=self.step,
            dry_run=self.dry_run,
            due_time=self.due_time,
            created_time=self.created_time,
            deleted_time=self.deleted_time,
        )
