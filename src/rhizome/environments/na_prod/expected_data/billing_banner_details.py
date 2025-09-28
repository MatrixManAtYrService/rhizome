"""
Expected data for banner_details table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.banner_details_v1 import BannerDetailsV1


class BannerDetailsNaProd(Emplacement[BannerDetailsV1]):
    """Expected data for BannerDetails in na_prod environment."""

    @classmethod
    def get_expected(cls) -> BannerDetailsV1:
        """Get expected banner_details data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_banner_details.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return BannerDetailsV1.model_validate(data)