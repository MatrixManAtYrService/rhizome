"""
SQLModel definition for the billing_hierarchy_type table, version 1.

This module provides the V1 implementation of the BillingHierarchyType model.
"""

from __future__ import annotations

from .billing_hierarchy_type import BillingHierarchyType


class BillingHierarchyTypeV1(BillingHierarchyType, table=True):
    """
    Version 1 of the BillingHierarchyType model.

    Currently a name-only inheritance from the base BillingHierarchyType class.
    """

    __tablename__ = "billing_hierarchy_type"  # type: ignore
