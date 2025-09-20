"""Base classes for rhizome models."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, TypeVar

from sqlmodel import SQLModel, select
from sqlmodel.sql._expression_select_cls import SelectOfScalar

T = TypeVar("T", bound="RhizomeModel")


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

    def assert_match(self, actual: T, expected: T | None = None) -> tuple[dict[str, Any], dict[str, Any]]:
        """Prepare actual and expected data for comparison."""
        if expected is None:
            expected = self.get_expected()

        try:
            assert actual.model_dump() == expected.model_dump()
        except AssertionError as e:
            from rhizome.test_utils import enhance_assertion_error_with_fix_commands
            enhanced_error = enhance_assertion_error_with_fix_commands(
                e, self.__class__.__module__
            )
            raise enhanced_error from e