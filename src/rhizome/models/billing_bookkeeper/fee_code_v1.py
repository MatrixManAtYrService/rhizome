"""
SQLModel definition for the fee_code table, version 1.

This module provides the V1 implementation of the FeeCode model.
"""

from __future__ import annotations

from .fee_code import FeeCode


class FeeCodeV1(FeeCode, table=True):
    """
    Version 1 of the FeeCode model.

    Currently a name-only inheritance from the base FeeCode class.
    """

    __tablename__ = "fee_code"  # type: ignore
