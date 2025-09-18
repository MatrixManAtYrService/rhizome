"""
SQLModel definition for the as_of_merchant table, version 1.

This module provides the V1 implementation of the AsOfMerchant model.
Currently, AsOfMerchantV1 is identical to the base AsOfMerchant class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .as_of_merchant import AsOfMerchant


class AsOfMerchantV1(AsOfMerchant, table=True):
    """
    Version 1 of the AsOfMerchant model.

    Currently a name-only inheritance from the base AsOfMerchant class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "as_of_merchant"  # type: ignore