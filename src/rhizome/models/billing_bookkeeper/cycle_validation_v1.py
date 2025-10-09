"""
SQLModel definition for the cycle_validation table, version 1.

This module provides the V1 implementation of the CycleValidation model.
"""

from __future__ import annotations

from .cycle_validation import CycleValidation


class CycleValidationV1(CycleValidation, table=True):
    """
    Version 1 of the CycleValidation model.

    Currently a name-only inheritance from the base CycleValidation class.
    """

    __tablename__ = "cycle_validation"  # type: ignore
