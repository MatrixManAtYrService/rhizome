"""
SQLModel definition for the ledger_journal_mutation table, version 1.

This module provides the V1 implementation of the LedgerJournalMutation model.
"""

from __future__ import annotations

from .ledger_journal_mutation import LedgerJournalMutation


class LedgerJournalMutationV1(LedgerJournalMutation, table=True):
    """
    Version 1 of the LedgerJournalMutation model.

    Currently a name-only inheritance from the base LedgerJournalMutation class.
    """

    __tablename__ = "ledger_journal_mutation"  # type: ignore
