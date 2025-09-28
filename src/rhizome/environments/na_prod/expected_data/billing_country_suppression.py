"""
Expected data for country_suppression table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.country_suppression_v1 import CountrySuppressionV1


class CountrySuppressionNaProd(Emplacement[CountrySuppressionV1]):
    """Expected data for CountrySuppression in na_prod environment."""

    @classmethod
    def get_expected(cls) -> CountrySuppressionV1:
        """Get expected country_suppression data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_country_suppression.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return CountrySuppressionV1.model_validate(data)
