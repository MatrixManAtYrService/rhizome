"""
SQLModel definition for the billing_pseudo_entity table, version 1.

This module provides the V1 implementation of the BillingPseudoEntity model.
"""

from __future__ import annotations

from .billing_pseudo_entity import BillingPseudoEntity


class BillingPseudoEntityV1(BillingPseudoEntity, table=True):
    """
    Version 1 of the BillingPseudoEntity model.

    Currently a name-only inheritance from the base BillingPseudoEntity class.
    """

    __tablename__ = "billing_pseudo_entity"  # type: ignore
