"""
SQLModel definition for the revenue_share_group table.

This module provides the SQLModel class for the revenue_share_group table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class RevenueShareGroup(RhizomeModel, table=False):
    """
    SQLModel for the `revenue_share_group` table.

    This model represents revenue share group records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    revenue_share_group: str = Field(max_length=20, description="Revenue Share Group")
    short_desc: str | None = Field(default=None, max_length=40, description="Short Desc")
    description: str | None = Field(default=None, max_length=255, description="Description")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")

    def sanitize(self) -> RevenueShareGroup:
        """Return a sanitized copy of this RevenueShareGroup instance."""
        return RevenueShareGroup(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            revenue_share_group=self.revenue_share_group,
            short_desc=self.short_desc,
            description=self.description,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
        )
