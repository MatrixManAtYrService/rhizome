"""
SQLModel definition for the fee_category table.

This module provides the SQLModel class for the fee_category table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class FeeCategory(RhizomeModel, table=False):
    """
    SQLModel for the `fee_category` table.

    This model represents fee category records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    fee_category: str = Field(max_length=25, description="Fee Category")
    sort_order: int = Field(description="Sort Order")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")

    def sanitize(self) -> FeeCategory:
        """Return a sanitized copy of this FeeCategory instance."""
        return FeeCategory(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            fee_category=self.fee_category,
            sort_order=self.sort_order,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
        )
