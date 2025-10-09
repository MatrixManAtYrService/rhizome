"""Expected data for merchant_detail table in demo environment."""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.merchant_detail_v1 import MerchantDetailV1


class MerchantDetailDemo(Emplacement[MerchantDetailV1]):
    """Expected data for MerchantDetail in demo environment."""

    @classmethod
    def get_expected(cls) -> MerchantDetailV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_bookkeeper_merchant_detail.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return MerchantDetailV1.model_validate(data)
