"""
Environment list for rhizome.

This module defines all environments tracked in rhizome across different
clusters and connection types.
"""

from __future__ import annotations

from enum import StrEnum, auto

from rhizome.environments.base import Environment
from rhizome.environments.demo.billing_bookkeeper import DemoBillingBookkeeper
from rhizome.environments.demo.billing_event import DemoBillingEvent
from rhizome.environments.dev.billing_bookkeeper import DevBillingBookkeeper
from rhizome.environments.dev.billing_event import DevBillingEvent
from rhizome.environments.na_prod.billing import NorthAmericaBilling
from rhizome.environments.na_prod.billing_bookkeeper import (
    NorthAmericaBillingBookkeeper,
)
from rhizome.environments.na_prod.billing_event import NorthAmericaBillingEvent
from rhizome.environments.na_prod.meta import NorthAmericaMeta


class RhizomeEnvironment(StrEnum):
    """Environment identifiers for rhizome database environments."""

    # Development environments
    dev_billing_bookkeeper = auto()
    dev_billing_event = auto()

    # Demo environments
    demo_billing_bookkeeper = auto()
    demo_billing_event = auto()

    # Production environments
    na_prod_billing = auto()
    na_prod_billing_bookkeeper = auto()
    na_prod_billing_event = auto()
    na_prod_meta = auto()


environment_type: dict[RhizomeEnvironment, type[Environment]] = {
    RhizomeEnvironment.dev_billing_bookkeeper: DevBillingBookkeeper,
    RhizomeEnvironment.dev_billing_event: DevBillingEvent,
    RhizomeEnvironment.demo_billing_bookkeeper: DemoBillingBookkeeper,
    RhizomeEnvironment.demo_billing_event: DemoBillingEvent,
    RhizomeEnvironment.na_prod_billing: NorthAmericaBilling,
    RhizomeEnvironment.na_prod_billing_bookkeeper: NorthAmericaBillingBookkeeper,
    RhizomeEnvironment.na_prod_billing_event: NorthAmericaBillingEvent,
    RhizomeEnvironment.na_prod_meta: NorthAmericaMeta,
}
