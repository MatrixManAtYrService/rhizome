"""
SQLModel definition for the look table.

This module provides the SQLModel class for the look table from the
billing-bookkeeper database, along with sanitization functions.
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

    This model represents look records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=32, unique=True, description="Uuid")
    hash: str = Field(max_length=64, description="Hash")
    namespace: str = Field(max_length=32, description="Namespace")
    meta_data: str | None = Field(default=None, sa_column=Column("metadata", String(1024)), description="Metadata")
    processed_timestamp: datetime.datetime | None = Field(default=None, description="Processed Timestamp")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")

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
