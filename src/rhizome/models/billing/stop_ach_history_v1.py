"""
SQLModel definition for the stop_ach_history table, version 1.

This module provides the V1 implementation of the StopAchHistory model.
Currently, StopAchHistoryV1 is identical to the base StopAchHistory class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .stop_ach_history import StopAchHistory


class StopAchHistoryV1(StopAchHistory, NaProdSQLModel, table=True):
    """
    Version 1 of the StopAchHistory model.

    Currently a name-only inheritance from the base StopAchHistory class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "stop_ach_history"  # type: ignore
