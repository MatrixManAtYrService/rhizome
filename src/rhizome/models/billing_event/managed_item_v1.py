"""
SQLModel definition for the managed_item table, version 1.

This module provides the V1 implementation of the ManagedItem model.
Currently, ManagedItemV1 is identical to the base ManagedItem class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .managed_item import ManagedItem


class ManagedItemV1(ManagedItem, table=True):
    """
    Version 1 of the ManagedItem model.

    Currently a name-only inheritance from the base ManagedItem class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "managed_item"  # type: ignore