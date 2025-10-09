"""Expected data for ledger_account_purpose table in dev environment."""

from __future__ import annotations

import json
from pathlib import Path

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.ledger_account_purpose_v1 import LedgerAccountPurposeV1


class LedgerAccountPurposeDev(Emplacement[LedgerAccountPurposeV1]):
    """Expected data for LedgerAccountPurpose in dev environment."""

    @classmethod
    def get_expected(cls) -> LedgerAccountPurposeV1:
        """Get expected data from JSON file."""
        module_path = Path(__file__).parent
        file_path = module_path / "billing_bookkeeper_ledger_account_purpose.json"

        if not file_path.exists():
            raise NotImplementedError(
                f"Expected data for {cls.__name__} not yet implemented. "
                f"JSON file {file_path.name} is missing. Run 'rhizome sync data' to generate it."
            )
        with open(file_path) as f:
            data = json.load(f)
        return LedgerAccountPurposeV1.model_validate(data)
