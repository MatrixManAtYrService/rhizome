"""
SQLModel definition for the ledger_account_key_purpose table, version 1.

This module provides the V1 implementation of the LedgerAccountKeyPurpose model.
"""

from __future__ import annotations

from .ledger_account_key_purpose import LedgerAccountKeyPurpose


class LedgerAccountKeyPurposeV1(LedgerAccountKeyPurpose, table=True):
    """
    Version 1 of the LedgerAccountKeyPurpose model.

    Currently a name-only inheritance from the base LedgerAccountKeyPurpose class.
    """

    __tablename__ = "ledger_account_key_purpose"  # type: ignore
