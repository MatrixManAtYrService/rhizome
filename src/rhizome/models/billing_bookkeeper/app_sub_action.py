"""
SQLModel definition for the app_sub_action table.

This module provides the SQLModel class for the app_sub_action table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from decimal import Decimal

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class AppSubAction(RhizomeModel, table=False):
    """
    SQLModel for the `app_sub_action` table.

    This model represents app sub action records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    billing_entity_uuid: str = Field(max_length=26, description="Billing Entity Uuid")
    developer_app_uuid: str = Field(max_length=13, description="Developer App Uuid")
    app_subscription_uuid: str = Field(max_length=13, description="App Subscription Uuid")
    app_sub_action_type: str = Field(max_length=25, description="App Sub Action Type")
    fee_category: str = Field(max_length=25, description="Fee Category")
    fee_code: str = Field(max_length=25, description="Fee Code")
    action_datetime: datetime.datetime = Field(description="Action Datetime")
    merchant_plan_uuid: str | None = Field(default=None, max_length=13, description="Merchant Plan Uuid")
    num_units: int = Field(description="Num Units")
    units_in_period: int = Field(description="Units In Period")
    basis_amount: Decimal | None = Field(default=None, max_digits=12, decimal_places=3, description="Basis Amount")
    basis_currency: str | None = Field(default=None, max_length=3, description="Basis Currency")
    reference: str | None = Field(default=None, max_length=50, description="Reference")
    app_sub_action_fee_code_uuid: str | None = Field(
        default=None, max_length=26, description="App Sub Action Fee Code Uuid"
    )
    fee_uuid: str | None = Field(default=None, max_length=26, description="Fee Uuid")
    event_uuid: str | None = Field(default=None, max_length=26, description="Event Uuid")
    request_uuid: str | None = Field(default=None, max_length=26, description="Request Uuid")
    date_to_post: datetime.date | None = Field(default=None, description="Date To Post")
    posting_date: datetime.date | None = Field(default=None, description="Posting Date")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")
    modified_timestamp: datetime.datetime = Field(description="Modified Timestamp")

    def sanitize(self) -> AppSubAction:
        """Return a sanitized copy of this AppSubAction instance."""
        return AppSubAction(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            billing_entity_uuid=sanitize_uuid_field(self.billing_entity_uuid, 26),  # type: ignore
            developer_app_uuid=sanitize_uuid_field(self.developer_app_uuid, 13),  # type: ignore
            app_subscription_uuid=sanitize_uuid_field(self.app_subscription_uuid, 13),  # type: ignore
            app_sub_action_type=self.app_sub_action_type,
            fee_category=self.fee_category,
            fee_code=self.fee_code,
            action_datetime=self.action_datetime,
            merchant_plan_uuid=sanitize_uuid_field(self.merchant_plan_uuid, 13),
            num_units=self.num_units,
            units_in_period=self.units_in_period,
            basis_amount=self.basis_amount,
            basis_currency=self.basis_currency,
            reference=self.reference,
            app_sub_action_fee_code_uuid=sanitize_uuid_field(self.app_sub_action_fee_code_uuid, 26),
            fee_uuid=sanitize_uuid_field(self.fee_uuid, 26),
            event_uuid=sanitize_uuid_field(self.event_uuid, 26),
            request_uuid=sanitize_uuid_field(self.request_uuid, 26),
            date_to_post=self.date_to_post,
            posting_date=self.posting_date,
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
        )
