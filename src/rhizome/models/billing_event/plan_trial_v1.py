"""
SQLModel definition for the plan_trial table, version 1.

This module provides the V1 implementation of the PlanTrial model.
Currently, PlanTrialV1 is identical to the base PlanTrial class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .plan_trial import PlanTrial


class PlanTrialV1(PlanTrial, table=True):
    """
    Version 1 of the PlanTrial model.

    Currently a name-only inheritance from the base PlanTrial class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "plan_trial"  # type: ignore
