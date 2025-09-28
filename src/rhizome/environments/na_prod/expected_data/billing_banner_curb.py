"""
Expected data for banner_curb table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.banner_curb_v1 import BannerCurbV1


class BannerCurbNaProd(Emplacement[BannerCurbV1]):
    """Expected data for BannerCurb in na_prod environment."""

    @classmethod
    def get_expected(cls) -> BannerCurbV1:
        """Get expected banner_curb data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_banner_curb.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return BannerCurbV1.model_validate(data)