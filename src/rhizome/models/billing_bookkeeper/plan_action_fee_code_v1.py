"""
SQLModel definition for the plan_action_fee_code table, version 1.

This module provides the V1 implementation of the PlanActionFeeCode model.
"""

from __future__ import annotations

from .plan_action_fee_code import PlanActionFeeCode


class PlanActionFeeCodeV1(PlanActionFeeCode, table=True):
    """
    Version 1 of the PlanActionFeeCode model.

    Currently a name-only inheritance from the base PlanActionFeeCode class.
    """

    __tablename__ = "plan_action_fee_code"  # type: ignore
