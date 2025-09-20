"""
SQLModel definition for the merchant_payment table, version 1.

This module provides the V1 implementation of the MerchantPayment model.
Currently, MerchantPaymentV1 is identical to the base MerchantPayment class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .merchant_payment import MerchantPayment


class MerchantPaymentV1(MerchantPayment, table=True):
    """
    Version 1 of the MerchantPayment model.

    Currently a name-only inheritance from the base MerchantPayment class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "merchant_payment"  # type: ignore
