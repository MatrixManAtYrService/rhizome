"""
SQLModel definition for the seasonal_merchant_trans_audit table, version 1.

This module provides the V1 implementation of the SeasonalMerchantTransAudit model.
Currently, SeasonalMerchantTransAuditV1 is identical to the base
SeasonalMerchantTransAudit class (name-only inheritance), but as the table schema
evolves across environments, future versions (V2, V3, etc.) will contain actual
schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .seasonal_merchant_trans_audit import SeasonalMerchantTransAudit


class SeasonalMerchantTransAuditV1(SeasonalMerchantTransAudit, NaProdSQLModel, table=True):
    """
    Version 1 of the SeasonalMerchantTransAudit model.

    Currently a name-only inheritance from the base SeasonalMerchantTransAudit class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "seasonal_merchant_trans_audit"  # type: ignore
