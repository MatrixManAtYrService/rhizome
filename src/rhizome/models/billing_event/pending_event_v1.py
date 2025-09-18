"""
SQLModel definition for the pending_event table, version 1.

This module provides the V1 implementation of the PendingEvent model.
Currently, PendingEventV1 is identical to the base PendingEvent class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .pending_event import PendingEvent


class PendingEventV1(PendingEvent, table=True):
    """
    Version 1 of the PendingEvent model.

    Currently a name-only inheritance from the base PendingEvent class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "pending_event"  # type: ignore