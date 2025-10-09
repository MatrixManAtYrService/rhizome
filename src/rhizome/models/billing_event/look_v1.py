"""
SQLModel definition for the look table, version 1.

This module provides the V1 implementation of the Look model.
Currently, LookV1 is identical to the base Look class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .look import Look


class LookV1(Look, table=True):
    """
    Version 1 of the Look model.

    Currently a name-only inheritance from the base Look class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "look"  # type: ignore
    __table_args__ = {"extend_existing": True}  # type: ignore
