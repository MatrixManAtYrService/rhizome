"""
SQLModel definition for the reseller_plan_fee table, version 1.

This module provides the V1 implementation of the ResellerPlanFee model.
Currently, ResellerPlanFeeV1 is identical to the base ResellerPlanFee class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .reseller_plan_fee import ResellerPlanFee


class ResellerPlanFeeV1(ResellerPlanFee, NaProdSQLModel, table=True):
    """
    Version 1 of the ResellerPlanFee model.

    Currently a name-only inheritance from the base ResellerPlanFee class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "reseller_plan_fee"  # type: ignore
