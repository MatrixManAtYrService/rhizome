"""
Expected data for merchant_acceptance table in dev environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.merchant_acceptance_v1 import MerchantAcceptanceV1


class MerchantAcceptanceDev(Emplacement[MerchantAcceptanceV1]):
    """Expected data for MerchantAcceptance in dev environment."""

    @classmethod
    def get_expected(cls) -> MerchantAcceptanceV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_merchant_acceptance.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return MerchantAcceptanceV1.model_validate(data)
