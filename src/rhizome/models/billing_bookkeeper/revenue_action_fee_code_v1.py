"""
SQLModel definition for the revenue_action_fee_code table, version 1.

This module provides the V1 implementation of the RevenueActionFeeCode model.
"""

from __future__ import annotations

from .revenue_action_fee_code import RevenueActionFeeCode


class RevenueActionFeeCodeV1(RevenueActionFeeCode, table=True):
    """
    Version 1 of the RevenueActionFeeCode model.

    Currently a name-only inheritance from the base RevenueActionFeeCode class.
    """

    __tablename__ = "revenue_action_fee_code"  # type: ignore
