"""
SQLModel definition for the combined_disbursement_tree table, version 1.

This module provides the V1 implementation of the CombinedDisbursementTree model.
Currently, CombinedDisbursementTreeV1 is identical to the base CombinedDisbursementTree class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .combined_disbursement_tree import CombinedDisbursementTree


class CombinedDisbursementTreeV1(CombinedDisbursementTree, NaProdSQLModel, table=True):
    """
    Version 1 of the CombinedDisbursementTree model.

    Currently a name-only inheritance from the base CombinedDisbursementTree class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "combined_disbursement_tree"  # type: ignore
