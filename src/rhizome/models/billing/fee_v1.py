"""
SQLModel definition for the fee table, version 1.

This module provides the V1 implementation of the Fee model.
Currently, FeeV1 is identical to the base Fee class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .fee import Fee


class FeeV1(Fee, NaProdSQLModel, table=True):
    """
    Version 1 of the Fee model.

    Currently a name-only inheritance from the base Fee class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "fee"  # type: ignore
