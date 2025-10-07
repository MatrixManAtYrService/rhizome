"""
SQLModel definition for the plan_meta table.

This module provides the SQLModel class for the plan_meta table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class PlanMeta(RhizomeModel, table=False):
    """
    SQLModel for the `plan_meta` table.

    This model represents plan_meta records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str | None = Field(default=None, description="UUID field")
    ref_type: str | None = Field(default=None, description="ref_type")
    ref_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    plan_type: str | None = Field(default=None, description="plan_type")
    plan_uuid: str | None = Field(default=None, max_length=13, description="plan_uuid")
    prop_name: str = Field(max_length=255, description="prop_name")
    prop_value: str | None = Field(default=None, max_length=2048, description="prop_value")

    def sanitize(self) -> PlanMeta:
        """Return a sanitized copy of this PlanMeta instance."""
        return PlanMeta(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),
            ref_type=self.ref_type,
            ref_id=self.ref_id,
            plan_type=self.plan_type,
            plan_uuid=sanitize_uuid_field(self.plan_uuid, 13),
            prop_name=self.prop_name,
            prop_value=self.prop_value,
        )
