"""
SQLModel definition for the processing_note table.

This module provides the SQLModel class for the processing_note table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class ProcessingNote(RhizomeModel, table=False):
    """
    SQLModel for the `processing_note` table.

    This model represents processing note records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    billing_entity_uuid: str = Field(max_length=26, description="Billing Entity Uuid")
    process_date: datetime.date | None = Field(default=None, description="Process Date")
    note_code: str = Field(max_length=25, description="Note Code")
    notes: str | None = Field(default=None, max_length=512, description="Notes")
    request_uuid: str | None = Field(default=None, max_length=26, description="Request Uuid")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")

    def sanitize(self) -> ProcessingNote:
        """Return a sanitized copy of this ProcessingNote instance."""
        return ProcessingNote(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            billing_entity_uuid=sanitize_uuid_field(self.billing_entity_uuid, 26),  # type: ignore
            process_date=self.process_date,
            note_code=self.note_code,
            notes=self.notes,
            request_uuid=sanitize_uuid_field(self.request_uuid, 26),
            created_timestamp=self.created_timestamp,
        )
