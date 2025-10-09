"""
SQLModel definition for the ledger_account_settlement table, version 1.

This module provides the V1 implementation of the LedgerAccountSettlement model.
"""

from __future__ import annotations

from .ledger_account_settlement import LedgerAccountSettlement


class LedgerAccountSettlementV1(LedgerAccountSettlement, table=True):
    """
    Version 1 of the LedgerAccountSettlement model.

    Currently a name-only inheritance from the base LedgerAccountSettlement class.
    """

    __tablename__ = "ledger_account_settlement"  # type: ignore
