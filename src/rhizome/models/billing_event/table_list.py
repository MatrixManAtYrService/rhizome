"""
Table list for billing_event database.

This module defines all tables tracked in the billing_event database
across different environments and versions.
"""

from __future__ import annotations

from enum import StrEnum, auto


class BillingEventTable(StrEnum):
    """Table identifiers for billing_event database."""

    app_metered_event = auto()
    app_subscription_event = auto()
