"""
SQLModel definition for the revenue_share_group table, version 1.

This module provides the V1 implementation of the RevenueShareGroup model.
"""

from __future__ import annotations

from .revenue_share_group import RevenueShareGroup


class RevenueShareGroupV1(RevenueShareGroup, table=True):
    """
    Version 1 of the RevenueShareGroup model.

    Currently a name-only inheritance from the base RevenueShareGroup class.
    """

    __tablename__ = "revenue_share_group"  # type: ignore
