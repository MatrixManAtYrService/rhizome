"""
Tests for result serialization/deserialization.

These tests verify that SQLModel query results can be reliably serialized
to JSON-compatible dicts and reconstructed on the client side.

This is critical for the rhizome refactor where results are serialized
on the server and deserialized on the client.
"""

from datetime import datetime

import pytest
from sqlmodel import SQLModel


# Test models
class SimpleModel(SQLModel):
    """Simple model for basic serialization tests."""

    id: int
    name: str
    value: int
    active: bool = True


class ModelWithOptionals(SQLModel):
    """Model with optional fields."""

    id: int
    name: str
    description: str | None = None
    tags: str | None = None
    created_at: datetime | None = None


class ModelWithSanitization(SQLModel):
    """Model with sanitization method."""

    id: int
    public_name: str
    secret_key: str
    internal_id: int

    def sanitize(self) -> "ModelWithSanitization":
        """Sanitize by removing sensitive fields."""
        return ModelWithSanitization(
            id=self.id,
            public_name=self.public_name,
            secret_key="[REDACTED]",
            internal_id=0,  # Hide internal ID
        )


def serialize_result(model: SQLModel) -> dict:
    """
    Serialize a SQLModel instance to JSON-compatible dict.

    Args:
        model: SQLModel instance

    Returns:
        Dictionary with serialized data
    """
    # Use mode='json' to ensure proper serialization of complex types like datetime
    return model.model_dump(mode="json")


def deserialize_result(data: dict, model_class: type[SQLModel]) -> SQLModel:
    """
    Deserialize a dict back to SQLModel instance.

    Args:
        data: Dictionary with serialized data
        model_class: The model class to instantiate

    Returns:
        SQLModel instance
    """
    return model_class.model_validate(data)


def test_simple_model_round_trip() -> None:
    """Test serialization and deserialization of simple model."""
    original = SimpleModel(id=1, name="test", value=42, active=True)

    # Serialize
    serialized = serialize_result(original)

    # Should be a dict
    assert isinstance(serialized, dict)
    assert serialized["id"] == 1
    assert serialized["name"] == "test"
    assert serialized["value"] == 42
    assert serialized["active"] is True

    # Deserialize
    restored = deserialize_result(serialized, SimpleModel)

    # Should match original
    assert restored.id == original.id
    assert restored.name == original.name
    assert restored.value == original.value
    assert restored.active == original.active


def test_model_with_none_values() -> None:
    """Test serialization of model with None values."""
    original = ModelWithOptionals(id=1, name="test", description=None, tags=None, created_at=None)

    # Serialize
    serialized = serialize_result(original)

    # None values should be preserved
    assert serialized["description"] is None
    assert serialized["tags"] is None
    assert serialized["created_at"] is None

    # Deserialize
    restored = deserialize_result(serialized, ModelWithOptionals)

    assert restored.description is None
    assert restored.tags is None
    assert restored.created_at is None


def test_model_with_datetime() -> None:
    """Test serialization of model with datetime field."""
    test_time = datetime(2024, 1, 1, 12, 0, 0)
    original = ModelWithOptionals(id=1, name="test", created_at=test_time)

    # Serialize
    serialized = serialize_result(original)

    # Datetime should be serialized (as string or timestamp)
    assert "created_at" in serialized
    # Pydantic converts datetime to ISO format string
    assert isinstance(serialized["created_at"], str)

    # Deserialize
    restored = deserialize_result(serialized, ModelWithOptionals)

    # Datetime should be restored
    assert restored.created_at == test_time


def test_list_serialization() -> None:
    """Test serialization of list of models."""
    models = [
        SimpleModel(id=1, name="first", value=10),
        SimpleModel(id=2, name="second", value=20),
        SimpleModel(id=3, name="third", value=30),
    ]

    # Serialize all
    serialized_list = [serialize_result(m) for m in models]

    assert len(serialized_list) == 3
    assert all(isinstance(d, dict) for d in serialized_list)

    # Deserialize all
    restored_list = [deserialize_result(d, SimpleModel) for d in serialized_list]

    assert len(restored_list) == 3
    for original, restored in zip(models, restored_list, strict=False):
        assert original.id == restored.id
        assert original.name == restored.name
        assert original.value == restored.value


def test_empty_list() -> None:
    """Test that empty list serializes/deserializes correctly."""
    models = []
    serialized_list = [serialize_result(m) for m in models]
    assert serialized_list == []

    restored_list = [deserialize_result(d, SimpleModel) for d in serialized_list]
    assert restored_list == []


def test_sanitization_before_serialization() -> None:
    """Test that sanitization works before serialization."""
    original = ModelWithSanitization(id=1, public_name="Public", secret_key="SECRET123", internal_id=999)

    # Sanitize first
    sanitized = original.sanitize()

    # Serialize the sanitized version
    serialized = serialize_result(sanitized)

    # Sensitive data should be redacted
    assert serialized["secret_key"] == "[REDACTED]"
    assert serialized["internal_id"] == 0

    # Public data should be preserved
    assert serialized["public_name"] == "Public"
    assert serialized["id"] == 1


def test_none_result() -> None:
    """Test handling of None result (e.g., from select_first with no match)."""
    result = None

    # Serializing None
    serialized = None if result is None else serialize_result(result)

    assert serialized is None

    # Deserializing None
    restored = None if serialized is None else deserialize_result(serialized, SimpleModel)

    assert restored is None


def test_model_with_defaults() -> None:
    """Test that default values are handled correctly."""
    # Create model without specifying default field
    original = SimpleModel(id=1, name="test", value=42)
    # active should default to True

    serialized = serialize_result(original)
    assert serialized["active"] is True

    restored = deserialize_result(serialized, SimpleModel)
    assert restored.active is True


def test_type_safety() -> None:
    """Test that deserialization validates types."""
    # Create valid data
    valid_data = {"id": 1, "name": "test", "value": 42, "active": True}

    # Should succeed
    restored = deserialize_result(valid_data, SimpleModel)
    assert isinstance(restored, SimpleModel)

    # Test with invalid type (string instead of int)
    invalid_data = {"id": "not_an_int", "name": "test", "value": 42, "active": True}

    # Should raise validation error
    from pydantic import ValidationError

    with pytest.raises(ValidationError):
        deserialize_result(invalid_data, SimpleModel)


def test_extra_fields_ignored() -> None:
    """Test that extra fields in serialized data are handled gracefully."""
    # Data with extra field not in model
    data_with_extra = {"id": 1, "name": "test", "value": 42, "active": True, "extra_field": "should_be_ignored"}

    # Should succeed and ignore extra field
    restored = deserialize_result(data_with_extra, SimpleModel)
    assert restored.id == 1
    assert restored.name == "test"
    # extra_field should not be on the model
    assert not hasattr(restored, "extra_field")


def test_missing_optional_field() -> None:
    """Test that missing optional fields are handled correctly."""
    # Data missing optional fields
    data = {"id": 1, "name": "test"}  # description, tags, created_at omitted

    # Should succeed with None for optional fields
    restored = deserialize_result(data, ModelWithOptionals)
    assert restored.id == 1
    assert restored.name == "test"
    assert restored.description is None
    assert restored.tags is None
    assert restored.created_at is None


def test_missing_required_field() -> None:
    """Test that missing required fields raise error."""
    # Data missing required field 'name'
    data = {"id": 1, "value": 42}

    # Should raise validation error
    from pydantic import ValidationError

    with pytest.raises(ValidationError):
        deserialize_result(data, SimpleModel)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
