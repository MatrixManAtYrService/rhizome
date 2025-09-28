"""
Expected data for charge_state_attempt table in na_prod environment.
"""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing.charge_state_attempt_v1 import ChargeStateAttemptV1


class ChargeStateAttemptNaProd(Emplacement[ChargeStateAttemptV1]):
    """Expected data for ChargeStateAttempt in na_prod environment."""

    @classmethod
    def get_expected(cls) -> ChargeStateAttemptV1:
        """Get expected charge_state_attempt data for na_prod environment."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_charge_state_attempt.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )

        with open(file_path) as f:
            data = json.load(f)
        return ChargeStateAttemptV1.model_validate(data)
