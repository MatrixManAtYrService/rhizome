"""
SQLModel definition for the model_fee_summary table, version 1.

This module provides the V1 implementation of the ModelFeeSummary model.
"""

from __future__ import annotations

from .model_fee_summary import ModelFeeSummary


class ModelFeeSummaryV1(ModelFeeSummary, table=True):
    """
    Version 1 of the ModelFeeSummary model.

    Currently a name-only inheritance from the base ModelFeeSummary class.
    """

    __tablename__ = "model_fee_summary"  # type: ignore
