"""
SQLModel definition for the tiered_rule table, version 1.

This module provides the V1 implementation of the TieredRule model.
"""

from __future__ import annotations

from .tiered_rule import TieredRule


class TieredRuleV1(TieredRule, table=True):
    """
    Version 1 of the TieredRule model.

    Currently a name-only inheritance from the base TieredRule class.
    """

    __tablename__ = "tiered_rule"  # type: ignore
