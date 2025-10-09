"""
SQLModel definition for the ledger_account_balance table, version 1.

This module provides the V1 implementation of the LedgerAccountBalance model.
"""

from __future__ import annotations

from .ledger_account_balance import LedgerAccountBalance


class LedgerAccountBalanceV1(LedgerAccountBalance, table=True):
    """
    Version 1 of the LedgerAccountBalance model.

    Currently a name-only inheritance from the base LedgerAccountBalance class.
    """

    __tablename__ = "ledger_account_balance"  # type: ignore
