"""
SQLModel definition for the as_of_merchant_plan table, version 2.

This module provides the V2 implementation of the AsOfMerchantPlan model.
V2 adds the modifier field which exists in dev and demo environments
but not in the na_prod environment.
"""

from __future__ import annotations

from sqlmodel import Field

from ...sanitize_helpers import sanitize_uuid_field
from ..metadata_registry import DevDemoSQLModel
from .as_of_merchant_plan import AsOfMerchantPlan


class AsOfMerchantPlanV2(AsOfMerchantPlan, DevDemoSQLModel, table=True):
    """
    Version 2 of the AsOfMerchantPlan model.

    Adds the modifier field introduced in newer schema versions.
    This version is used in dev and demo environments.
    """

    __tablename__ = "as_of_merchant_plan"  # type: ignore

    # New field in V2
    modifier: str | None = Field(default=None, max_length=25, description="Modifier for the plan")

    def sanitize(self) -> AsOfMerchantPlanV2:
        """Return a sanitized copy of this AsOfMerchantPlanV2 instance."""
        return AsOfMerchantPlanV2(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            as_of_merchant_uuid=sanitize_uuid_field(self.as_of_merchant_uuid, 26),  # type: ignore
            merchant_plan_uuid=sanitize_uuid_field(self.merchant_plan_uuid, 13),  # type: ignore
            trial_start_date=self.trial_start_date,
            trial_days=self.trial_days,
            created_timestamp=self.created_timestamp,
            modifier=self.modifier,
        )
