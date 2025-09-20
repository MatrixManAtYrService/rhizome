"""
Expected data for merchant_payment_history table in demo environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.merchant_payment_history_v1 import MerchantPaymentHistoryV1


class MerchantPaymentHistoryDemo(Emplacement[MerchantPaymentHistoryV1]):
    """Expected data for MerchantPaymentHistory in demo environment."""

    @classmethod
    def get_expected(cls) -> MerchantPaymentHistoryV1:
        """Get expected merchant_payment_history data for demo environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_merchant_payment_history.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return MerchantPaymentHistoryV1.model_validate(data)
