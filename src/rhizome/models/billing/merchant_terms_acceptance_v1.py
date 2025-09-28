"""
SQLModel definition for the merchant_terms_acceptance table, version 1.

This module provides the V1 implementation of the MerchantTermsAcceptance model.
Currently, MerchantTermsAcceptanceV1 is identical to the base MerchantTermsAcceptance class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .merchant_terms_acceptance import MerchantTermsAcceptance


class MerchantTermsAcceptanceV1(MerchantTermsAcceptance, NaProdSQLModel, table=True):
    """
    Version 1 of the MerchantTermsAcceptance model.

    Currently a name-only inheritance from the base MerchantTermsAcceptance class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "merchant_terms_acceptance"  # type: ignore
