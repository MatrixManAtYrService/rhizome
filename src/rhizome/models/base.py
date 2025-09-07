"""Base classes for rhizome models."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from sqlmodel import SQLModel, select

T = TypeVar("T", bound="RhizomeModel")


class RhizomeModel(SQLModel, ABC):
    """Abstract base class for models that support sanitization."""

    id: Any | None = None

    @abstractmethod
    def sanitize(self: T) -> T:
        """Return a sanitized copy of this model instance."""


class Emplacement(ABC, Generic[T]):
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
    def expectation_query(cls, model: T) -> T:
        """
        Returns a query that will be used to fetch the expected data.
        """
        return select(model).limit(1)

    def assert_match(self, actual: T, expected: T | None = None) -> None:
        """Assert that the actual data matches expected data."""
        if expected is None:
            expected = self.get_expected()
        assert actual.model_dump() == expected.model_dump()
