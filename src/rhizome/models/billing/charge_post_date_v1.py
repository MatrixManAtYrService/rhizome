"""
SQLModel definition for the charge_post_date table, version 1.

This module provides the V1 implementation of the ChargePostDate model.
Currently, ChargePostDateV1 is identical to the base ChargePostDate class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .charge_post_date import ChargePostDate


class ChargePostDateV1(ChargePostDate, NaProdSQLModel, table=True):
    """
    Version 1 of the ChargePostDate model.

    Currently a name-only inheritance from the base ChargePostDate class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "charge_post_date"  # type: ignore
