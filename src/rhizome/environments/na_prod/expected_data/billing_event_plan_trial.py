"""
Expected data for plan_trial table in na_prod environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.plan_trial_v1 import PlanTrialV1


class PlanTrialNaProd(Emplacement[PlanTrialV1]):
    """Expected data for PlanTrial in na_prod environment."""

    @classmethod
    def get_expected(cls) -> PlanTrialV1:
        """Get expected plan_trial data for na_prod environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )
