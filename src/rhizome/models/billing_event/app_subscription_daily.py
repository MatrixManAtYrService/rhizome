"""
SQLModel definition for the app_subscription_daily table.

This module provides the SQLModel class for the app_subscription_daily table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class AppSubscriptionDaily(RhizomeModel, table=False):
    """
    SQLModel for the `app_subscription_daily` table.

    This model represents daily app subscription records in the billing system,
    tracking subscription states and events by date.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=26, unique=True, description="Unique identifier for the app subscription daily record")
    merchant_uuid: str = Field(max_length=13, description="UUID of the merchant")
    developer_app_uuid: str = Field(max_length=13, description="UUID of the developer application")
    environment: str = Field(max_length=25, description="Environment (e.g., usprod)")
    event_date: datetime.date = Field(description="Date for this daily record")
    starting_app_subscription_uuid: str | None = Field(default=None, max_length=13, description="UUID of subscription at start of day")
    ending_app_subscription_uuid: str | None = Field(default=None, max_length=13, description="UUID of subscription at end of day")
    highest_app_subscription_uuid: str = Field(max_length=13, description="UUID of highest subscription during the day")
    billing_event_uuid: str | None = Field(default=None, max_length=26, description="UUID of the billing event")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")

    def sanitize(self) -> AppSubscriptionDaily:
        """Return a sanitized copy of this AppSubscriptionDaily instance."""
        return AppSubscriptionDaily(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            merchant_uuid=sanitize_uuid_field(self.merchant_uuid, 13),  # type: ignore
            developer_app_uuid=sanitize_uuid_field(self.developer_app_uuid, 13),  # type: ignore
            environment=self.environment,
            event_date=self.event_date,
            starting_app_subscription_uuid=sanitize_uuid_field(self.starting_app_subscription_uuid, 13),
            ending_app_subscription_uuid=sanitize_uuid_field(self.ending_app_subscription_uuid, 13),
            highest_app_subscription_uuid=sanitize_uuid_field(self.highest_app_subscription_uuid, 13),  # type: ignore
            billing_event_uuid=sanitize_uuid_field(self.billing_event_uuid, 26),
            created_timestamp=self.created_timestamp,
        )