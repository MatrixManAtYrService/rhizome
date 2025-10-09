"""
SQLModel definition for the billing_hierarchy_type table.

This module provides the SQLModel class for the billing_hierarchy_type table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class BillingHierarchyType(RhizomeModel, table=False):
    """
    SQLModel for the `billing_hierarchy_type` table.

    This model represents billing hierarchy type records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    hierarchy_type: str = Field(max_length=20, description="Hierarchy Type")
    description: str | None = Field(default=None, max_length=255, description="Description")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")

    def sanitize(self) -> BillingHierarchyType:
        """Return a sanitized copy of this BillingHierarchyType instance."""
        return BillingHierarchyType(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            hierarchy_type=self.hierarchy_type,
            description=self.description,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
        )
