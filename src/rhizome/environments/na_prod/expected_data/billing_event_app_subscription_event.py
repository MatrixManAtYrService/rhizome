"""
Expected data for app_subscription_event table in na_prod environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.app_subscription_event_v1 import AppSubscriptionEventV1


class AppSubscriptionEventNaProd(Emplacement[AppSubscriptionEventV1]):
    """Expected data for AppSubscriptionEvent in na_prod environment."""

    @classmethod
    def get_expected(cls) -> AppSubscriptionEventV1:
        """Get expected app subscription event data for na_prod environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please create AppSubscriptionEventV1 model and add test data based on real data from this environment."
        )
