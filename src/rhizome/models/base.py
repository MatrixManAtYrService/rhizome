"""Base classes for rhizome models."""

from __future__ import annotations

import json
from abc import ABC, abstractmethod
from typing import Any, TypeVar

from jsondiff import diff  # type: ignore[import-untyped]
from sqlmodel import SQLModel, select
from sqlmodel.sql._expression_select_cls import SelectOfScalar

T = TypeVar("T", bound="RhizomeModel")


class DataMismatchError(AssertionError):
    """Custom exception to hold structured data about a data mismatch."""

    def __init__(self, message: str, env_name: str, table_name: str) -> None:
        super().__init__(message)
        self.env_name = env_name
        self.table_name = table_name


class RhizomeModel(SQLModel, ABC):
    """Abstract base class for models that support sanitization."""

    id: Any | None = None

    @abstractmethod
    def sanitize(self: T) -> T:
        """Return a sanitized copy of this model instance."""


class Emplacement[T: "RhizomeModel"](ABC):
    """
    Extra metadata about a RhizomeModel which can only be known if we also know which
    environment we're working in.

    Generic over the specific RhizomeModel type this emplacement is for.
    """

    @classmethod
    @abstractmethod
    def get_expected(cls) -> T:
        """
        Returns a row that's expected to be in this database.
        Used for testing.
        """

    @classmethod
    def expectation_query(cls, model: type[T]) -> SelectOfScalar[T]:
        """
        Returns a query that will be used to fetch the expected data.
        """
        return select(model).limit(1)

    def assert_match(self, actual: T, expected: T | None, env_name: str, table_name: str) -> None:
        """Compare actual and expected models, raising a detailed error on mismatch."""
        if expected is None:
            expected = self.get_expected()

        # Use exclude_unset=False to ensure all fields are present for comparison
        actual_dict = actual.model_dump(exclude_unset=False)
        expected_dict = expected.model_dump(exclude_unset=False)

        if actual_dict == expected_dict:
            return

        # Use marshal=True to get a JSON-serializable dict with '$' prefixed symbols.
        # Use syntax='symmetric' to get a clear [old, new] diff format.
        difference = diff(expected_dict, actual_dict, syntax="symmetric", marshal=True)  # type: ignore[call-arg]

        # Pretty-print the serializable dict into a readable report.
        # The `default=str` argument handles non-serializable types like datetimes.
        diff_report = (
            f"Data mismatch found for {env_name}/{table_name}.\n"
            f"Difference (Expected -> Actual):\n{json.dumps(difference, indent=2, default=str)}"
        )

        # Raise our custom exception with the pre-formatted, detailed report.
        raise DataMismatchError(
            message=diff_report,
            env_name=env_name,
            table_name=table_name,
        )
