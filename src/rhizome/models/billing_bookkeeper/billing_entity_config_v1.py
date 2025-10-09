"""
SQLModel definition for the billing_entity_config table, version 1.

This module provides the V1 implementation of the BillingEntityConfig model.
"""

from __future__ import annotations

from .billing_entity_config import BillingEntityConfig


class BillingEntityConfigV1(BillingEntityConfig, table=True):
    """
    Version 1 of the BillingEntityConfig model.

    Currently a name-only inheritance from the base BillingEntityConfig class.
    """

    __tablename__ = "billing_entity_config"  # type: ignore
