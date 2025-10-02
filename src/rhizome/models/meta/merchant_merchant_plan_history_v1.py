"""
SQLModel definition for the merchant_merchant_plan_history table, version 1.

This module provides the V1 implementation of the MerchantMerchantPlanHistory model.
Currently, MerchantMerchantPlanHistoryV1 is identical to the base MerchantMerchantPlanHistory class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import MetaSQLModel
from .merchant_merchant_plan_history import MerchantMerchantPlanHistory


class MerchantMerchantPlanHistoryV1(MerchantMerchantPlanHistory, MetaSQLModel, table=True):
    """
    Version 1 of the MerchantMerchantPlanHistory model.

    Currently a name-only inheritance from the base MerchantMerchantPlanHistory class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "merchant_merchant_plan_history"  # type: ignore

    def sanitize(self) -> MerchantMerchantPlanHistoryV1:
        """Return a sanitized copy of this MerchantMerchantPlanHistoryV1 instance."""
        return MerchantMerchantPlanHistoryV1(
            changed_timestamp=self.changed_timestamp,
            id=self.id,
            merchant_id=self.merchant_id,
            new_merchant_plan_id=self.new_merchant_plan_id,
            old_merchant_plan_id=self.old_merchant_plan_id,
        )
