"""
SQLModel definition for the fee_rate table, version 1.
"""

from __future__ import annotations

from .fee_rate import FeeRate


class FeeRateV1(FeeRate, table=True):
    """Version 1 of the FeeRate model."""

    __tablename__ = "fee_rate"  # type: ignore
