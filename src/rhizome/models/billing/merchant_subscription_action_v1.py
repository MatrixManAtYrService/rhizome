"""
SQLModel definition for the merchant_subscription_action table, version 1.

This module provides the V1 implementation of the MerchantSubscriptionAction model.
Currently, MerchantSubscriptionActionV1 is identical to the base MerchantSubscriptionAction class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .merchant_subscription_action import MerchantSubscriptionAction


class MerchantSubscriptionActionV1(MerchantSubscriptionAction, NaProdSQLModel, table=True):
    """
    Version 1 of the MerchantSubscriptionAction model.

    Currently a name-only inheritance from the base MerchantSubscriptionAction class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "merchant_subscription_action"  # type: ignore
