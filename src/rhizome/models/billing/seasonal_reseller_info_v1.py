"""
SQLModel definition for the seasonal_reseller_info table, version 1.

This module provides the V1 implementation of the SeasonalResellerInfo model.
Currently, SeasonalResellerInfoV1 is identical to the base SeasonalResellerInfo class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .seasonal_reseller_info import SeasonalResellerInfo


class SeasonalResellerInfoV1(SeasonalResellerInfo, NaProdSQLModel, table=True):
    """
    Version 1 of the SeasonalResellerInfo model.

    Currently a name-only inheritance from the base SeasonalResellerInfo class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "seasonal_reseller_info"  # type: ignore
