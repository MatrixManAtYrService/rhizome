"""
SQLModel definition for the jobrunr_metadata table.

This module provides the SQLModel class for the jobrunr_metadata table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel


class JobrunrMetadata(RhizomeModel, table=False):
    """
    SQLModel for the `jobrunr_metadata` table.

    This model represents metadata entries in the JobRunr system,
    containing key-value pairs for system configuration and state.
    """

    id: str | None = Field(default=None, primary_key=True, max_length=156, description="Primary key, unique identifier for the metadata entry")
    name: str = Field(max_length=92, description="Name of the metadata entry")
    owner: str = Field(max_length=64, description="Owner of the metadata entry")
    value: str = Field(description="Value of the metadata entry")
    createdAt: datetime.datetime = Field(description="Timestamp when the metadata was created")
    updatedAt: datetime.datetime = Field(description="Timestamp when the metadata was last updated")

    def sanitize(self) -> JobrunrMetadata:
        """Return a sanitized copy of this JobrunrMetadata instance."""
        return JobrunrMetadata(
            id=self.id,
            name=self.name,
            owner=self.owner,
            value=self.value,
            createdAt=self.createdAt,
            updatedAt=self.updatedAt,
        )