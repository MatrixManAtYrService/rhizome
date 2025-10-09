"""
SQLModel definition for the cycle_validation_mutation table, version 1.

This module provides the V1 implementation of the CycleValidationMutation model.
"""

from __future__ import annotations

from .cycle_validation_mutation import CycleValidationMutation


class CycleValidationMutationV1(CycleValidationMutation, table=True):
    """
    Version 1 of the CycleValidationMutation model.

    Currently a name-only inheritance from the base CycleValidationMutation class.
    """

    __tablename__ = "cycle_validation_mutation"  # type: ignore
