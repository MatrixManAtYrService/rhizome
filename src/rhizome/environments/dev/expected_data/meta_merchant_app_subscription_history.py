"""
Expected data for merchant_app_subscription_history table in dev environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.meta.merchant_app_subscription_history_v1 import MerchantAppSubscriptionHistoryV1


class MerchantAppSubscriptionHistoryDev(Emplacement[MerchantAppSubscriptionHistoryV1]):
    """Expected data for MerchantAppSubscriptionHistoryV1 in dev environment."""

    @classmethod
    def get_expected(cls) -> MerchantAppSubscriptionHistoryV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "meta_merchant_app_subscription_history.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return MerchantAppSubscriptionHistoryV1.model_validate(data)
