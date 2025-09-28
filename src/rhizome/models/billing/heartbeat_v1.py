"""
SQLModel definition for the heartbeat table, version 1.

This module provides the V1 implementation of the Heartbeat model.
Currently, HeartbeatV1 is identical to the base Heartbeat class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .heartbeat import Heartbeat


class HeartbeatV1(Heartbeat, NaProdSQLModel, table=True):
    """
    Version 1 of the Heartbeat model.

    Currently a name-only inheritance from the base Heartbeat class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "heartbeat"  # type: ignore