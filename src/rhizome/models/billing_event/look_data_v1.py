"""
SQLModel definition for the look_data table, version 1.

This module provides the V1 implementation of the LookData model.
Currently, LookDataV1 is identical to the base LookData class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .look_data import LookData


class LookDataV1(LookData, table=True):
    """
    Version 1 of the LookData model.

    Currently a name-only inheritance from the base LookData class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "look_data"  # type: ignore
    __table_args__ = {"extend_existing": True}  # type: ignore
