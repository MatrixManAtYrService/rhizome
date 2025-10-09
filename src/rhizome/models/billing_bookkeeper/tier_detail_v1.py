"""
SQLModel definition for the tier_detail table, version 1.

This module provides the V1 implementation of the TierDetail model.
"""

from __future__ import annotations

from .tier_detail import TierDetail


class TierDetailV1(TierDetail, table=True):
    """
    Version 1 of the TierDetail model.

    Currently a name-only inheritance from the base TierDetail class.
    """

    __tablename__ = "tier_detail"  # type: ignore
