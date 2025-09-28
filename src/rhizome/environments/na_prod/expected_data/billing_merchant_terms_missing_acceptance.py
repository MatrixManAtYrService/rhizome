"""
Expected data for merchant_terms_missing_acceptance table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.merchant_terms_missing_acceptance_v1 import MerchantTermsMissingAcceptanceV1


class MerchantTermsMissingAcceptanceNaProd(Emplacement[MerchantTermsMissingAcceptanceV1]):
    """Expected data for MerchantTermsMissingAcceptance in na_prod environment."""

    @classmethod
    def get_expected(cls) -> MerchantTermsMissingAcceptanceV1:
        """Get expected merchant_terms_missing_acceptance data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_merchant_terms_missing_acceptance.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return MerchantTermsMissingAcceptanceV1.model_validate(data)
