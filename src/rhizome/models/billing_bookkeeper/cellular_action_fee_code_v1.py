"""
SQLModel definition for the cellular_action_fee_code table, version 1.

This module provides the V1 implementation of the CellularActionFeeCode model.
"""

from __future__ import annotations

from .cellular_action_fee_code import CellularActionFeeCode


class CellularActionFeeCodeV1(CellularActionFeeCode, table=True):
    """
    Version 1 of the CellularActionFeeCode model.

    Currently a name-only inheritance from the base CellularActionFeeCode class.
    """

    __tablename__ = "cellular_action_fee_code"  # type: ignore
