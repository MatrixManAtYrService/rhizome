"""
Expected data for merchant_terms_acceptance_events table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.merchant_terms_acceptance_events_v1 import MerchantTermsAcceptanceEventsV1


class MerchantTermsAcceptanceEventsNaProd(Emplacement[MerchantTermsAcceptanceEventsV1]):
    """Expected data for MerchantTermsAcceptanceEvents in na_prod environment."""

    @classmethod
    def get_expected(cls) -> MerchantTermsAcceptanceEventsV1:
        """Get expected merchant_terms_acceptance_events data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_merchant_terms_acceptance_events.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return MerchantTermsAcceptanceEventsV1.model_validate(data)
