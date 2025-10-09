"""
SQLModel definition for the billing_hierarchy_cycle table, version 1.

This module provides the V1 implementation of the BillingHierarchyCycle model.
"""

from __future__ import annotations

from .billing_hierarchy_cycle import BillingHierarchyCycle


class BillingHierarchyCycleV1(BillingHierarchyCycle, table=True):
    """
    Version 1 of the BillingHierarchyCycle model.

    Currently a name-only inheritance from the base BillingHierarchyCycle class.
    """

    __tablename__ = "billing_hierarchy_cycle"  # type: ignore
