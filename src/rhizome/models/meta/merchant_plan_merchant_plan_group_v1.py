"""
SQLModel definition for the merchant_plan_merchant_plan_group table, version 1.

This module provides the V1 implementation of the MerchantPlanMerchantPlanGroup model.
Currently, MerchantPlanMerchantPlanGroupV1 is identical to the base MerchantPlanMerchantPlanGroup class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import MetaSQLModel
from .merchant_plan_merchant_plan_group import MerchantPlanMerchantPlanGroup


class MerchantPlanMerchantPlanGroupV1(MerchantPlanMerchantPlanGroup, MetaSQLModel, table=True):
    """
    Version 1 of the MerchantPlanMerchantPlanGroup model.

    Currently a name-only inheritance from the base MerchantPlanMerchantPlanGroup class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "merchant_plan_merchant_plan_group"  # type: ignore

    def sanitize(self) -> MerchantPlanMerchantPlanGroupV1:
        """Return a sanitized copy of this MerchantPlanMerchantPlanGroupV1 instance."""
        return MerchantPlanMerchantPlanGroupV1(
            default_plan=self.default_plan,
            id=self.id,
            merchant_plan_group_id=self.merchant_plan_group_id,
            merchant_plan_id=self.merchant_plan_id,
        )
