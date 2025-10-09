"""
SQLModel definition for the prototype_fee_rate table, version 1.

This module provides the V1 implementation of the PrototypeFeeRate model.
"""

from __future__ import annotations

from .prototype_fee_rate import PrototypeFeeRate


class PrototypeFeeRateV1(PrototypeFeeRate, table=True):
    """
    Version 1 of the PrototypeFeeRate model.

    Currently a name-only inheritance from the base PrototypeFeeRate class.
    """

    __tablename__ = "prototype_fee_rate"  # type: ignore
