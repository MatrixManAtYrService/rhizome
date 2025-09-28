"""
SQLModel definition for the stage_app_metered_event table, version 1.

This module provides the V1 implementation of the StageAppMeteredEvent model.
Currently, StageAppMeteredEventV1 is identical to the base StageAppMeteredEvent class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .stage_app_metered_event import StageAppMeteredEvent


class StageAppMeteredEventV1(StageAppMeteredEvent, NaProdSQLModel, table=True):
    """
    Version 1 of the StageAppMeteredEvent model.

    Currently a name-only inheritance from the base StageAppMeteredEvent class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "stage_app_metered_event"  # type: ignore
