"""
SQLModel definition for the merchant_app_subscription_history table, version 1.

This module provides the V1 implementation of the MerchantAppSubscriptionHistory model.
Currently, MerchantAppSubscriptionHistoryV1 is identical to the base
MerchantAppSubscriptionHistory class (name-only inheritance), but as the table schema
evolves across environments, future versions (V2, V3, etc.) will contain actual
schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import MetaSQLModel
from .merchant_app_subscription_history import MerchantAppSubscriptionHistory


class MerchantAppSubscriptionHistoryV1(MerchantAppSubscriptionHistory, MetaSQLModel, table=True):
    """
    Version 1 of the MerchantAppSubscriptionHistory model.

    Currently a name-only inheritance from the base MerchantAppSubscriptionHistory class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "merchant_app_subscription_history"  # type: ignore

    def sanitize(self) -> MerchantAppSubscriptionHistoryV1:
        """Return a sanitized copy of this MerchantAppSubscriptionHistoryV1 instance."""
        return MerchantAppSubscriptionHistoryV1(
            created_time=self.created_time,
            id=self.id,
            merchant_app_id=self.merchant_app_id,
            old_app_subscription_id=self.old_app_subscription_id,
        )
