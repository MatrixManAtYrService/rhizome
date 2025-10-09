"""
SQLModel definition for the billing_schedule table, version 1.

This module provides the V1 implementation of the BillingSchedule model.
"""

from __future__ import annotations

from .billing_schedule import BillingSchedule


class BillingScheduleV1(BillingSchedule, table=True):
    """
    Version 1 of the BillingSchedule model.

    Currently a name-only inheritance from the base BillingSchedule class.
    """

    __tablename__ = "billing_schedule"  # type: ignore
