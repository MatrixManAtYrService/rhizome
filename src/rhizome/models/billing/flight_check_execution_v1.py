"""
SQLModel definition for the flight_check_execution table, version 1.

This module provides the V1 implementation of the FlightCheckExecution model.
Currently, FlightCheckExecutionV1 is identical to the base FlightCheckExecution class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .flight_check_execution import FlightCheckExecution


class FlightCheckExecutionV1(FlightCheckExecution, NaProdSQLModel, table=True):
    """
    Version 1 of the FlightCheckExecution model.

    Currently a name-only inheritance from the base FlightCheckExecution class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "flight_check_execution"  # type: ignore
