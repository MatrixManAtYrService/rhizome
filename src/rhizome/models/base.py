"""Base classes for rhizome models."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, TypeVar

from sqlmodel import SQLModel

T = TypeVar("T", bound="SanitizableModel")


class SanitizableModel(SQLModel, ABC):
    """Abstract base class for models that support sanitization."""

    id: Any | None = None

    @abstractmethod
    def sanitize(self: T) -> T:
        """Return a sanitized copy of this model instance."""
