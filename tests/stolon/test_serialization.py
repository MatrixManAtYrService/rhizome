"""Tests for stolon serialization/deserialization."""

from stolon.serialization import deserialize_argument, serialize_argument


def test_serialize_unset_value() -> None:
    """Test that UNSET values are properly serialized to a string sentinel."""
    # Import UNSET from one of the OpenAPI clients
    from stolon.openapi_generated.agreement_k8s_dev.open_api_definition_client.types import UNSET

    # Serialize UNSET - should become a string
    result = serialize_argument(UNSET)

    # Should be a JSON-serializable string sentinel
    assert result == "__UNSET__"
    assert isinstance(result, str)


def test_deserialize_unset_value() -> None:
    """Test that UNSET sentinel strings are properly deserialized back to UNSET."""
    from stolon.openapi_generated.agreement_k8s_dev.open_api_definition_client.types import UNSET

    # Deserialize the sentinel string back to UNSET
    result = deserialize_argument("__UNSET__", "Union[Unset, str]", "agreement_k8s_dev")

    # Should be the actual UNSET singleton
    assert result is UNSET


def test_serialize_model_with_unset_fields() -> None:
    """Test serialization of a model that contains UNSET field values."""
    from stolon.openapi_generated.agreement_k8s_dev.open_api_definition_client.models import (
        get_bulk_acceptances_service_scope_body,
    )

    GetBulkAcceptancesServiceScopeBody = get_bulk_acceptances_service_scope_body.GetBulkAcceptancesServiceScopeBody

    # Create a model with UNSET fields (default values)
    body = GetBulkAcceptancesServiceScopeBody()

    # Serialize it
    result = serialize_argument(body)

    # Should be a dict (from to_dict())
    assert isinstance(result, dict)

    # The dict should not contain UNSET values - they should be omitted by to_dict()
    # (OpenAPI models typically exclude UNSET fields in their to_dict() method)


def test_serialize_dict_with_unset_values() -> None:
    """Test that dicts containing UNSET values are properly serialized."""
    from stolon.openapi_generated.agreement_k8s_dev.open_api_definition_client.types import UNSET

    # Create a dict with an UNSET value
    data = {
        "field1": "value1",
        "field2": UNSET,
        "field3": 42,
    }

    # Serialize it
    result = serialize_argument(data)

    # Should be a dict with UNSET converted to string
    assert isinstance(result, dict)
    assert result["field1"] == "value1"
    assert result["field2"] == "__UNSET__"
    assert result["field3"] == 42


def test_serialize_list_with_unset_values() -> None:
    """Test that lists containing UNSET values are properly serialized."""
    from stolon.openapi_generated.agreement_k8s_dev.open_api_definition_client.types import UNSET

    # Create a list with an UNSET value
    data = ["value1", UNSET, 42]

    # Serialize it
    result = serialize_argument(data)

    # Should be a list with UNSET converted to string
    assert isinstance(result, list)
    assert result[0] == "value1"
    assert result[1] == "__UNSET__"
    assert result[2] == 42


def test_roundtrip_unset_in_model() -> None:
    """Test that UNSET values survive a serialize-deserialize roundtrip."""
    from stolon.openapi_generated.agreement_k8s_dev.open_api_definition_client.models import (
        get_bulk_acceptances_service_scope_body,
    )

    GetBulkAcceptancesServiceScopeBody = get_bulk_acceptances_service_scope_body.GetBulkAcceptancesServiceScopeBody

    # Create a model with some fields set and others UNSET
    original = GetBulkAcceptancesServiceScopeBody()
    original["merchantId"] = ["test-uuid"]  # Use dict-style to add to additional_properties

    # Serialize
    serialized = serialize_argument(original)

    # Deserialize
    deserialized = deserialize_argument(serialized, "GetBulkAcceptancesServiceScopeBody", "agreement_k8s_dev")

    # Should be a GetBulkAcceptancesServiceScopeBody instance
    assert isinstance(deserialized, GetBulkAcceptancesServiceScopeBody)

    # The additional_properties should have been preserved
    assert hasattr(deserialized, "additional_properties")
    assert deserialized["merchantId"] == ["test-uuid"]  # type: ignore[index]


def test_serialize_primitives() -> None:
    """Test that primitive types are serialized correctly."""
    assert serialize_argument(None) is None
    assert serialize_argument("string") == "string"
    assert serialize_argument(42) == 42
    assert serialize_argument(3.14) == 3.14
    assert serialize_argument(True) is True
    assert serialize_argument(False) is False


def test_deserialize_primitives() -> None:
    """Test that primitive types are deserialized correctly."""
    assert deserialize_argument(None, "str", "agreement_k8s_dev") is None
    assert deserialize_argument("string", "str", "agreement_k8s_dev") == "string"
    assert deserialize_argument(42, "int", "agreement_k8s_dev") == 42
    assert deserialize_argument(3.14, "float", "agreement_k8s_dev") == 3.14
    assert deserialize_argument(True, "bool", "agreement_k8s_dev") is True
