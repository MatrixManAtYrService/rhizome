"""
SQLModel definition for the merchant_queue_sensitive table, version 1.

This module provides the V1 implementation of the MerchantQueueSensitive model.
Currently, MerchantQueueSensitiveV1 is identical to the base MerchantQueueSensitive class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .merchant_queue_sensitive import MerchantQueueSensitive


class MerchantQueueSensitiveV1(MerchantQueueSensitive, NaProdSQLModel, table=True):
    """
    Version 1 of the MerchantQueueSensitive model.

    Currently a name-only inheritance from the base MerchantQueueSensitive class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "merchant_queue_sensitive"  # type: ignore
