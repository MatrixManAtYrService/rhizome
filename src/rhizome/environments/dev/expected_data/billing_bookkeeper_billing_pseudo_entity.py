"""Expected data for billing_pseudo_entity table in dev environment."""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.billing_pseudo_entity_v1 import BillingPseudoEntityV1


class BillingPseudoEntityDev(Emplacement[BillingPseudoEntityV1]):
    """Expected data for BillingPseudoEntity in dev environment."""

    @classmethod
    def get_expected(cls) -> BillingPseudoEntityV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_bookkeeper_billing_pseudo_entity.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return BillingPseudoEntityV1.model_validate(data)
