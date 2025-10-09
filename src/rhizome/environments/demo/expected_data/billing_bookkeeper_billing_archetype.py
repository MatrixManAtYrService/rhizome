"""Expected data for billing_archetype table in demo environment."""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.billing_archetype_v1 import BillingArchetypeV1


class BillingArchetypeDemo(Emplacement[BillingArchetypeV1]):
    """Expected data for BillingArchetype in demo environment."""

    @classmethod
    def get_expected(cls) -> BillingArchetypeV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_bookkeeper_billing_archetype.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return BillingArchetypeV1.model_validate(data)
