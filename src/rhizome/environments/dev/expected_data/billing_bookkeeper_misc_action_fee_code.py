"""Expected data for misc_action_fee_code table in dev environment."""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.misc_action_fee_code_v1 import MiscActionFeeCodeV1


class MiscActionFeeCodeDev(Emplacement[MiscActionFeeCodeV1]):
    """Expected data for MiscActionFeeCode in dev environment."""

    @classmethod
    def get_expected(cls) -> MiscActionFeeCodeV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_bookkeeper_misc_action_fee_code.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return MiscActionFeeCodeV1.model_validate(data)
