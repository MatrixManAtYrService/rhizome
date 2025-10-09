"""
SQLModel definition for the auto_adjust_rule table, version 1.

This module provides the V1 implementation of the AutoAdjustRule model.
"""

from __future__ import annotations

from .auto_adjust_rule import AutoAdjustRule


class AutoAdjustRuleV1(AutoAdjustRule, table=True):
    """
    Version 1 of the AutoAdjustRule model.

    Currently a name-only inheritance from the base AutoAdjustRule class.
    """

    __tablename__ = "auto_adjust_rule"  # type: ignore
