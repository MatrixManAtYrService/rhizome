"""
SQLModel definition for the merchant_payment_history table, version 1.

This module provides the V1 implementation of the MerchantPaymentHistory model.
Currently, MerchantPaymentHistoryV1 is identical to the base MerchantPaymentHistory class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .merchant_payment_history import MerchantPaymentHistory


class MerchantPaymentHistoryV1(MerchantPaymentHistory, table=True):
    """
    Version 1 of the MerchantPaymentHistory model.

    Currently a name-only inheritance from the base MerchantPaymentHistory class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "merchant_payment_history"  # type: ignore