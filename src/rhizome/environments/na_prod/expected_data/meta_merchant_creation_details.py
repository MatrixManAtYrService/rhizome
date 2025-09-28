"""
Expected data for merchant_creation_details table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.meta.merchant_creation_details import MerchantCreationDetails


class MerchantCreationDetailsNaProd(Emplacement[MerchantCreationDetails]):
    """Expected data for MerchantCreationDetails in na_prod environment."""

    @classmethod
    def get_expected(cls) -> MerchantCreationDetails:
        """Get expected merchant_creation_details data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "meta_merchant_creation_details.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return MerchantCreationDetails.model_validate(data)
