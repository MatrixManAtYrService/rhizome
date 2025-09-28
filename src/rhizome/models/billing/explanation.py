"""
SQLModel definition for the explanation table.

This module provides the SQLModel class for the explanation table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class Explanation(RhizomeModel, table=False):
    """
    SQLModel for the `explanation` table.

    This model represents explanation records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    request_uuid: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    merchant_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    explanation_uuid: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    created_time: datetime.datetime = Field(description="created_time")

    def sanitize(self) -> Explanation:
        """Return a sanitized copy of this Explanation instance."""
        return Explanation(
            id=self.id,
            request_uuid=sanitize_uuid_field(self.request_uuid, 13),
            merchant_id=self.merchant_id,
            explanation_uuid=sanitize_uuid_field(self.explanation_uuid, 13),
            created_time=self.created_time,
        )
