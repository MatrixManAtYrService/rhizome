"""
Table lists for all rhizome databases.

This module defines all tables tracked across different databases
and environments in rhizome.
"""

from __future__ import annotations

from enum import StrEnum, auto


class BillingTable(StrEnum):
    """Table identifiers for billing database."""

    stage_charge = auto()


class BillingBookkeeperTable(StrEnum):
    """Table identifiers for billing_bookkeeper database."""

    fee_summary = auto()
    settlement = auto()


class BillingEventTable(StrEnum):
    """Table identifiers for billing_event database."""

    app_metered_event = auto()
    app_subscription_event = auto()
