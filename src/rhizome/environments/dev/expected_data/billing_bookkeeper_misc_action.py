"""Expected data for misc_action table in dev environment."""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.misc_action_v1 import MiscActionV1


class MiscActionDev(Emplacement[MiscActionV1]):
    """Expected data for MiscAction in dev environment."""

    @classmethod
    def get_expected(cls) -> MiscActionV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_bookkeeper_misc_action.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return MiscActionV1.model_validate(data)
