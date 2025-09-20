"""
SQLModel definition for the as_of_merchant_device table, version 1.

This module provides the V1 implementation of the AsOfMerchantDevice model.
Currently, AsOfMerchantDeviceV1 is identical to the base AsOfMerchantDevice class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .as_of_merchant_device import AsOfMerchantDevice


class AsOfMerchantDeviceV1(AsOfMerchantDevice, table=True):
    """
    Version 1 of the AsOfMerchantDevice model.

    Currently a name-only inheritance from the base AsOfMerchantDevice class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "as_of_merchant_device"  # type: ignore
