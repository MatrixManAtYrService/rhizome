"""
SQLModel definition for the fee_tax_mutation table, version 1.

This module provides the V1 implementation of the FeeTaxMutation model.
"""

from __future__ import annotations

from .fee_tax_mutation import FeeTaxMutation


class FeeTaxMutationV1(FeeTaxMutation, table=True):
    """
    Version 1 of the FeeTaxMutation model.

    Currently a name-only inheritance from the base FeeTaxMutation class.
    """

    __tablename__ = "fee_tax_mutation"  # type: ignore
