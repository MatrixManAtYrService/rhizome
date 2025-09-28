"""
SQLModel definition for the flight_check table, version 1.

This module provides the V1 implementation of the FlightCheck model.
Currently, FlightCheckV1 is identical to the base FlightCheck class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .flight_check import FlightCheck


class FlightCheckV1(FlightCheck, NaProdSQLModel, table=True):
    """
    Version 1 of the FlightCheck model.

    Currently a name-only inheritance from the base FlightCheck class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "flight_check"  # type: ignore
