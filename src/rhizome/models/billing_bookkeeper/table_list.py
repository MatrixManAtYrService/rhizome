"""
Table list for billing_bookkeeper database.

This module defines all tables tracked in the billing_bookkeeper database
across different environments and versions.
"""

from __future__ import annotations

from enum import StrEnum, auto


# Table identifiers for billing_bookkeeper database
class BillingBookkeeperTable(StrEnum):
    billing_entity = auto()
    fee_rate = auto()
    fee_summary = auto()
    invoice_info = auto()
    settlement = auto()
