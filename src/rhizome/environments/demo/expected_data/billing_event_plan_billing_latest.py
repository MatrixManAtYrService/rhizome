"""
Expected data for plan_billing_latest table in demo environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.plan_billing_latest_v1 import PlanBillingLatestV1


class PlanBillingLatestDemo(Emplacement[PlanBillingLatestV1]):
    """Expected data for PlanBillingLatest in demo environment."""

    @classmethod
    def get_expected(cls) -> PlanBillingLatestV1:
        """Get expected plan_billing_latest data for demo environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )
