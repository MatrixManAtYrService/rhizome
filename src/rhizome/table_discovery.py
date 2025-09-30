"""Centralized table discovery logic for rhizome sync commands.

This module provides a single source of truth for mapping environments to their
table enums, avoiding fragile substring matching and ensuring consistency across
all sync commands (schema, data, report).
"""

from __future__ import annotations

from enum import StrEnum

from rhizome.environments.environment_list import RhizomeEnvironment
from rhizome.models.table_list import BillingBookkeeperTable, BillingEventTable, BillingTable, MetaTable


def get_table_enum_for_environment(env_enum: RhizomeEnvironment) -> type[StrEnum] | None:
    """Get the table enum class for a given environment.

    This is the centralized mapping used by all sync commands to determine
    which tables belong to each environment.

    Args:
        env_enum: The environment enum value

    Returns:
        The table enum class for this environment, or None if not found

    Example:
        >>> from rhizome.environments.environment_list import RhizomeEnvironment
        >>> table_enum = get_table_enum_for_environment(RhizomeEnvironment.dev_billing_bookkeeper)
        >>> print(table_enum)
        <enum 'BillingBookkeeperTable'>
    """
    env_map: dict[RhizomeEnvironment, type[StrEnum]] = {
        # Billing Bookkeeper environments
        RhizomeEnvironment.dev_billing_bookkeeper: BillingBookkeeperTable,
        RhizomeEnvironment.demo_billing_bookkeeper: BillingBookkeeperTable,
        RhizomeEnvironment.na_prod_billing_bookkeeper: BillingBookkeeperTable,
        # Billing Event environments
        RhizomeEnvironment.dev_billing_event: BillingEventTable,
        RhizomeEnvironment.demo_billing_event: BillingEventTable,
        RhizomeEnvironment.na_prod_billing_event: BillingEventTable,
        # Billing environments
        RhizomeEnvironment.dev_billing: BillingTable,
        RhizomeEnvironment.demo_billing: BillingTable,
        RhizomeEnvironment.na_prod_billing: BillingTable,
        # Meta environments
        RhizomeEnvironment.dev_meta: MetaTable,
        RhizomeEnvironment.demo_meta: MetaTable,
        RhizomeEnvironment.na_prod_meta: MetaTable,
    }
    return env_map.get(env_enum)


def get_table_list_for_environment(env_enum: RhizomeEnvironment) -> list[StrEnum] | None:
    """Get the list of table enum values for a given environment.

    This is a convenience wrapper around get_table_enum_for_environment()
    that returns the list of table values instead of the enum class.

    Args:
        env_enum: The environment enum value

    Returns:
        List of table enum values for this environment, or None if not found

    Example:
        >>> from rhizome.environments.environment_list import RhizomeEnvironment
        >>> tables = get_table_list_for_environment(RhizomeEnvironment.dev_billing_bookkeeper)
        >>> print(tables[0])
        BillingBookkeeperTable.fee_summary
    """
    table_enum = get_table_enum_for_environment(env_enum)
    return list(table_enum) if table_enum else None