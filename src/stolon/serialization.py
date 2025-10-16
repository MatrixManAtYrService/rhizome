"""Serialization and deserialization helpers for OpenAPI models."""

from __future__ import annotations

import importlib
from collections.abc import Mapping, MutableMapping
from http import HTTPStatus
from typing import Any, Protocol, TypeGuard, TypeVar

# JSON-serializable types
JsonPrimitive = str | int | float | bool | None
JsonValue = JsonPrimitive | dict[str, "JsonValue"] | list["JsonValue"]

T = TypeVar("T")


class OpenAPIModel(Protocol):
    """Protocol for OpenAPI-generated model classes."""

    def to_dict(self) -> dict[str, Any]: ...

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T: ...


class ResponseObject(Protocol):
    """Protocol for OpenAPI Response[T] objects."""

    status_code: HTTPStatus
    content: bytes
    headers: MutableMapping[str, str]
    parsed: Any


def _is_model_with_to_dict(obj: object) -> TypeGuard[OpenAPIModel]:
    """Check if object is a model with to_dict method."""
    return hasattr(obj, "to_dict") and callable(obj.to_dict)  # type: ignore[arg-type]


def _serialize_list(items: list[object]) -> list[JsonValue]:
    """Serialize a list of items."""
    return [serialize_argument(item) for item in items]


def _serialize_dict(data: dict[str, object]) -> dict[str, JsonValue]:
    """Serialize a dictionary."""
    return {k: serialize_argument(v) for k, v in data.items()}


def serialize_argument(arg: object) -> JsonValue:
    """
    Serialize a function argument for JSON transport.

    Handles:
    - Pydantic/attrs models with .to_dict()
    - Lists of models
    - Dicts with model values
    - Primitive types (str, int, bool, None, etc.)

    Args:
        arg: Argument to serialize

    Returns:
        JSON-serializable value
    """
    if arg is None:
        return None
    if isinstance(arg, str | int | float | bool):
        return arg
    if _is_model_with_to_dict(arg):
        return arg.to_dict()  # type: ignore[union-attr]
    if isinstance(arg, list):
        return _serialize_list(arg)  # type: ignore[arg-type]
    if isinstance(arg, dict):
        return _serialize_dict(arg)  # type: ignore[arg-type]
    # For types like UNSET, return as-is (will be handled by Pydantic serialization)
    return arg  # type: ignore[return-value]


def _is_primitive_type(type_hint: str) -> bool:
    """Check if type hint represents a primitive type."""
    return type_hint in ("str", "int", "float", "bool", "Any")


def _handle_unset_type(data: JsonValue, type_hint: str, service: str) -> object:
    """Handle UNSET types from OpenAPI generated code."""
    types_module = importlib.import_module(f"stolon.openapi_generated.{service}.open_api_definition_client.types")
    UNSET = types_module.UNSET
    if data == "UNSET" or data is UNSET:
        return UNSET
    return data


def _deserialize_list_type(data: JsonValue, type_hint: str, service: str) -> list[object] | JsonValue:
    """Deserialize a list type."""
    element_type = extract_element_type(type_hint)
    if not isinstance(data, list):
        return data
    return [deserialize_argument(item, element_type, service) for item in data]


def _deserialize_model_type(data: JsonValue, type_hint: str, service: str) -> object | JsonValue:
    """Deserialize a model type (capitalized class name)."""
    if not type_hint or not type_hint[0].isupper() or type_hint.startswith("Union["):
        return data
    try:
        model_class = import_model_class(type_hint, service)
        if isinstance(data, dict):
            return model_class.from_dict(data)  # type: ignore[arg-type]
        return data
    except (ImportError, AttributeError):
        return data


def deserialize_argument(data: JsonValue, type_hint: str, service: str) -> object:
    """
    Deserialize data into the appropriate type based on type hint.

    Args:
        data: Serialized data (from JSON)
        type_hint: Type annotation string (e.g., "ApiModel", "list[ApiModel]", "str")
        service: Service name for model imports (e.g., "billing_bookkeeper_dev")

    Returns:
        Deserialized object
    """
    if data is None:
        return None

    if _is_primitive_type(type_hint):
        return data

    if "Unset" in type_hint or "UNSET" in type_hint:
        return _handle_unset_type(data, type_hint, service)

    if type_hint.startswith("list["):
        return _deserialize_list_type(data, type_hint, service)

    if type_hint.startswith("dict["):
        return data  # Return dicts as-is for now

    return _deserialize_model_type(data, type_hint, service)


def _is_response_object(obj: object) -> TypeGuard[ResponseObject]:
    """Check if object is a Response object from OpenAPI client."""
    return hasattr(obj, "status_code") and hasattr(obj, "parsed")


def _serialize_response(response: ResponseObject) -> dict[str, JsonValue]:
    """Serialize a Response[T] object from OpenAPI client."""
    status_code = response.status_code
    status_value = status_code.value

    content = response.content
    content_str = content.decode("utf-8")

    headers = response.headers
    parsed = response.parsed

    return {
        "_response_type": "Response",
        "status_code": status_value,
        "headers": dict(headers),
        "content": content_str,
        "parsed": serialize_argument(parsed),
    }


def serialize_result(result: object) -> JsonValue:
    """
    Serialize a function result for JSON transport.

    Handles Response[T] objects from OpenAPI client.

    Args:
        result: Function result to serialize

    Returns:
        JSON-serializable value
    """
    if result is None:
        return None

    if _is_response_object(result):
        return _serialize_response(result)

    return serialize_argument(result)


def _is_serialized_response(data: JsonValue) -> bool:
    """Check if data is a serialized Response object."""
    return isinstance(data, dict) and data.get("_response_type") == "Response"


def _deserialize_response(data: dict[str, JsonValue], type_hint: str, service: str) -> object:
    """Deserialize a Response[T] object."""
    from http import HTTPStatus

    types_module = importlib.import_module(f"stolon.openapi_generated.{service}.open_api_definition_client.types")
    Response = types_module.Response

    parsed_type = extract_response_parsed_type(type_hint)
    parsed = deserialize_argument(data["parsed"], parsed_type, service) if parsed_type else data["parsed"]

    content = data["content"]
    content_bytes = content.encode("utf-8") if isinstance(content, str) else content

    return Response(
        status_code=HTTPStatus(int(data["status_code"])),  # type: ignore[arg-type]
        content=content_bytes,
        headers=data["headers"],  # type: ignore[arg-type]
        parsed=parsed,
    )


def deserialize_result(data: JsonValue, type_hint: str, service: str) -> object:
    """
    Deserialize a function result from JSON transport.

    Handles Response[T] objects from OpenAPI client.

    Args:
        data: Serialized result data
        type_hint: Type annotation string
        service: Service name for imports

    Returns:
        Deserialized object
    """
    if data is None:
        return None

    if _is_serialized_response(data):
        return _deserialize_response(data, type_hint, service)  # type: ignore[arg-type]

    return deserialize_argument(data, type_hint, service)


def extract_element_type(list_type: str) -> str:
    """
    Extract the element type from a list type annotation.

    Args:
        list_type: Type annotation like "list[Model]" or "list['Model']"

    Returns:
        Element type (e.g., "Model")
    """
    if not list_type.startswith("list[") or not list_type.endswith("]"):
        return "Any"

    element_type = list_type[5:-1].strip()  # Extract "Model" from "list[Model]"

    # Remove quotes if present: list["Model"] -> Model
    if (element_type.startswith('"') and element_type.endswith('"')) or (
        element_type.startswith("'") and element_type.endswith("'")
    ):
        element_type = element_type[1:-1]

    return element_type


def extract_response_parsed_type(response_type: str) -> str:
    """
    Extract the parsed type from a Response type annotation.

    Args:
        response_type: Type annotation like "Response[Model]" or "Response[list[Model]]"

    Returns:
        Parsed type (e.g., "Model" or "list[Model]")
    """
    if not response_type.startswith("Response[") or not response_type.endswith("]"):
        return "Any"

    return response_type[9:-1].strip()  # Extract content from "Response[...]"


def import_model_class(model_name: str, service: str) -> type[OpenAPIModel]:
    """
    Import a model class from the OpenAPI generated models.

    Args:
        model_name: Name of the model class (e.g., "ApiBillingEntity")
        service: Service name (e.g., "billing_bookkeeper_dev")

    Returns:
        The model class
    """
    # Convert CamelCase to snake_case for module name
    module_name = camel_to_snake(model_name)

    # Import the model
    module_path = f"stolon.openapi_generated.{service}.open_api_definition_client.models.{module_name}"
    module = importlib.import_module(module_path)

    return getattr(module, model_name)  # type: ignore[return-value]


def camel_to_snake(name: str) -> str:
    """
    Convert CamelCase to snake_case.

    Args:
        name: CamelCase string (e.g., "ApiBillingEntity")

    Returns:
        snake_case string (e.g., "api_billing_entity")
    """
    result = ""
    prev_char = ""

    for i, c in enumerate(name):
        # Add underscore before uppercase letter (if previous wasn't uppercase)
        # Add underscore before digit only if previous was a lowercase letter
        if i > 0 and (c.isupper() and not prev_char.isupper() or c.isdigit() and prev_char.islower()):
            result += "_"
        result += c.lower()
        prev_char = c

    return result
