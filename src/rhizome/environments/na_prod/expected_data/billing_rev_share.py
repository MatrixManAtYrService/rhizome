"""
Expected data for rev_share table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.rev_share_v1 import RevShareV1


class RevShareNaProd(Emplacement[RevShareV1]):
    """Expected data for RevShare in na_prod environment."""

    @classmethod
    def get_expected(cls) -> RevShareV1:
        """Get expected rev_share data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_rev_share.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return RevShareV1.model_validate(data)
