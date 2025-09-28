"""
SQLModel definition for the flight_check_archive table, version 1.

This module provides the V1 implementation of the FlightCheckArchive model.
Currently, FlightCheckArchiveV1 is identical to the base FlightCheckArchive class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .flight_check_archive import FlightCheckArchive


class FlightCheckArchiveV1(FlightCheckArchive, NaProdSQLModel, table=True):
    """
    Version 1 of the FlightCheckArchive model.

    Currently a name-only inheritance from the base FlightCheckArchive class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "flight_check_archive"  # type: ignore
