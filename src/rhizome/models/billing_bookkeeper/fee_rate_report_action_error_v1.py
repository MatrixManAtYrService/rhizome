"""
SQLModel definition for the fee_rate_report_action_error table, version 1.

This module provides the V1 implementation of the FeeRateReportActionError model.
"""

from __future__ import annotations

from .fee_rate_report_action_error import FeeRateReportActionError


class FeeRateReportActionErrorV1(FeeRateReportActionError, table=True):
    """
    Version 1 of the FeeRateReportActionError model.

    Currently a name-only inheritance from the base FeeRateReportActionError class.
    """

    __tablename__ = "fee_rate_report_action_error"  # type: ignore
