"""
SQLModel definition for the as_of_merchant_plan table, version 1.

This module provides the V1 implementation of the AsOfMerchantPlan model.
V1 is the base version used in na_prod environment without the modifier field.
"""

from __future__ import annotations

from ...sanitize_helpers import sanitize_uuid_field
from ..metadata_registry import NaProdSQLModel
from .as_of_merchant_plan import AsOfMerchantPlan


class AsOfMerchantPlanV1(AsOfMerchantPlan, NaProdSQLModel, table=True):
    """
    Version 1 of the AsOfMerchantPlan model.

    This version includes only the base fields and is used in environments
    that don't have the modifier field (like na_prod).
    """

    __tablename__ = "as_of_merchant_plan"  # type: ignore

    def sanitize(self) -> AsOfMerchantPlanV1:
        """Return a sanitized copy of this AsOfMerchantPlanV1 instance."""
        return AsOfMerchantPlanV1(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            as_of_merchant_uuid=sanitize_uuid_field(self.as_of_merchant_uuid, 26),  # type: ignore
            merchant_plan_uuid=sanitize_uuid_field(self.merchant_plan_uuid, 13),  # type: ignore
            trial_start_date=self.trial_start_date,
            trial_days=self.trial_days,
            created_timestamp=self.created_timestamp,
        )