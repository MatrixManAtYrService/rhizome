"""
Expected data for merchant_queue_sensitive table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.merchant_queue_sensitive_v1 import MerchantQueueSensitiveV1


class MerchantQueueSensitiveNaProd(Emplacement[MerchantQueueSensitiveV1]):
    """Expected data for MerchantQueueSensitive in na_prod environment."""

    @classmethod
    def get_expected(cls) -> MerchantQueueSensitiveV1:
        """Get expected merchant_queue_sensitive data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_merchant_queue_sensitive.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return MerchantQueueSensitiveV1.model_validate(data)
