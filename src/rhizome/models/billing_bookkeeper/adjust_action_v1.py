"""
SQLModel definition for the adjust_action table, version 1.

This module provides the V1 implementation of the AdjustAction model.
"""

from __future__ import annotations

from .adjust_action import AdjustAction


class AdjustActionV1(AdjustAction, table=True):
    """
    Version 1 of the AdjustAction model.

    Currently a name-only inheritance from the base AdjustAction class.
    """

    __tablename__ = "adjust_action"  # type: ignore
