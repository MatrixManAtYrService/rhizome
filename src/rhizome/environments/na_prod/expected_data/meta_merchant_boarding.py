"""
Expected data for merchant_boarding table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.meta.merchant_boarding import MerchantBoarding


class MerchantBoardingNaProd(Emplacement[MerchantBoarding]):
    """Expected data for MerchantBoarding in na_prod environment."""

    @classmethod
    def get_expected(cls) -> MerchantBoarding:
        """Get expected merchant_boarding data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "meta_merchant_boarding.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return MerchantBoarding.model_validate(data)
