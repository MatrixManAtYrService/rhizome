"""
SQLModel definition for the corollary_data table, version 1.

This module provides the V1 implementation of the CorollaryData model.
Currently, CorollaryDataV1 is identical to the base CorollaryData class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .corollary_data import CorollaryData


class CorollaryDataV1(CorollaryData, NaProdSQLModel, table=True):
    """
    Version 1 of the CorollaryData model.

    Currently a name-only inheritance from the base CorollaryData class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "corollary_data"  # type: ignore
