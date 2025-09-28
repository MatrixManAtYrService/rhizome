"""
SQLModel definition for the suppression_metrics table, version 1.

This module provides the V1 implementation of the SuppressionMetrics model.
Currently, SuppressionMetricsV1 is identical to the base SuppressionMetrics class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .suppression_metrics import SuppressionMetrics


class SuppressionMetricsV1(SuppressionMetrics, NaProdSQLModel, table=True):
    """
    Version 1 of the SuppressionMetrics model.

    Currently a name-only inheritance from the base SuppressionMetrics class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "suppression_metrics"  # type: ignore
