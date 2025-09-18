"""
SQLModel definition for the as_of_merchant_plan table.

This module provides the SQLModel class for the as_of_merchant_plan table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="AsOfMerchantPlan")


class AsOfMerchantPlan(RhizomeModel, table=False):
    """
    SQLModel for the `as_of_merchant_plan` table.

    This model represents merchant plan information associated with merchant snapshots,
    tracking plan details at specific points in time.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    uuid: str = Field(max_length=26, unique=True, description="Unique identifier for the as-of-merchant-plan record")
    as_of_merchant_uuid: str = Field(max_length=26, description="UUID of the associated as-of-merchant record")
    merchant_plan_uuid: str = Field(max_length=13, description="UUID of the merchant plan")
    trial_start_date: datetime.date | None = Field(default=None, description="Start date of trial period")
    trial_days: int | None = Field(default=None, description="Number of trial days")
    created_timestamp: datetime.datetime = Field(description="Timestamp when the record was created")

    def sanitize(self: T) -> T:
        """Return a sanitized copy of this AsOfMerchantPlan instance."""
        # This will be overridden by concrete subclasses
        raise NotImplementedError("Subclasses must implement sanitize()")