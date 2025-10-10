"""
Expected data for merchant_boarding table in demo environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.meta.merchant_boarding_v1 import MerchantBoardingV1


class MerchantBoardingDemo(Emplacement[MerchantBoardingV1]):
    """Expected data for MerchantBoarding in demo environment."""

    @classmethod
    def get_expected(cls) -> MerchantBoardingV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "meta_merchant_boarding.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return MerchantBoardingV1.model_validate(data)
