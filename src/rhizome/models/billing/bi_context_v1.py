"""
SQLModel definition for the bi_context table, version 1.

This module provides the V1 implementation of the BiContext model.
Currently, BiContextV1 is identical to the base BiContext class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .bi_context import BiContext


class BiContextV1(BiContext, NaProdSQLModel, table=True):
    """
    Version 1 of the BiContext model.

    Currently a name-only inheritance from the base BiContext class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "bi_context"  # type: ignore
