"""Expected data for cycle_validation_mutation table in dev environment."""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.cycle_validation_mutation_v1 import CycleValidationMutationV1


class CycleValidationMutationDev(Emplacement[CycleValidationMutationV1]):
    """Expected data for CycleValidationMutation in dev environment."""

    @classmethod
    def get_expected(cls) -> CycleValidationMutationV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_bookkeeper_cycle_validation_mutation.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return CycleValidationMutationV1.model_validate(data)
