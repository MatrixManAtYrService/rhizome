"""
SQLModel definition for the merchant_terms_missing_acceptance table, version 1.

This module provides the V1 implementation of the MerchantTermsMissingAcceptance model.
Currently, MerchantTermsMissingAcceptanceV1 is identical to the base MerchantTermsMissingAcceptance class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .merchant_terms_missing_acceptance import MerchantTermsMissingAcceptance


class MerchantTermsMissingAcceptanceV1(MerchantTermsMissingAcceptance, NaProdSQLModel, table=True):
    """
    Version 1 of the MerchantTermsMissingAcceptance model.

    Currently a name-only inheritance from the base MerchantTermsMissingAcceptance class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "merchant_terms_missing_acceptance"  # type: ignore
