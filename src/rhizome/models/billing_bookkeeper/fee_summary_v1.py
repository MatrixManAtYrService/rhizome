"""
SQLModel definition for the fee_summary table, version 1.

This module provides the V1 implementation of the FeeSummary model.
Currently, FeeSummaryV1 is identical to the base FeeSummary class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .fee_summary import FeeSummary


class FeeSummaryV1(FeeSummary, table=True):
    """
    Version 1 of the FeeSummary model.
    
    Currently a name-only inheritance from the base FeeSummary class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """
    
    __tablename__ = "fee_summary"  # type: ignore