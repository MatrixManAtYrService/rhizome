"""
SQLModel definition for the tiered_pricing table, version 1.

This module provides the V1 implementation of the TieredPricing model.
"""

from __future__ import annotations

from .tiered_pricing import TieredPricing


class TieredPricingV1(TieredPricing, table=True):
    """
    Version 1 of the TieredPricing model.

    Currently a name-only inheritance from the base TieredPricing class.
    """

    __tablename__ = "tiered_pricing"  # type: ignore
