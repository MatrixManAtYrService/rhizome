"""
SQLModel definition for the settlement_action table, version 1.

This module provides the V1 implementation of the SettlementAction model.
"""

from __future__ import annotations

from .settlement_action import SettlementAction


class SettlementActionV1(SettlementAction, table=True):
    """
    Version 1 of the SettlementAction model.

    Currently a name-only inheritance from the base SettlementAction class.
    """

    __tablename__ = "settlement_action"  # type: ignore
