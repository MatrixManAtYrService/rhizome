"""
SQLModel definition for the as_of_merchant table, version 2.

This module provides the V2 implementation of the AsOfMerchant model.
V2 adds the request_uuid field which exists in dev and demo environments
but not in the na_prod environment.
"""

from __future__ import annotations

from sqlmodel import Field

from ...sanitize_helpers import sanitize_uuid_field
from ..metadata_registry import DevDemoSQLModel
from .as_of_merchant import AsOfMerchant


class AsOfMerchantV2(AsOfMerchant, DevDemoSQLModel, table=True):
    """
    Version 2 of the AsOfMerchant model.

    Adds the request_uuid field introduced in newer schema versions.
    This version is used in dev and demo environments.
    """

    __tablename__ = "as_of_merchant"  # type: ignore

    # New field in V2
    request_uuid: str | None = Field(default=None, max_length=26, description="UUID of the request")

    def sanitize(self) -> AsOfMerchantV2:
        """Return a sanitized copy of this AsOfMerchantV2 instance."""
        return AsOfMerchantV2(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            merchant_uuid=sanitize_uuid_field(self.merchant_uuid, 13),  # type: ignore
            as_of_timestamp=self.as_of_timestamp,
            event_datetime=self.event_datetime,
            billing_event_uuid=sanitize_uuid_field(self.billing_event_uuid, 26),
            created_timestamp=self.created_timestamp,
            request_uuid=sanitize_uuid_field(self.request_uuid, 26),
        )