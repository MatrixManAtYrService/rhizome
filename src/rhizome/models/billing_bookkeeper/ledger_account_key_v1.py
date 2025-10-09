"""
SQLModel definition for the ledger_account_key table, version 1.

This module provides the V1 implementation of the LedgerAccountKey model.
"""

from __future__ import annotations

from .ledger_account_key import LedgerAccountKey


class LedgerAccountKeyV1(LedgerAccountKey, table=True):
    """
    Version 1 of the LedgerAccountKey model.

    Currently a name-only inheritance from the base LedgerAccountKey class.
    """

    __tablename__ = "ledger_account_key"  # type: ignore
