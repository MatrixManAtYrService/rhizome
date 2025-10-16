"""
Tests for model class resolution.

These tests verify that we can extract model information from queries
and dynamically import model classes on the server side.
"""

import pytest
from sqlmodel import Field, SQLModel, select

from rhizome.serialization import get_model_info, import_model_class


# Test model in this module
class LocalTestModel(SQLModel, table=True):
    """Test model defined in this test module."""

    __tablename__ = "local_test"  # type: ignore[assignment]

    id: int | None = Field(default=None, primary_key=True)
    name: str
    value: int


def test_get_model_info_from_query() -> None:
    """Test extracting model information from a query."""
    query = select(LocalTestModel)
    info = get_model_info(query)

    assert info["model_class"] == "LocalTestModel"
    assert info["model_module"] == "tests.test_model_resolution"


def test_get_model_info_with_where() -> None:
    """Test that model info extraction works with WHERE clauses."""
    query = select(LocalTestModel).where(LocalTestModel.name == "test")
    info = get_model_info(query)

    assert info["model_class"] == "LocalTestModel"
    assert info["model_module"] == "tests.test_model_resolution"


def test_import_model_class_from_info() -> None:
    """Test that we can import a model class from extracted info."""
    # Get info from query
    query = select(LocalTestModel)
    info = get_model_info(query)

    # Import the class
    imported_class = import_model_class(info["model_module"], info["model_class"])

    # Should be the same class
    assert imported_class is LocalTestModel
    assert imported_class.__name__ == "LocalTestModel"


def test_import_real_model() -> None:
    """Test importing an actual rhizome model class."""
    # Import a real model from rhizome
    from rhizome.models.meta.reseller import Reseller

    # Get info from query
    query = select(Reseller)
    info = get_model_info(query)

    assert info["model_class"] == "Reseller"
    assert "rhizome.models.meta" in info["model_module"]

    # Import it back
    imported_class = import_model_class(info["model_module"], info["model_class"])

    assert imported_class is Reseller


def test_import_nonexistent_module() -> None:
    """Test that importing nonexistent module raises error."""
    with pytest.raises(ImportError):
        import_model_class("nonexistent.module", "SomeClass")


def test_import_nonexistent_class() -> None:
    """Test that importing nonexistent class raises error."""
    with pytest.raises(AttributeError):
        import_model_class("tests.test_model_resolution", "NonexistentClass")


def test_round_trip_with_actual_data() -> None:
    """Test full round trip: query -> info -> import -> instantiate."""
    # Create a query
    query = select(LocalTestModel).where(LocalTestModel.value > 10)

    # Extract model info
    info = get_model_info(query)

    # On "server side", import the model class
    model_class = import_model_class(info["model_module"], info["model_class"])

    # Create an instance (simulating deserialization on server)
    instance = model_class(id=1, name="test", value=42)

    # Verify it's the right type
    assert isinstance(instance, LocalTestModel)
    assert instance.name == "test"
    assert instance.value == 42


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
