"""
Expected data for promo_control table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.promo_control_v1 import PromoControlV1


class PromoControlNaProd(Emplacement[PromoControlV1]):
    """Expected data for PromoControl in na_prod environment."""

    @classmethod
    def get_expected(cls) -> PromoControlV1:
        """Get expected promo_control data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_promo_control.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return PromoControlV1.model_validate(data)
