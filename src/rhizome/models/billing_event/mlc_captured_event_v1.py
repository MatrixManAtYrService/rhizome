"""
SQLModel definition for the mlc_captured_event table, version 1.

This module provides the V1 implementation of the MlcCapturedEvent model.
Currently, MlcCapturedEventV1 is identical to the base MlcCapturedEvent class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .mlc_captured_event import MlcCapturedEvent


class MlcCapturedEventV1(MlcCapturedEvent, table=True):
    """
    Version 1 of the MlcCapturedEvent model.

    Currently a name-only inheritance from the base MlcCapturedEvent class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "mlc_captured_event"  # type: ignore
