"""
SQLModel definition for the processing_group_dates table, version 1.

This module provides the V1 implementation of the ProcessingGroupDates model.
"""

from __future__ import annotations

from .processing_group_dates import ProcessingGroupDates


class ProcessingGroupDatesV1(ProcessingGroupDates, table=True):
    """
    Version 1 of the ProcessingGroupDates model.

    Currently a name-only inheritance from the base ProcessingGroupDates class.
    """

    __tablename__ = "processing_group_dates"  # type: ignore
