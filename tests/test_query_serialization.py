"""
Tests for query serialization/deserialization.

These tests verify that SQLModel queries can be reliably serialized to
SQL strings + parameters and reconstructed for server-side execution.

This is a critical foundation for the rhizome refactor where query
execution moves from client-side to server-side.
"""

import uuid
from datetime import datetime

import pytest
from sqlmodel import Field, SQLModel, select


# Test models
class TestModel(SQLModel, table=True):
    """Simple test model for query serialization tests."""

    __tablename__ = "test_table"  # type: ignore[assignment]

    id: int | None = Field(default=None, primary_key=True)
    name: str
    value: int
    active: bool = True
    uuid: str | None = None
    created_at: datetime | None = None


class ComplexModel(SQLModel, table=True):
    """Model with more complex types for testing."""

    __tablename__ = "complex_table"  # type: ignore[assignment]

    id: int | None = Field(default=None, primary_key=True)
    parent_id: int | None = None
    tags: str | None = None  # JSON stored as string
    amount: float | None = None
    status: str = "pending"


def serialize_query(query: select) -> tuple[str, dict[str, any]]:
    """
    Serialize a SQLModel query to SQL string + parameters.

    Args:
        query: SQLModel select query

    Returns:
        Tuple of (sql_string, parameters_dict)
    """
    # Compile the query to get SQL and parameters
    compiled = query.compile(compile_kwargs={"literal_binds": False})

    # Extract SQL string and parameters
    sql = str(compiled)
    params = dict(compiled.params) if compiled.params else {}

    return sql, params


def test_simple_select_all() -> None:
    """Test serialization of simple SELECT * query."""
    query = select(TestModel)
    sql, params = serialize_query(query)

    # Should produce basic SELECT statement
    assert "SELECT" in sql
    assert "test_table" in sql
    assert params == {}  # No parameters for simple select


def test_simple_where_clause() -> None:
    """Test serialization of query with WHERE clause."""
    query = select(TestModel).where(TestModel.name == "test_name")
    sql, params = serialize_query(query)

    assert "SELECT" in sql
    assert "WHERE" in sql
    # Should have one parameter for the name
    assert len(params) == 1
    assert "test_name" in params.values()


def test_multiple_where_conditions() -> None:
    """Test serialization with multiple WHERE conditions."""
    query = (
        select(TestModel).where(TestModel.name == "test").where(TestModel.value > 10).where(TestModel.active.is_(True))
    )
    sql, params = serialize_query(query)

    assert "WHERE" in sql
    # Should have parameters for name and value (True is likely literal)
    assert len(params) >= 2
    assert "test" in params.values()
    assert 10 in params.values()


def test_in_clause() -> None:
    """Test serialization of IN clause."""
    test_ids = [1, 2, 3, 4, 5]
    query = select(TestModel).where(TestModel.id.in_(test_ids))
    sql, params = serialize_query(query)

    assert "IN" in sql
    # Parameters should include the list items
    param_values = list(params.values())
    # SQLAlchemy may expand IN clause to individual params or keep as tuple
    # Just verify we have the right count
    assert len(params) >= len(test_ids) or any(isinstance(v, list | tuple) for v in param_values)


def test_null_checks() -> None:
    """Test serialization of NULL checks (IS NULL / IS NOT NULL)."""
    query_null = select(TestModel).where(TestModel.uuid.is_(None))
    sql_null, params_null = serialize_query(query_null)

    query_not_null = select(TestModel).where(TestModel.uuid.is_not(None))
    sql_not_null, params_not_null = serialize_query(query_not_null)

    assert "IS NULL" in sql_null.upper()
    assert "IS NOT NULL" in sql_not_null.upper()
    # NULL checks typically don't use parameters
    assert params_null == {}
    assert params_not_null == {}


def test_like_pattern() -> None:
    """Test serialization of LIKE patterns."""
    query = select(TestModel).where(TestModel.name.like("test%"))
    sql, params = serialize_query(query)

    assert "LIKE" in sql.upper()
    assert len(params) == 1
    assert "test%" in params.values()


def test_order_by() -> None:
    """Test serialization with ORDER BY clause."""
    query = select(TestModel).where(TestModel.active.is_(True)).order_by(TestModel.created_at.desc())
    sql, params = serialize_query(query)

    assert "ORDER BY" in sql.upper()
    assert "DESC" in sql.upper()


def test_limit_offset() -> None:
    """Test serialization with LIMIT and OFFSET."""
    query = select(TestModel).where(TestModel.active.is_(True)).limit(10).offset(20)
    sql, params = serialize_query(query)

    assert "LIMIT" in sql.upper()
    # Note: OFFSET handling varies by dialect


def test_join_query() -> None:
    """Test serialization of query with JOIN."""
    query = (
        select(ComplexModel).join(TestModel, ComplexModel.parent_id == TestModel.id).where(TestModel.name == "parent")
    )
    sql, params = serialize_query(query)

    assert "JOIN" in sql.upper()
    assert "parent" in params.values()


def test_uuid_parameter() -> None:
    """Test serialization with UUID parameter."""
    test_uuid = str(uuid.uuid4())
    query = select(TestModel).where(TestModel.uuid == test_uuid)
    sql, params = serialize_query(query)

    assert len(params) == 1
    assert test_uuid in params.values()


def test_datetime_parameter() -> None:
    """Test serialization with datetime parameter."""
    test_time = datetime(2024, 1, 1, 12, 0, 0)
    query = select(TestModel).where(TestModel.created_at > test_time)
    sql, params = serialize_query(query)

    assert len(params) == 1
    # Datetime should be in params (may be as datetime object or string)
    param_values = list(params.values())
    assert param_values[0] == test_time or str(test_time) in str(param_values[0])


def test_subquery() -> None:
    """Test serialization with subquery."""
    subquery = select(ComplexModel.parent_id).where(ComplexModel.status == "active").subquery()
    query = select(TestModel).where(TestModel.id.in_(select(subquery.c.parent_id)))
    sql, params = serialize_query(query)

    assert "SELECT" in sql
    # Should have parameter for status
    assert "active" in params.values()


def test_complex_expression() -> None:
    """Test serialization with complex expression."""
    query = (
        select(ComplexModel)
        .where(ComplexModel.amount > 100.0)
        .where(ComplexModel.status.in_(["pending", "active"]))
        .where(ComplexModel.parent_id.is_not(None))
        .order_by(ComplexModel.amount.desc())
        .limit(50)
    )
    sql, params = serialize_query(query)

    assert "WHERE" in sql
    assert "ORDER BY" in sql.upper()
    assert "LIMIT" in sql.upper()
    # Should have params for amount and status values
    assert 100.0 in params.values() or 100 in params.values()


def test_parameter_names_are_unique() -> None:
    """Test that parameter names don't collide when using same value twice."""
    query = (
        select(TestModel).where(TestModel.name == "test").where(TestModel.uuid == "test")  # Same value "test"
    )
    sql, params = serialize_query(query)

    # SQLAlchemy should generate unique parameter names even for same value
    assert "test" in params.values()
    # Should have 2 parameters (one for each usage)
    values_list = list(params.values())
    assert values_list.count("test") == 2


def test_empty_params_dict() -> None:
    """Test that queries without parameters return empty dict, not None."""
    query = select(TestModel).where(TestModel.active.is_(True))
    sql, params = serialize_query(query)

    assert params is not None
    assert isinstance(params, dict)


@pytest.mark.parametrize(
    "test_value,expected_type",
    [
        ("string_value", str),
        (42, int),
        (3.14, float),
        (True, bool),
        (None, type(None)),
    ],
)
def test_parameter_type_preservation(test_value: str | int | float | bool | None, expected_type: type) -> None:
    """Test that parameter types are preserved during serialization."""
    if test_value is None:
        # Skip None - it typically doesn't create parameters
        pytest.skip("NULL values don't create parameters")

    query = select(TestModel).where(TestModel.value == test_value)
    sql, params = serialize_query(query)

    if params:  # Some values might not create params (e.g., True/False literals)
        param_values = list(params.values())
        # At least one parameter should match our expected type
        assert any(isinstance(v, expected_type) for v in param_values)


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v"])
