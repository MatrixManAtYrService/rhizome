"""
SQLModel definition for the stage_email table.

This module provides the SQLModel class for the stage_email table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlalchemy import Column, String
from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class StageEmail(RhizomeModel, table=False):
    """
    SQLModel for the `stage_email` table.

    This model represents stage_email records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    request_uuid: str | None = Field(default=None, description="UUID field")
    reference_type: str | None = Field(default=None, description="reference_type")
    reference_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    type: str | None = Field(default=None, description="type")
    to_email: str = Field(sa_column=Column("to", String(127)), description="Email to address")
    from_email: str | None = Field(
        default=None, sa_column=Column("from", String(127)), description="Email from address"
    )
    from_name: str | None = Field(default=None, max_length=127, description="from_name")
    replyTo: str | None = Field(default=None, max_length=127, description="replyTo")
    bcc: str | None = Field(default=None, max_length=127, description="bcc")
    subject: str = Field(max_length=511, description="subject")
    body: str | None = Field(default=None, max_length=8191, description="body")
    created_time: datetime.datetime = Field(description="created_time")
    sent_time: datetime.datetime | None = Field(default=None, description="sent_time")

    def sanitize(self) -> StageEmail:
        """Return a sanitized copy of this StageEmail instance."""
        return StageEmail(
            id=self.id,
            request_uuid=sanitize_uuid_field(self.request_uuid, 13),
            reference_type=self.reference_type,
            reference_id=self.reference_id,
            type=self.type,
            to_email=self.to_email,
            from_email=self.from_email,
            from_name=self.from_name,
            replyTo=self.replyTo,
            bcc=self.bcc,
            subject=self.subject,
            body=self.body,
            created_time=self.created_time,
            sent_time=self.sent_time,
        )
