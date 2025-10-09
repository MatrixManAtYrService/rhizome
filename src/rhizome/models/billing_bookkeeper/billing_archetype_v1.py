"""
SQLModel definition for the billing_archetype table, version 1.

This module provides the V1 implementation of the BillingArchetype model.
"""

from __future__ import annotations

from .billing_archetype import BillingArchetype


class BillingArchetypeV1(BillingArchetype, table=True):
    """
    Version 1 of the BillingArchetype model.

    Currently a name-only inheritance from the base BillingArchetype class.
    """

    __tablename__ = "billing_archetype"  # type: ignore
