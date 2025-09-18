"""
Expected data for as_of_merchant_plan table in dev environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.as_of_merchant_plan_v1 import AsOfMerchantPlanV1


class AsOfMerchantPlanDev(Emplacement[AsOfMerchantPlanV1]):
    """Expected data for AsOfMerchantPlan in dev environment."""

    @classmethod
    def get_expected(cls) -> AsOfMerchantPlanV1:
        """Get expected as of merchant plan data for dev environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )