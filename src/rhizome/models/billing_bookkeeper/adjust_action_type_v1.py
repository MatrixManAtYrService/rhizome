"""
SQLModel definition for the adjust_action_type table, version 1.

This module provides the V1 implementation of the AdjustActionType model.
"""

from __future__ import annotations

from .adjust_action_type import AdjustActionType


class AdjustActionTypeV1(AdjustActionType, table=True):
    """
    Version 1 of the AdjustActionType model.

    Currently a name-only inheritance from the base AdjustActionType class.
    """

    __tablename__ = "adjust_action_type"  # type: ignore
