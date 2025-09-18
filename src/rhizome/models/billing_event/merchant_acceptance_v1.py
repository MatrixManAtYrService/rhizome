"""
SQLModel definition for the merchant_acceptance table, version 1.

This module provides the V1 implementation of the MerchantAcceptance model.
Currently, MerchantAcceptanceV1 is identical to the base MerchantAcceptance class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .merchant_acceptance import MerchantAcceptance


class MerchantAcceptanceV1(MerchantAcceptance, table=True):
    """
    Version 1 of the MerchantAcceptance model.

    Currently a name-only inheritance from the base MerchantAcceptance class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "merchant_acceptance"  # type: ignore