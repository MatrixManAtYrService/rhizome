"""
SQLModel definition for the fee_summary_mutation table, version 1.

This module provides the V1 implementation of the FeeSummaryMutation model.
"""

from __future__ import annotations

from .fee_summary_mutation import FeeSummaryMutation


class FeeSummaryMutationV1(FeeSummaryMutation, table=True):
    """
    Version 1 of the FeeSummaryMutation model.

    Currently a name-only inheritance from the base FeeSummaryMutation class.
    """

    __tablename__ = "fee_summary_mutation"  # type: ignore
