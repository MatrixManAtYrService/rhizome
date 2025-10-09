"""
SQLModel definition for the billing_hierarchy table.

This module provides the SQLModel class for the billing_hierarchy table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class BillingHierarchy(RhizomeModel, table=False):
    """
    SQLModel for the `billing_hierarchy` table.

    This model represents billing hierarchy records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    hierarchy_type: str = Field(max_length=20, description="Hierarchy Type")
    billing_entity_uuid: str = Field(max_length=26, description="Billing Entity Uuid")
    effective_date: datetime.date = Field(description="Effective Date")
    deleted_date: datetime.date | None = Field(default=None, description="Deleted Date")
    parent_billing_hierarchy_uuid: str | None = Field(default=None, max_length=26, description="Parent Billing Hierarchy Uuid")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")

    def sanitize(self) -> BillingHierarchy:
        """Return a sanitized copy of this BillingHierarchy instance."""
        return BillingHierarchy(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            hierarchy_type=self.hierarchy_type,
            billing_entity_uuid=sanitize_uuid_field(self.billing_entity_uuid, 26),  # type: ignore
            effective_date=self.effective_date,
            deleted_date=self.deleted_date,
            parent_billing_hierarchy_uuid=sanitize_uuid_field(self.parent_billing_hierarchy_uuid, 26),
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
        )
