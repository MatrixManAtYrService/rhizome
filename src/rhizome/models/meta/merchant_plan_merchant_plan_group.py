"""
SQLModel definition for the merchant_plan_merchant_plan_group table.
"""

from __future__ import annotations

from typing import TypeVar

from sqlmodel import Field

from ...models.base import RhizomeModel

T = TypeVar("T", bound="MerchantPlanMerchantPlanGroup")


class MerchantPlanMerchantPlanGroup(RhizomeModel, table=False):
    """
    Base MerchantPlanMerchantPlanGroup model - defines common fields across all versions.
    """

    id: int | None = Field(default=None, primary_key=True, description="Primary key, auto-incrementing")
    merchant_plan_id: int
    merchant_plan_group_id: int
    default_plan: bool = Field(default=False)

    def sanitize(self: T) -> T:
        """Return a sanitized copy of this MerchantPlanMerchantPlanGroup instance."""
        # This will be overridden by concrete subclasses
        raise NotImplementedError("Subclasses must implement sanitize()")
