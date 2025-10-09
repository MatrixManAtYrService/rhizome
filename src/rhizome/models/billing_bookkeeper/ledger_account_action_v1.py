"""
SQLModel definition for the ledger_account_action table, version 1.

This module provides the V1 implementation of the LedgerAccountAction model.
"""

from __future__ import annotations

from .ledger_account_action import LedgerAccountAction


class LedgerAccountActionV1(LedgerAccountAction, table=True):
    """
    Version 1 of the LedgerAccountAction model.

    Currently a name-only inheritance from the base LedgerAccountAction class.
    """

    __tablename__ = "ledger_account_action"  # type: ignore
