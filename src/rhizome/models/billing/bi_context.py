"""
SQLModel definition for the bi_context table.

This module provides the SQLModel class for the bi_context table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel


class BiContext(RhizomeModel, table=False):
    """
    SQLModel for the `bi_context` table.

    This model represents bi_context records in the billing system.
    """

    id: int = Field(primary_key=True, description="id")
    context: str | None = Field(default=None, description="context")
    context_id: int = Field(description="context_id")
    billing_business_initiative_id: int = Field(description="billing_business_initiative_id")
    created_time: datetime.datetime = Field(description="created_time")

    def sanitize(self) -> BiContext:
        """Return a sanitized copy of this BiContext instance."""
        return BiContext(
            id=self.id,
            context=self.context,
            context_id=self.context_id,
            billing_business_initiative_id=self.billing_business_initiative_id,
            created_time=self.created_time,
        )
