"""
SQLModel definition for the prototype_fee_set table, version 1.

This module provides the V1 implementation of the PrototypeFeeSet model.
"""

from __future__ import annotations

from .prototype_fee_set import PrototypeFeeSet


class PrototypeFeeSetV1(PrototypeFeeSet, table=True):
    """
    Version 1 of the PrototypeFeeSet model.

    Currently a name-only inheritance from the base PrototypeFeeSet class.
    """

    __tablename__ = "prototype_fee_set"  # type: ignore
