"""
SQLModel definition for the ledger_account_transition table, version 1.

This module provides the V1 implementation of the LedgerAccountTransition model.
"""

from __future__ import annotations

from .ledger_account_transition import LedgerAccountTransition


class LedgerAccountTransitionV1(LedgerAccountTransition, table=True):
    """
    Version 1 of the LedgerAccountTransition model.

    Currently a name-only inheritance from the base LedgerAccountTransition class.
    """

    __tablename__ = "ledger_account_transition"  # type: ignore
