"""
SQLModel definition for the merchant_offboarding table, version 1.

This module provides the V1 implementation of the MerchantOffboarding model.
Currently, MerchantOffboardingV1 is identical to the base MerchantOffboarding class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .merchant_offboarding import MerchantOffboarding


class MerchantOffboardingV1(MerchantOffboarding, table=True):
    """
    Version 1 of the MerchantOffboarding model.

    Currently a name-only inheritance from the base MerchantOffboarding class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "merchant_offboarding"  # type: ignore