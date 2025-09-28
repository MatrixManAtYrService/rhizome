"""
SQLModel definition for the biie_file_def table, version 1.

This module provides the V1 implementation of the BiieFileDef model.
Currently, BiieFileDefV1 is identical to the base BiieFileDef class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .biie_file_def import BiieFileDef


class BiieFileDefV1(BiieFileDef, NaProdSQLModel, table=True):
    """
    Version 1 of the BiieFileDef model.

    Currently a name-only inheritance from the base BiieFileDef class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "biie_file_def"  # type: ignore
