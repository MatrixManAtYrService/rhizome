"""
SQLModel definition for the country_suppression table, version 1.

This module provides the V1 implementation of the CountrySuppression model.
Currently, CountrySuppressionV1 is identical to the base CountrySuppression class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .country_suppression import CountrySuppression


class CountrySuppressionV1(CountrySuppression, NaProdSQLModel, table=True):
    """
    Version 1 of the CountrySuppression model.

    Currently a name-only inheritance from the base CountrySuppression class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "country_suppression"  # type: ignore
