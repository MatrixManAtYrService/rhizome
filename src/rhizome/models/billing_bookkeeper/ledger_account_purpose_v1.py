"""
SQLModel definition for the ledger_account_purpose table, version 1.

This module provides the V1 implementation of the LedgerAccountPurpose model.
"""

from __future__ import annotations

from .ledger_account_purpose import LedgerAccountPurpose


class LedgerAccountPurposeV1(LedgerAccountPurpose, table=True):
    """
    Version 1 of the LedgerAccountPurpose model.

    Currently a name-only inheritance from the base LedgerAccountPurpose class.
    """

    __tablename__ = "ledger_account_purpose"  # type: ignore
