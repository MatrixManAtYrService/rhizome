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


def test_deserialize_optional_model() -> None:
    """Test that Optional[Model] types are properly deserialized."""
    from stolon.openapi_generated.agreement_k8s_dev.open_api_definition_client.models.acceptance import Acceptance

    # Create a dict representing an Acceptance model (with required fields)
    acceptance_dict = {
        "agreementId": "550e8400-e29b-41d4-a716-446655440000",
        "signerName": "Test Signer",
        "id": "550e8400-e29b-41d4-a716-446655440001",
    }

    # Deserialize with Optional wrapper
    result = deserialize_argument(acceptance_dict, "Optional[Acceptance]", "agreement_k8s_dev")  # type: ignore[arg-type]

    # Should be an Acceptance instance, not a dict
    assert isinstance(result, Acceptance)
    assert str(result.id) == "550e8400-e29b-41d4-a716-446655440001"
    assert str(result.agreement_id) == "550e8400-e29b-41d4-a716-446655440000"
    assert result.signer_name == "Test Signer"


def test_deserialize_optional_list_of_models() -> None:
    """Test that Optional[list[Model]] types are properly deserialized."""
    from stolon.openapi_generated.agreement_k8s_dev.open_api_definition_client.models.acceptance import Acceptance

    # Create list of dicts representing Acceptance models (with required fields)
    acceptances_list = [
        {
            "agreementId": "550e8400-e29b-41d4-a716-446655440000",
            "signerName": "Test Signer 1",
            "id": "550e8400-e29b-41d4-a716-446655440002",
        },
        {
            "agreementId": "550e8400-e29b-41d4-a716-446655440001",
            "signerName": "Test Signer 2",
            "id": "550e8400-e29b-41d4-a716-446655440003",
        },
    ]

    # Deserialize with Optional[list[...]] wrapper
    result = deserialize_argument(acceptances_list, 'Optional[list["Acceptance"]]', "agreement_k8s_dev")  # type: ignore[arg-type]

    # Should be a list of Acceptance instances, not dicts
    assert isinstance(result, list)
    assert len(result) == 2  # type: ignore[arg-type]
    assert all(isinstance(item, Acceptance) for item in result)  # type: ignore[arg-type]
    # Type narrowing for accessing attributes
    acceptance_list: list[Acceptance] = result  # type: ignore[assignment]
    assert acceptance_list[0].signer_name == "Test Signer 1"
    assert acceptance_list[1].signer_name == "Test Signer 2"


def test_deserialize_list_of_models_without_optional() -> None:
    """Test that list[Model] types work without Optional wrapper."""
    from stolon.openapi_generated.agreement_k8s_dev.open_api_definition_client.models.acceptance import Acceptance

    # Create list of dicts representing Acceptance models (with required fields)
    acceptances_list = [
        {
            "agreementId": "550e8400-e29b-41d4-a716-446655440000",
            "signerName": "Test Signer",
            "id": "550e8400-e29b-41d4-a716-446655440004",
        },
    ]

    # Deserialize without Optional wrapper
    result = deserialize_argument(acceptances_list, 'list["Acceptance"]', "agreement_k8s_dev")  # type: ignore[arg-type]

    # Should be a list of Acceptance instances
    assert isinstance(result, list)
    assert len(result) == 1  # type: ignore[arg-type]
    assert isinstance(result[0], Acceptance)  # type: ignore[arg-type]
    # Type narrowing for accessing attributes
    acceptance_list: list[Acceptance] = result  # type: ignore[assignment]
    assert acceptance_list[0].signer_name == "Test Signer"
