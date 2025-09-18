"""
SQLModel definition for the consumer_failure table, version 1.

This module provides the V1 implementation of the ConsumerFailure model.
Currently, ConsumerFailureV1 is identical to the base ConsumerFailure class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .consumer_failure import ConsumerFailure


class ConsumerFailureV1(ConsumerFailure, table=True):
    """
    Version 1 of the ConsumerFailure model.

    Currently a name-only inheritance from the base ConsumerFailure class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "consumer_failure"  # type: ignore