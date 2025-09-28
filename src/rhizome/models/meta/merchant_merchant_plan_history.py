"""
SQLModel definition for the merchant_merchant_plan_history table.
"""

from __future__ import annotations

import datetime
from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="MerchantMerchantPlanHistory")


class MerchantMerchantPlanHistory(RhizomeModel, table=False):
    """
    Base MerchantMerchantPlanHistory model - defines common fields across all versions.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    merchant_id: int
    old_merchant_plan_id: int | None = Field(default=None)
    new_merchant_plan_id: int | None = Field(default=None)
    changed_timestamp: datetime.datetime

    def sanitize(self: T) -> T:
        """Return a sanitized copy of this MerchantMerchantPlanHistory instance."""
        # This will be overridden by concrete subclasses
        raise NotImplementedError("Subclasses must implement sanitize()")
