"""
SQLModel definition for the adjust_action_fee_code table, version 1.

This module provides the V1 implementation of the AdjustActionFeeCode model.
"""

from __future__ import annotations

from .adjust_action_fee_code import AdjustActionFeeCode


class AdjustActionFeeCodeV1(AdjustActionFeeCode, table=True):
    """
    Version 1 of the AdjustActionFeeCode model.

    Currently a name-only inheritance from the base AdjustActionFeeCode class.
    """

    __tablename__ = "adjust_action_fee_code"  # type: ignore
