"""
Expected data for merchant_subscription_action table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.merchant_subscription_action_v1 import MerchantSubscriptionActionV1


class MerchantSubscriptionActionNaProd(Emplacement[MerchantSubscriptionActionV1]):
    """Expected data for MerchantSubscriptionAction in na_prod environment."""

    @classmethod
    def get_expected(cls) -> MerchantSubscriptionActionV1:
        """Get expected merchant_subscription_action data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_merchant_subscription_action.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return MerchantSubscriptionActionV1.model_validate(data)
