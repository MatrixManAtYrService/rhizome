"""
Expected data for app_subscription_daily table in na_prod environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.app_subscription_daily_v1 import AppSubscriptionDailyV1


class AppSubscriptionDailyNaProd(Emplacement[AppSubscriptionDailyV1]):
    """Expected data for AppSubscriptionDaily in na_prod environment."""

    @classmethod
    def get_expected(cls) -> AppSubscriptionDailyV1:
        """Get expected app subscription daily data for na_prod environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )