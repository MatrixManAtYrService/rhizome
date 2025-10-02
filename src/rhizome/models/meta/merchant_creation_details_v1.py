"""
SQLModel definition for the merchant_creation_details table, version 1.

This module provides the V1 implementation of the MerchantCreationDetails model.
Currently, MerchantCreationDetailsV1 is identical to the base MerchantCreationDetails class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import MetaSQLModel
from .merchant_creation_details import MerchantCreationDetails


class MerchantCreationDetailsV1(MerchantCreationDetails, MetaSQLModel, table=True):
    """
    Version 1 of the MerchantCreationDetails model.

    Currently a name-only inheritance from the base MerchantCreationDetails class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "merchant_creation_details"  # type: ignore

    def sanitize(self) -> MerchantCreationDetailsV1:
        """Return a sanitized copy of this MerchantCreationDetailsV1 instance."""
        return MerchantCreationDetailsV1(
            created_time=self.created_time,
            creation_source=self.creation_source,
            id=self.id,
            merchant_id=self.merchant_id,
            modified_time=self.modified_time,
            pre_create=self.pre_create,
            pre_source=self.pre_source,
            source_identifier=self.source_identifier,
        )
