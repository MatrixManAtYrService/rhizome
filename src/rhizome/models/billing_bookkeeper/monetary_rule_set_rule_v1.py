"""
SQLModel definition for the monetary_rule_set_rule table, version 1.

This module provides the V1 implementation of the MonetaryRuleSetRule model.
"""

from __future__ import annotations

from .monetary_rule_set_rule import MonetaryRuleSetRule


class MonetaryRuleSetRuleV1(MonetaryRuleSetRule, table=True):
    """
    Version 1 of the MonetaryRuleSetRule model.

    Currently a name-only inheritance from the base MonetaryRuleSetRule class.
    """

    __tablename__ = "monetary_rule_set_rule"  # type: ignore
