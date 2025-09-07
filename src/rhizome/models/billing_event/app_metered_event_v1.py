"""
SQLModel definition for the app_metered_event table, version 1.

This module provides the V1 implementation of the AppMeteredEvent model.
Currently, AppMeteredEventV1 is identical to the base AppMeteredEvent class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .app_metered_event import AppMeteredEvent


class AppMeteredEventV1(AppMeteredEvent, table=True):
    """
    Version 1 of the AppMeteredEvent model.
    
    Currently a name-only inheritance from the base AppMeteredEvent class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """
    
    __tablename__ = "app_metered_event"  # type: ignore