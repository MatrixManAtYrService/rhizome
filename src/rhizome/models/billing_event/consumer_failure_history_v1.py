"""
SQLModel definition for the consumer_failure_history table, version 1.

This module provides the V1 implementation of the ConsumerFailureHistory model.
Currently, ConsumerFailureHistoryV1 is identical to the base ConsumerFailureHistory class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .consumer_failure_history import ConsumerFailureHistory


class ConsumerFailureHistoryV1(ConsumerFailureHistory, table=True):
    """
    Version 1 of the ConsumerFailureHistory model.

    Currently a name-only inheritance from the base ConsumerFailureHistory class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "consumer_failure_history"  # type: ignore