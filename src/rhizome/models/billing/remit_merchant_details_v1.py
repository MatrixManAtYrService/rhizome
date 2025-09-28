"""
SQLModel definition for the remit_merchant_details table, version 1.

This module provides the V1 implementation of the RemitMerchantDetails model.
Currently, RemitMerchantDetailsV1 is identical to the base RemitMerchantDetails class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .remit_merchant_details import RemitMerchantDetails


class RemitMerchantDetailsV1(RemitMerchantDetails, NaProdSQLModel, table=True):
    """
    Version 1 of the RemitMerchantDetails model.

    Currently a name-only inheritance from the base RemitMerchantDetails class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "remit_merchant_details"  # type: ignore
