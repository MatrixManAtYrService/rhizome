"""
Registry of pre-defined write queries that require user approval.

All write operations to databases must go through canned queries defined here.
This ensures that:
1. All writes are reviewed and approved
2. Queries are parameterized to prevent SQL injection
3. Users can see exactly what will be executed before approving
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class CannedQuery:
    """A pre-defined query that can be executed with user approval."""

    name: str
    description: str
    sql: str
    environment: str  # e.g., "dev1.meta", "demo2.billing_bookkeeper"


# Registry of all available canned queries
CANNED_QUERIES: dict[str, CannedQuery] = {
    "create_account": CannedQuery(
        name="create_account",
        description="Create a new account with uuid, name, email, and claim code",
        environment="dev1.meta",
        sql="""
            INSERT INTO account (uuid, name, email, claim_code)
            VALUES (:uuid, :name, :email, :claim_code)
        """,
    ),
    "create_reseller_role": CannedQuery(
        name="create_reseller_role",
        description="Create a reseller_role entry to grant reseller permissions to an account",
        environment="dev1.meta",
        sql="""
            INSERT INTO reseller_role (reseller_id, account_id, permissions_id)
            VALUES (:reseller_id, :account_id, :permissions_id)
        """,
    ),
    "update_account_primary_role": CannedQuery(
        name="update_account_primary_role",
        description="Update an account's primary_reseller_role_id",
        environment="dev1.meta",
        sql="""
            UPDATE account
            SET primary_reseller_role_id = :primary_reseller_role_id
            WHERE id = :account_id
        """,
    ),
}


def get_query(query_name: str) -> CannedQuery:
    """
    Get a canned query by name.

    Args:
        query_name: Name of the query to retrieve

    Returns:
        CannedQuery instance

    Raises:
        KeyError: If query name is not found
    """
    if query_name not in CANNED_QUERIES:
        available = ", ".join(CANNED_QUERIES.keys())
        raise KeyError(f"Unknown query '{query_name}'. Available queries: {available}")
    return CANNED_QUERIES[query_name]


def render_query(query_name: str, params: dict[str, Any]) -> str:
    """
    Render a query with parameters for display.

    Args:
        query_name: Name of the query
        params: Parameters to substitute

    Returns:
        SQL string with parameters substituted for display
    """
    query = get_query(query_name)
    rendered = query.sql

    for key, value in params.items():
        # Simple string substitution for display (not for execution)
        placeholder = f":{key}"
        if isinstance(value, str):
            rendered = rendered.replace(placeholder, f"'{value}'")
        else:
            rendered = rendered.replace(placeholder, str(value))

    return rendered.strip()
