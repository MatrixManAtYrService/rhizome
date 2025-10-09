"""
SQLModel definition for the consumer_failure_history table, version 1.

This module provides the V1 implementation of the ConsumerFailureHistory model.
"""

from __future__ import annotations

from .consumer_failure_history import ConsumerFailureHistory


class ConsumerFailureHistoryV1(ConsumerFailureHistory, table=True):
    """
    Version 1 of the ConsumerFailureHistory model.

    Currently a name-only inheritance from the base ConsumerFailureHistory class.
    """

    __tablename__ = "consumer_failure_history"  # type: ignore
    __table_args__ = {"extend_existing": True}  # type: ignore
