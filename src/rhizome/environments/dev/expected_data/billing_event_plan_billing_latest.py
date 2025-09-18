"""
Expected data for plan_billing_latest table in dev environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.plan_billing_latest_v1 import PlanBillingLatestV1


class PlanBillingLatestDev(Emplacement[PlanBillingLatestV1]):
    """Expected data for PlanBillingLatest in dev environment."""

    @classmethod
    def get_expected(cls) -> PlanBillingLatestV1:
        """Get expected plan_billing_latest data for dev environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )
