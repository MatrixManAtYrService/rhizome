"""
Expected data for migrated_merchant table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.migrated_merchant_v1 import MigratedMerchantV1


class MigratedMerchantNaProd(Emplacement[MigratedMerchantV1]):
    """Expected data for MigratedMerchant in na_prod environment."""

    @classmethod
    def get_expected(cls) -> MigratedMerchantV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_event_migrated_merchant.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return MigratedMerchantV1.model_validate(data)
