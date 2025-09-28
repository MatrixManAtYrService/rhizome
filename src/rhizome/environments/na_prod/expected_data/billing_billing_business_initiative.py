"""
Expected data for billing_business_initiative table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.billing_business_initiative_v1 import BillingBusinessInitiativeV1


class BillingBusinessInitiativeNaProd(Emplacement[BillingBusinessInitiativeV1]):
    """Expected data for BillingBusinessInitiative in na_prod environment."""

    @classmethod
    def get_expected(cls) -> BillingBusinessInitiativeV1:
        """Get expected billing_business_initiative data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_billing_business_initiative.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return BillingBusinessInitiativeV1.model_validate(data)
