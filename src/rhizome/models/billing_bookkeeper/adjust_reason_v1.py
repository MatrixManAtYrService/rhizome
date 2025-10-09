"""
SQLModel definition for the adjust_reason table, version 1.

This module provides the V1 implementation of the AdjustReason model.
"""

from __future__ import annotations

from .adjust_reason import AdjustReason


class AdjustReasonV1(AdjustReason, table=True):
    """
    Version 1 of the AdjustReason model.

    Currently a name-only inheritance from the base AdjustReason class.
    """

    __tablename__ = "adjust_reason"  # type: ignore
