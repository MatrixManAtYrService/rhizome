"""
SQLModel definition for the fee_ytd table, version 1.

This module provides the V1 implementation of the FeeYtd model.
"""

from __future__ import annotations

from .fee_ytd import FeeYtd


class FeeYtdV1(FeeYtd, table=True):
    """
    Version 1 of the FeeYtd model.

    Currently a name-only inheritance from the base FeeYtd class.
    """

    __tablename__ = "fee_ytd"  # type: ignore
