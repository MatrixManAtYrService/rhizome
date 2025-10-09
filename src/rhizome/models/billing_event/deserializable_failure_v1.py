"""
SQLModel definition for the deserializable_failure table, version 1.

This module provides the V1 implementation of the DeserializableFailure model.
Currently, DeserializableFailureV1 is identical to the base DeserializableFailure class
(name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .deserializable_failure import DeserializableFailure


class DeserializableFailureV1(DeserializableFailure, table=True):
    """
    Version 1 of the DeserializableFailure model.

    Currently a name-only inheritance from the base DeserializableFailure class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "deserializable_failure"  # type: ignore
    __table_args__ = {"extend_existing": True}  # type: ignore
