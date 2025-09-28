"""
SQLModel definition for the reseller_usage_job_config table, version 1.

This module provides the V1 implementation of the ResellerUsageJobConfig model.
Currently, ResellerUsageJobConfigV1 is identical to the base ResellerUsageJobConfig class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .reseller_usage_job_config import ResellerUsageJobConfig


class ResellerUsageJobConfigV1(ResellerUsageJobConfig, NaProdSQLModel, table=True):
    """
    Version 1 of the ResellerUsageJobConfig model.

    Currently a name-only inheritance from the base ResellerUsageJobConfig class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "reseller_usage_job_config"  # type: ignore
