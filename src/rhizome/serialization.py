"""
Serialization utilities for rhizome queries and results.

This module provides functions to serialize SQLModel queries and results
for transmission between client and server. Query execution happens on
the server side, with queries serialized as SQL + parameters.
"""

from typing import Any, TypeVar

from sqlmodel import SQLModel
from sqlmodel.sql._expression_select_cls import SelectOfScalar

TModel = TypeVar("TModel", bound=SQLModel)


def serialize_query[TModel: SQLModel](query: SelectOfScalar[TModel]) -> tuple[str, dict[str, Any]]:
    """
    Serialize a SQLModel query to SQL string + parameters.

    This extracts the compiled SQL and parameter bindings from a SQLAlchemy
    query object. The SQL string contains parameter placeholders (:param_name)
    and the parameters dict maps those names to values.

    Args:
        query: SQLModel select query to serialize

    Returns:
        Tuple of (sql_string, parameters_dict)

    Example:
        >>> from sqlmodel import select
        >>> from rhizome.models.meta.reseller import Reseller
        >>> query = select(Reseller).where(Reseller.name == "test")
        >>> sql, params = serialize_query(query)
        >>> print(sql)  # "SELECT ... FROM reseller WHERE reseller.name = :name_1"
        >>> print(params)  # {"name_1": "test"}
    """
    # Compile query with parameter binding (not literal binds)
    compiled = query.compile(compile_kwargs={"literal_binds": False})

    # Extract SQL string and parameters
    sql = str(compiled)
    params = dict(compiled.params) if compiled.params else {}

    return sql, params


def serialize_result(result: SQLModel | None, sanitize: bool = True) -> dict[str, Any] | None:
    """
    Serialize a single SQLModel result to JSON-compatible dict.

    Args:
        result: SQLModel instance or None
        sanitize: Whether to call .sanitize() if the method exists

    Returns:
        Dictionary with serialized data, or None if result is None

    Example:
        >>> from rhizome.models.meta.reseller import Reseller
        >>> reseller = Reseller(id=1, name="Test", ...)
        >>> data = serialize_result(reseller, sanitize=True)
        >>> # data is JSON-compatible dict
    """
    if result is None:
        return None

    # Apply sanitization if requested and available
    sanitized_result: SQLModel = result
    if sanitize and hasattr(result, "sanitize"):
        sanitized_result = result.sanitize()  # type: ignore[attr-defined]

    # Serialize to dict using Pydantic's JSON mode for proper datetime/UUID handling
    # Type ignore needed because Pydantic's model_dump has complex overloads that include Unknown
    return sanitized_result.model_dump(mode="json")  # type: ignore[return-value]


def serialize_result_list(results: list[SQLModel], sanitize: bool = True) -> list[dict[str, Any]]:
    """
    Serialize a list of SQLModel results to JSON-compatible dicts.

    Args:
        results: List of SQLModel instances
        sanitize: Whether to call .sanitize() on each result if the method exists

    Returns:
        List of dictionaries with serialized data

    Example:
        >>> resellers = [Reseller(id=1, name="A"), Reseller(id=2, name="B")]
        >>> data_list = serialize_result_list(resellers, sanitize=True)
        >>> len(data_list)  # 2
    """
    serialized_list: list[dict[str, Any]] = []
    for result in results:
        # Apply sanitization if requested and available
        sanitized_result: SQLModel = result
        if sanitize and hasattr(result, "sanitize"):
            sanitized_result = result.sanitize()  # type: ignore[attr-defined]

        # Serialize to dict
        # Type ignore needed because Pydantic's model_dump has complex overloads that include Unknown
        serialized_list.append(sanitized_result.model_dump(mode="json"))  # type: ignore[arg-type]

    return serialized_list


def deserialize_result[TModel: SQLModel](data: dict[str, Any] | None, model_class: type[TModel]) -> TModel | None:
    """
    Deserialize a dict back to a SQLModel instance.

    Args:
        data: Dictionary with serialized data, or None
        model_class: The model class to instantiate

    Returns:
        SQLModel instance or None

    Example:
        >>> from rhizome.models.meta.reseller import Reseller
        >>> data = {"id": 1, "name": "Test", ...}
        >>> reseller = deserialize_result(data, Reseller)
        >>> reseller.name  # "Test"
    """
    if data is None:
        return None

    return model_class.model_validate(data)


def deserialize_result_list[TModel: SQLModel](
    data_list: list[dict[str, Any]], model_class: type[TModel]
) -> list[TModel]:
    """
    Deserialize a list of dicts back to SQLModel instances.

    Args:
        data_list: List of dictionaries with serialized data
        model_class: The model class to instantiate

    Returns:
        List of SQLModel instances

    Example:
        >>> from rhizome.models.meta.reseller import Reseller
        >>> data_list = [{"id": 1, "name": "A"}, {"id": 2, "name": "B"}]
        >>> resellers = deserialize_result_list(data_list, Reseller)
        >>> len(resellers)  # 2
    """
    return [model_class.model_validate(data) for data in data_list]


def get_model_info[TModel: SQLModel](query: SelectOfScalar[TModel]) -> dict[str, str]:
    """
    Extract model class information from a query.

    This is used by the client to tell the server what model class
    to use for deserialization.

    Args:
        query: SQLModel select query

    Returns:
        Dictionary with model_module and model_class keys

    Example:
        >>> from sqlmodel import select
        >>> from rhizome.models.meta.reseller import Reseller
        >>> query = select(Reseller)
        >>> info = get_model_info(query)
        >>> info["model_class"]  # "Reseller"
        >>> info["model_module"]  # "rhizome.models.meta.reseller"
    """
    # Get the model class from the query
    # SQLModel queries have column_descriptions that tell us the entity
    if hasattr(query, "column_descriptions") and query.column_descriptions:
        entity = query.column_descriptions[0]["entity"]
        if entity:
            return {
                "model_class": entity.__name__,
                "model_module": entity.__module__,
            }

    raise ValueError("Could not extract model class from query")


def import_model_class(model_module: str, model_class: str) -> type[SQLModel]:
    """
    Dynamically import a model class by module and class name.

    This is used by the server to reconstruct the model class from
    information sent by the client.

    Args:
        model_module: Python module path (e.g., "rhizome.models.meta.reseller")
        model_class: Class name (e.g., "Reseller")

    Returns:
        The model class

    Raises:
        ImportError: If module cannot be imported
        AttributeError: If class does not exist in module

    Example:
        >>> cls = import_model_class("rhizome.models.meta.reseller", "Reseller")
        >>> cls.__name__  # "Reseller"
    """
    import importlib

    module = importlib.import_module(model_module)
    return getattr(module, model_class)
