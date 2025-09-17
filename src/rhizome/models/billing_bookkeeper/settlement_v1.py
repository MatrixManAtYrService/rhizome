"""
SQLModel definition for the settlement table, version 1.

This module provides the V1 implementation of the Settlement model.
Currently, SettlementV1 is identical to the base Settlement class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .settlement import Settlement


class SettlementV1(Settlement, table=True):
    """
    Version 1 of the Settlement model.

    Currently a name-only inheritance from the base Settlement class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "settlement"  # type: ignore
