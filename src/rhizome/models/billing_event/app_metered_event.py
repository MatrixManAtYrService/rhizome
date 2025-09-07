"""
SQLModel definition for the app_metered_event table.

This module provides the SQLModel class for the app_metered_event table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from decimal import Decimal

from sqlmodel import Field

from ...models.base import SanitizableModel
from ...sanitize_helpers import sanitize_uuid_field


class AppMeteredEvent(SanitizableModel, table=False):
    """
    SQLModel for the `app_metered_event` table.

    This model represents app metered events in the billing system,
    containing usage data for metered applications.
    """


    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=26, unique=True, description="Unique identifier for the app metered event")
    merchant_uuid: str = Field(max_length=13, description="UUID of the merchant")
    developer_app_uuid: str = Field(max_length=13, description="UUID of the developer application")
    environment: str = Field(max_length=25, description="Environment (e.g., usprod)")
    app_metered_uuid: str = Field(max_length=13, description="UUID of the app metered configuration")
    count: int | None = Field(default=None, description="Count of events or usage")
    basis_amount: Decimal | None = Field(
        default=None, max_digits=12, decimal_places=3, description="Basis amount for billing calculation"
    )
    basis_currency: str | None = Field(default=None, max_length=3, description="Currency code for basis amount")
    action_timestamp: datetime.datetime = Field(description="Timestamp when the action occurred")
    credit_for_trial: int = Field(default=0, description="Flag indicating if this is a trial credit (0/1)")
    cos_event_uuid: str | None = Field(default=None, max_length=26, description="UUID of the COS event")
    processed_timestamp: datetime.datetime | None = Field(
        default=None, description="Timestamp when the event was processed"
    )
    billing_event_uuid: str | None = Field(default=None, max_length=26, description="UUID of the billing event")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")

    def sanitize(self) -> AppMeteredEvent:
        """Return a sanitized copy of this AppMeteredEvent instance."""
        return AppMeteredEvent(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            merchant_uuid=sanitize_uuid_field(self.merchant_uuid, 13),  # type: ignore
            developer_app_uuid=sanitize_uuid_field(self.developer_app_uuid, 13),  # type: ignore
            environment=self.environment,
            app_metered_uuid=sanitize_uuid_field(self.app_metered_uuid, 13),  # type: ignore
            count=self.count,
            basis_amount=self.basis_amount,
            basis_currency=self.basis_currency,
            action_timestamp=self.action_timestamp,
            credit_for_trial=self.credit_for_trial,
            cos_event_uuid=sanitize_uuid_field(self.cos_event_uuid, 26),
            processed_timestamp=self.processed_timestamp,
            billing_event_uuid=sanitize_uuid_field(self.billing_event_uuid, 26),
            created_timestamp=self.created_timestamp,
        )
