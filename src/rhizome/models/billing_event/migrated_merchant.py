"""
SQLModel definition for the migrated_merchant table.

This module provides the SQLModel class for the migrated_merchant table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class MigratedMerchant(RhizomeModel, table=False):
    """
    SQLModel for the `migrated_merchant` table.

    This model represents merchants that have been migrated in the billing system,
    containing migration status and progress information.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    reseller_uuid: str = Field(max_length=13, description="UUID of the reseller")
    merchant_uuid: str = Field(max_length=13, description="UUID of the merchant")
    backbook_merchant: bool = Field(description="Flag indicating if this is a backbook merchant")
    added_to_ebb_group: bool = Field(description="Flag indicating if merchant was added to EBB group")
    plan_trials_migrated: bool = Field(description="Flag indicating if plan trials were migrated")
    apps_migrated: bool = Field(description="Flag indicating if apps were migrated")
    app_sub_events_caught_up: bool = Field(description="Flag indicating if app subscription events are caught up")
    app_meter_events_caught_up: bool = Field(description="Flag indicating if app meter events are caught up")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")
    modified_timestamp: datetime.datetime = Field(description="Timestamp when the record was last modified")

    def sanitize(self) -> MigratedMerchant:
        """Return a sanitized copy of this MigratedMerchant instance."""
        return MigratedMerchant(
            id=self.id,
            reseller_uuid=sanitize_uuid_field(self.reseller_uuid, 13),  # type: ignore
            merchant_uuid=sanitize_uuid_field(self.merchant_uuid, 13),  # type: ignore
            backbook_merchant=self.backbook_merchant,
            added_to_ebb_group=self.added_to_ebb_group,
            plan_trials_migrated=self.plan_trials_migrated,
            apps_migrated=self.apps_migrated,
            app_sub_events_caught_up=self.app_sub_events_caught_up,
            app_meter_events_caught_up=self.app_meter_events_caught_up,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
        )