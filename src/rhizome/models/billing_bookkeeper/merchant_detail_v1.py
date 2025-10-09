"""
SQLModel definition for the merchant_detail table, version 1.

This module provides the V1 implementation of the MerchantDetail model.
"""

from __future__ import annotations

from .merchant_detail import MerchantDetail


class MerchantDetailV1(MerchantDetail, table=True):
    """
    Version 1 of the MerchantDetail model.

    Currently a name-only inheritance from the base MerchantDetail class.
    """

    __tablename__ = "merchant_detail"  # type: ignore
