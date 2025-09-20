"""
SQLModel definition for the plan_billing_latest table, version 1.

This module provides the V1 implementation of the PlanBillingLatest model.
Currently, PlanBillingLatestV1 is identical to the base PlanBillingLatest class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .plan_billing_latest import PlanBillingLatest


class PlanBillingLatestV1(PlanBillingLatest, table=True):
    """
    Version 1 of the PlanBillingLatest model.

    Currently a name-only inheritance from the base PlanBillingLatest class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "plan_billing_latest"  # type: ignore
