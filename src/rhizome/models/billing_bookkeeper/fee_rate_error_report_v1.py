"""
SQLModel definition for the fee_rate_error_report table, version 1.

This module provides the V1 implementation of the FeeRateErrorReport model.
"""

from __future__ import annotations

from .fee_rate_error_report import FeeRateErrorReport


class FeeRateErrorReportV1(FeeRateErrorReport, table=True):
    """
    Version 1 of the FeeRateErrorReport model.

    Currently a name-only inheritance from the base FeeRateErrorReport class.
    """

    __tablename__ = "fee_rate_error_report"  # type: ignore
