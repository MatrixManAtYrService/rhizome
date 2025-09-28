"""
Expected data for bank_routing table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.bank_routing_v1 import BankRoutingV1


class BankRoutingNaProd(Emplacement[BankRoutingV1]):
    """Expected data for BankRouting in na_prod environment."""

    @classmethod
    def get_expected(cls) -> BankRoutingV1:
        """Get expected bank_routing data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_bank_routing.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return BankRoutingV1.model_validate(data)