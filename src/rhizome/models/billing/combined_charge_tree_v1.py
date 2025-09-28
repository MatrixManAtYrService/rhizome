"""
SQLModel definition for the combined_charge_tree table, version 1.

This module provides the V1 implementation of the CombinedChargeTree model.
Currently, CombinedChargeTreeV1 is identical to the base CombinedChargeTree class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .combined_charge_tree import CombinedChargeTree


class CombinedChargeTreeV1(CombinedChargeTree, NaProdSQLModel, table=True):
    """
    Version 1 of the CombinedChargeTree model.

    Currently a name-only inheritance from the base CombinedChargeTree class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "combined_charge_tree"  # type: ignore
