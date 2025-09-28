"""
SQLModel definition for the stage_email table, version 1.

This module provides the V1 implementation of the StageEmail model.
Currently, StageEmailV1 is identical to the base StageEmail class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .stage_email import StageEmail


class StageEmailV1(StageEmail, NaProdSQLModel, table=True):
    """
    Version 1 of the StageEmail model.

    Currently a name-only inheritance from the base StageEmail class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "stage_email"  # type: ignore
