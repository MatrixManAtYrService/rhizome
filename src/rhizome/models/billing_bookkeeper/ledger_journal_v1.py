"""
SQLModel definition for the ledger_journal table, version 1.

This module provides the V1 implementation of the LedgerJournal model.
"""

from __future__ import annotations

from .ledger_journal import LedgerJournal


class LedgerJournalV1(LedgerJournal, table=True):
    """
    Version 1 of the LedgerJournal model.

    Currently a name-only inheritance from the base LedgerJournal class.
    """

    __tablename__ = "ledger_journal"  # type: ignore
