"""
SQLModel definition for the app_subscription_event table.

This module provides the SQLModel class for the app_subscription_event table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from decimal import Decimal
from enum import StrEnum

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class ActionType(StrEnum):
    """Enum for subscription action types."""

    INSTALL = "INSTALL"
    UNINSTALL = "UNINSTALL"
    SUBSCRIPTION_CHANGE = "SUBSCRIPTION_CHANGE"


class AppSubscriptionEvent(RhizomeModel, table=False):
    """
    SQLModel for the `app_subscription_event` table.

    This model represents app subscription events in the billing system,
    tracking installations, uninstallations, and subscription changes.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=26, unique=True, description="Unique identifier for the app subscription event")
    merchant_uuid: str = Field(max_length=13, description="UUID of the merchant")
    developer_app_uuid: str = Field(max_length=13, description="UUID of the developer application")
    environment: str = Field(max_length=25, description="Environment (e.g., usprod)")
    action_type: ActionType = Field(description="Type of action (INSTALL, UNINSTALL, SUBSCRIPTION_CHANGE)")
    app_subscription_uuid: str = Field(max_length=13, description="UUID of the app subscription")
    app_subscription_cost: Decimal = Field(max_digits=12, decimal_places=3, description="Cost of the app subscription")
    bundled_with_plan: bool = Field(default=False, description="Whether bundled with a plan")
    trial_end_date: datetime.date | None = Field(default=None, description="End date of trial period")
    is_hidden_or_sys_app: bool = Field(default=False, description="Whether this is a hidden or system app")
    cos_event_uuid: str | None = Field(default=None, max_length=26, description="UUID of the COS event")
    action_timestamp: datetime.datetime = Field(description="Timestamp when the action occurred")
    processed_timestamp: datetime.datetime | None = Field(
        default=None, description="Timestamp when the event was processed"
    )
    app_subscription_daily_uuid: str | None = Field(
        default=None, max_length=26, description="UUID of the app subscription daily record"
    )
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")

    def sanitize(self) -> AppSubscriptionEvent:
        """Return a sanitized copy of this AppSubscriptionEvent instance."""
        return AppSubscriptionEvent(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            merchant_uuid=sanitize_uuid_field(self.merchant_uuid, 13),  # type: ignore
            developer_app_uuid=sanitize_uuid_field(self.developer_app_uuid, 13),  # type: ignore
            environment=self.environment,
            action_type=self.action_type,
            app_subscription_uuid=sanitize_uuid_field(self.app_subscription_uuid, 13),  # type: ignore
            app_subscription_cost=self.app_subscription_cost,
            bundled_with_plan=self.bundled_with_plan,
            trial_end_date=self.trial_end_date,
            is_hidden_or_sys_app=self.is_hidden_or_sys_app,
            cos_event_uuid=sanitize_uuid_field(self.cos_event_uuid, 26),
            action_timestamp=self.action_timestamp,
            processed_timestamp=self.processed_timestamp,
            app_subscription_daily_uuid=sanitize_uuid_field(self.app_subscription_daily_uuid, 26),
            created_timestamp=self.created_timestamp,
        )
