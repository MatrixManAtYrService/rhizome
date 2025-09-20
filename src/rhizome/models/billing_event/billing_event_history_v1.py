"""
SQLModel definition for the billing_event_history table, version 1.

This module provides the V1 implementation of the BillingEventHistory model.
Currently, BillingEventHistoryV1 is identical to the base BillingEventHistory class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .billing_event_history import BillingEventHistory


class BillingEventHistoryV1(BillingEventHistory, table=True):
    """
    Version 1 of the BillingEventHistory model.

    Currently a name-only inheritance from the base BillingEventHistory class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "billing_event_history"  # type: ignore
