"""
SQLModel definition for the fee_tax table, version 1.

This module provides the V1 implementation of the FeeTax model.
"""

from __future__ import annotations

from .fee_tax import FeeTax


class FeeTaxV1(FeeTax, table=True):
    """
    Version 1 of the FeeTax model.

    Currently a name-only inheritance from the base FeeTax class.
    """

    __tablename__ = "fee_tax"  # type: ignore
