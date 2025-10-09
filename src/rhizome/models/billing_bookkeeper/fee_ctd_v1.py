"""
SQLModel definition for the fee_ctd table, version 1.

This module provides the V1 implementation of the FeeCtd model.
"""

from __future__ import annotations

from .fee_ctd import FeeCtd


class FeeCtdV1(FeeCtd, table=True):
    """
    Version 1 of the FeeCtd model.

    Currently a name-only inheritance from the base FeeCtd class.
    """

    __tablename__ = "fee_ctd"  # type: ignore
