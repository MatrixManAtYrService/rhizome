"""
SQLModel definition for the merchant_suppression_by_app table, version 1.

This module provides the V1 implementation of the MerchantSuppressionByApp model.
Currently, MerchantSuppressionByAppV1 is identical to the base MerchantSuppressionByApp class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .merchant_suppression_by_app import MerchantSuppressionByApp


class MerchantSuppressionByAppV1(MerchantSuppressionByApp, NaProdSQLModel, table=True):
    """
    Version 1 of the MerchantSuppressionByApp model.

    Currently a name-only inheritance from the base MerchantSuppressionByApp class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "merchant_suppression_by_app"  # type: ignore
