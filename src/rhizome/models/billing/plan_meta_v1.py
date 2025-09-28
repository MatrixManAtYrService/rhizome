"""
SQLModel definition for the plan_meta table, version 1.

This module provides the V1 implementation of the PlanMeta model.
Currently, PlanMetaV1 is identical to the base PlanMeta class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .plan_meta import PlanMeta


class PlanMetaV1(PlanMeta, NaProdSQLModel, table=True):
    """
    Version 1 of the PlanMeta model.

    Currently a name-only inheritance from the base PlanMeta class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "plan_meta"  # type: ignore
