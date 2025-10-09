"""
SQLModel definition for the monetary_adjustment table, version 1.

This module provides the V1 implementation of the MonetaryAdjustment model.
"""

from __future__ import annotations

from .monetary_adjustment import MonetaryAdjustment


class MonetaryAdjustmentV1(MonetaryAdjustment, table=True):
    """
    Version 1 of the MonetaryAdjustment model.

    Currently a name-only inheritance from the base MonetaryAdjustment class.
    """

    __tablename__ = "monetary_adjustment"  # type: ignore
