"""
Environment list for rhizome.

This module defines all environments tracked in rhizome across different
clusters and connection types.
"""

from __future__ import annotations

from enum import StrEnum, auto

from rhizome.environments.base import Environment
from rhizome.environments.demo.billing import DemoBilling
from rhizome.environments.demo.billing_bookkeeper import DemoBillingBookkeeper
from rhizome.environments.demo.billing_event import DemoBillingEvent
from rhizome.environments.demo.meta import DemoMeta
from rhizome.environments.dev.billing import DevBilling
from rhizome.environments.dev.billing_bookkeeper import DevBillingBookkeeper
from rhizome.environments.dev.billing_event import DevBillingEvent
from rhizome.environments.dev.meta import DevMeta
from rhizome.environments.na_prod.billing import NorthAmericaBilling
from rhizome.environments.na_prod.billing_bookkeeper import (
    NorthAmericaBillingBookkeeper,
)
from rhizome.environments.na_prod.billing_event import NorthAmericaBillingEvent
from rhizome.environments.na_prod.meta import NorthAmericaMeta


class RhizomeEnvironment(StrEnum):
    """Environment identifiers for rhizome database environments."""

    # Development environments
    dev_billing = auto()
    dev_billing_bookkeeper = auto()
    dev_billing_event = auto()
    dev_meta = auto()

    # Demo environments
    demo_billing = auto()
    demo_billing_bookkeeper = auto()
    demo_billing_event = auto()
    demo_meta = auto()

    # Production environments
    na_prod_billing = auto()
    na_prod_billing_bookkeeper = auto()
    na_prod_billing_event = auto()
    na_prod_meta = auto()


environment_type: dict[RhizomeEnvironment, type[Environment]] = {
    RhizomeEnvironment.dev_billing: DevBilling,
    RhizomeEnvironment.dev_billing_bookkeeper: DevBillingBookkeeper,
    RhizomeEnvironment.dev_billing_event: DevBillingEvent,
    RhizomeEnvironment.dev_meta: DevMeta,
    RhizomeEnvironment.demo_billing: DemoBilling,
    RhizomeEnvironment.demo_billing_bookkeeper: DemoBillingBookkeeper,
    RhizomeEnvironment.demo_billing_event: DemoBillingEvent,
    RhizomeEnvironment.demo_meta: DemoMeta,
    RhizomeEnvironment.na_prod_billing: NorthAmericaBilling,
    RhizomeEnvironment.na_prod_billing_bookkeeper: NorthAmericaBillingBookkeeper,
    RhizomeEnvironment.na_prod_billing_event: NorthAmericaBillingEvent,
    RhizomeEnvironment.na_prod_meta: NorthAmericaMeta,
}


def get_environment_enum_by_name(env_name: str) -> RhizomeEnvironment | None:
    """
    Look up RhizomeEnvironment enum by environment instance name.

    The environment instance name comes from the Environment.name property (e.g., "DevMeta"),
    and we need to find the corresponding RhizomeEnvironment enum value.

    Args:
        env_name: The environment name from Environment.name property

    Returns:
        RhizomeEnvironment enum value, or None if not found

    Examples:
        >>> get_environment_enum_by_name("DevMeta")
        RhizomeEnvironment.dev_meta
        >>> get_environment_enum_by_name("NorthAmericaMeta")
        RhizomeEnvironment.na_prod_meta
    """
    # Build reverse mapping from environment class name to enum
    # This iterates through environment_type and calls env_class().name for each
    # to create a mapping like {"DevMeta": RhizomeEnvironment.dev_meta, ...}

    # Since we can't instantiate environment classes without a client, we'll use
    # class names and string matching instead
    name_to_enum: dict[str, RhizomeEnvironment] = {}

    for enum_value, env_class in environment_type.items():
        # Map class names to enums
        # DevMeta -> dev_meta
        # DemoBillingBookkeeper -> demo_billing_bookkeeper
        # NorthAmericaMeta -> na_prod_meta
        class_name = env_class.__name__
        name_to_enum[class_name] = enum_value

    return name_to_enum.get(env_name)
