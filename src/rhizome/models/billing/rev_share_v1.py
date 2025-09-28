"""
SQLModel definition for the rev_share table, version 1.

This module provides the V1 implementation of the RevShare model.
Currently, RevShareV1 is identical to the base RevShare class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .rev_share import RevShare


class RevShareV1(RevShare, NaProdSQLModel, table=True):
    """
    Version 1 of the RevShare model.

    Currently a name-only inheritance from the base RevShare class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "rev_share"  # type: ignore
