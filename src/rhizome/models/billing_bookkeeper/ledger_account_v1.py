"""
SQLModel definition for the ledger_account table, version 1.

This module provides the V1 implementation of the LedgerAccount model.
"""

from __future__ import annotations

from .ledger_account import LedgerAccount


class LedgerAccountV1(LedgerAccount, table=True):
    """
    Version 1 of the LedgerAccount model.

    Currently a name-only inheritance from the base LedgerAccount class.
    """

    __tablename__ = "ledger_account"  # type: ignore
