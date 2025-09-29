"""
SQLModel definition for the email_audit table.

This module provides the SQLModel class for the email_audit table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class EmailAudit(RhizomeModel, table=False):
    """
    SQLModel for the `email_audit` table.

    This model represents email_audit records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str | None = Field(default=None, description="UUID field")
    email_type: str = Field(max_length=127, description="email_type")
    recipient_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    email_status: str = Field(max_length=127, description="email_status")
    track_id: str | None = Field(default=None, description="UUID field")
    done_time: datetime.datetime | None = Field(default=None, description="done_time")
    created_time: datetime.datetime | None = Field(default=None, description="created_time")
    modified_time: datetime.datetime = Field(description="modified_time")

    def sanitize(self) -> EmailAudit:
        """Return a sanitized copy of this EmailAudit instance."""
        return EmailAudit(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),
            email_type=self.email_type,
            recipient_id=self.recipient_id,
            email_status=self.email_status,
            track_id=self.track_id,
            done_time=self.done_time,
            created_time=self.created_time,
            modified_time=self.modified_time,
        )
