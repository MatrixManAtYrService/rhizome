"""
SQLModel definition for the as_of_merchant table, version 1.

This module provides the V1 implementation of the AsOfMerchant model.
V1 is the base version used in na_prod environment without the request_uuid field.
"""

from __future__ import annotations

from ...sanitize_helpers import sanitize_uuid_field
from ..metadata_registry import NaProdSQLModel
from .as_of_merchant import AsOfMerchant


class AsOfMerchantV1(AsOfMerchant, NaProdSQLModel, table=True):
    """
    Version 1 of the AsOfMerchant model.

    This version includes only the base fields and is used in environments
    that don't have the request_uuid field (like na_prod).
    """

    __tablename__ = "as_of_merchant"  # type: ignore

    def sanitize(self) -> AsOfMerchantV1:
        """Return a sanitized copy of this AsOfMerchantV1 instance."""
        return AsOfMerchantV1(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            merchant_uuid=sanitize_uuid_field(self.merchant_uuid, 13),  # type: ignore
            as_of_timestamp=self.as_of_timestamp,
            event_datetime=self.event_datetime,
            billing_event_uuid=sanitize_uuid_field(self.billing_event_uuid, 26),
            created_timestamp=self.created_timestamp,
        )