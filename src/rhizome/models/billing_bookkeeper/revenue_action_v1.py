"""
SQLModel definition for the revenue_action table, version 1.

This module provides the V1 implementation of the RevenueAction model.
"""

from __future__ import annotations

from .revenue_action import RevenueAction


class RevenueActionV1(RevenueAction, table=True):
    """
    Version 1 of the RevenueAction model.

    Currently a name-only inheritance from the base RevenueAction class.
    """

    __tablename__ = "revenue_action"  # type: ignore
