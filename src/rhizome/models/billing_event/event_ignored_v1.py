"""
SQLModel definition for the event_ignored table, version 1.

This module provides the V1 implementation of the EventIgnored model.
Currently, EventIgnoredV1 is identical to the base EventIgnored class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .event_ignored import EventIgnored


class EventIgnoredV1(EventIgnored, table=True):
    """
    Version 1 of the EventIgnored model.

    Currently a name-only inheritance from the base EventIgnored class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "event_ignored"  # type: ignore