"""
SQLModel definition for the deserializable_failure table, version 1.

This module provides the V1 implementation of the DeserializableFailure model.
"""

from __future__ import annotations

from .deserializable_failure import DeserializableFailure


class DeserializableFailureV1(DeserializableFailure, table=True):
    """
    Version 1 of the DeserializableFailure model.

    Currently a name-only inheritance from the base DeserializableFailure class.
    """

    __tablename__ = "deserializable_failure"  # type: ignore
    __table_args__ = {"extend_existing": True}  # type: ignore
