"""Expected data for partner_config table in demo environment."""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.partner_config_v1 import PartnerConfigV1


class PartnerConfigDemo(Emplacement[PartnerConfigV1]):
    """Expected data for PartnerConfig in demo environment."""

    @classmethod
    def get_expected(cls) -> PartnerConfigV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_bookkeeper_partner_config.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return PartnerConfigV1.model_validate(data)
