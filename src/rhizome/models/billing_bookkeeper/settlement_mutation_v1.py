"""
SQLModel definition for the settlement_mutation table, version 1.

This module provides the V1 implementation of the SettlementMutation model.
"""

from __future__ import annotations

from .settlement_mutation import SettlementMutation


class SettlementMutationV1(SettlementMutation, table=True):
    """
    Version 1 of the SettlementMutation model.

    Currently a name-only inheritance from the base SettlementMutation class.
    """

    __tablename__ = "settlement_mutation"  # type: ignore
