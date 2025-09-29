"""
SQLModel definition for the promo table.

This module provides the SQLModel class for the promo table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class Promo(RhizomeModel, table=False):
    """
    SQLModel for the `promo` table.

    This model represents promo records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str | None = Field(default=None, description="UUID field")
    code: str = Field(max_length=32, description="code")
    description: str | None = Field(default=None, max_length=511, description="description")
    plan_trial_days: int | None = Field(default=None, description="plan_trial_days")
    plan_type: str | None = Field(default=None, description="plan_type")
    app_trial_days: str | None = Field(default=None, description="app_trial_days")
    developer_app_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    activation_time: datetime.datetime | None = Field(default=None, description="activation_time")
    deactivation_time: datetime.datetime | None = Field(default=None, description="deactivation_time")
    created_time: datetime.datetime = Field(description="created_time")
    modified_time: datetime.datetime = Field(description="modified_time")

    def sanitize(self) -> Promo:
        """Return a sanitized copy of this Promo instance."""
        return Promo(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),
            code=self.code,
            description=self.description,
            plan_trial_days=self.plan_trial_days,
            plan_type=self.plan_type,
            app_trial_days=self.app_trial_days,
            developer_app_id=self.developer_app_id,
            activation_time=self.activation_time,
            deactivation_time=self.deactivation_time,
            created_time=self.created_time,
            modified_time=self.modified_time,
        )
