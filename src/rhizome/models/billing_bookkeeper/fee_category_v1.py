"""
SQLModel definition for the fee_category table, version 1.

This module provides the V1 implementation of the FeeCategory model.
"""

from __future__ import annotations

from .fee_category import FeeCategory


class FeeCategoryV1(FeeCategory, table=True):
    """
    Version 1 of the FeeCategory model.

    Currently a name-only inheritance from the base FeeCategory class.
    """

    __tablename__ = "fee_category"  # type: ignore
