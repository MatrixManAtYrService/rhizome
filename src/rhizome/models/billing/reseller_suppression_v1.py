"""
SQLModel definition for the reseller_suppression table, version 1.

This module provides the V1 implementation of the ResellerSuppression model.
Currently, ResellerSuppressionV1 is identical to the base ResellerSuppression class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .reseller_suppression import ResellerSuppression


class ResellerSuppressionV1(ResellerSuppression, NaProdSQLModel, table=True):
    """
    Version 1 of the ResellerSuppression model.

    Currently a name-only inheritance from the base ResellerSuppression class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "reseller_suppression"  # type: ignore
