"""
Expected data for merchant_offboarding table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.merchant_offboarding_v1 import MerchantOffboardingV1


class MerchantOffboardingNaProd(Emplacement[MerchantOffboardingV1]):
    """Expected data for MerchantOffboarding in na_prod environment."""

    @classmethod
    def get_expected(cls) -> MerchantOffboardingV1:
        """Get expected merchant_offboarding data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_merchant_offboarding.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return MerchantOffboardingV1.model_validate(data)
