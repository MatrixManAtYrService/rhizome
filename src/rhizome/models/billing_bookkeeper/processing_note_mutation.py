"""
SQLModel definition for the processing_note_mutation table.

This module provides the SQLModel class for the processing_note_mutation table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class ProcessingNoteMutation(RhizomeModel, table=False):
    """
    SQLModel for the `processing_note_mutation` table.

    This model represents processing note mutation records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    mutation_action: str = Field(description="Mutation Action")
    mutation_timestamp: datetime.datetime = Field(description="Mutation Timestamp")
    processing_note_id: int = Field(description="Processing Note Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    billing_entity_uuid: str | None = Field(default=None, max_length=26, description="Billing Entity Uuid")
    process_date: datetime.date | None = Field(default=None, description="Process Date")
    note_code: str | None = Field(default=None, max_length=25, description="Note Code")
    notes: str | None = Field(default=None, max_length=512, description="Notes")
    request_uuid: str | None = Field(default=None, max_length=26, description="Request Uuid")
    created_timestamp: datetime.datetime | None = Field(default=None, description="Created Timestamp")

    def sanitize(self) -> ProcessingNoteMutation:
        """Return a sanitized copy of this ProcessingNoteMutation instance."""
        return ProcessingNoteMutation(
            id=self.id,
            mutation_action=self.mutation_action,
            mutation_timestamp=self.mutation_timestamp,
            processing_note_id=self.processing_note_id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            billing_entity_uuid=sanitize_uuid_field(self.billing_entity_uuid, 26),
            process_date=self.process_date,
            note_code=self.note_code,
            notes=self.notes,
            request_uuid=sanitize_uuid_field(self.request_uuid, 26),
            created_timestamp=self.created_timestamp,
        )
