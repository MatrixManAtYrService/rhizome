"""
Table list for billing database.

This module defines all tables tracked in the billing database
across different environments and versions.
"""

from __future__ import annotations

from enum import StrEnum, auto


class BillingTable(StrEnum):
    """Table identifiers for billing database."""

    stage_charge = auto()
