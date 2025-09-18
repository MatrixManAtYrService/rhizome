"""
SQLModel definition for the iccid_carrier table, version 1.

This module provides the V1 implementation of the IccidCarrier model.
Currently, IccidCarrierV1 is identical to the base IccidCarrier class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .iccid_carrier import IccidCarrier


class IccidCarrierV1(IccidCarrier, table=True):
    """
    Version 1 of the IccidCarrier model.

    Currently a name-only inheritance from the base IccidCarrier class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "iccid_carrier"  # type: ignore