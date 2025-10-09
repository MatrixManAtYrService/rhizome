"""
SQLModel definition for the adjust_action_type table.

This module provides the SQLModel class for the adjust_action_type table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class AdjustActionType(RhizomeModel, table=False):
    """
    SQLModel for the `adjust_action_type` table.

    This model represents adjust action type records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    adjust_action_type: str = Field(max_length=25, description="Adjust Action Type")
    fee_category_group: str = Field(max_length=25, description="Fee Category Group")
    revenue_group: str | None = Field(default=None, max_length=25, description="Revenue Group")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")

    def sanitize(self) -> AdjustActionType:
        """Return a sanitized copy of this AdjustActionType instance."""
        return AdjustActionType(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            adjust_action_type=self.adjust_action_type,
            fee_category_group=self.fee_category_group,
            revenue_group=self.revenue_group,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
        )
