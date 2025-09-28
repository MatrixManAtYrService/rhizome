"""
SQLModel definition for the plan_meta_history table.

This module provides the SQLModel class for the plan_meta_history table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class PlanMetaHistory(RhizomeModel, table=False):
    """
    SQLModel for the `plan_meta_history` table.

    This model represents plan_meta_history records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    created_time: datetime.datetime = Field(description="created_time")
    action: str | None = Field(default=None, description="action")
    plan_meta_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    ref_type: str | None = Field(default=None, description="ref_type")
    ref_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    plan_type: str | None = Field(default=None, description="plan_type")
    plan_uuid: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    prop_name: str = Field(max_length=255, description="prop_name")
    prop_value: str | None = Field(default=None, max_length=2048, description="prop_value")

    def sanitize(self) -> PlanMetaHistory:
        """Return a sanitized copy of this PlanMetaHistory instance."""
        return PlanMetaHistory(
            id=self.id,
            created_time=self.created_time,
            action=self.action,
            plan_meta_id=self.plan_meta_id,
            ref_type=self.ref_type,
            ref_id=self.ref_id,
            plan_type=self.plan_type,
            plan_uuid=sanitize_uuid_field(self.plan_uuid, 13),
            prop_name=self.prop_name,
            prop_value=self.prop_value,
        )
