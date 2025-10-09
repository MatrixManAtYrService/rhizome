"""
SQLModel definition for the fee_code_ledger_account table, version 1.

This module provides the V1 implementation of the FeeCodeLedgerAccount model.
"""

from __future__ import annotations

from .fee_code_ledger_account import FeeCodeLedgerAccount


class FeeCodeLedgerAccountV1(FeeCodeLedgerAccount, table=True):
    """
    Version 1 of the FeeCodeLedgerAccount model.

    Currently a name-only inheritance from the base FeeCodeLedgerAccount class.
    """

    __tablename__ = "fee_code_ledger_account"  # type: ignore
