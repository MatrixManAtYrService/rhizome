"""
SQLModel definition for the jobrunr_metadata table.

This module provides the SQLModel class for the jobrunr_metadata table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel


class JobrunrMetadata(RhizomeModel, table=False):
    """
    SQLModel for the `jobrunr_metadata` table.

    This model represents jobrunr metadata records in the billing system.
    """

    id: str = Field(primary_key=True, max_length=156, description="Id")
    name: str = Field(max_length=92, description="Name")
    owner: str = Field(max_length=64, description="Owner")
    value: str = Field(description="Value")
    createdAt: datetime.datetime = Field(description="Createdat")
    updatedAt: datetime.datetime = Field(description="Updatedat")

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
