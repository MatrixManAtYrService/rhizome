"""
SQLModel definition for the uninstalled_app table, version 1.

This module provides the V1 implementation of the UninstalledApp model.
Currently, UninstalledAppV1 is identical to the base UninstalledApp class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .uninstalled_app import UninstalledApp


class UninstalledAppV1(UninstalledApp, table=True):
    """
    Version 1 of the UninstalledApp model.

    Currently a name-only inheritance from the base UninstalledApp class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "uninstalled_app"  # type: ignore