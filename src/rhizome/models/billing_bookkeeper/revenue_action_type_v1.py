"""
SQLModel definition for the revenue_action_type table, version 1.

This module provides the V1 implementation of the RevenueActionType model.
"""

from __future__ import annotations

from .revenue_action_type import RevenueActionType


class RevenueActionTypeV1(RevenueActionType, table=True):
    """
    Version 1 of the RevenueActionType model.

    Currently a name-only inheritance from the base RevenueActionType class.
    """

    __tablename__ = "revenue_action_type"  # type: ignore
