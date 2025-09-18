"""
SQLModel definition for the event_filter table, version 1.

This module provides the V1 implementation of the EventFilter model.
Currently, EventFilterV1 is identical to the base EventFilter class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .event_filter import EventFilter


class EventFilterV1(EventFilter, table=True):
    """
    Version 1 of the EventFilter model.

    Currently a name-only inheritance from the base EventFilter class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "event_filter"  # type: ignore