"""
SQLModel definition for the stage_charge_history table, version 1.

This module provides the V1 implementation of the StageChargeHistory model.
Currently, StageChargeHistoryV1 is identical to the base StageChargeHistory class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .stage_charge_history import StageChargeHistory


class StageChargeHistoryV1(StageChargeHistory, NaProdSQLModel, table=True):
    """
    Version 1 of the StageChargeHistory model.

    Currently a name-only inheritance from the base StageChargeHistory class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "stage_charge_history"  # type: ignore
