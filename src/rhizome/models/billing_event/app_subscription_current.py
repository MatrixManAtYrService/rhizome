"""
SQLModel definition for the app_subscription_current table.

This module provides the SQLModel class for the app_subscription_current table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from decimal import Decimal

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class AppSubscriptionCurrent(RhizomeModel, table=False):
    """
    SQLModel for the `app_subscription_current` table.

    This model represents current app subscriptions in the billing system,
    tracking active subscriptions and their details.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=26, unique=True, description="Unique identifier for the app subscription current record")
    merchant_uuid: str = Field(max_length=13, description="UUID of the merchant")
    developer_app_uuid: str = Field(max_length=13, description="UUID of the developer application")
    environment: str = Field(max_length=25, description="Environment (e.g., usprod)")
    app_subscription_uuid: str = Field(max_length=13, description="UUID of the app subscription")
    app_subscription_cost: Decimal = Field(max_digits=12, decimal_places=3, description="Cost of the app subscription")
    bundled_with_plan: bool = Field(default=False, description="Whether bundled with a plan")
    trial_end_date: datetime.date | None = Field(default=None, description="End date of trial period")
    last_advance_date: datetime.date | None = Field(default=None, description="Last advance date")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")
    modified_timestamp: datetime.datetime = Field(description="Timestamp when the record was last modified")

    def sanitize(self) -> AppSubscriptionCurrent:
        """Return a sanitized copy of this AppSubscriptionCurrent instance."""
        return AppSubscriptionCurrent(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            merchant_uuid=sanitize_uuid_field(self.merchant_uuid, 13),  # type: ignore
            developer_app_uuid=sanitize_uuid_field(self.developer_app_uuid, 13),  # type: ignore
            environment=self.environment,
            app_subscription_uuid=sanitize_uuid_field(self.app_subscription_uuid, 13),  # type: ignore
            app_subscription_cost=self.app_subscription_cost,
            bundled_with_plan=self.bundled_with_plan,
            trial_end_date=self.trial_end_date,
            last_advance_date=self.last_advance_date,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
        )