"""
SQLModel definition for the billing_event_history table, version 1.

This module provides the V1 implementation of the BillingEventHistory model.
"""

from __future__ import annotations

from .billing_event_history import BillingEventHistory


class BillingEventHistoryV1(BillingEventHistory, table=True):
    """
    Version 1 of the BillingEventHistory model.

    Currently a name-only inheritance from the base BillingEventHistory class.
    """

    __tablename__ = "billing_event_history"  # type: ignore
    __table_args__ = {"extend_existing": True}  # type: ignore
