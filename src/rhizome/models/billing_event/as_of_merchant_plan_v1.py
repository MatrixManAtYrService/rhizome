"""
SQLModel definition for the as_of_merchant_plan table, version 1.

This module provides the V1 implementation of the AsOfMerchantPlan model.
Currently, AsOfMerchantPlanV1 is identical to the base AsOfMerchantPlan class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .as_of_merchant_plan import AsOfMerchantPlan


class AsOfMerchantPlanV1(AsOfMerchantPlan, table=True):
    """
    Version 1 of the AsOfMerchantPlan model.

    Currently a name-only inheritance from the base AsOfMerchantPlan class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "as_of_merchant_plan"  # type: ignore