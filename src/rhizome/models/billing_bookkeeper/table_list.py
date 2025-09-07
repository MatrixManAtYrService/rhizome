"""
Table list for billing_bookkeeper database.

This module defines all tables tracked in the billing_bookkeeper database
across different environments and versions.
"""

from __future__ import annotations

from enum import StrEnum, auto


# Table identifiers for billing_bookkeeper database
class BillingBookkeeperTable(StrEnum):
    fee_summary = auto()
    settlement = auto()
