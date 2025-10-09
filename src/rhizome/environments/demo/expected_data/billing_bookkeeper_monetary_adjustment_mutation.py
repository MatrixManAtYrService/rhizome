"""Expected data for monetary_adjustment_mutation table in demo environment."""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.monetary_adjustment_mutation_v1 import MonetaryAdjustmentMutationV1


class MonetaryAdjustmentMutationDemo(Emplacement[MonetaryAdjustmentMutationV1]):
    """Expected data for MonetaryAdjustmentMutation in demo environment."""

    @classmethod
    def get_expected(cls) -> MonetaryAdjustmentMutationV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_bookkeeper_monetary_adjustment_mutation.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return MonetaryAdjustmentMutationV1.model_validate(data)
