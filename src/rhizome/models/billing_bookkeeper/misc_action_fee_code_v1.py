"""
SQLModel definition for the misc_action_fee_code table, version 1.

This module provides the V1 implementation of the MiscActionFeeCode model.
"""

from __future__ import annotations

from .misc_action_fee_code import MiscActionFeeCode


class MiscActionFeeCodeV1(MiscActionFeeCode, table=True):
    """
    Version 1 of the MiscActionFeeCode model.

    Currently a name-only inheritance from the base MiscActionFeeCode class.
    """

    __tablename__ = "misc_action_fee_code"  # type: ignore
