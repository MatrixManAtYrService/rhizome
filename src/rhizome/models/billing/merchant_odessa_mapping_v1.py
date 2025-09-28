"""
SQLModel definition for the merchant_odessa_mapping table, version 1.

This module provides the V1 implementation of the MerchantOdessaMapping model.
Currently, MerchantOdessaMappingV1 is identical to the base MerchantOdessaMapping class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .merchant_odessa_mapping import MerchantOdessaMapping


class MerchantOdessaMappingV1(MerchantOdessaMapping, NaProdSQLModel, table=True):
    """
    Version 1 of the MerchantOdessaMapping model.

    Currently a name-only inheritance from the base MerchantOdessaMapping class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "merchant_odessa_mapping"  # type: ignore
