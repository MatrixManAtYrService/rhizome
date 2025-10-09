"""
SQLModel definition for the revenue_action_error table, version 1.

This module provides the V1 implementation of the RevenueActionError model.
"""

from __future__ import annotations

from .revenue_action_error import RevenueActionError


class RevenueActionErrorV1(RevenueActionError, table=True):
    """
    Version 1 of the RevenueActionError model.

    Currently a name-only inheritance from the base RevenueActionError class.
    """

    __tablename__ = "revenue_action_error"  # type: ignore
