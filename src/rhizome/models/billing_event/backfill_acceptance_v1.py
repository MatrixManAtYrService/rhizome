"""
SQLModel definition for the backfill_acceptance table, version 1.

This module provides the V1 implementation of the BackfillAcceptance model.
Currently, BackfillAcceptanceV1 is identical to the base BackfillAcceptance class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .backfill_acceptance import BackfillAcceptance


class BackfillAcceptanceV1(BackfillAcceptance, table=True):
    """
    Version 1 of the BackfillAcceptance model.

    Currently a name-only inheritance from the base BackfillAcceptance class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "backfill_acceptance"  # type: ignore
