"""
SQLModel definition for the email_developer_charge table.

This module provides the SQLModel class for the email_developer_charge table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class EmailDeveloperCharge(RhizomeModel, table=False):
    """
    SQLModel for the `email_developer_charge` table.

    This model represents email_developer_charge records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    developer_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    charge_id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    app_uuid: str = Field(max_length=13, description="app_uuid")
    merchant_uuid: str = Field(max_length=13, description="merchant_uuid")
    app_name: str = Field(max_length=250, description="app_name")
    merchant_name: str = Field(max_length=127, description="merchant_name")
    charge_status: str = Field(max_length=127, description="charge_status")
    charge_amount: int = Field(description="charge_amount")
    currency: str = Field(max_length=3, description="currency")
    developer_portion_amount: int | None = Field(default=None, description="developer_portion_amount")
    charge_created_time: datetime.datetime | None = Field(default=None, description="charge_created_time")
    done_time: datetime.datetime | None = Field(default=None, description="done_time")
    created_time: datetime.datetime = Field(description="created_time")
    modified_time: datetime.datetime = Field(description="modified_time")

    def sanitize(self) -> EmailDeveloperCharge:
        """Return a sanitized copy of this EmailDeveloperCharge instance."""
        return EmailDeveloperCharge(
            id=self.id,
            developer_id=self.developer_id,
            charge_id=self.charge_id,
            app_uuid=sanitize_uuid_field(self.app_uuid, 13),
            merchant_uuid=sanitize_uuid_field(self.merchant_uuid, 13),
            app_name=self.app_name,
            merchant_name=self.merchant_name,
            charge_status=self.charge_status,
            charge_amount=self.charge_amount,
            currency=self.currency,
            developer_portion_amount=self.developer_portion_amount,
            charge_created_time=self.charge_created_time,
            done_time=self.done_time,
            created_time=self.created_time,
            modified_time=self.modified_time,
        )
