"""
SQLModel definition for the payment_processor table, version 1.

This module provides the V1 implementation of the PaymentProcessor model.
Currently, PaymentProcessorV1 is identical to the base PaymentProcessor class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ...sanitize_helpers import sanitize_uuid_field
from ..metadata_registry import MetaSQLModel
from .payment_processor import PaymentProcessor


class PaymentProcessorV1(PaymentProcessor, MetaSQLModel, table=True):
    """
    Version 1 of the PaymentProcessor model.

    Currently a name-only inheritance from the base PaymentProcessor class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "payment_processor"  # type: ignore

    def sanitize(self) -> PaymentProcessorV1:
        """Return a sanitized copy of this PaymentProcessorV1 instance."""
        return PaymentProcessorV1(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),
            name=self.name,
            payment_gateway_api=self.payment_gateway_api,
            production=self.production,
            config=self.config,
            modified_time=self.modified_time,
        )
