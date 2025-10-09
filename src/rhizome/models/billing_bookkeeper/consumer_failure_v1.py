"""
SQLModel definition for the consumer_failure table, version 1.

This module provides the V1 implementation of the ConsumerFailure model.
"""

from __future__ import annotations

from .consumer_failure import ConsumerFailure


class ConsumerFailureV1(ConsumerFailure, table=True):
    """
    Version 1 of the ConsumerFailure model.

    Currently a name-only inheritance from the base ConsumerFailure class.
    """

    __tablename__ = "consumer_failure"  # type: ignore
    __table_args__ = {"extend_existing": True}  # type: ignore
