"""
SQLModel definition for the stage_merchant_plan_charge table, version 1.

This module provides the V1 implementation of the StageMerchantPlanCharge model.
Currently, StageMerchantPlanChargeV1 is identical to the base StageMerchantPlanCharge class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .stage_merchant_plan_charge import StageMerchantPlanCharge


class StageMerchantPlanChargeV1(StageMerchantPlanCharge, NaProdSQLModel, table=True):
    """
    Version 1 of the StageMerchantPlanCharge model.

    Currently a name-only inheritance from the base StageMerchantPlanCharge class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "stage_merchant_plan_charge"  # type: ignore
