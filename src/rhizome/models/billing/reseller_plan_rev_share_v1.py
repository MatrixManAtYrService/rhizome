"""
SQLModel definition for the reseller_plan_rev_share table, version 1.

This module provides the V1 implementation of the ResellerPlanRevShare model.
Currently, ResellerPlanRevShareV1 is identical to the base ResellerPlanRevShare class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .reseller_plan_rev_share import ResellerPlanRevShare


class ResellerPlanRevShareV1(ResellerPlanRevShare, NaProdSQLModel, table=True):
    """
    Version 1 of the ResellerPlanRevShare model.

    Currently a name-only inheritance from the base ResellerPlanRevShare class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "reseller_plan_rev_share"  # type: ignore
