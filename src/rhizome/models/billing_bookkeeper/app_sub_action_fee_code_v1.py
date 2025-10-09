"""
SQLModel definition for the app_sub_action_fee_code table, version 1.

This module provides the V1 implementation of the AppSubActionFeeCode model.
"""

from __future__ import annotations

from .app_sub_action_fee_code import AppSubActionFeeCode


class AppSubActionFeeCodeV1(AppSubActionFeeCode, table=True):
    """
    Version 1 of the AppSubActionFeeCode model.

    Currently a name-only inheritance from the base AppSubActionFeeCode class.
    """

    __tablename__ = "app_sub_action_fee_code"  # type: ignore
