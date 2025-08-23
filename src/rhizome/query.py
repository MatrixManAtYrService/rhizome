"""Query execution utilities for rhizome."""

from enum import StrEnum


class GetMode(StrEnum):
    """Modes for retrieving query results."""

    FIRST = "first"  # Get first result using .first()
    ALL = "all"  # Get all results using .all()
    ONE = "one"  # Get exactly one result using .one()
