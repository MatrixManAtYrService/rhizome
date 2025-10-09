"""
SQLModel definition for the ledger_account_key_app table, version 1.

This module provides the V1 implementation of the LedgerAccountKeyApp model.
"""

from __future__ import annotations

from .ledger_account_key_app import LedgerAccountKeyApp


class LedgerAccountKeyAppV1(LedgerAccountKeyApp, table=True):
    """
    Version 1 of the LedgerAccountKeyApp model.

    Currently a name-only inheritance from the base LedgerAccountKeyApp class.
    """

    __tablename__ = "ledger_account_key_app"  # type: ignore
