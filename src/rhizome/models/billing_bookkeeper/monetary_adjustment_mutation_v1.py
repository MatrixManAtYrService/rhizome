"""
SQLModel definition for the monetary_adjustment_mutation table, version 1.

This module provides the V1 implementation of the MonetaryAdjustmentMutation model.
"""

from __future__ import annotations

from .monetary_adjustment_mutation import MonetaryAdjustmentMutation


class MonetaryAdjustmentMutationV1(MonetaryAdjustmentMutation, table=True):
    """
    Version 1 of the MonetaryAdjustmentMutation model.

    Currently a name-only inheritance from the base MonetaryAdjustmentMutation class.
    """

    __tablename__ = "monetary_adjustment_mutation"  # type: ignore
