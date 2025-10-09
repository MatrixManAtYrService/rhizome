"""
SQLModel definition for the skip_fee_category_lexi_tag table.

This module provides the SQLModel class for the skip_fee_category_lexi_tag table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class SkipFeeCategoryLexiTag(RhizomeModel, table=False):
    """
    SQLModel for the `skip_fee_category_lexi_tag` table.

    This model represents skip fee category lexi tag records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    fee_category: str = Field(max_length=25, description="Fee Category")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")

    def sanitize(self) -> SkipFeeCategoryLexiTag:
        """Return a sanitized copy of this SkipFeeCategoryLexiTag instance."""
        return SkipFeeCategoryLexiTag(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            fee_category=self.fee_category,
            created_timestamp=self.created_timestamp,
        )
