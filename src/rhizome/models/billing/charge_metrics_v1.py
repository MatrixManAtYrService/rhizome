"""
SQLModel definition for the charge_metrics table, version 1.

This module provides the V1 implementation of the ChargeMetrics model.
Currently, ChargeMetricsV1 is identical to the base ChargeMetrics class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .charge_metrics import ChargeMetrics


class ChargeMetricsV1(ChargeMetrics, NaProdSQLModel, table=True):
    """
    Version 1 of the ChargeMetrics model.

    Currently a name-only inheritance from the base ChargeMetrics class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "charge_metrics"  # type: ignore
