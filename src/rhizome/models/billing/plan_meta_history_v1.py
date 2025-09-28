"""
SQLModel definition for the plan_meta_history table, version 1.

This module provides the V1 implementation of the PlanMetaHistory model.
Currently, PlanMetaHistoryV1 is identical to the base PlanMetaHistory class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .plan_meta_history import PlanMetaHistory


class PlanMetaHistoryV1(PlanMetaHistory, NaProdSQLModel, table=True):
    """
    Version 1 of the PlanMetaHistory model.

    Currently a name-only inheritance from the base PlanMetaHistory class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "plan_meta_history"  # type: ignore
