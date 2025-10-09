"""
SQLModel definition for the tiered_qualifier table, version 1.

This module provides the V1 implementation of the TieredQualifier model.
"""

from __future__ import annotations

from .tiered_qualifier import TieredQualifier


class TieredQualifierV1(TieredQualifier, table=True):
    """
    Version 1 of the TieredQualifier model.

    Currently a name-only inheritance from the base TieredQualifier class.
    """

    __tablename__ = "tiered_qualifier"  # type: ignore
