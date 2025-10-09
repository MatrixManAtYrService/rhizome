"""
SQLModel definition for the monetary_rule_alias table, version 1.

This module provides the V1 implementation of the MonetaryRuleAlias model.
"""

from __future__ import annotations

from .monetary_rule_alias import MonetaryRuleAlias


class MonetaryRuleAliasV1(MonetaryRuleAlias, table=True):
    """
    Version 1 of the MonetaryRuleAlias model.

    Currently a name-only inheritance from the base MonetaryRuleAlias class.
    """

    __tablename__ = "monetary_rule_alias"  # type: ignore
