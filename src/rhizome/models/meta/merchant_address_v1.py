"""
SQLModel definition for the merchant_address table, version 1.

This module provides the V1 implementation of the MerchantAddress model.
Currently, MerchantAddressV1 is identical to the base MerchantAddress class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import MetaSQLModel
from .merchant_address import MerchantAddress


class MerchantAddressV1(MerchantAddress, MetaSQLModel, table=True):
    """
    Version 1 of the MerchantAddress model.

    Currently a name-only inheritance from the base MerchantAddress class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "merchant_address"  # type: ignore

    def sanitize(self) -> MerchantAddressV1:
        """Return a sanitized copy of this MerchantAddressV1 instance."""
        return MerchantAddressV1(
            id=self.id,
            address_1=self.address_1,
            address_2=self.address_2,
            address_3=self.address_3,
            city=self.city,
            state=self.state,
            zip=self.zip,
            country=self.country,
            phone_number=self.phone_number,
            latitude=self.latitude,
            longitude=self.longitude,
            created_time=self.created_time,
            modified_time=self.modified_time,
        )