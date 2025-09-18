"""
SQLModel definition for the look table.

This module provides the SQLModel class for the look table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlalchemy import Column, String
from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class Look(RhizomeModel, table=False):
    """
    SQLModel for the `look` table.

    This model represents lookup entries in the billing system,
    containing hash-based references with namespace organization.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing unsigned integer")
    uuid: str = Field(max_length=32, description="UUID identifier for the look entry")
    hash: str = Field(max_length=64, description="Hash value for content identification")
    namespace: str = Field(max_length=32, description="Namespace for organizing look entries")
    meta_data: str | None = Field(default=None, sa_column=Column("metadata", String(1024)), description="Optional metadata as JSON or string")
    processed_timestamp: datetime.datetime | None = Field(default=None, description="Timestamp when the entry was processed")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")

    def sanitize(self) -> Look:
        """Return a sanitized copy of this Look instance."""
        return Look(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 32),  # type: ignore
            hash=self.hash,
            namespace=self.namespace,
            meta_data=self.meta_data,
            processed_timestamp=self.processed_timestamp,
            created_timestamp=self.created_timestamp,
        )