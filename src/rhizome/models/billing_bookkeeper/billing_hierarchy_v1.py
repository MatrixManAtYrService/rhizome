"""
SQLModel definition for the billing_hierarchy table, version 1.

This module provides the V1 implementation of the BillingHierarchy model.
"""

from __future__ import annotations

from .billing_hierarchy import BillingHierarchy


class BillingHierarchyV1(BillingHierarchy, table=True):
    """
    Version 1 of the BillingHierarchy model.

    Currently a name-only inheritance from the base BillingHierarchy class.
    """

    __tablename__ = "billing_hierarchy"  # type: ignore
