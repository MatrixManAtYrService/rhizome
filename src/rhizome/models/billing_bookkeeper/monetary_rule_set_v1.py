"""
SQLModel definition for the monetary_rule_set table, version 1.

This module provides the V1 implementation of the MonetaryRuleSet model.
"""

from __future__ import annotations

from .monetary_rule_set import MonetaryRuleSet


class MonetaryRuleSetV1(MonetaryRuleSet, table=True):
    """
    Version 1 of the MonetaryRuleSet model.

    Currently a name-only inheritance from the base MonetaryRuleSet class.
    """

    __tablename__ = "monetary_rule_set"  # type: ignore
