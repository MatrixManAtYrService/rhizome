"""
SQLModel definition for the producer_failure table, version 1.

This module provides the V1 implementation of the ProducerFailure model.
Currently, ProducerFailureV1 is identical to the base ProducerFailure class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .producer_failure import ProducerFailure


class ProducerFailureV1(ProducerFailure, table=True):
    """
    Version 1 of the ProducerFailure model.

    Currently a name-only inheritance from the base ProducerFailure class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "producer_failure"  # type: ignore