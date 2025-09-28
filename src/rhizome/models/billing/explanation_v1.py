"""
SQLModel definition for the explanation table, version 1.

This module provides the V1 implementation of the Explanation model.
Currently, ExplanationV1 is identical to the base Explanation class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .explanation import Explanation


class ExplanationV1(Explanation, NaProdSQLModel, table=True):
    """
    Version 1 of the Explanation model.

    Currently a name-only inheritance from the base Explanation class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "explanation"  # type: ignore
