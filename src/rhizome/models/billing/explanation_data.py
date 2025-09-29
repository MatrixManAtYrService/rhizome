"""
SQLModel definition for the explanation_data table.

This module provides the SQLModel class for the explanation_data table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class ExplanationData(RhizomeModel, table=False):
    """
    SQLModel for the `explanation_data` table.

    This model represents explanation_data records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    explanation_uuid: str | None = Field(default=None, description="UUID field")
    json_class: str = Field(max_length=255, description="json_class")
    json_data: str = Field(max_length=2047, description="json_data")
    created_time: datetime.datetime = Field(description="created_time")

    def sanitize(self) -> ExplanationData:
        """Return a sanitized copy of this ExplanationData instance."""
        return ExplanationData(
            id=self.id,
            explanation_uuid=sanitize_uuid_field(self.explanation_uuid, 13),
            json_class=self.json_class,
            json_data=self.json_data,
            created_time=self.created_time,
        )
