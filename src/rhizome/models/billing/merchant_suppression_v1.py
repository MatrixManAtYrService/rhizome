"""
SQLModel definition for the merchant_suppression table, version 1.

This module provides the V1 implementation of the MerchantSuppression model.
Currently, MerchantSuppressionV1 is identical to the base MerchantSuppression class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .merchant_suppression import MerchantSuppression


class MerchantSuppressionV1(MerchantSuppression, NaProdSQLModel, table=True):
    """
    Version 1 of the MerchantSuppression model.

    Currently a name-only inheritance from the base MerchantSuppression class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "merchant_suppression"  # type: ignore
