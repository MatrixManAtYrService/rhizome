"""
SQLModel definition for the merchant_gateway table, version 1.

This module provides the V1 implementation of the MerchantGateway model.
Currently, MerchantGatewayV1 is identical to the base MerchantGateway class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ...sanitize_helpers import sanitize_uuid_field
from ..metadata_registry import MetaSQLModel
from .merchant_gateway import MerchantGateway


class MerchantGatewayV1(MerchantGateway, MetaSQLModel, table=True):
    """
    Version 1 of the MerchantGateway model.

    Currently a name-only inheritance from the base MerchantGateway class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "merchant_gateway"  # type: ignore

    def sanitize(self) -> MerchantGatewayV1:
        """Return a sanitized copy of this MerchantGatewayV1 instance."""
        return MerchantGatewayV1(
            id=self.id,
            merchant_id=self.merchant_id,
            payment_processor_id=self.payment_processor_id,
            processor_key_id=self.processor_key_id,
            rki_processor_id=self.rki_processor_id,
            partner_uuid=sanitize_uuid_field(self.partner_uuid, 64),
            stan=self.stan,
            config=self.config,
            closing_time=self.closing_time,
            new_batch_close_enabled=self.new_batch_close_enabled,
            modified_time=self.modified_time,
        )