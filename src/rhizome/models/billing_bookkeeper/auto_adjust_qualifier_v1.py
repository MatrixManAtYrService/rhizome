"""
SQLModel definition for the auto_adjust_qualifier table, version 1.

This module provides the V1 implementation of the AutoAdjustQualifier model.
"""

from __future__ import annotations

from .auto_adjust_qualifier import AutoAdjustQualifier


class AutoAdjustQualifierV1(AutoAdjustQualifier, table=True):
    """
    Version 1 of the AutoAdjustQualifier model.

    Currently a name-only inheritance from the base AutoAdjustQualifier class.
    """

    __tablename__ = "auto_adjust_qualifier"  # type: ignore
