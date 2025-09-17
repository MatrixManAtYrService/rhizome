"""
SQLModel definition for the stage_charge table, version 1.

This module provides the V1 implementation of the StageCharge model.
Currently, StageChargeV1 is identical to the base StageCharge class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .stage_charge import StageCharge


class StageChargeV1(StageCharge, table=True):
    """
    Version 1 of the StageCharge model.

    Currently a name-only inheritance from the base StageCharge class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "stage_charge"  # type: ignore
