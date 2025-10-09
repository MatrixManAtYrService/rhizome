"""
SQLModel definition for the auto_adjust_advice table, version 1.

This module provides the V1 implementation of the AutoAdjustAdvice model.
"""

from __future__ import annotations

from .auto_adjust_advice import AutoAdjustAdvice


class AutoAdjustAdviceV1(AutoAdjustAdvice, table=True):
    """
    Version 1 of the AutoAdjustAdvice model.

    Currently a name-only inheritance from the base AutoAdjustAdvice class.
    """

    __tablename__ = "auto_adjust_advice"  # type: ignore
