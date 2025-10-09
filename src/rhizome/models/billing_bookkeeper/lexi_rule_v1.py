"""
SQLModel definition for the lexi_rule table, version 1.

This module provides the V1 implementation of the LexiRule model.
"""

from __future__ import annotations

from .lexi_rule import LexiRule


class LexiRuleV1(LexiRule, table=True):
    """
    Version 1 of the LexiRule model.

    Currently a name-only inheritance from the base LexiRule class.
    """

    __tablename__ = "lexi_rule"  # type: ignore
