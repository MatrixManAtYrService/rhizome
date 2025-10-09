"""
SQLModel definition for the fee_code table.

This module provides the SQLModel class for the fee_code table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class FeeCode(RhizomeModel, table=False):
    """
    SQLModel for the `fee_code` table.

    This model represents fee code records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    fee_category: str = Field(max_length=25, description="Fee Category")
    fee_code: str = Field(max_length=25, description="Fee Code")
    short_desc: str = Field(max_length=40, description="Short Desc")
    full_desc: str | None = Field(default=None, max_length=255, description="Full Desc")
    sort_order: int = Field(description="Sort Order")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")

    def sanitize(self) -> FeeCode:
        """Return a sanitized copy of this FeeCode instance."""
        return FeeCode(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            fee_category=self.fee_category,
            fee_code=self.fee_code,
            short_desc=self.short_desc,
            full_desc=self.full_desc,
            sort_order=self.sort_order,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
        )
