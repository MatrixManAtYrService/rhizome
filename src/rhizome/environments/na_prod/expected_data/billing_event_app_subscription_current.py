"""
Expected data for app_subscription_current table in na_prod environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.app_subscription_current_v1 import AppSubscriptionCurrentV1


class AppSubscriptionCurrentNaProd(Emplacement[AppSubscriptionCurrentV1]):
    """Expected data for AppSubscriptionCurrent in na_prod environment."""

    @classmethod
    def get_expected(cls) -> AppSubscriptionCurrentV1:
        """Get expected app subscription current data for na_prod environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )